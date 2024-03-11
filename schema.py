import sqlite3

conn = sqlite3.connect('product_database.db')
cursor = conn.cursor()

create_product_category_table = """
CREATE TABLE IF NOT EXISTS Product_Category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    created_at TIMESTAMP,
    modified_at TIMESTAMP,
    deleted_at TIMESTAMP
)
"""

create_product_table = """
CREATE TABLE IF NOT EXISTS Product (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    SKU TEXT,
    category_id INTEGER,
    inventory_id INTEGER,
    price DECIMAL(10, 2),
    discount_id INTEGER,
    created_at TIMESTAMP,
    modified_at TIMESTAMP,
    deleted_at TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Product_Category(id),
    FOREIGN KEY (inventory_id) REFERENCES Product_Inventory(id),
    FOREIGN KEY (discount_id) REFERENCES Discount(id)
)
"""

create_product_inventory_table = """
CREATE TABLE IF NOT EXISTS Product_Inventory (
    id INTEGER PRIMARY KEY,
    quantity INTEGER,
    created_at TIMESTAMP,
    modified_at TIMESTAMP,
    deleted_at TIMESTAMP
)
"""

create_discount_table = """
CREATE TABLE IF NOT EXISTS Discount (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    discount_percent DECIMAL(10, 2),
    active BOOLEAN,
    created_at TIMESTAMP,
    modified_at TIMESTAMP,
    deleted_at TIMESTAMP
)
"""

# Execute the SQL statements to create tables
cursor.execute(create_product_category_table)
cursor.execute(create_product_table)
cursor.execute(create_product_inventory_table)
cursor.execute(create_discount_table)

# Sample data for product_category
product_category_data = [
    ('Electronics', 'Category for electronic products'),
    ('Clothing', 'Category for clothing items')
]

# Sample data for product
product_data = [
    (1, 'Laptop', 'High-performance laptop', 'SKU123', 1, 1, 999.99, None),
    (2, 'T-shirt', 'Casual cotton t-shirt', 'SKU456', 2, 2, 19.99, 1)
]

# Sample data for product_inventory
product_inventory_data = [
    (1, 10),
    (2, 50)
]

# Sample data for discount
discount_data = [
    ('10% Off', '10% discount for all products', 10.00, True)
]

# SQL statements to insert sample data
insert_product_category = "INSERT INTO Product_Category (name, description, created_at, modified_at, deleted_at) VALUES (?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL)"
insert_product = "INSERT INTO Product (id, name, description, SKU, category_id, inventory_id, price, discount_id, created_at, modified_at, deleted_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL)"
insert_product_inventory = "INSERT INTO Product_Inventory (id, quantity, created_at, modified_at, deleted_at) VALUES (?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL)"
insert_discount = "INSERT INTO Discount (name, description, discount_percent, active, created_at, modified_at, deleted_at) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL)"

# Insert sample data into respective tables
cursor.executemany(insert_product_category, product_category_data)
cursor.executemany(insert_product, product_data)
cursor.executemany(insert_product_inventory, product_inventory_data)
cursor.executemany(insert_discount, discount_data)

# Commit changes and close connection
conn.commit()
conn.close()
