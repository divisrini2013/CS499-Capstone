CS 499 Milestone Two
Enhancement One Narrative: Software Design and Engineering
Name: Divya Rangaraj
Course: CS 499 – Computer Science Capstone
Artifact: Enhanced MongoDB CRUD Module (crud.py)

 
1. Artifact Description
The Python module Crud.py from CS 340: Client/Server Development is my Software Design and Engineering upgrade. In early 2024, I constructed a Flask-based web application that linked to MongoDB to conduct CRUD operations on the Animal Adoption Center's animal records collection. The item included all AnimalShelter backend database communication. It created a database connection in its constructor, saved connection information in code, and offered MongoDB animal data CRUD capabilities.
Although functional, the initial implementation had engineering issues. It has hard-coded credentials:
self.uri = "mongodb://aacuser:aacuser123@nv-desktop-services.apporto.com:34540/aac?authSource=aac"
Although this connection string succeeded, revealing sensitive credentials in the source code was hazardous. It lacked modularity, logging, and ordered error handling. CRUD operations were excellent but lacked industrial maintainability, security, and resilience. It may enhance software engineering, secure design, modular architecture, validation, and maintainability due to these restrictions.
2. Justification for Inclusion in My ePortfolio
My ePortfolio contains this item because it shows my software engineering journey from functional programming to professional software architecture. Many novice projects focus on “making the program run,” but this artifact showed secure code, modularity, logging, environment, and database engineering best practices. These skills are essential for backend and full-stack computer science.
The item shows my abilities to discover and fix old code issues for engineering criteria. Several crucial features of the upgraded artifact demonstrate these talents. As an example:
Secure Configuration Management
Using python-dotenv to replace hard-coded credentials with environment variables was the biggest improvement. Updated connection logic uses:
 
Secure credential processing avoids security breaches and safeguards critical systems.
Improved Modularity
In the original class, one file handled connections, error messages, and CRUD. I moduleized settings, connection setup, and CRUD to rebuild the artifact. The Single Responsibility Principle is respected and code expansion is simplified.
Enhanced Error Handling and Logging
I replaced print() statements with structured logging:
 
using MongoDB exception handling. This facilitates debugging and auditing and promotes professional coding.
Validation and Defensive Programming
New validation ensures CRUD inputs match structures:
 
We secure the system against mistakes and hazardous data.
These improvements turned the class assignment into a professional ePortfolio. My upgraded artifact shows my technological maturity and ability to build safe, modular, maintainable, industry-ready software.
3. Course Outcomes Addressed
To improve, I chose course outcomes in Module One. Once finished, I checked that the improvement meets and occasionally exceeds my expectations. Discussed outcomes:
Outcome 3: Use algorithms and computer science to design and assess computing solutions
Redesigning the AnimalShelter module showed my abilities to analyze a computer solution, identify structural faults, and restructure it using modularization, separation of concerns, and design patterns. The modified artifact fulfills software engineering scalability, readability, and reuse standards.
Outcome 4: Use proven and new computing methods, skills, and tools
After this adjustment, I used dotenv, pytest, and Python's logging library. Now error handling matches professional backends. Using current libraries and tools increased product security and maintainability.
Outcome 5: Develop a security mindset
The upgrading process supported this conclusion since I included secure credential processing, defensive code, exception management, and validation. Secure design moves credentials from source code to environment variables. I checked queries for errors and noted them.
Updates to Planned Outcome Coverage
My original plan focused Outcomes 4 and 5. By enhancing architecture, addressing design trade-offs, and rearranging code for maintainability, I achieved Outcome 3. Now I cover all three outcomes.
4. Reflection on the Enhancement Process
I enjoyed the upgrading process and got one of the greatest computer science major hands-on experiences. I thought the artifact needed minor changes, but it needed structural redesign, security, error handling, and greater documentation to be professional. Now I know the difference between functioning and professional coding.
The Single Responsibility Principle and modular system design were my main learning. Originally, one class handled setup, connection, and CRUD. Small changes might interrupt the class since the code was tougher to understand. By moduleizing code, I discovered how modularity simplifies and clarifies. Testing is easy since each component may be assessed separately.
Also useful was learning about security vulnerability fixes. After reviewing my code, I was astonished at how easily I ignored hard-coded credentials while building the artifact. Technical project success was my goal. Developers without security plans make software susceptible, as this update taught me. I questioned configuration management, deployment environments, and how professional software teams secure sensitive data due to environment variable credentials.
Logging and error management were tricky. Log levels, formatting, file management, and sensitive data capture were needed for proper logging. The logger writes to the wrong file and structured errors wrongly. Debugging these difficulties showed me that logs are essential for long-term maintenance and should be a system component, not an add-on.
Getting test-driven development. Writing pytest tests forced me consider edge cases and failure strategies. It revealed original code faults and usability concerns I may have missed. I learned how comprehensive testing improves software dependability and maintainability.
The artifact got stronger, safer, and more professional while helping me develop. I witnessed how engineering errors might generate serious vulnerabilities or long-term maintenance after applying industry standards. The modification enhanced the artifact and my software engineering skills.

 
References
Pressman, R. S., & Maxim, B. R. (2020). Software engineering: A practitioner’s approach (9th ed.). McGraw-Hill Education.
Hunt, A., & Thomas, D. (2019). The pragmatic programmer: Your journey to mastery (20th anniversary ed.). Addison-Wesley Professional.
Banker, K., Bakkum, P., Garret, B., Verch, M., & Chodorow, K. (2016). MongoDB in action (2nd ed.). Manning Publications.
