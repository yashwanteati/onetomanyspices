import streamlit as st
from pathlib import Path
import base64

# ---------------- Page Settings ----------------
st.set_page_config(page_title="Learn | One to Many Spices", layout="wide")

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

# ---------------- Image Encoding Function ----------------
def img_to_base64(path):
    try:
        return base64.b64encode(Path(path).read_bytes()).decode()
    except Exception:
        return ""


# ---------------- Header Section (Logos + Title) ----------------
header_cols = st.columns([1, 4, 1])
with header_cols[0]:
    st.image("otms_assets/otms_logo_light.png", use_container_width=True)

with header_cols[1]:
    st.markdown("""
        <div style='text-align: center; margin-top: 05px;'>
            <h1 style='font-size: 52px; margin-bottom: 5px;'>L  E  A  R  N</h1>
            <h2 style='letter-spacing: 14px; font-size: 30px; margin-top: -20px;'>ABOUT  O  T  M  S</h2>
            <h4 style='font-size: 22px; margin-top: 12px;'>
                <span style='color: #FF3C38; margin-right: 12px;'>CREATE</span> 
                <span style='color: #FDCB52; margin-right: 12px;'>RECIPES</span> 
                <span style='color: #2ECC71; margin-right: 12px;'>THAT</span> 
                <span style='color: #FF3C38;'>LET</span>
                <span style='color: #FDCB52;'>MEMORIES</span>
                <span style='color: #2ECC71;'>LAST</span>
            </h4>
            <h5 style='letter-spacing: 10px; font-size: 30px; margin-top: -10px;color: #C7AF6Bs;'>WORLD'S FIRST ONE STOP FOOD APP</h5>

        </div>
    """, unsafe_allow_html=True)

with header_cols[2]:
    st.image("otms_assets/cookfinity_logo_light.png", use_container_width=True)

# ---------------- Brand Description ----------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
    <div class="description">
        One to Many Spices (OTMS) is on a mission to simplify cooking for everyone. 
        With our curated, versatile spice blends, you can create restaurant-quality dishes right at home. 
        Whether you’re a beginner or an expert, OTMS helps you cook with confidence, flavor, and joy — 
        one spice blend, many memories.
    </div>
""", unsafe_allow_html=True)

# ---------------- Button Config ----------------
buttons = [
    {"label": "Indian Spices 101", "image": "otms_assets/learn_spices.png", "page": "learn_spices"},
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