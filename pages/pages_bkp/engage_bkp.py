import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Engage | One to Many Spices", layout="wide")

# ---------------- CSS Styling ----------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }

    .card {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 2px 4px 16px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.3s ease;
        height: 100%;
    }

    .card:hover {
        transform: scale(1.05);
    }

    .card-title {
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #333333;
    }

    .card-desc {
        font-size: 16px;
        margin-bottom: 20px;
        color: #666666;
    }

    .card-btn {
        background-color: #FF3C38;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 12px;
        font-weight: bold;
        text-decoration: none;
        display: inline-block;
        margin-top: 10px;
    }

    .card-btn:hover {
        background-color: #cc2c2a;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Header Section ----------------
header_cols = st.columns([1, 4, 1])
with header_cols[0]:
    st.image("otms_assets/otms_logo_light.png", use_container_width=True)
with header_cols[1]:
    st.markdown("""
        <div style='text-align: center; margin-top: 20px;'>
            <h1 style='font-size: 48px;'>ENGAGE WITH US</h1>
            <p style='font-size: 20px; color: #555555;'>Your creativity makes our community stronger.</p>
        </div>
    """, unsafe_allow_html=True)
with header_cols[2]:
    st.image("otms_assets/cookfinity_logo_light.png", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- Engagement Cards ----------------
card_cols = st.columns(3)

with card_cols[0]:
    st.markdown("""
        <div class="card">
            <div class="card-title">📸 Share Your Dish</div>
            <div class="card-desc">
                Upload your favorite recipe made with OTMS blends.<br>We’ll feature the best ones on our app and socials!
            </div>
            <a href="#" class="card-btn">Upload Now</a>
        </div>
    """, unsafe_allow_html=True)

with card_cols[1]:
    st.markdown("""
        <div class="card">
            <div class="card-title">💬 Join the Community</div>
            <div class="card-desc">
                Connect with other food lovers, home cooks, and creators just like you. 
            </div>
            <a href="#" class="card-btn">Join Chat Group</a>
        </div>
    """, unsafe_allow_html=True)

with card_cols[2]:
    st.markdown("""
        <div class="card">
            <div class="card-title">🎥 Become a Creator</div>
            <div class="card-desc">
                Want to build your brand with OTMS? Start by sharing your food stories & videos.
            </div>
            <a href="#" class="card-btn">Apply Now</a>
        </div>
    """, unsafe_allow_html=True)

# ---------------- Divider ----------------
st.markdown("<br><hr><br>", unsafe_allow_html=True)

# ---------------- Email Subscription ----------------
st.markdown("<h3 style='text-align: center;'>📬 Stay Updated</h3>", unsafe_allow_html=True)
email = st.text_input("Enter your email to subscribe:")
if st.button("Subscribe"):
    if email:
        st.success(f"Thanks for subscribing, {email}!")
    else:
        st.error("Please enter a valid email.")

# ---------------- Optional Animations ----------------
with st.expander("✨ Want to see something cool?"):
    st.markdown("OTMS is building the future of food — powered by your creativity.")
    st.image("otms_assets/community_banner.png", use_column_width=True)

