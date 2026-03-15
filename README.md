# ☕ AI Coffee Shop Assistant

This is a simple web-based chatbot that acts as a virtual assistant for a coffee shop called "BrewAI". It can provide information about menu items and their prices by leveraging the OpenAI API with function calling and a local SQLite database.

---

### Key Features
- **Interactive Chat Interface**: A user-friendly web UI powered by Gradio.
- **Natural Language Understanding**: Uses OpenAI's GPT models to understand customer queries.
- **Function Calling**: Employs OpenAI's function calling feature to query a local database for real-time coffee prices.
- **Persistent Data**: Menu prices are stored and managed in a local SQLite database.
- **Secure Configuration**: API keys are kept secure and separate from code using a `.env` file.

---

### Technology Stack
- **Backend**: Python
- **AI Model**: OpenAI API (GPT-4)
- **Web UI**: Gradio
- **Database**: SQLite
- **Environment Management**: python-dotenv

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites
- Python 3.8 or newer
- An OpenAI API Key

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/AI-Coffee-Shop-Assistant.git
    cd AI-Coffee-Shop-Assistant
    ```
    *(Jangan lupa ganti `your-username` dengan username GitHub Anda)*

2.  **Create and activate a virtual environment:**
    This keeps your project dependencies isolated.

    - **On Windows:**
      ```sh
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - **On macOS & Linux:**
      ```sh
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure your API Key:**
    - Create a new file named `.env` in the root directory of the project.
    - Add your OpenAI API key to the `.env` file like this:
      ```
      OPENAI_API_KEY='your_secret_api_key_here'
      ```

### Running the Application

1.  **Execute the main script:**
    ```sh
    python coffee_assistant.py
    ```

2.  **Open the interface:**
    The terminal will display a local URL (usually `http://127.0.0.1:7860`). Open this URL in your web browser to start chatting with the assistant.
