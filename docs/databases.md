CS 499 Milestone Four
Enhancement Three: Databases
Student: Divya Rangaraj
Course: CS-499 Computer Science Capstone

 
1. Description of the Artifact
Enhancement 3 utilizes CS340 crud.py. This Python and MongoDB online software creates, reads, changes, and deletes animal shelter data. An artifact from CS 340 covering client-server architectures, MongoDB integration, and NoSQL document storage. The purpose was to link Flask users to a distant MongoDB server for structured data interaction. First AnimalShelter class operated MongoDB client, kept connection parameters, and supported insert_one, find, update_many, and delete_many CRUD requests.
Early database interfaces were procedural. There was no data validation, indexing, normalization, or environmental security for essential credentials. Initial code hard-coded MongoDB URI:
self.uri = "mongodb://aacuser:aacuser123@nv-desktop-services.apporto.com:34540/aac?authSource=aac"
The class constructor connected to MongoDB without setup or database structure abstraction using this URI. All CRUD methods searched for dictionaries before MongoDB transactions. Although it matched assignment requirements, it lacked database engineering expertise and robustness. It enhanced database categories with safe setup, data validation, schema refinement, normalization, indexing, query optimization, and professional database design.
To demonstrate my database skills, I developed a basic script into a secure, maintainable, and scalable database access layer. Note that CS 499's capstone covers database theory and professional database engineering.
2. Justification for Inclusion in the ePortfolio
In my ePortfolio, I cover database interface, architecture, data security, and efficient query techniques. Previous solutions met CRUD needs but not professional software engineering requirements for database safety, scalability, and data assurance. I applied my collegiate database abilities to commercial standards including secure credential management, indexing, schema validation, and normalization by improving the artifact.
Updates to database credentials and setup parameters improve artifacts. Baseline credentials in source code violated database-driven application security. The updated code uses dotenv to handle environmental parameters. Secure.env files store the MongoDB connection string outside of version control to protect credentials and fulfill contemporary database and software engineering frameworks' secure software development standards (Silberschatz et al., 2020). Better code:
from dotenv import load_dotenv
import os

load_dotenv()

self.user = os.getenv("DB_USER")
self.password = os.getenv("DB_PASS")
self.host = os.getenv("DB_HOST")
self.port = os.getenv("DB_PORT")
self.database_name = os.getenv("DB_NAME")
Schools and employers may see I make secure database-backed applications.
This version improves database stability and traceability by detecting and reporting errors. Database exception handling as per professional software engineering standards may cause botched transactions, incomplete writes, and application-level failures. The revised read function splits database requests in organized exception handling for predictable system behavior:
try:
    results = self.collection.find(query)
    logging.info("Query executed successfully.")
    return list(results)
except Exception as e:
    logging.error(f"Error executing read operation: {e}")
    return []
This item improved ePortfolio database performance and data retrieval. Indexing frequently accessed columns speeds database searches and reads in the upgraded version. Indexing simplifies queries and improves database performance in MongoDB, which does not require a schema.
The augmented artifact conceptually normalizes data entry and validation. Normalization-inspired solutions reduce data inconsistency and duplication in schema-flexible MongoDB, enhancing maintainability and lowering storage redundancy. Silberschatz et al. (2020) that database designers learn First, Second, and Third Normal Form.
This artifact now shows my ability to build CRUD operations, use advanced database design, maximize performance, enforce security, and ensure data integrity. These skills are required for back-end, full-stack, and data engineers. This updated item in my ePortfolio shows my computer science talents and knowledge of theoretically sound and industry-aligned database strategies.
3. Demonstrating the Course Outcomes and Updates to Outcome Coverage
This artifact was enhanced for Module One. I used computer science to create and evaluate ordered logical computing systems. My creation enhances database architecture, security, retrieval, and manipulation.
The first course result challenges students to design and evaluate algorithmic computer solutions. Indexing and database interface validation accelerated queries. Flexible MongoDB might be unreliable and challenging to query if validated poorly. Validation and normalization-inspired changes demonstrate algorithmic data access, structure, and maintenance.
Second, new, proven computing approaches, tools, and talents are emphasized. I log databases, secure credentials, and handle structured exceptions using environment variables. These modifications were made using the professional-recommended dotenv package and Python logging module. Implementing them proves I know software development theory and tools.
I stressed security to minimize system design problems. Eliminating hard-coded passwords, checking user inputs, and managing errors improved artifact security. These improvements complement Pressman and Maxim's (2020) database vulnerability and safe software engineering emphasis.
Since the improvements fulfilled my goals, my outcome-coverage approaches have not altered. I help with software design, security, problem-solving, and computing. My database and application abilities confirm I reached this milestone.
4. Reflection on the Enhancement Process
The new database-focused parts of this artifact help me understand theoretical database fundamentals. I learned how safe, orderly, and efficient data management and database architecture affect application performance and reliability.
Small database design changes may have long-term implications, according to an update. In CS 340, I needed this to access the database and conduct simple CRUD. I discovered databases require durability. Though it may not break the code, hard-coding credentials may compromise application security. Lack of indexes or input checks may generate inefficiencies and data quality issues as collection grows. Speed, security, and maintainability are needed for scalable database systems, this update said.
Again, efficient logging and error handling taught. Python's logging design taught me how crucial production logging is without debugging. Developers use detailed logs to detect bugs and oddities. It taught me to build useful, transparent, and robust systems. Success and exceptions from better reading:
def read(self, query):
    try:
        results = self.collection.find(query)
        logging.info("Query executed successfully.")
        return list(results)
    except Exception as e:
        logging.error(f"Error during read operation: {e}")
        return []
I learned from this upgrade that database engineering requires failure and success readiness.
Challenges were educational during this progress. Runtime-wide environment variables were difficult to implement. Testing revealed various connection issues as the.env file failed to load. I need to enhance file path and environment variable approaches. Another issue was data validation logic rearrangement. Data consistency without impacting NoSQL document model semantics may be achieved using normalization-inspired methods. This balance required preparation and MongoDB document structure knowledge.
MongoDB indexing was problematic due to uncertain source dataset variables. Avoiding indexing mixed-data fields required testing. These problems taught me NoSQL schema flexibility and data purity.
It improved my database development. We covered database security, error management, query optimization, indexing, and schema validation. My software development and database architecture design abilities increased. Artifact correctness, professional quality, maintainability, and industry-standard alignment boost my ePortfolio.
 
References
Pressman, R. S., & Maxim, B. R. (2020). Software engineering: A practitioner’s approach (9th ed.). McGraw-Hill Education.
Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020). Database system concepts (7th ed.). McGraw-Hill Education.
Python Software Foundation. (2024). Logging facility for Python. https://docs.python.org/3/library/logging.html

