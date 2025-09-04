import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Engage | One to Many Spices", layout="wide")

# ---- CSS: Sidebar hidden, clean look, top bar layout ----
st.markdown("""
    <style>
    body, .stApp, .block-container { background: #111 !important; }
    [data-testid="stSidebar"] { display: none !important; }
    .otms-header-bar {
        display: flex; align-items: center; justify-content: space-between;
        width: 100vw; max-width: 100vw;
        margin-left: -2.2rem; margin-right: -2.2rem; margin-top: -1.8rem;
        padding: 0 42px 0 42px;
        min-height: 90px;
    }
    .otms-header-left {
        display: flex; align-items: center;
    }
    .cookfinity-logo {
        width: 82px; height: 82px; object-fit: contain;
        background: transparent;
        margin-right: 24px;
        margin-left: 10px;
    }
    .story-avatar {
        width: 75px; height: 75px; border-radius: 50%;
        border: 4px solid #fff; margin-right: 16px;
        object-fit: cover;
        box-shadow: 0 2px 8px #0007;
        transition: transform 0.18s;
    }
    .story-avatar:hover { transform: scale(1.09);}
    .story-label { color: #fff; font-size: 15px; text-align: center; margin-top: 4px;}
    .story-block { text-align: center; display: inline-block; }
    .top-right-btns {
        display: flex;
        gap: 12px;
    }
    .otms-btn {
        background: #ff3c38;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 8px 18px;
        font-weight: bold;
        font-size: 15px;
        cursor: pointer;
        box-shadow: 0 2px 12px #0001;
        transition: background 0.2s;
    }
    .otms-btn.secondary { background: #004aad; margin-left: 8px;}
    </style>
""", unsafe_allow_html=True)

# --- Top bar with logo + stories + buttons ---
stories = [
    {"avatar": "engage_assets/story1.png", "label": "Yashwant"},
    {"avatar": "engage_assets/story2.jpg", "label": "Priya"},
    {"avatar": "engage_assets/story3.png", "label": "Alex"},
    {"avatar": "engage_assets/story4.jpg", "label": "Maria"},
    {"avatar": "engage_assets/story5.jpg", "label": "Chef Ria"},
]

def avatar_base64(path):
    try:
        data = Path(path).read_bytes()
        return base64.b64encode(data).decode()
    except Exception:
        return ""

# ----------- Top Header Bar (logo + stories + buttons) -----------
st.markdown("""
    <div class="otms-header-bar">
        <div class="otms-header-left">
            <img src="otms_assets/cookfinity_logo_dark.png" class="cookfinity-logo"/>
""", unsafe_allow_html=True)

# Inline: Add all the stories right after the logo:
stories_html = ""
for s in stories:
    b64 = avatar_base64(s["avatar"])
    ext = Path(s["avatar"]).suffix[1:]
    if b64:
        stories_html += f'''
        <div class="story-block">
            <img class="story-avatar" src="data:image/{ext};base64,{b64}">
            <div class="story-label">{s["label"]}</div>
        </div>
        '''
    else:
        stories_html += f'''
        <div class="story-block">
            <div class="story-avatar" style="background:#444;display:flex;align-items:center;justify-content:center;">?</div>
            <div class="story-label">{s["label"]}</div>
        </div>
        '''
st.markdown(stories_html, unsafe_allow_html=True)

st.markdown("""
        </div>
        <div class="top-right-btns">
            <button class="otms-btn" onclick="window.location.href='/signin'">Sign In / Create Account</button>
            <button class="otms-btn secondary" onclick="window.location.href='/collab'">COLLAB with OTMS</button>
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)

# --- Example Feed Cards (same as before, for posts) ---
posts = [
    {
        "username": "Yashwant",
        "caption": "Tried the new RED blend on this masala chicken – Mindblowing!",
        "media": "engage_assets/post1.jpg",
        "media_type": "image",
    },
    {
        "username": "Priya",
        "caption": "Family dinner night. Thanks OTMS for making it easy 💛",
        "media": "engage_assets/post2.jpg",
        "media_type": "image",
    },
]

st.write("")  # Small space below header bar

for post in posts:
    st.markdown(
        """
        <div style="
            background: #19191a;
            border-radius: 22px;
            box-shadow: 0 2px 32px #0006;
            margin: 0 auto 36px auto; max-width: 430px; padding: 25px 30px 16px 30px; color: #fff; position: relative;">
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='font-weight: bold; font-size: 18px; color: #ffd700; margin-bottom: 3px;'>{post['username']}</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='color: #eee; font-size: 17px; margin-bottom: 11px;'>{post['caption']}</div>",
        unsafe_allow_html=True,
    )
    if post["media_type"] == "image":
        b64 = avatar_base64(post["media"])
        ext = Path(post["media"]).suffix[1:]
        if b64:
            st.markdown(
                f"<img style='border-radius: 18px; width: 100%; object-fit: cover; box-shadow: 0 2px 16px #0004; margin-bottom: 18px;' src='data:image/{ext};base64,{b64}'>",
                unsafe_allow_html=True,
            )
        else:
            st.warning("Image not found.")
    elif post["media_type"] == "video":
        video_path = post["media"]
        if Path(video_path).exists():
            st.video(str(video_path))
        else:
            st.warning("Video not found.")
    st.markdown("""
        <div style="display: flex; gap: 30px; margin-top: 11px; color: #ffd700; font-size: 19px; cursor: pointer;">
            ❤️ Like &nbsp; 💬 Comment &nbsp; 🔄 Share
        </div>
    </div>
    """, unsafe_allow_html=True)

