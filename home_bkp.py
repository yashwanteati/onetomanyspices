import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="One to Many Spices", layout="wide")

# ---------------- CSS Styling ----------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }

    .button-img {
        border-radius: 20px;
        transition: transform 0.3s ease-in-out;
        cursor: pointer;
    }

    .button-img:hover {
        transform: scale(1.1);
    }

    .menu-button {
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Image Conversion ----------------
def img_to_base64(path):
    try:
        image_bytes = Path(path).read_bytes()
        return base64.b64encode(image_bytes).decode()
    except Exception:
        return ""

# ---------------- Header Section (Logos + Title) ----------------
header_cols = st.columns([1, 4, 1])
with header_cols[0]:
    st.image("otms_assets/otms_logo_light.png", use_container_width=True)

with header_cols[1]:
    st.markdown("""
        <div style='text-align: center; margin-top: 20px;'>
            <h1 style='font-size: 52px; margin-bottom: 5px;'>ONE TO MANY</h1>
            <h2 style='letter-spacing: 14px; font-size: 30px; margin-top: -20px;'>S   P   I   C   E   S</h2>
            <h4 style='font-size: 22px; margin-top: 12px;'>
                <span style='color: #FF3C38; margin-right: 12px;'>CREATE</span> 
                <span style='color: #FDCB52; margin-right: 12px;'>RECIPES</span> 
                <span style='color: #000000; margin-right: 12px;'>THAT</span> 
                <span style='color: #2ECC71;'>LET</span>S
                <span style='color: #FDCB52;'>LMEMORIES</span>
                <span style='color: #FF3C38;'>LAST</span>
                <span style='color: #000000;'>WORLD'S FIRST ONE STOP FOOD APP</span>
            </h4>
        </div>
    """, unsafe_allow_html=True)

with header_cols[2]:
    st.image("otms_assets/cookfinity_logo_light.png", use_container_width=True)

# ---------------- Button Config ----------------
buttons = [
    {"label": "LEARN", "image": "otms_assets/learn.png", "page": "learn"},
    {"label": "COOK", "image": "otms_assets/cook.png", "page": "cook"},
    {"label": "SHOP", "image": "otms_assets/shop.png", "page": "shop"},
    {"label": "CREATE", "image": "otms_assets/create.png", "page": "create"},
    {"label": "ENGAGE", "image": "otms_assets/engage.png", "page": "engage"},
]

# ---------------- Render 3D Icon Buttons ----------------
img_cols = st.columns(5)
for col, btn in zip(img_cols, buttons):
    with col:
        b64_img = img_to_base64(btn["image"])
        if b64_img:
            col.markdown(
                f"""
                <div class="menu-button">
                    <a href="/{btn['page']}" target="_self">
                        <img src="data:image/png;base64,{b64_img}" class="button-img" style="height: 100000;">
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning(f"Image not found: {btn['image']}")

# ---------------- Email Subscription ----------------
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>📬 Stay Updated</h3>", unsafe_allow_html=True)
email = st.text_input("Enter your email to subscribe:")
if st.button("Subscribe"):
    if email:
        st.success(f"Thanks for subscribing, {email}!")
    else:
        st.error("Please enter a valid email.")
