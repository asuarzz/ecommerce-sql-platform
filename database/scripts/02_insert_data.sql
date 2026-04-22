
INSERT INTO Users (first_name, last_name, email)
    VALUES
        ('Alberto', 'Rodriguez', 'alb@aol.com'),
        ('Manuel', 'Alvarez', 'man@aol.');

INSERT INTO Products(product_name, category, price)
    VALUES
        ('hp','laptop', 500.22),
        ('Asus', 'laptop', 750.30 );

INSERT INTO Orders(user_id, total_amount)
    VALUES
        (1, 500.22),
        (2, 600);

UPDATE Users
SET email = 'man@aol.com'
WHERE user_id = 2;

SELECT *
FROM Users;

SELECT *
FROM Products;

SELECT *
FROM Orders;