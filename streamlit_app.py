import streamlit as st
from openai import OpenAI

# License & Watermark
st.markdown("### 🔒 Protected Code — © 2025 Pruthak Brahmbhatt")
st.markdown("This chatbot implementation is licensed and published for portfolio and demonstration purposes only.")

# Developer Token Check (you'll define this in secrets.toml)
if "developer_code" not in st.secrets or st.secrets["developer_code"] != "PRUTHAK-DEV-KEY":
    st.warning("🚫 Unauthorized environment. This app is protected and requires developer authorization to run.")
    st.stop()

# Title and description
st.title("💬 AI Chatbot (Cortex/OpenAI)")
st.write(
    "This chatbot uses GPT-3.5-turbo via OpenAI to generate responses.\n"
    "This version is part of a protected project. To build something similar, contact the author.\n\n"
    "🔐 Code integrity enforced by developer authentication layer."
)

# API key field
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please enter your OpenAI API key.", icon="🗝️")
else:
    client = OpenAI(api_key=openai_api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask something..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
        )

        with st.chat_message("assistant"):
            response = st.write_stream(stream)

        st.session_state.messages.append({"role": "assistant", "content": response})
