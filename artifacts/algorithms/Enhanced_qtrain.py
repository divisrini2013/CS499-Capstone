import numpy as np
import datetime
import logging
import random
from collections import deque

# Configure logging
logging.basicConfig(
    filename="training.log",
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

# Enhanced epsilon decay schedule
def decay_epsilon(epsilon, min_epsilon=0.05, decay_rate=0.995):
    return max(min_epsilon, epsilon * decay_rate)


def select_action(model, state, epsilon):
    """Select an action using improved epsilon-greedy policy with error-handled prediction."""
    if np.random.rand() < epsilon:
        return random.choice(ACTIONS)

    try:
        q_values = model.predict(state)[0]
        return np.argmax(q_values)
    except Exception as e:
        logging.error(f"Model prediction failed: {e}")
        return random.choice(ACTIONS)


def train_from_replay(model, memory, batch_size):
    """Sample experiences and train the model using replay memory."""
    if len(memory) < batch_size:
        return 0.0  # Not enough memory to train

    batch = random.sample(memory, batch_size)
    inputs = []
    targets = []

    for prev_state, action, reward, next_state, done in batch:
        try:
            target = model.predict(prev_state)[0]
            if done:
                target[action] = reward
            else:
                q_future = np.max(model.predict(next_state)[0])
                target[action] = reward + 0.9 * q_future

            inputs.append(prev_state[0])
            targets.append(target)

        except Exception as e:
            logging.error(f"Replay training error: {e}")

    history = model.fit(
        np.array(inputs),
        np.array(targets),
        epochs=1,
        verbose=0
    )
    return history.history["loss"][0]


def qtrain(model, maze, **opt):
    """
    Enhanced Q-Learning training loop with structured modular design,
    improved memory management, logging, epsilon decay,
    and runtime performance tracking.
    """

    # Load configuration
    n_epoch = opt.get("n_epoch", 15000)
    max_memory = opt.get("max_memory", 2000)
    batch_size = opt.get("batch_size", 64)
    epsilon = opt.get("epsilon", 1.0)

    # Initialize environment and memory
    qmaze = TreasureMaze(maze)
    memory = deque(maxlen=max_memory)

    win_history = deque(maxlen=qmaze.maze.size // 2)
    start_time = datetime.datetime.now()

    logging.info("Starting Q-Learning training...")
    logging.info(f"Epochs: {n_epoch}, Memory Size: {max_memory}, Batch Size: {batch_size}")

    for epoch in range(n_epoch):
        agent_cell = random.choice(qmaze.free_cells)
        qmaze.reset(agent_cell)
        state = qmaze.observe()

        game_over = False
        total_loss = 0.0
        steps = 0
        reward = 0

        while not game_over:
            prev_state = state

            action = select_action(model, prev_state, epsilon)

            # Execute action
            try:
                state, reward, game_over = qmaze.act(action)
            except Exception as e:
                logging.error(f"Environment act() failed: {e}")
                break

            # Store experience
            memory.append((prev_state, action, reward, state, game_over))

            # Train from memory
            loss = train_from_replay(model, memory, batch_size)
            total_loss += loss
            steps += 1

        # Track wins
        win_history.append(1 if reward > 0 else 0)
        win_rate = sum(win_history) / len(win_history)

        # Decay epsilon
        epsilon = decay_epsilon(epsilon)

        elapsed = datetime.datetime.now() - start_time
        logging.info(
            f"Epoch {epoch}/{n_epoch} | Loss: {total_loss:.4f} | "
            f"Steps: {steps} | Win Rate: {win_rate:.3f} | Time: {elapsed}"
        )

        # Early stopping if perfect win streak
        if win_rate >= 0.9 and completion_check(model, qmaze):
            logging.info(f"Early stopping at epoch {epoch} due to high win rate")
            break

    total_time = datetime.datetime.now() - start_time
    logging.info(f"Training completed in {total_time}")

    return total_time
