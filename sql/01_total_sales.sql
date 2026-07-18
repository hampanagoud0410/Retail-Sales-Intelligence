SELECT
    SUM(
        p.selling_price *
        oi.quantity *
        (1 - oi.discount / 100.0)
    ) AS total_revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id;
