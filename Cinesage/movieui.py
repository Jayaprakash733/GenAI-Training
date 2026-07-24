import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

model=ChatMistralAI(model="mistral-small-2603")

prompt_template = ChatPromptTemplate.from_messages([
    ("system",
    """
You are a professional Movie Information Extraction Assistant.

Your task:
Extract useful structured information from a movie paragraph and present it in a clean readable format.

Rules:
- Do NOT add explanations
- Do NOT add extra commentary
- Follow the exact format
- If information is missing → write NULL
- Keep summary short (2-3 lines max)
- Do NOT guess unknown facts

Output Format:

Movie Title:
Release Year:
Genre:
Director:
Main Cast:
Setting/Location:
Plot:
Themes:
Ratings:
Notable Features:

Short Summary:
"""
    ),

    ("human",
    """
Extract information from this paragraph:

{paragraph}
"""
    )
])


# ---------------- STREAMLIT UI ----------------

st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")

st.markdown(
    """
    Enter a movie paragraph below and let AI extract
    **structured movie information** for you.
    """
)

st.divider()

para = st.text_area(
    "📝 Enter Movie Paragraph",
    placeholder="Paste your movie paragraph here...",
    height=250
)

if st.button("✨ Extract Movie Information", use_container_width=True):

    if para:

        with st.spinner("🎬 Analyzing movie information..."):

            final_prompt=prompt_template.invoke(
                {"paragraph":para}
            )

            response=model.invoke(final_prompt)

        st.success("✅ Information Extracted Successfully!")

        st.subheader("🍿 Movie Details")

        st.markdown(response.content)

    else:

        st.warning("⚠️ Please enter a movie paragraph first.")