import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Learn - One to Many Spices", layout="wide")

# Load logo
logo = Image.open("logo_left.png")

# Top navigation
col1, col2 = st.columns([1, 8])
with col1:
    st.image(logo, width=80)
with col2:
    st.markdown("[← Back to Home](/)", unsafe_allow_html=True)

# Page Title
st.markdown("<h1 style='text-align: center;'>LEARN</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Start your journey with One to Many Spices — understand our blends, master your kitchen, and elevate your cooking skills.</p>", unsafe_allow_html=True)
st.markdown("---")

# Learn Sections
st.markdown("## 📚 Choose a Learning Path")

colA, colB, colC = st.columns(3)

with colA:
    st.markdown("""
        <div style='border: 2px solid #e74c3c; border-radius: 12px; padding: 20px; text-align: center; background-color: #fdecea;'>
            <h3>🌶️ Spice Blend Basics</h3>
            <p>Learn how each OTMS blend works, what it replaces, and how to use it.</p>
        </div>
    """, unsafe_allow_html=True)

with colB:
    st.markdown("""
        <div style='border: 2px solid #2ecc71; border-radius: 12px; padding: 20px; text-align: center; background-color: #e8f7f0;'>
            <h3>🍳 Beginner Recipes</h3>
            <p>Simple, delicious recipes using our blends — ready in under 30 minutes.</p>
        </div>
    """, unsafe_allow_html=True)

with colC:
    st.markdown("""
        <div style='border: 2px solid #f39c12; border-radius: 12px; padding: 20px; text-align: center; background-color: #fef5e7;'>
            <h3>🔥 Advanced Techniques</h3>
            <p>Learn how to layer flavors, pair blends, and cook restaurant-quality dishes.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Future: Add routing when clicked
st.info("Routing to sub-pages coming soon. Let me know when you're ready to build each section.")
