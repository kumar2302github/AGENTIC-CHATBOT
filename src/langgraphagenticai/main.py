import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI


def load_langgraph_agenticai_app():
    """
    Load the LangGraph Agentic AI UI using Streamlit.
    """
    ui= LoadStreamlitUI()
    user_input= ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user input from ui")
        return 
    
    user_message = st.chat_input("Enter Message")
