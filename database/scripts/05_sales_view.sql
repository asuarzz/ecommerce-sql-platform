CREATE OR ALTER VIEW v_SalesPerformance AS
SELECT 
    u.user_id,
    u.first_name + ' ' + u.last_name AS customer_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_spent,
    MAX(o.order_date) AS last_purchase_date

FROM Users u
LEFT JOIN Orders o ON u.user_id = o.user_id
LEFT JOIN OrderItems oi ON o.order_id = oi.order_id
GROUP BY u.user_id, u.first_name, u.last_name;