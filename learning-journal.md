#Learning Journal - Alejandro's Data Engineering Path

##Day 1 - 2026/04/22
-Reorganized my project structure
-Created .env file to protect my database credentials
-Created .gitignire to prevent secrets from going to GitHub
-Learned why passwords never be in source code 

###What I learned 
-The .env file store secrets outside of the code 
-The .gitignore tells Git which files never upload


###Dificult parts
-Understanding were each file goes in the project structure

##Day 2 - 2026/04/23
-Created, Users, Products and Orders tables (01_create_table.sql)
-Established relationships using Foreign Keys to ensure data integrity
-Populated tables with initial data test (02_insert_data.sql)
-Created the OrderItems bridge table to handle many-to-many relationships (03_create_order_items.sql)
-Mastered INNER JOIN connecting 4 different tables in a single query
-Debugged syntax error related to SQL aliases (oi, u , p), and pluralization
-Created Database View (v_OrderSummaries) to abstract complex JOIN logic

###What I learned
-Foreign Keys enforce data integrity between related tables
-Bridge tables solve many-to-many relantionships between entities
-VIEWs decouple complex logic from the application layer
-Aliases make qu¡eries readable but need to be consistent throughout

###Difficult parts
-Understanding when to use a bridge table vs direct relationships
-Debugging alias errors when multiple table share similar column names

##Day 3 - 2026/04/24
-Implemented the **Context Manager** pattern (`__enter__` / `__exit__`) in Python
-Refactored `main.py` to use the `with` statement for automatic resource cleanup

###What I learned
-Using `with` ensures database connections close automatically, preventing memory leaks.
-How `__enter__` and `__exit__` work under the hood to manage object lifecycles

###Day 4 - 2026/04/25
-Installed and integrated the Faker library for synthetic data generation
-Created `seed_data.py` to automate the population of the database
-Implemented `Parameterized Queries`using `?` to prevent SQL injection
-Successfully generated 10 realistic users records into SQL Server

###What I learned
-The concept of `Data Mocking` and his importance of using realistic synthetic data for testing scalability
-How SQL UNIQUE constraints protects the database from duplicates automated entries
-Why passing data though `params`is safer than string formatting in SQL

###Diffcult parts
-Understanding why "re-running"an script can lead to data accumulation or constraints violations

###Day 5 - 2026/04/26
-Created `reset_db.py` to handle data to cleanup

###What I learned
-Undertood why child records (OrderItems) must be deleted before parent record (Users) to avoid Foreign Key violations

###Day 6 - 2026/04/27
-Developed `generate_sales.py` to automate the transaction workflow
-Used `@@IDENTITY` to capture the auto-generated primary key from SQL Server

###What I learned
-Why is mandatory to fetch existig IDs before inserting child records to mantain Referential Integrity
-**Transactional Logic:** The business process of splitting a single purchase into two tables (Order summary vs. Item details)
-How to use Python's `random` library to create diverse testing scenarios

###Difficult parts
-Ensuring the loops correctly mapped products to the specific `order_id` generated in the previous step

###Day 7 - 2026/04/28
-Created a SQL View `v_SalesPerformance` to aggregate business data
-Developed `check_performance.py` to extract and format data for end-users
-Implemented `LEFT JOIN` logic in views to include users with zero sales

###What I learned
-Why using a SQL VIEW is better than hardcoding complex JOINs in Python
-Using Python's f-strings (`:<25`) to create clean, readable tables in the terminal

###Difficult parts
-Understanding why `LEFT JOIN` is necessary: if I use `INNER JOIN`, users who haven't bought anything desappear from the report
-Formatting floating-point numbers in python to show exactly two decimals for currency
