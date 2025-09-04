import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="One to Many Spices", layout="wide")

# ---------------- CSS Styling (white theme) ----------------
st.markdown("""
    <style>
    :root{
        --page:#ffffff;
        --ink:#111827;          /* primary text */
        --muted:#475569;        /* secondary text */
        --card:#ffffff;         /* tile bg */
        --border:#e5e7eb;       /* light grey */
        --shadow:0 10px 28px rgba(2,8,23,.08);
    }

    [data-testid="stSidebar"] { display: none; }

    /* Page background + default text */
    body, .stApp, .block-container, .main {
        background: var(--page) !important;
        color: var(--ink) !important;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Buttons (top-right) */
    .top-right-btns {
        position: absolute;
        top: 15px;
        right: 64px;
        z-index: 999;
        display: flex;
        gap: 6px;
    }
    .otms-btn {
        background: #ff3c38;
        color: #fff;
        border: none;
        border-radius: 12px;
        padding: 8px 22px;
        font-weight: 800;
        font-size: 12px;
        cursor: pointer;
        box-shadow: var(--shadow);
        transition: transform .12s ease, filter .12s ease;
    }
    .otms-btn:hover { transform: translateY(-1px); filter: brightness(.98); }
    .otms-btn.secondary { background: #004aad; }

    /* Menu image buttons */
    .button-img {
        border-radius: 50px;
        transition: transform 0.3s ease-in-out;
        cursor: pointer;
    }
    .button-img:hover { transform: scale(1.1); }
    .menu-button { text-align: center; margin-top: 6px; background: transparent; box-shadow: none; }

    /* Floating chat button */
    .floating-chat { position: fixed; right: 32px; bottom: 32px; z-index: 9999; }
    .chat-circle-btn {
        width: 66px; height: 66px;
        background: #fddb52;
        border-radius: 50%;
        border: 2px solid #ff3c38;
        box-shadow: 0 2px 12px #0003;
        display: flex; align-items: center; justify-content: center;
        cursor: pointer; font-size: 38px; color: #ff3c38; font-weight: bold;
        transition: transform 0.2s;
    }
    .chat-circle-btn:hover { transform: scale(1.1); }
    .chat-popup {
        position: fixed; right: 120px; bottom: 44px; width: 330px;
        background: #fff; border-radius: 18px; box-shadow: 0 4px 28px #0002;
        padding: 16px; z-index: 99999; border: 1.5px solid #ff3c38; animation: fadein .2s;
    }
    @keyframes fadein { from {opacity:0; transform: translateY(40px);} to {opacity:1; transform:none;} }

    /* Spacing fixes around columns / icons */
    div[data-testid="column"] > div:first-child { margin-bottom: 0 !important; padding-bottom: 0 !important; }
    .menu-button { margin-top: 0 !important; }

    /* Email section on white */
    .custom-email-box { margin-top: 5px !important; margin-bottom: 0 !important; display:flex; flex-direction:column; align-items:center; }
    .custom-email-box h3 { margin: 6px 0 6px 0 !important; color: var(--ink); }
    section[data-testid="stTextInput"] { padding-top: 0 !important; margin-top: -30px !important; }
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
    st.image("otms_assets/otms_logo_light.png", width=250)
# ---------------- Button Config ----------------
buttons = [
    {"label": "LEARN", "image": "otms_assets/learn.png", "page": "learn"},
    {"label": "SHOP", "image": "otms_assets/shop.png", "page": "shop"},
    {"label": "COOK", "image": "otms_assets/cook.png", "page": "cook"},
    {"label": "DINE", "image": "otms_assets/dine.png", "page": "dine"},
    {"label": "ENGAGE", "image": "otms_assets/engage.png", "page": "engage"},
]

# ---------------- Render 3D Icon Buttons (now on white cards) ----------------
img_cols = st.columns(5)
for col, btn in zip(img_cols, buttons):
    with col:
        b64_img = img_to_base64(btn["image"])
        if b64_img:
            st.markdown(
                f"""
                <div style="display:flex;justify-content:center;align-items:center;background:transparent;border:none;padding:4px;">
                    <a href="/{btn['page']}" target="_self">
                        <div style="
                            height:350px;width:350px;background: var(--card);
                            border-radius:32px; display:flex; align-items:center; justify-content:center;
                            box-shadow: var(--shadow); border:1px solid var(--border);
                        ">
                            <img src="data:image/png;base64,{b64_img}" class="button-img"
                                 style="height:350px;width:350px;object-fit:contain;background:transparent;">
                        </div>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning(f"Image not found: {btn['image']}")

# ---------------- Email Subscription ----------------
st.markdown("""
    <div class="custom-email-box">
        <h3>📬 Stay Updated</h3>
    </div>
""", unsafe_allow_html=True)

email = st.text_input("", placeholder="Enter your email to subscribe:")
if st.button("Subscribe"):
    if email:
        st.success(f"Thanks for subscribing, {email}!")
    else:
        st.error("Please enter a valid email.")

# ------------------- OPTIONAL: FLOATING CHAT BUBBLE -------------------
if "chat_open" not in st.session_state:
    st.session_state["chat_open"] = False

st.markdown("""
    <div class="floating-chat">
        <div onclick="window.parent.postMessage({isOpen: true}, '*')" class="chat-circle-btn" id="otms-chat-btn">💬</div>
    </div>
""", unsafe_allow_html=True)

if st.session_state["chat_open"]:
    st.markdown("""
        <div class="chat-popup">
            <b>Ask Me (OTMS AI Chat)</b>
            <br>
            <input style="width:93%;margin:8px 0 0 0;padding:6px;border-radius:6px;border:1px solid var(--border);" placeholder="Type your question..."/>
            <div style="margin-top: 12px; color: #888; font-size:13px;">(Demo: Integration ready)</div>
            <button style="float:right;background:#ff3c38;color:#fff;border:none;border-radius:8px;padding:7px 15px;margin-top:9px;">Send</button>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
<script>
    window.addEventListener("message", function(event){
        if(event.data && event.data.isOpen){
            // trigger any UI you want when chat opens
        }
    }, false);
</script>
""", unsafe_allow_html=True)
