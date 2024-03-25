import streamlit as st

from mycode.shared_one import shared_fn_one

st.title('Hello World!')

st.divider()

st.button('Click me!')
st.text(shared_fn_one())