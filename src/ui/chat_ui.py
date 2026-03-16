import gradio as gr
from src.agent.chat_agent import chat

def launch_ui():
    gr.ChatInterface(
        fn=chat,
        title="☕ BrewAI Coffee Assistant"
    ).launch()