SELECT
    strftime('%Y-%m', o.order_date) AS month,
    ROUND(
        SUM(
            p.selling_price *
            oi.quantity *
            (1 - oi.discount / 100.0)
        ),
        2
    ) AS revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY month
ORDER BY month;