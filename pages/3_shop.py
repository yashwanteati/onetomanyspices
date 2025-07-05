import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="One to Many Spices", layout="wide")

# Logos
logo_left = Image.open("logo_left.png")
logo_right = Image.open("logo_right.png")

# HEADER
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    st.image(logo_left, width=100)
with col2:
    st.markdown("<h1 style='text-align:center; margin-bottom: 0;'>ONE TO MANY</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; letter-spacing: 30px;'>S P I C E S</h2>", unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align: center;'>
        <span style='color:#e74c3c;'>CREATE</span>
        <span style='color:#2ecc71;'> RECIPIES</span>
        <span style='color:#f1c40f;'> THAT</span>
        <span style='color:#d35400;'> LET</span>
        <span style='color:#7f8c8d;'> MEMORIES</span>
        <span style='color:#27ae60;'> LAST</span>
    </h4>
    """, unsafe_allow_html=True)
with col3:
    st.image(logo_right, width=100)

st.markdown("---")

# ICON NAVIGATION ROW
colA, colB, colC, colD, colE = st.columns(5)

with colA:
    st.page_link("learn.py", label="", icon=None)
    st.image("icon_learn.png", use_container_width=True)

with colB:
    st.page_link("cook.py", label="", icon=None)
    st.image("icon_cook.png", use_container_width=True)

with colC:
    st.page_link("shop.py", label="", icon=None)
    st.image("icon_shop.png", use_container_width=True)

with colD:
    st.page_link("create.py", label="", icon=None)
    st.image("icon_create.png", use_container_width=True)

with colE:
    st.page_link("engage.py", label="", icon=None)
    st.image("icon_engage.png", use_container_width=True)

st.markdown("---")

# EMAIL SUBSCRIBE
st.markdown("### 📬 Stay Updated")
email = st.text_input("Enter your email to subscribe:")
if st.button("Subscribe"):
    if email and "@" in email:
        st.success(f"Thanks for subscribing, {email}!")
    else:
        st.error("Please enter a valid email address.")
