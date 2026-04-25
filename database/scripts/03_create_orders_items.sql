--OrderItems: is the bridge between Products and Orders.
--Tell Us WHAT Products are in EACH Order

CREATE TABLE OrderItems(
    item_id INT PRIMARY KEY IDENTITY(1,1),
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT CHECK(quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY(order_id) REFERENCES Orders(order_id) ON DELETE NO ACTION,
    FOREIGN KEY(product_id) REFERENCES Products(product_id) ON DELETE NO ACTION
);

--Insert sample order items
INSERT INTO OrderItems(order_id, product_id, quantity, unit_price)
    VALUES
        --Order 3 (Alberto): bought one HP Laptop at \$500.22
        (3, 1, 1, 500.22),
        --Order 3(Alberto): Also bought 2 Asus laptops at \$750.30 each
        (3, 2, 2, 750.30),
        --Order 4 (Manuel): Bought one Asus laptop at \$750.30
        (4, 2, 1, 750.30);