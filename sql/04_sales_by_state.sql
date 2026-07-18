SELECT

    s.state,

    SUM(
        p.selling_price *
        oi.quantity
    ) AS revenue

FROM orders o

JOIN stores s

ON o.store_id = s.store_id

JOIN order_items oi

ON o.order_id = oi.order_id

JOIN products p

ON oi.product_id = p.product_id

GROUP BY s.state

ORDER BY revenue DESC;