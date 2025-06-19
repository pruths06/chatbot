# 💬 Chatbot template

A simple Streamlit app that shows how to build a chatbot using OpenAI's GPT-3.5.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
# 🧠 AI Chatbot with Snowflake Cortex Search + Streamlit

A production-grade chatbot powered by **Streamlit**, **Snowflake Cortex**, and **RAG (Retrieval Augmented Generation)** for enterprise-ready, secure, and scalable data querying.

![screenshot](./screenshots/chat-ui.png)

## 🚀 Features

- ✅ Chat interface built with Streamlit
- ❄️ Integrates directly with Snowflake Cortex Search Services
- 🧠 Uses RAG techniques to build prompts from structured and unstructured data
- 🔐 Secure configuration using `secrets.toml`
- ⚙️ Easy deployment with `streamlit run`

---

## 🧰 Technologies

- Python 3.11
- Streamlit
- Snowflake Cortex Search
- Snowflake Snowpark
- pandas

---

## ⚙️ Setup Instructions

### 🔐 1. Configure `secrets.toml`

Create `.streamlit/secrets.toml` with your Snowflake credentials:

```toml
[snowflake]
user = "<your-username>"
password = "<your-password>"
account = "<your-account>.snowflakecomputing.com"
warehouse = "<your-warehouse>"
database = "<your-db>"
schema = "<your-schema>"
role = "<your-role>"
