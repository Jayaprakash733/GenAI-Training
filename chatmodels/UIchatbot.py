import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Load .env
load_dotenv()

st.set_page_config(
    page_title="Mood AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 Mood AI Chatbot")

# -------------------------
# Initialize chat state
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "personality_selected" not in st.session_state:
    st.session_state.personality_selected = False


# -------------------------
# Personality Selection
# -------------------------

if not st.session_state.personality_selected:

    st.subheader("Choose AI Personality")

    user = st.radio(
        "Select personality:",
        ["😡 Angry", "😢 Sad", "😂 Funny"],
        index=None
    )

    if user:

        if user == "😡 Angry":
            mood = """
            You are an angry AI assistant.
            Answer questions correctly but use an angry tone.
            """

        elif user == "😢 Sad":
            mood = """
            You are a sad AI assistant.
            Answer questions correctly but speak in a sad tone.
            """

        else:
            mood = """
            You are a funny AI assistant.
            Answer questions correctly but make your responses humorous.
            """

        st.session_state.messages = [
            SystemMessage(content=mood)
        ]

        st.session_state.personality_selected = True

        st.rerun()


# -------------------------
# Chat Interface
# -------------------------

else:

    # Display previous messages
    for message in st.session_state.messages:

        if isinstance(message, HumanMessage):

            with st.chat_message("user"):
                st.write(message.content)

        elif isinstance(message, AIMessage):

            with st.chat_message("assistant"):
                st.write(message.content)


    # User input
    prompt = st.chat_input("Ask something...")


    if prompt:

        # Display user message
        with st.chat_message("user"):
            st.write(prompt)

        st.session_state.messages.append(
            HumanMessage(content=prompt)
        )

        try:

            # Create model only when needed
            model = ChatMistralAI(
                model="mistral-small-2603",
                temperature=0.9
            )

            with st.spinner("Thinking..."):

                response = model.invoke(
                    st.session_state.messages
                )

            st.session_state.messages.append(
                AIMessage(content=response.content)
            )

            with st.chat_message("assistant"):
                st.write(response.content)

        except Exception as e:

            st.error(f"Error: {e}")


    # -------------------------
    # Restart Button
    # -------------------------

    if st.button("🔄 Restart Chat"):

        st.session_state.messages = []
        st.session_state.personality_selected = False

        st.rerun()