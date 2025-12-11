CS 499 Milestone One

 
INTRODUCTION
My name is Divya Rangaraj, and this is my CS 499 code review. I will examine three computer science artifacts from earlier classes since the capstone includes software engineering and design, algorithms and data structures, and databases. I can critically evaluate my earlier artifacts since I have learned more and matured as an engineer throughout my degree program. I made these artifacts with accuracy and usability in mind. Now that I understand maintainability, secure code, algorithmic efficiency, database integrity, and professional software development standards, I can evaluate my prior work.
The crud.py file from CS 340 controlled Python application access to a MongoDB backend; the reinforcement learning training function qtrain() from CS 370 implemented Q-Learning with experience replay; and the database integration portion of CS 340, which I am evaluating separately under the database category. I will explain each artifact's functionality, code review it, and propose capstone enhancements. To show the transition from academic to professional engineering and how I will polish these artifacts into portfolio-ready components.
CATEGORY ONE: SOFTWARE ENGINEERING AND DESIGN
Artifact: crud.py from CS 340
A. Description of Existing Code Functionality
The CS 340 crud.py file was analyzed first. Application's MongoDB backend interface was AnimalShelter. This file allowed the system's data access layer to connect to the database, authenticate with the server, choose the database and collection, and create, read, update, and delete. Class constructor links to MongoDB. The required code is below:
 
This constructor creates a MongoDB client using a URI that embeds the username and password in the connection string. The aac database and animals collection are obtained after joining. Ping checks connection status. If successful, the console confirms and the instance runs.
CRUD methods are separate. Create() adds a MongoDB document. See the original implementation below:
 
The read() function accepts a query dictionary and returns a list of matching records:
 
The update and delete functions use similar structures:
 
 
These routines match class assignments nicely. They implemented MongoDB CRUD functionality well and provided an easy interface. This code has significant flaws, according to professional engineering examination.
B. Code Analysis Under Software Engineering Principles
Credential management in crud.py is bad. The connection URI includes plaintext username and password. This code is quite unsafe. Putting credentials in code files exposes the database to repository users. Even in academia, this is hazardous and inappropriate in professional settings.
Class breaches of separation of concerns are another major issue. Too many tasks for builders. It sets setup settings, constructs the URI, builds the MongoDB client, manages authentication, selects the database and collection, produces log messages, and handles failures. Scalable and professional architectures may divide these duties into modules so each system component handles one particular function.
Third, CRUD approaches need error handling. Unlike the constructor, CRUD methods do not use try-except blocks for authentication and connection problems. They anticipate every operation to work. For instance, a network outage during an update crashes the software. To smoothly recover from failures, production-quality systems need effective exception handling. This is essential for reliable real-time or multi-user apps.
Very little input validation is applied here. The code examines query and update values as dictionaries but not required fields, data types, or document structure. The database may include inaccurate or incomplete entries without validation.
Artifact lacks logging. The artifact prints console messages instead of updating a structured log. For debugging or auditing, logs must be persistent, timestamped, categorized, and searchable.
Finally, the code lacks unit testing. This makes testing CRUD processes with incorrect queries, connection failures, and corrupted data difficult. A thorough set of automated checks ensures expert installation reliability.
C. Planned Enhancements for Category One
My extensive improvement goal for this item is to make the code safe, maintainable, modular, and real-world-tested. A first enhancement is deleting hard-coded credentials. Dotenv will load credentials from environment variables instead than embedding sensitive information in code. Rather of producing the URI directly.
 
This follows industry standards and eliminates source code credentials.
Refactoring the class improves modularity. Configuration loading, database connection management, and CRUD will be moduleized. Readability and dependency injection increase, making the artifact easier to test.
Each CRUD method will have robust error handling. Some create method updates:
 
This avoids crashes and produces helpful logs.
Custom validation procedures or Pydantic libraries guarantee only valid documents enter the database.
For final testing without a MongoDB server, I will build unit tests using PyTest and mongomock.
Academic implementation will become professional, production-ready with these upgrades.
CATEGORY TWO: ALGORITHMS AND DATA STRUCTURES
Artifact: qtrain() from CS 370
A. Description of Existing Code Functionality
The second artifact I evaluated was CS 370 qtrain(). This function used Q-Learning and neural networks to train a reinforcement learning agent. A labyrinth had barriers, free cells, and a destination. The agent navigated the labyrinth using predicted Q-values.
Hyperparameter loading begins with optional keyword arguments. For example:
 
