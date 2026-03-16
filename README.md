# BrewAI

BrewAI is an intelligent coffee shop assistant that interacts with users to provide coffee shop services such as showing the menu, telling drink prices, recommending drinks, and taking orders.

## Features

- **Show Menu**: Display the current coffee menu.
- **Tell Drink Prices**: Provide prices for specific drinks.
- **Recommend Drinks**: Suggest coffee options based on user preferences.
- **Take Orders**: Accept orders for coffee drinks.

## Project Structure

- `src/agent/chat_agent.py`: Handles incoming tool call messages and interacts with the necessary functions to fulfill user requests.
- `src/agent/prompts.py`: Contains predefined system messages that govern BrewAI's interaction rules and capabilities.
- `src/database/db.py`: Manages database connections.
- `app.py`: Initializes the database and launches the user interface.

## Usage

To run the application:

1. Ensure you have an appropriate Python environment setup.
2. Run the application using:
   ```bash
   python app.py
   ```
   This will seed the database with menu data and launch the user interface.

## Dependencies

- Python 3.x
- SQLite (for database management)

## Contributing

Feel free to open issues or submit PRs to improve the functionality or fix issues within BrewAI.

## License

[Specify your license here]
