import sqlite3

DB_PATH = "data/coffee.db"

def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            drink TEXT PRIMARY KEY,
            price REAL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            drink TEXT
        )
        """)

        conn.commit()

def seed_menu():

    menu_items = {
        "espresso": 1,
        "americano": 2,
        "caffè latte": 3,
        "cappuccino": 4,
        "flat white": 5,
        "es kopi susu gula aren": 6,
        "caramel macchiato": 1,
        "caffè mocha": 2,
        "hazelnut latte": 3,
        "spanish latte": 4,
        "cold brew": 5,
        "avocado coffee": 6,
        "dalgona coffee": 1,
        "sea salt latte": 2,
        "coconut coffee": 3
    }

    with get_connection() as conn:
        cursor = conn.cursor()

        for drink, price in menu_items.items():

            cursor.execute(
                """
                INSERT OR IGNORE INTO menu (drink, price)
                VALUES (?, ?)
                """,
                (drink, price)
            )

        conn.commit()