Environment and experience replay buffer initialization follow:
 
The algorithm balances exploration and exploitation with epsilon-greed. The current implementation includes:
 
Every episode step contains a prior state, action, reward, future state, and flag indicating whether the episode is over. Experience is preserved:
 
Training on new experiences updates the neural network's weights. Every step has training:
 
The function shows period loss and win rates. Training continues until all epochs are completed or the agent wins often.
B. Code Analysis Under Algorithmic and Structural Principles
Understanding algorithmic design and data structures shows this item's improved potential. Every neural network training phase is inefficient. Computationally intensive inner loop training increases runtime without benefit. Training in batches after each episode or at regular intervals is more efficient.
Python lists as experience replay data are another issue. Lists are terrible queues, especially when memory constraints require eliminating older experiences. Deque data structures are more efficient since append and pop are O(1).
Long function does too many tasks. Hyperparameter management, environment interaction, neural network training, performance recording, and termination verification are in one function. This violates the Single Responsibility Principle and hinders code expansion and maintenance.
The function also utilizes global epsilon. Global variables generate hidden dependencies, making applications hard to test and reason about. Rather, handle Epsilon locally or in class.
Documentation is limited. The function does not explain hyperparameter selection or Q-value calculation. Complex reinforcement learning principles need considerable documentation for maintenance.
Insufficient visual performance analysis is last. Without loss curves or win-rate graphs, model improvement or hyperparameter modification cannot be detected.
C. Planned Enhancements for Category Two
To solve the artifact, I will redesign qtrain(). First, split it into select_action(), train_batch(), and epsilon decay update(). Separation improves readability, cognitive strain, and testability.
Using a deque instead of list-based replay memory speeds up append and pop. This data structure will be added to memory management code:
 
Mini-batch train too. after a certain number of steps or after each episode, I will modify the neural network training approach. Change will significantly minimize computational overhead and stabilize learning.
Detailed code documentation follows. Hyperparameters, Q-values, experience replay, and epsilon-greedy exploration will be explained.
I will visualize performance using matplotlib; The improved artifact will feature loss curves, win-rate trends, and reward progression. Illuminates training.
At last, I will export hyperparameters to JSON or YAML. This will make the artifact more versatile and applicable to experiments.
Upgraded algorithms, data structures, and machine learning implementation will be found in the artifact.
CATEGORY THREE: DATABASES
Artifact: MongoDB Integration Layer from CS 340
A. Detailed Description of Existing Database Functionality
The CS 340 database integration project was my third evaluation. This component connects to Apporto's MongoDB. This class handles all data operations: create, read, update, and delete.
The database connection code follows:
 
Flexible JSON-like documents are used by MongoDB. This flexibility let me integrate animal recordings with diverse structures in the original course. Some records lacked breed information. Flexibility helps early prototyping but may be dangerous if uncontrolled.
All CRUD actions visit the collection. Example: update
 
and the delete operation:
 
These actions enable the UI layer to filter, search, and alter animal data.
B. Database Review Under Professional Standards
A greater understanding of databases reveals numerous key flaws. Hard-coded credentials in the connection string are the first issue. This exposes the database to unauthorized access.
Lack of schema validation is another concern. MongoDB does not require a schema, but schema validation rules organize and standardize. The current implementation allows adding any document, regardless of fields or formats.
Collection lacks indexes. Database searches may lag without indexes as datasets grow. If users often search for animals, index breed and result data to improve query performance.
Also lacking: database error handling. Without exception handling, the program crashes whenever a query or database operation fails unexpectedly. Systems that must be reliable confront this.
Finally, sensitive data is unencrypted. Unencrypted owner and medical notes are dangerous.
C. Planned Enhancements for Category Three
My first enhancement is secure credential management. Dotenv library environment variables preserve all connection info.
JSON schema rules verify MongoDB schema next. As an example:
 
This will standardize all inserted papers.
To increase query efficiency, I will index breed and age often searched fields:
 
I will encrypt sensitive fields using the cryptography library. Error handling will include try-except blocks around all database requests.
Finally, I will emulate MongoDB interactions using PyTest and mongomock unit tests.
Conclusion
In conclusion, this code review helped me assess my work professionally and discover areas for development. I found security, maintainability, performance, scalability, algorithmic efficiency, and database integrity problems for each item. My update proposals demonstrate my program understanding and professional software development mindset. I will transform student work into industry-ready professional portfolio components with capstones.

