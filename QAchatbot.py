from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash",
                            google_api_key=st.secrets["GOOGLE_API_KEY"])

st.title("🤖 AskBuddy – AI QnA Bot")

st.markdown("My QnA Bot with LangChain and Google Gemini!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    role = message["role"]
    content = message["content"]

    st.chat_message(role).markdown(content)


query = st.chat_input("Ask anything?")

if query:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    st.chat_message("user").markdown(query)

    # Get Gemini response
    res = llm.invoke(query)

    # Extract only the text
    content = res.content

    if isinstance(content, list):
        content = content[0]["text"]

    # Show AI response
    st.chat_message("ai").markdown(content)

    # Save AI response
    st.session_state.messages.append({
        "role": "ai",
        "content": content
    })
