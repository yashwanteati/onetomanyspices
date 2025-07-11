import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="One to Many Spices", layout="wide")

# -------------------- Hide Sidebar --------------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .button-img {
        border-radius: 20px;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.2);
        transition: transform 0.2s ease-in-out;
        cursor: pointer;
    }
    .button-img:hover {
        transform: scale(1.05);
        box-shadow: 0px 12px 20px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- Function: Convert Image to base64 --------------------
def img_to_base64(path):
    image_bytes = Path(path).read_bytes()
    return base64.b64encode(image_bytes).decode()

# -------------------- Display Logos (Left and Right) --------------------
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    try:
        st.image("assets/otms_logo.png", width=1000)
    except:
        st.warning("Left logo not found")

with col3:
    try:
        st.image("assets/cookfinity_logo.png", width=1000)
    except:
        st.warning("Right logo not found")

# -------------------- Title and Tagline --------------------
st.markdown("""
<div style='text-align: center; margin-top: -40px;'>
    <h1 style='font-size: 48px;'>ONE TO MANY</h1>
    <h2 style='letter-spacing: 12px; margin-top: -20px;'>SPICES</h2>
    <h4 style='font-size: 20px;'>
        <span style='color: #E63946;'>CREATE</span> 
        <span style='color: #F4A261;'>RECIPES</span> 
        <span style='color: #000000;'>THAT</span> 
        <span style='color: #2A9D8F;'>LET MEMORIES LAST</span>
    </h4>
</div>
""", unsafe_allow_html=True)

# -------------------- Clickable Image Buttons --------------------
buttons = [
    {"label": "LEARN", "image": "assets/learn.png", "target": "learn"},
    {"label": "COOK", "image": "assets/cook.png", "target": "cook"},
    {"label": "SHOP", "image": "assets/shop.png", "target": "shop"},
    {"label": "CREATE", "image": "assets/create.png", "target": "create"},
    {"label": "ENGAGE", "image": "assets/engage.png", "target": "engage"},
]

cols = st.columns(5)

for col, btn in zip(cols, buttons):
    with col:
        try:
            b64_img = img_to_base64(btn["image"])
            col.markdown(f"""
                <a href="{btn['target']}.py">
                    <img src="data:image/png;base64,{b64_img}" class="button-img" style="width: 100%; max-width: 160px;">
                </a>
            """, unsafe_allow_html=True)
        except FileNotFoundError:
            st.error(f"Image not found: {btn['image']}")

# -------------------- Email Subscription --------------------
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>📬 Stay Updated</h3>", unsafe_allow_html=True)
email = st.text_input("Enter your email to subscribe:")
if st.button("Subscribe"):
    if email:
        st.success(f"Thanks for subscribing, {email}!")
    else:
        st.error("Please enter a valid email.")
