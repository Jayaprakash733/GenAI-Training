import random
import pandas as pd
import streamlit as st
st.set_page_config(page_title="Hour 1-Foundations",page_icon="1",layout="wide")
st.title("ITER COHORT 2026")
st.caption("Stramlit class")

st.header("A. The Reurn Model")

st.markdown(
     """
    **The one idea that explains everything in Streamlit:**
    there is no concept of "update this one element." Instead, the
    **entire Python script re-runs, top to bottom, every time the user
    interacts with any widget.**
    """
)

st.code(
    "import streamlit as st\n\n"
    "st.title('Hello, Streamlit!')\n"
    "name = st.text_input(\"What's your name?\")\n"
    "if name:\n"
    "    st.write(f'Welcome, {name} 👋')",
    language="python",
)
name=st.text_input("Try it withs your name?")
if name:
    st.write(f"Welcome,{name} 👋")


st.divider()

st.subheader("🔴 Live proof of the rerun model")

st.write(
    "Touch the text box above, or the slider below — this random number "
    "changes every time, because the *whole script re-executes*, not "
    "just the widget you touched."
)

st.metric(
    "Random number generated this run",
    random.randint(1, 100000)
)

st.slider(
    "Wiggle me to trigger another rerun",
    0,
    10,
    5,
    key="rerun_demo_slider"
)

st.divider()
st.header("B. Text & Markdown Elements")

st.title("This is st.title")
st.header("This is st.header")
st.subheader("This is st.subheader")

st.text("This is st.text - plain fixed-width text")

st.markdown(
    "This is **st.markdown** — supports *italics*, `code`, and [links](https://streamlit.io)"
)

st.caption("This is st.caption - small grey text, good for footnotes")

st.code("print('this is st.code')", language="python")

st.latex(r"\sum_{i=1}^{n} i = \frac{n(n+1)}{2}")

st.divider()

st.header("C. Basic Data Display")

df = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Units Sold": [120, 340, 210, 95],
    "Revenue": [96000, 6800, 8400, 28500],
})

st.subheader("st.dataframe — interactive (sort, resize, search)")
st.dataframe(df, use_container_width=True)

st.subheader("st.table — static, for small fixed summaries")
st.table(df.head(2))

st.subheader("st.metric — a single KPI with a trend delta")
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${df['Revenue'].sum():,.0f}", "+12.4%")
col2.metric("Orders", "1,204", "+5%")
col3.metric("Returns", "18", "-1%")