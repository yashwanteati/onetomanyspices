import streamlit as st

st.set_page_config(page_title="Welcome | OTMS BETA", layout="wide")

# ------------- White theme + More Animations + All-Black/Bold Text -------------
st.markdown("""
    <style>
    :root {
        --otms-bg: #ffffff;
        --otms-text: #000000;    /* very black */
        --otms-card: #f9fafb;
        --otms-border: #e5e7eb;
        --otms-cta: #ffd000;     /* soft golden yellow */
    }

    /* Base + global typography overrides */
    body, .stApp { background: var(--otms-bg) !important; color: var(--otms-text) !important; }
    .block-container { padding-top: 1.2rem; max-width: 1200px; }
    /* Make EVERYTHING black & bold */
    .stMarkdown, .stText, .stCaption, p, span, li, label,
    h1, h2, h3, h4, h5, h6, b, strong { color: var(--otms-text) !important; font-weight: 800 !important; }

    /* Title: pop in + slight drop shadow */
    .otms-beta-title {
        font-size: 52px;
        text-align: center;
        font-family: 'Georgia', serif;
        margin-top: 40px;
        letter-spacing: 3px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.08);
        animation: popin 0.9s cubic-bezier(.8,2.5,.8,1) forwards;
    }

    /* Subtitle: fade up */
    .otms-beta-sub {
        font-size: 30px;
        text-align: center;
        margin-top: 0px;
        margin-bottom: 28px;
        font-family: 'Trebuchet MS', sans-serif;
        opacity: 0;
        transform: translateY(6px);
        animation: fadeup 0.9s ease-out 0.2s forwards;
    }

    /* Info card: float + soft shadow pulse */
    .otms-beta-note {
        background: var(--otms-card);
        font-size: 20px;
        border-radius: 18px;
        text-align: center;
        margin: 0 auto 36px auto;
        max-width: 760px;
        padding: 22px 28px;
        border: 1px solid var(--otms-border);
        box-shadow: 0 12px 34px rgba(2, 8, 23, 0.06);
        animation: floaty 4.5s ease-in-out infinite, fadein 0.8s ease 0.35s both, shadowpulse 2.8s ease-in-out infinite;
    }

    .helper { text-align:center; margin-top: 8px; font-size: 14px; opacity: .85; }

    /* CTA button: breathing + wiggle on hover */
    .stButton>button {
        font-size: 22px;
        color: #000;
        background: var(--otms-cta);
        border: 2px solid var(--otms-cta);
        border-radius: 9999px;
        padding: 13px 24px;
        box-shadow: 0 10px 30px rgba(234, 179, 8, 0.35);
        cursor: pointer;
        margin-top: 12px !important;
        width: 100%;
        font-weight: 900;
        animation: breathe 2.2s ease-in-out infinite;
        transition: transform 0.14s, box-shadow 0.2s, filter 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.035) rotate(-0.4deg);
        animation: wiggle 0.6s ease-in-out;
        box-shadow: 0 12px 36px rgba(2, 8, 23, 0.18);
        filter: brightness(0.98);
    }
    .stButton>button:focus { outline: 3px solid rgba(0,0,0,0.25); }

    /* Confetti marquee (infinite scroll) */
    .confetti-wrap {
        overflow: hidden;
        white-space: nowrap;
        width: 100%;
        opacity: .95;
        margin-bottom: 6px;
        user-select: none;
    }
    .confetti, .confetti-2 {
        display: inline-block;
        padding-left: 100%;
    }
    .confetti { animation: marquee 18s linear infinite; }
    .confetti-2 { animation: marquee-rev 22s linear infinite; opacity: .9; }

    /* Hide left sidebar */
    [data-testid="stSidebar"] {display: none !important;}

    /* ------- Keyframes ------- */
    @keyframes popin { 0% {transform: scale(0.96); opacity:0;} 100% {transform: scale(1); opacity:1;} }
    @keyframes fadein {from {opacity:0;} to {opacity:1;} }
    @keyframes fadeup {from {opacity:0; transform: translateY(10px);} to {opacity:1; transform: translateY(0);} }
    @keyframes floaty { 0%,100% { transform: translateY(0) } 50% { transform: translateY(-6px) } }
    @keyframes shadowpulse {
        0%,100% { box-shadow: 0 12px 34px rgba(2, 8, 23, 0.06); }
        50%     { box-shadow: 0 14px 42px rgba(2, 8, 23, 0.10); }
    }
    @keyframes breathe { 0%,100% { transform: scale(1.00); } 50% { transform: scale(1.03); } }
    @keyframes wiggle {
        0% { transform: rotate(0deg) scale(1.03); }
        25% { transform: rotate(-1.2deg) scale(1.035); }
        50% { transform: rotate(1.2deg) scale(1.035); }
        75% { transform: rotate(-0.6deg) scale(1.035); }
        100% { transform: rotate(0deg) scale(1.035); }
    }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    @keyframes marquee-rev { 0% { transform: translateX(-10%); } 100% { transform: translateX(90%); } }
    </style>
""", unsafe_allow_html=True)

# ----------------- Confetti Marquee -----------------
st.markdown(
    "<div class='confetti-wrap'><div class='confetti'>🌶️ 🥳 🌿 🟠 🟡 🍲 ✨ 🧄 🥒 🧅 🌶️ WELCOME TO ONE TO MANY SPICES 🌶️ 🥳 🌿 🟠 🟡 🍲 ✨ 🧄 🥒 🧅 🌶️</div></div>",
    unsafe_allow_html=True,
)
# ----------- Headline and Welcome Message -------------
st.markdown("<div class='otms-beta-title'>Welcome to OTMS BETA</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='otms-beta-sub'>A whole new world of flavor, recipes & discovery awaits you…</div>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class='otms-beta-note'>
        <b>This is a BETA version of One To Many Spices.</b><br>
        Some features may be limited or unlocked as we grow!<br><br>
        <b>Ready to explore &amp; create?</b><br>
        Jump in and let’s cook up something unforgettable with <b>OTMS</b>!<br><br>
        Get ready to <b>LEARN</b> new skills, <b>SHOP</b> for flavors, <b>COOK</b> with ease,
        <b>DINE</b> in style, and <b>ENGAGE</b> with a food-loving community. Your world of spices starts here!<br>
        <span style="font-size: 15px; opacity:.75">(Best experienced on Chrome/Edge/Firefox/Safari)</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Single CTA ----------
col = st.columns([1,2,1])[1]
with col:
    go = st.button("Enter the OTMS World ↘", type="primary", use_container_width=True)
    st.markdown("<div class='helper'>(Best on Chrome · Edge · Firefox · Safari)</div>", unsafe_allow_html=True)

# ---------- Navigation to pages/home.py ----------
if go:
    st.switch_page("pages/home.py")
