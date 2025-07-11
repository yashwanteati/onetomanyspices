import streamlit as st
import base64
from pathlib import Path

# ---------------- Page Config ----------------
st.set_page_config(page_title="Engage | One to Many Spices", layout="wide")

# ---------------- CSS Styling ----------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }

    .hero {
        background: linear-gradient(90deg, #ffddb0, #ffe6cc);
        padding: 2rem;
        border-radius: 25px;
        text-align: center;
        margin-bottom: 2rem;
    }

    .hero h1 {
        font-size: 3rem;
        color: #b3541e;
        margin-bottom: 0.5rem;
    }

    .hero p {
        font-size: 1.2rem;
        color: #333;
        font-style: italic;
    }

    .section {
        background-color: #fff9f0;
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    }

    .section h3 {
        font-size: 1.8rem;
        color: #a64b2a;
    }

    .upload-box {
        border: 2px dashed #ffa94d;
        padding: 2rem;
        border-radius: 15px;
        background-color: #fffdf8;
        text-align: center;
    }

    .upload-box p {
        margin-top: 1rem;
        color: #555;
    }

    .social-links a {
        font-weight: bold;
        color: #b3541e !important;
    }

    .carousel-img {
        height: 300px;
        border-radius: 20px;
        margin-top: 1rem;
        object-fit: cover;
    }

    .auth-box {
        background-color: #ffe9db;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .tagline {
        font-size: 1.1rem;
        color: #333;
        font-style: italic;
        margin-top: -10px;
    }
    </style>
""", unsafe_allow_html=True)


# ---------------- Utility ----------------
def img_to_base64(image_path):
    if Path(image_path).exists():
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# ---------------- Hero Section ----------------
left_logo = "otms_assets/otms_logo_white.png"
right_logo = "otms_assets/otms_logo_white.png"
left_b64 = img_to_base64(left_logo)
right_b64 = img_to_base64(right_logo)

st.markdown('<div class="hero">', unsafe_allow_html=True)

if left_b64 and right_b64:
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; gap: 2rem;">
            <img src="data:image/png;base64,{left_b64}" style="height: 80px;">
            <h1>ENGAGE</h1>
            <img src="data:image/png;base64,{right_b64}" style="height: 80px;">
        </div>
        """, unsafe_allow_html=True
    )

st.markdown('<p class="tagline">Create. Share. Connect with the OTMS family.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ---------------- Message ----------------
st.markdown("<div class='construction'>", unsafe_allow_html=True)
st.markdown("🚧 **COOK page is under construction** 🚧<br><br>We're spicing things up! Recipes coming soon!", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
