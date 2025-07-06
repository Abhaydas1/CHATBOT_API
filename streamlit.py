import streamlit as st
import requests

# --- Configuration ---
API_KEY = st.secrets["OPENROUTER_API_KEY"]
MODEL = "google/gemini-2.5-flash-preview-05-20"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "Streamlit Chatbot"
}

# --- Page config ---
st.set_page_config(page_title="🧠 Your Friencdly Chatbot", layout="wide")

# --- Custom CSS ---
st.markdown("""
<style>
.chat-container {
    background-color: #f0f2f6;
    padding: 20px;
    border-radius: 15px;
}
.user-msg, .bot-msg {
    padding: 12px 16px;
    border-radius: 12px;
    margin-bottom: 10px;
    max-width: 80%;
    word-wrap: break-word;
}
.user-msg {
    background-color: darkcyan ;
    align-self: flex-end;
    margin-left: auto;
}
.bot-msg {
    background-color: coral;
    border: 1px solid #ccc;
    align-self: flex-start;
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("⚙️ Settings")
temperature = st.sidebar.slider("Creativity (temperature)", 0.0, 1.0, 0.7, 0.1)
clear = st.sidebar.button("🧹 Clear Chat")

# --- Session state for history ---
if clear or "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

# --- Title ---
st.title("🤖 Web Chatbot")
st.caption("Talk to a powerful LLM using OpenRouter & Gemini.")

# --- Display chat history ---
with st.container():
    for msg in st.session_state.messages[1:]:  # Skip system message
        if msg["role"] == "user":
            st.markdown(f"<div class='user-msg'>{msg['content']}</div>", unsafe_allow_html=True)
        elif msg["role"] == "assistant":
            st.markdown(f"<div class='bot-msg'>{msg['content']}</div>", unsafe_allow_html=True)

# --- Chat input ---
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f"<div class='user-msg'>{user_input}</div>", unsafe_allow_html=True)

    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                API_URL,
                headers=HEADERS,
                json={
                    "model": MODEL,
                    "messages": st.session_state.messages,
                    "temperature": temperature,
                    "max_tokens": 1024
                },
                timeout=30
            )

            if response.status_code == 200:
                reply = response.json()["choices"][0]["message"]["content"]
                st.session_state.messages.append({"role": "assistant", "content": reply})
                st.markdown(f"<div class='bot-msg'>{reply}</div>", unsafe_allow_html=True)
            else:
                error_msg = f"❌ {response.status_code}: {response.text}"
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
                st.markdown(f"<div class='bot-msg'>{error_msg}</div>", unsafe_allow_html=True)

        except Exception as e:
            err = f"❌ Exception: {str(e)}"
            st.session_state.messages.append({"role": "assistant", "content": err})
            st.markdown(f"<div class='bot-msg'>{err}</div>", unsafe_allow_html=True)
