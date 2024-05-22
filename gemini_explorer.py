import vertexai
import time
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

# Initialize VertexAI project
project = "geminiexplorer-424016"
vertexai.init(project=project)

# Initialize generative model config
config = generative_models.GenerationConfig(
    temperature=0.4
)

# Initialize the generative model
model = GenerativeModel(
    "gemini-pro",
    generation_config=config
)

# Start a chat session
chat = model.start_chat()

# Send a message in the chat and display in the Streamlit app
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    with st.chat_message("model"):
        st.markdown(output)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )


st.title("Gemini Explorer")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display and load to chat history
for index, message in enumerate(st.session_state.messages):
    content = Content(
            role = message["role"],
            parts = [Part.from_text(message["content"])]
        )
    
    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    chat.history.append(content)

# Initial prompt
if len(st.session_state.messages) == 0:
    # Capture user's name
    user_name = st.text_input("Please enter your name")
    # Button to trigger the initial prompt
    if st.button("Ready to Chat"):
        if user_name:
            personalized_greeting = f"Introduce yourself as ReX, an assistant powered by Google Gemini. You are talking with {user_name}. Use emojis to be interactive."
            llm_function(chat, personalized_greeting)
        else:
            default_greeting = "Introduce yourself as ReX, an assistant powered by Google Gemini. You talk like a pirate."
            llm_function(chat, default_greeting)

# For capture user input
query = st.chat_input("Gemini Explorer")

# Function to show "ReX is typing" indicator
def typing_indicator():
    with st.empty():
        st.text("ReX is typing...")
        time.sleep(1)
        st.empty()

if query:
    with st.chat_message("user"):
        st.markdown(query)
    typing_indicator()
    llm_function(chat, query)