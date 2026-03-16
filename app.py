from src.ui.chat_ui import launch_ui
from src.database.db import init_db, seed_menu


if __name__ == "__main__":

    init_db()
    seed_menu()

    launch_ui()