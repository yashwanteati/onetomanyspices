import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="One to Many Spices", layout="wide")

# ---------------- CSS Styling ----------------

st.markdown("""
    <style>
    [data-testid="stSidebar"] {display: none;}
    .main, .stApp, body, .block-container {
        background: #000 !important;
    }
    /* ... rest of your CSS ... */
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    [data-testid="stSidebar"] {display: none;}
    body { background: #000 !important; }
    .button-img {
        border-radius: 50px;
        transition: transform 0.3s ease-in-out;
        cursor: pointer;
    }
    .button-img:hover {transform: scale(1.1);}
    .menu-button {text-align: center; margin-top: 6px;background: transparent;box-shadow: none;}
    .top-right-btns {
        position: absolute; 
        top: 15px; 
        right: 64px; 
        z-index: 999;
        display: flex;
        gap: 5px;
    }
    .otms-btn {
        background: #ff3c38;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 8px 22px;
        font-weight: bold;
        font-size: 18px;
        cursor: pointer;
        box-shadow: 0 2px 12px #0001;
        transition: background 0.2s;
    }
    .otms-btn.secondary {
        background: #004aad;
        margin-left: 6px;
    }
    /* Floating chat button */
    .floating-chat {
        position: fixed;
        right: 32px;
        bottom: 32px;
        z-index: 9999;
    }
    .chat-circle-btn {
        width: 66px; height: 66px;
        background: #fddb52;
        border-radius: 50%;
        border: 2px solid #ff3c38;
        box-shadow: 0 2px 12px #0003;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        font-size: 38px;
        color: #ff3c38;
        font-weight: bold;
        transition: transform 0.2s;
    }
    .chat-circle-btn:hover {transform: scale(1.1);}
    .chat-popup {
        position: fixed;
        right: 120px;
        bottom: 44px;
        width: 330px;
        background: white;
        border-radius: 18px;
        box-shadow: 0 4px 28px #0002;
        padding: 16px;
        z-index: 99999;
        border: 1.5px solid #ff3c38;
        animation: fadein .2s;
    }
    @keyframes fadein {from {opacity:0;transform:translateY(40px);} to {opacity:1;transform:none;}}
    </style>
""", unsafe_allow_html=True)

# ---------------- Image Conversion ----------------
def img_to_base64(path):
    try:
        image_bytes = Path(path).read_bytes()
        return base64.b64encode(image_bytes).decode()
    except Exception:
        return ""

# ------------------- TOP RIGHT BUTTONS -------------------
st.markdown("""
    <div class="top-right-btns">
        <button class="otms-btn" onclick="window.location.href='/signin'">Sign In / Create Account</button>
        <button class="otms-btn secondary" onclick="window.location.href='/collab'">COLLAB with OTMS</button>
    </div>
""", unsafe_allow_html=True)

# ---------------- Header Section (Logos + Title) ----------------
header_cols = st.columns([10, 15, 10])

with header_cols[0]:
    st.image("otms_assets/otms_logo_dark.png", width=250)
with header_cols[1]:
    # Use st.markdown to control spacing below the banner
    st.image("otms_assets/otms_banner.png", width=700)
    st.markdown("<div style='margin-bottom: 0px;'></div>", unsafe_allow_html=True)  # Reduce gap
with header_cols[2]:
    st.image("otms_assets/cookfinity_logo_dark.png", width=250)



# ---------------- Button Config ----------------
buttons = [
    {"label": "About OTMS", "image": "otms_assets/about_otms.png", "page": "about"},
    {"label": "Understanding OTMS Blends", "image": "otms_assets/learn_blends.png", "page": "learn_blends"},
    {"label": "Basic to Pro Cooking Techniques", "image": "otms_assets/learn_techniques.png", "page": "learn_techniques"},
    {"label": "Watch Recipe Videos", "image": "otms_assets/learn_videos.png", "page": "learn_videos"},
    {"label": "Health & Diet with OTMS", "image": "otms_assets/learn_health.png", "page": "learn_health"},
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
                        <img src="data:image/png;base64,{b64_img}" class="button-img" style="height: 250px; width: 250px; object-fit: cover;">
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning(f"Image not found: {btn['image']}")





# ---------------- Video Learning Section ----------------
st.markdown('<div class="section-title">🎥 Watch & Cook Along</div>', unsafe_allow_html=True)

video_cols = st.columns(3)
video_links = [
    "https://www.youtube.com/embed/QrY9eHkXTa4",
    "https://www.youtube.com/embed/NpEaa2P7qZI",
    "https://www.youtube.com/embed/ysz5S6PUM-U"
]
for i in range(3):
    with video_cols[i]:
        st.video(video_links[i])

# ---------------- Email Subscription ----------------
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>📬 Stay Updated</h3>", unsafe_allow_html=True)
email = st.text_input("Enter your email to subscribe:")
if st.button("Subscribe"):
    if email:
        st.success(f"Thanks for subscribing, {email}!")
    else:
        st.error("Please enter a valid email.")