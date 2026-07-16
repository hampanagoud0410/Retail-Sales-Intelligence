-- ==========================================
-- Retail Sales Intelligence Platform
-- Database Schema
-- ==========================================

DROP TABLE IF EXISTS returns;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS stores;
DROP TABLE IF EXISTS customers;

-- Customers
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gender TEXT,
    age INTEGER,
    city TEXT,
    state TEXT,
    join_date DATE
);

-- Categories
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL
);

-- Products
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    product_name TEXT NOT NULL,
    brand TEXT,
    cost_price REAL,
    selling_price REAL,
    FOREIGN KEY(category_id) REFERENCES categories(category_id)
);

-- Stores
CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY AUTOINCREMENT,
    store_name TEXT,
    city TEXT,
    state TEXT
);

-- Orders
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    store_id INTEGER,
    order_date DATE,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(store_id) REFERENCES stores(store_id)
);

-- Order Items
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    discount REAL,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);

-- Payments
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER UNIQUE,
    payment_method TEXT,
    payment_status TEXT,
    FOREIGN KEY(order_id) REFERENCES orders(order_id)
);

-- Returns
CREATE TABLE returns (
    return_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_item_id INTEGER UNIQUE,
    return_reason TEXT,
    return_date DATE,
    FOREIGN KEY(order_item_id) REFERENCES order_items(order_item_id)
);