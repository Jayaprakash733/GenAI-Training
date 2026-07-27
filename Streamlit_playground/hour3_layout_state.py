import time 
import numpy as np 
import pandas as pd
import streamlit as st 

st.set_page_config(page_title="Hour 3 - Layout & State",page_icon="3",layout="wide")
st.title("3️⃣. Hour 3 - Layout,Forms,Session & caching")
st.caption("shaping the page, and solving the two costs of rerun model")

st.header("Columns (with relative widths)")
c1,c2,c3=st.columns([2,1,1])
c1.info("wide column (ratio 2)")
c2.warning("Narrow column")
c3.success("Narrow column")

st.subheader("Tabs")
tab1,tab2=st.tabs(["📉 Chart"," 📊Data"])
with tab1:
    st.line_chart(pd.DataFrame(np.random.rand(15,2),columns=["X","Y"]))
with tab2:
    st.dataframe(pd.DataFrame({"col1":[1,2,3],"col2":[4,5,6]}))
st.subheader("Expander")
with st.expander("click to see raw data"):
    st.write(pd.DataFrame({"col1":[1,2],"col2":[3,4]}))

st.subheader("Container - group elements visually")
with st.container(border=True):
    st.write("Everything inside this 'with' block renders in a bordered box.")

st.subheader("st.empty - a placeholder you can overwrite")
placeholder = st.empty()
placeholder.write("Initial content...")
if st.button("Replace placeholder content"):
    placeholder.write("...replaced! 🎉")

st.subheader("Sidebar")
st.sidebar.markdown("### Example sidebar filter")
st.sidebar.selectbox(
    "Region",
    ["North", "South", "East", "West"],
    key="hour3_region"
)

st.divider()

st.header("B. Forms & Session State")
st.subheader("Forms-batch input,single rerun on submit")
with st.form("order_form"):
    product=st.selectbox("product",["Laptop","Mouse","Keyboard"])
    qty=st.number_input("Qty",1,50,1)
    submitted=st.form_submit_button("place order")
    if submitted:
        st.success(f"order placed:{qty}X{product}")

st.subheader("Session State - a counter that survives reruns")

if "counter" not in st.session_state:
    st.session_state.counter = 0


def increment():
    st.session_state.counter += 1


def reset():
    st.session_state.counter = 0


col1, col2 = st.columns(2)

col1.button("Increment", on_click=increment)
col2.button("Reset", on_click=reset)

st.metric(
    "Count (persists across reruns)",
    st.session_state.counter
)

st.caption(
    "Unlike normal variables, session_state survives reruns for each user."
)

st.header("C. Caching")

st.write(
    "This section runs a **slow, uncached** function next to a **fast,"
    "cached** one so you can feel the difference live"
)

def slow_uncached_computation(n):
    time.sleep(1.5)
    return sum(i*i for i in range(n))
@st.cache_data
def fast_cached_computation(n):
    time.sleep(1.5)
    return sum(i*i for i in range(n))

n= st.slider("Input value(n)",100,10000,1000, key="cache_n")
col1,col2 = st.columns(2)

with col1:
    st.markdown("**Without caching**")
    if st.button("Run uncached"):
        start= time.time()
        result= slow_uncached_computation(n)
        st.write(f"Result= {result}")
        st.write(f"Took: {time.time()- start:.2f}s - every single time")

with col2:
    st.markdown("**with '@st.cache_data'**") 
    if st.button("Run cached"):
            start= time.time()
            result= fast_cached_computation(n)
            st.write(f"Result= {result}")
            st.write(f"Took: {time.time()- start:.2f}s - instant on repeat calls with same n")
    
if st.button("Clear Cache"):
    st.cache_data.clear()
    st.toast("Cache Cleared!")

st.success("End of Hour 3")
