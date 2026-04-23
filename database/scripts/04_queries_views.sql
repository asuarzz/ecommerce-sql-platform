--1. Simple Join (What you already did)
--Technical English: "Joining orders with users"
SELECT
    o.order_id,
    u.first_name,
    o.total_amount;
FROM Orders o
INNER JOIN Users u ON o.user_id = u.user_id;

--CREATE A VIEW (The professional way)
--We call it 'v_OrderSummaries' (v for View)
IF OBJECT_ID('v_OrderSummaries', 'V') IS NOT NULL
    DROP VIEW v_OrderSummaries;
GO

CREATE VIEW v_OrderSummaries AS
SELECT
    o.order_id,
    u.first_name + ' ' + u.last_name AS customer_name,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * o.unit_price) AS line_total
FROM Orders o
INNER JOIN Users u ON o.user_id = u.user_id
INNER JOIN OrderItems oi ON o.order_id = oi.order_id
INNER JOIN Products p ON oi.product_id = p.product_id;
GO