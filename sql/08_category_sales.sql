SELECT
    c.category_name,
    ROUND(
        SUM(
            p.selling_price *
            oi.quantity *
            (1 - oi.discount / 100.0)
        ),
        2
    ) AS revenue
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
JOIN categories c
    ON p.category_id = c.category_id
GROUP BY c.category_name
ORDER BY revenue DESC;