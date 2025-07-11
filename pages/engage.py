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

# ---------------- Share Section ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("### ✨ Share Your Creations")

st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload your OTMS recipe creation (image or video)", type=["png", "jpg", "jpeg", "mp4"])
st.markdown("<p>Share your love of spices! Get featured on our community wall 🌟</p>", unsafe_allow_html=True)
if uploaded_file:
    st.success("Thanks for sharing! Our team will review it soon. 🌟")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- Follow & Tag Us ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("### 📱 Follow & Tag Us")
st.markdown("""
<div class="social-links">
- Instagram: [@onetomanyspices](https://instagram.com/onetomanyspices)  
- YouTube: [One to Many Spices Channel](https://youtube.com)  
- Pinterest: [One to Many Pins](https://pinterest.com)  
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- Email Signup ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("### 📬 Join the Community")
user_email = st.text_input("Enter your email to subscribe:")
if user_email:
    st.success("You're on the list! 🔔")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- Community Carousel ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("### 🌍 OTMS Community Highlights")

community_posts = [
    {"title": "Paneer Tikka by Anjali", "caption": "Cooked over campfire using GREEN Blend", "image": "otms_assets/community1.jpg"},
    {"title": "Biriyani Day Vlog by Karthik", "caption": "Behind the scenes with OTMS", "image": "otms_assets/vlog1.jpg"},
    {"title": "My Journey with OTMS", "caption": "A delicious year of discovery!", "image": "otms_assets/blog1.jpg"},
]

titles = [p["title"] for p in community_posts]
selected = st.selectbox("Select a featured post", titles)
post = next((p for p in community_posts if p["title"] == selected), None)
if post:
    img_b64 = img_to_base64(post["image"])
    if img_b64:
        st.markdown(f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{img_b64}" class="carousel-img">
                <h4>{post['title']}</h4>
                <p><i>{post['caption']}</i></p>
            </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- Auth Box ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("### 👤 Join the Creator Community")

st.markdown('<div class="auth-box">', unsafe_allow_html=True)
auth_mode = st.radio("Choose an option", ["Sign In", "Create Account"], horizontal=True)

if auth_mode == "Sign In":
    st.text_input("Email", key="signin_email")
    st.text_input("Password", type="password", key="signin_password")
    if st.button("Sign In"):
        st.success("Signed in successfully! (Mockup)")

elif auth_mode == "Create Account":
    st.text_input("Name", key="signup_name")
    st.text_input("Email", key="signup_email")
    st.text_input("Password", type="password", key="signup_password")
    if st.button("Create Account"):
        st.success("Account created! You're ready to ENGAGE ✨")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
