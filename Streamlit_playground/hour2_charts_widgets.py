import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

st.header("A. Charts")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.subheader("Native quick charts (built on Vega-Lite)")

t1, t2, t3, t4 = st.tabs(
    ["line_chart", "bar_chart", "area_chart", "scatter_chart"]
)

with t1:
    st.line_chart(chart_data)

with t2:
    st.bar_chart(chart_data)

with t3:
    st.area_chart(chart_data)

with t4:
    st.scatter_chart(chart_data)

st.subheader(
    "Plotly — full control (recommended for polished dashboards)"
)
df = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Revenue": [96000, 6800, 8400, 28500],
})

fig = px.bar(
    df,
    x="Product",
    y="Revenue",
    color="Product",
    title="Revenue by Product"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Matplotlib")

fig2, ax = plt.subplots()

ax.pie(
    df["Revenue"],
    labels=df["Product"],
    autopct="%1.1f%%"
)

st.pyplot(fig2)

st.subheader("st.map")

map_df = pd.DataFrame({
    "lat": [20.29 + np.random.randn() * 0.05 for _ in range(30)],
    "lon": [85.82 + np.random.randn() * 0.05 for _ in range(30)],
})

st.map(map_df)

st.subheader("Selections")
option=st.selectbox("choose a city",["BBSR","Delhi","Mumbai"])
options=st.multiselect("choose products",["Laptop","Mouse","Keyboard"])
st.write("selectbox:",option,"|multiselect:",options)

st.subheader("Numeric & text")
age=st.slider("select age",0,100,25)
price_range=st.slider("Price range",0,1000,(200,700))
qty=st.number_input("Quantity",min_value=1,max_value=100,value=1)
comment=st.text_input("Short comment")
notes=st.text_area("Long notes")
st.write(f"age={age},price_range={price_range},qty={qty},comment={comment!r},notes={notes}")

st.subheader("Date & time")
d = st.date_input("Pick a date")
t = st.time_input("Pick a time")
st.write("date:", d, "| time:", t)
st.subheader("File & color")
uploaded = st.file_uploader("Upload any CSV (optional)", type=["csv"])
if uploaded is not None:
    st.dataframe(pd.read_csv(uploaded))
color = st.color_picker("Pick a color", "#00f900")
st.write("You picked:", color)
st.divider()





