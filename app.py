from src.ui.chat_ui import launch_ui
from src.database.db import init_and_seed_db as setup_database


if __name__ == "__main__":

    setup_database()
    launch_ui()
