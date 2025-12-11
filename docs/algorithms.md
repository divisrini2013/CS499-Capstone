CS 499 Milestone Three
Enhancement Two: Algorithms and Data Structure
Name: Divya Rangaraj
Course: CS-499 – Computer Science Capstone

 
1. Artifact Description
In Enhancement Two, my undergraduate computer science course CS 370 – Current and Emerging Trends built the Q-Learning Reinforcement Learning Training Function. A software taught an intelligent agent to traverse a labyrinth using reinforcement learning. Python complete function taught neural-network-based Q-Learning model, stored agent experience, selected actions, updated Q-values, and tracked agent performance across thousands of training epochs.
Design and computational errors plagued the initial machine learning code. Monolithic, unmodular training used inefficient list-based data structures for experience replay and a basic epsilon-greedy decay mechanism. Additionally, the solution lacked input validation, batching logic, and specific data structures. Long functions made debugging harder and restricted reinforcement learning uses. This was original code.
 
The code functioned, but algorithmic design, efficiency, data structure, and computational clarity might be improved. I used it for this milestone because it improved data management, algorithmic thinking, and writing concise, modular, professional-grade computational code.
2. Justification for Inclusion in the ePortfolio and Artifact Improvements
My ePortfolio includes algorithmic thinking, optimization, data structure selection, complexity analysis, and AI implementation, all essential computer scientist talents. This product shows how I apply theory to complex reinforcement learning using data structures and algorithms. Cormen et al. (2022) say sophisticated algorithm design demands utility, computational efficiency, and data structure integrity. I enhanced this relic to prove it.
Why I Selected This Item
My toughest algorithmic software job. The neural network for Q-value prediction, replay memory buffer, action-selection method, reward updating, and dynamic episode-based learning make up Q-Learning.
Since it employed algorithms and data structures, this milestone may improve it. Moreover, computer scientists need reinforcement learning. EPortfolio item shows machine learning algorithm expertise, increasing my reputation.
Components of the Artifact That Showcase Skills
The item shows numerous professional skills:
1.	Method of dynamic programming Q-Learning cycles values and optimizes rewards. My original and enhanced versions show reinforcement learning agents' optimum policy generation over time.
2.	Advanced Data Structures: Initial artifact replay buffers employed inefficient lists. The improved version used a collections module deque with O(1) append and pop operations for queue-like behavior. Professionals advocate this replay buffer optimization modification.
3.	To integrate neural networks and machine learning models, manage input arrays, tensor shapes, and training loops. My algorithm and machine learning engineering talents are shown.
4.	Q-Learning needs discount factors, Bellman equations, and state-transition logic. My modifications ease these concerns with explicit explanations and modular architecture.
How the Artifact Was Improved
Algorithmic and design modifications make the item more professional:
a. Modularizing the Training Pipeline
I split the code into many helper functions:
 
 
Pressman and Maxim (2020) software engineering best practices improve code readability and maintainability in this modular design.
b. Improved Data Structure Optimization
The experience replay buffer was replaced with a deque when the list reached capacity, reducing latency. Data structure literature prefers deque for replay buffers, which function like queues.
c. Enhanced Epsilon-Greedy Strategy
To stabilize model learning, I smoothed epsilon decay:
 
This ensures gradual transition from exploration to exploitation.
d. Performance Visualization and Logging
To analyze and comprehend algorithmic loss and win-rate patterns over training epochs, I utilized matplotlib.
e. Better Error Handling and Input Validation
Invalid environment states, model prediction failures, and empty replay buffers now trigger controlled errors or fallbacks.
f. Complexity Analysis and Documentation
On replay memory space and time complexity (O(n) each episode), I provided thorough inline comments, docstrings, and design notes. Reeves (2021) recommends algorithmic reasoning for long-term maintainability.
These improvements meet real-world AI engineering demands and exhibit my ability to critically examine and design high-level algorithms.
3. Meeting Course Outcomes: Planned Outcomes and Updates
I exceeded Module One course objectives with this upgrade. Key milestone outcomes:
Outcome 3: Designing and Evaluating Computing Solutions
This balances algorithmic design trade-offs and implements solutions. I assessed performance, data structure, and computational trade-offs to improve qtrain(). By switching from list-based memory to deque, modularizing training routines, and boosting epsilon decay, I could create fast, efficient, and mathematically sound algorithmic solutions (Cormen et al., 2022).
Outcome 4: Using Innovative Tools and Computing Techniques
Better NumPy operations, logging, and visualization libraries were required. Modularizing the reinforcement learning pipeline demonstrates my creativity in work settings.
Outcome 5: Developing a Security Mindset
I predicted and reduced algorithmic errors using reinforcement learning without disclosing passwords or data. State validation, prohibiting system training with an empty replay buffer, and model prediction shaping are defensive programming techniques.
Outcome-Coverage Updates
I wanted to concentrate on Outcomes 3 and 4, but defensive programming allowed 5. Now my outcome-coverage technique has this capacity. No big modifications were needed since I accomplished Module One's learning objectives.
4. Reflection on the Enhancement Process
Enriching this artifact was academically and professionally satisfying. More than CS 370, it improved my computational thinking. Improving the function showed me the difference between functioning code and well-written, scalable, maintainable, and efficient code.
What I Learned from Enhancing the Artifact
I used reinforcement and Q-Learning. Bellman equations, temporal difference learning, state-action value approximation, and exploration-exploitation balancing were discussed.
I also understood performance-intensive jobs require excellent data structures. A deque structure optimizes algorithms better than Python lists (Cormen et al., 2022).
Complex computational pipelines need modularization. We divided the monolithic training loop into helper functions to reduce cognitive strain, improve readability, and simplify debugging. Pressman and Maxim (2020) claimed software engineering creates controllable, versatile, and useful systems.
I finally saw and recorded algorithm performance. I could use new tools in algorithm-heavy systems to improve code readability and interpretability.
Challenges I Faced During Enhancement
Integration of modularized functionality was hard. State, action, reward, and episode termination were needed to break a massive reinforcement learning loop. Before logging, these interactions needed print-based debugging.
I had trouble seeing how my data structure choices affected performance. The replay memory must last thousands of iterations, therefore the improper structure might impair runtime. Structure testing and comparison helped me evaluate performance carefully.
Seeing patterns requires altering training outputs. Planning and integration were needed to regulate outputs without disrupting training.
How These Challenges Contributed to My Growth
Challenges improved my computational thinking, algorithm design, and machine learning theory and practice. I improved program goals and algorithmic engineering abilities by modifying this item.
 
References
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to algorithms (4th ed.). MIT Press.
Pressman, R. S., & Maxim, B. R. (2020). Software engineering: A practitioner’s approach (9th ed.). McGraw-Hill Education.
Reeves, A. (2021). Designing maintainable algorithms: Principles and practices. Wiley & Sons.

