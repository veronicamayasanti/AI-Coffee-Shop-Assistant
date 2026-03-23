import sqlite3

DB_PATH = "data/coffee.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():

    with get_connection() as conn:
        cursor = conn.cursor()

        print("Initializing database...")

        # Dropping the existing menu table to recreate it with new schema
        cursor.execute("DROP TABLE IF EXISTS menu")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price INTEGER NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT
        )
        """)

        conn.commit()
        print("Database initialized.")

def seed_menu():

    menu_items = [
        ('Latte', 'drink', 30000),
        ('Cappuccino', 'drink', 32000),
        ('Americano', 'drink', 25000),
        ('Mocha', 'drink', 35000),
        ('Sandwich', 'food', 40000),
        ('Croissant', 'food', 30000),
        ('Chocolate Cake', 'food', 35000),
        ('Cheese Cake', 'food', 38000)
    ]
    with get_connection() as conn:
        cursor = conn.cursor()

        for name, category, price in menu_items:
            cursor.execute(
                """
                INSERT OR IGNORE INTO menu (name, category, price)
                VALUES (?, ?, ?)
                """,
                (name, category, price)
            )
            print(f"Inserted menu item: {name}, Category: {category}, Price: {price}")

        conn.commit()

def init_and_seed_db():
    init_db()
    seed_menu()
