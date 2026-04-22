--Create users table
CREATE TABLE Users(
    user_id INT PRIMARY KEY IDENTITY(1,1), --Unique ID that sum itself( 1, 2, 3)
    first_name VARCHAR(50) NOT NULL, -- It can't be empty
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,  --It can't be two equal emails
    created_at DATETIME DEFAULT GETDATE()
);

--Create table products
CREATE TABLE Products(
    product_id INT PRIMARY KEY IDENTITY(1,1),
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2) CHECK (price > 0), --Gold rule, the price has to be always higher than 0
    stock INT DEFAULT 0
);

--Create the order table (the bridge)
CREATE TABLE Orders(
    order_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT,
    order_date DATETIME DEFAULT GETDATE(),
    total_amount DECIMAL(10, 2) ,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)--If a user is deleted, we don't want orphan orders
);

