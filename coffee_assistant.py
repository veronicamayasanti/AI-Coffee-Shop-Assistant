import os
import json
from platform import system

from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
import sqlite3

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key:
    print("API key loaded")
else:
    print("API key not loaded")

MODEL = "gpt-4.1-mini"
client = OpenAI()

system_message = """
You are a helpful assistant for a coffee shop called BrewAI.
Answer politely and briefly in one sentence.
Help customers with coffee menu prices.
"""

price_function = {
    "name": "get_coffee_price",
    "description": "Get the price of a coffee drink from the menu",
    "parameters": {
        "type": "object",
        "properties": {
            "drink_name": {
                "type": "string",
                "description": "The coffee drink the customer wants"
            }
        },
        "required": ["drink_name"],
        "additionalProperties": False
    }
}

tools = [{"type": "function", "function": price_function}]

DB = "coffee_prices.db"

with sqlite3.connect(DB) as conn:
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu (
        drink TEXT PRIMARY KEY,
        price REAL
    )
    """)

def set_coffee_price(drink, price):
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO menu (drink, price)
            VALUES (?, ?)
            ON CONFLICT(drink) DO UPDATE SET price=?
            """,
            (drink.lower(), price, price)
        )

menu_prices = {
    "espresso": 15000,
    "latte": 16000,
    "cappuccino": 17000,
    "americano": 18000,
    "mocha": 19000
}

for drink, price in menu_prices.items():
    set_coffee_price(drink, price)

def get_coffee_price(drink):
    print(f"DATABASE TOOL CALLED: Getting price for {drink}")

    with sqlite3.connect(DB) as conn:
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

def handle_tool_calls(message):

    responses = []

    for tool_call in message.tool_calls:

        if tool_call.function.name == "get_coffee_price":

            arguments = json.loads(tool_call.function.arguments)

            drink = arguments.get("drink_name")

            result = get_coffee_price(drink)

            responses.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })

    return responses

def chat(message, history):

    history = [{"role": h["role"], "content": h["content"]} for h in history]

    messages = [{"role": "system", "content": system_message}] + history + [
        {"role": "user", "content": message}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools
    )

    while response.choices[0].finish_reason == "tool_calls":

        message = response.choices[0].message

        tool_responses = handle_tool_calls(message)

        messages.append(message)
        messages.extend(tool_responses)

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

    return response.choices[0].message.content

gr.ChatInterface(fn=chat, title="☕ Coffee Shop Assistant").launch()