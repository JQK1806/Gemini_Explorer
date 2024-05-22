# Gemini Explorer
Gemini Explorer is a Streamlit based chat interface that is powered by Google Gemini. Users can interact
with the model through text input. This application uses Vertex AI for the model initialization and communication.

# Features
- Chat Interface: Users interact with the model through typed messages in the chat box. Chat history is maintained,
displaying both the user's and model's messages.
- Personalized Greetings: Users can input their name to have a personalized greeting. If no name is input, ReX's
stlye of speaking changes.

# Setup
1. Clone the repository
2. Install dependencies in requirements.txt

# Usage
1. Run the Streamlit app
    - streamlit run gemini_explorer.py
2. Enter name (optional)
3. Press "Ready to chat"