import streamlit as st
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    system_instruction="""
You are an expert Python developer.
Answer only questions related to Python programming.
For any non-Python question, reply exactly:
Please ask a Python-related question.
Do not answer questions outside the Python domain.
"""
)

st.markdown(
    """
    <h1 style='text-align:center;'>Python AI Assistant</h1>
    <p style='text-align:center;font-size:18px;'>
    Ask any Python programming question.
    </p>
    """,
    unsafe_allow_html=True,
)

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

chat = client.chats.create(
    model="gemini-3-flash-preview"
)

# Placeholder for the response
response_placeholder = st.empty()

question = st.text_input(
    "",
    placeholder="Enter your Python question here..."
)

_, col2, _ = st.columns([4, 1, 4])

with col2:
    send = st.button("Send")

if send and question.strip():
    try:
        response = chat.send_message(
            question,
            config=config
        )
        response_placeholder.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
