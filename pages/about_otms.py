import streamlit as st
from pathlib import Path
import base64

# ---------------- Page Settings ----------------
st.set_page_config(page_title="About | One to Many Spices", layout="wide")

# ---------------- CSS Styling ----------------
st.markdown("""
    <style>
    body, .stApp {
        background: #0b0d10 !important;
        color: #e9eef4 !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    [data-testid="stSidebar"] {
        display: none;
    }
    .block-container {
        padding-top: 2rem;
        max-width: 1100px;
    }
    h1 {
        text-align: center;
        color: #ffd700;
        margin-bottom: 1rem;
    }
    h2 {
        color: #f5f5f5;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .about-card {
        background: #1a1c20;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.2);
        margin-bottom: 2rem;
    }
    .tagline {
        text-align: center;
        font-size: 20px;
        font-style: italic;
        color: #ffd700;
        margin-top: 0.5rem;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Content ----------------
st.title("About One to Many Spices")
st.markdown('<div class="tagline">CREATE RECIPES THAT LET MEMORIES LAST</div>', unsafe_allow_html=True)

st.markdown("""
<div class="about-card">
    <h2>Our Story</h2>
    <p>
        One to Many Spices (OTMS) was born out of a simple yet powerful idea: 
        one spice box, endless possibilities. We believe cooking should be effortless, 
        creative, and deeply connected to culture and memories. With our curated blends, 
        anyone can create authentic Indian dishes and global fusions without the complexity 
        of sourcing dozens of spices.
    </p>
</div>

<div class="about-card">
    <h2>Our Mission</h2>
    <p>
        To simplify cooking while preserving authenticity. We empower home cooks 
        and food lovers with versatile spice blends that unlock hundreds of recipes, 
        reduce kitchen stress, and bring joy back to everyday meals.
    </p>
</div>

<div class="about-card">
    <h2>Our Vision</h2>
    <p>
        To become the world’s first one-stop culinary ecosystem where food, culture, 
        and technology meet. From our innovative spice packaging to our Cookfinity app, 
        we aim to inspire creativity in kitchens across the globe and make 
        “Flavors Without Borders” a reality.
    </p>
</div>

<div class="about-card">
    <h2>Why OTMS?</h2>
    <ul>
        <li>Six powerful blends — RED, WHITE, YELLOW, BROWN, GREEN, GRAY</li>
        <li>One spice box can cook an entire Bahubali thali</li>
        <li>Packaging designed for simplicity and innovation</li>
        <li>Integrated with the Cookfinity app: LEARN • COOK • SHOP • CREATE • ENGAGE</li>
    </ul>
</div>
""", unsafe_allow_html=True)
