SELECT

    p.product_name,

    SUM(oi.quantity) AS total_quantity,

    SUM(
        p.selling_price *
        oi.quantity
    ) AS revenue

FROM order_items oi

JOIN products p

ON oi.product_id = p.product_id

GROUP BY p.product_name

ORDER BY revenue DESC

LIMIT 10;