SELECT
    SUM(
        (
            p.selling_price -
            p.cost_price
        ) *
        oi.quantity *
        (1 - oi.discount / 100.0)
    ) AS total_profit
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id;