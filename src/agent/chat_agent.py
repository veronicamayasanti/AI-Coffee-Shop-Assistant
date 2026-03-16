import json
from src.config.settings import client, MODEL
from src.tools.coffee_tools import (
    get_coffee_price,
    show_menu,
    recommend_coffee,
    place_order
)
from src.tools.tool_registry import tools
from src.agent.prompts import SYSTEM_MESSAGE_V1

def handle_tool_calls(message):

    responses = []

    for tool_call in message.tool_calls:

        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments or "{}")

        if name == "get_coffee_price":

            result = get_coffee_price(args["drink_name"])

        elif name == "show_menu":

            result = show_menu()

        elif name == "recommend_coffee":

            result = recommend_coffee()

        elif name == "place_order":

            result = place_order(args["drink_name"])

        responses.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result
        })

    return responses

def chat(message, history):

    history = [{"role": h["role"], "content": h["content"]} for h in history]

    messages = [
                   {"role": "system", "content": SYSTEM_MESSAGE_V1}
               ] + history + [
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

