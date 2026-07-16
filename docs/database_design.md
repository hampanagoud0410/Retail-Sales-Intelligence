# Database Design

## Tables

### Customers
- customer_id (PK)
- first_name
- last_name
- gender
- age
- city
- state
- join_date

### Categories
- category_id (PK)
- category_name

### Products
- product_id (PK)
- category_id (FK)
- product_name
- brand
- cost_price
- selling_price

### Stores
- store_id (PK)
- store_name
- city
- state

### Orders
- order_id (PK)
- customer_id (FK)
- store_id (FK)
- order_date

### Order_Items
- order_item_id (PK)
- order_id (FK)
- product_id (FK)
- quantity
- discount

### Payments
- payment_id (PK)
- order_id (FK)
- payment_method
- payment_status

### Returns
- return_id (PK)
- order_item_id (FK)
- return_reason
- return_date