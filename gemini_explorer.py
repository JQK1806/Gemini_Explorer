import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = "geminiexplorer-424016"
vertexai.init(project=project)

config = generative_models.GenerationConfig(
    temperature=0.4
)

model = GenerativeModel(
    "gemini-pro",
    generation_config=config
)

chat = model.start_chat()

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
            personalized_greeting = f"👋 Hello, I'm {user_name}! An assistant powered by Google Gemini."
            llm_function(chat, personalized_greeting)
        else:
            default_greeting = f"👋 Hello! I'm ReX, an assistant powered by Google Gemini."
            llm_function(chat, default_greeting)

# For capture user input
query = st.chat_input("Gemini Explorer")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)

