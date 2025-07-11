import streamlit as st
import openai
import base64
from pathlib import Path

st.set_page_config(page_title="Cook | One to Many Spices", layout="wide")

# ---------------- Load and Encode Image ----------------
def img_to_base64(img_path):
    if Path(img_path).exists():
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

# ---------------- Logo and Tagline Setup ----------------
logo_left = img_to_base64("otms_assets/logo_dark.png")
logo_right = img_to_base64("otms_assets/logo_dark.png")

col1, col2, col3 = st.columns([1, 4, 1])
with col1:
    if logo_left:
        st.image(f"data:image/png;base64,{logo_left}", width=80)
with col2:
    st.markdown("""
        <h2 style='text-align: center; margin-bottom: 5px;'>CREATE RECIPES THAT LET MEMORIES LAST</h2>
    """, unsafe_allow_html=True)
with col3:
    if logo_right:
        st.image(f"data:image/png;base64,{logo_right}", width=80)

# ---------------- CSS Styling ----------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .button-main {
        text-align: center;
        padding: 20px;
    }
    .button-styled {
        background-color: #ff9c33;
        border: none;
        color: white;
        padding: 15px 32px;
        font-size: 18px;
        border-radius: 12px;
        transition: 0.3s ease-in-out;
        cursor: pointer;
    }
    .button-styled:hover {
        background-color: #ff7a00;
        transform: scale(1.05);
    }
    .recipe-block {
        background-color: #fff4e6;
        padding: 25px;
        border-radius: 16px;
        margin-top: 25px;
        font-size: 17px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- GPT Recipe Generator ----------------
st.markdown("<div class='button-main'>", unsafe_allow_html=True)
generate = st.button("🍳 Generate Recipe", key="generate", help="Click to create a recipe using OTMS blends", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

if generate:
    with st.spinner("Cooking up your recipe with OTMS magic... 🍲"):
        prompt = (
            "Generate a unique, delicious Indian recipe using professional culinary style, "
            "based on OTMS (One to Many Spices) blends such as RED Blend, WHITE Blend, YELLOW Blend, BROWN Blend, GREEN Blend, GRAY Blend. "
            "Replace individual spices like red chili or garam masala with these blends. "
            "Include dish name, preparation, ingredients, cooking steps, texture, spice level, pairing suggestions, serving size, pro tips. "
            "Avoid ginger garlic paste—use GRAY Blend as its substitute. Format the output professionally."
        )
        try:
            openai.api_key = st.secrets["openai"]["api_key"]
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            recipe_text = response.choices[0].message.content
        except Exception as e:
            recipe_text = f"❌ Failed to generate recipe. Error: {str(e)}"

    st.markdown(f"<div class='recipe-block'>{recipe_text}</div>", unsafe_allow_html=True)

# ---------------- Additional Buttons ----------------
st.markdown("<div class='button-main'>", unsafe_allow_html=True)
col_upload, col_save = st.columns(2)

with col_upload:
    st.button("📤 Upload Your Own", key="upload", help="Coming soon: Share your own recipe")
with col_save:
    st.button("💾 Save Recipe", key="save", help="Coming soon: Save recipes to your collection")
st.markdown("</div>", unsafe_allow_html=True)
