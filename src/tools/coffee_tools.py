import random
from src.database.db import get_connection

def get_coffee_price(drink):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT price FROM menu WHERE drink = ?",
            (drink.lower(),)
        )

        result = cursor.fetchone()

    if result:
        return f"The price of {drink} is ${result[0]}"
    else:
        return f"Sorry, we don't have {drink} on the menu."


def show_menu():

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT name, category, price FROM menu")

        items = cursor.fetchall()

    if not items:
        return "The menu is currently empty."

    menu_text = "Here is our menu:\n"

    for name, category, price in items:
        menu_text += f"{name.title()} ({category}) - Rp{price}\n"

    return menu_text


def recommend_coffee():

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT drink FROM menu")

        drinks = cursor.fetchall()

    if not drinks:
        return "Sorry, I cannot recommend a drink right now."

    drink = random.choice(drinks)[0]

    return f"I recommend trying our {drink}!"

def place_order(drink):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO orders (drink) VALUES (?)",
            (drink.lower(),)
        )

        conn.commit()

    return f"Your order for {drink} has been placed ☕"
