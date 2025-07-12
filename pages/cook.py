import streamlit as st
import base64
import time
import itertools
import openai
from pathlib import Path
import re
import urllib.parse


st.set_page_config(page_title="One to Many Spices", layout="wide")

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

# ---------------- Image Conversion ----------------
def img_to_base64(path):
    try:
        image_bytes = Path(path).read_bytes()
        return base64.b64encode(image_bytes).decode()
    except Exception:
        return ""

# ---------------- Header Section (Logos + Title) ----------------
header_cols = st.columns([1, 4, 1])
with header_cols[0]:
    st.image("otms_assets/otms_logo_light.png", use_container_width=True)

with header_cols[1]:
    st.markdown("""
        <div style='text-align: center; margin-top: 05px;'>
            <h1 style='font-size: 52px; margin-bottom: 5px;'>ONE TO MANY</h1>
            <h2 style='letter-spacing: 14px; font-size: 30px; margin-top: -20px;'>S   P   I   C   E   S</h2>
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
# ---------------- Hide Sidebar ----------------
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
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Page Header ----------------
st.markdown("""
    <h1 style='font-size: 40px;'>🔍 Cook with OTMS</h1>
    <p style='font-size: 18px;'>GENERATING RECIPES THAT LET MEMORIES LAST FOR YOUR LOVED ONE's</p>
""", unsafe_allow_html=True)

# ---------------- Dish Input ----------------
dish_name = st.text_input("🍽️ What dish would you like to cook today?", "")

# ---------------- Use OTMS Blends ----------------
us_blends = st.radio("Would you like the recipe with OTMS Blends?", ["YES", "NO"], index=0)

# ---------------- Language Selection ----------------
st.markdown("### Select language for voice:")
lang = st.selectbox("Language", ["English", "Hindi", "Telugu", "Tamil", "Marathi", "Kannada"])

# ---------------- Loader Image ----------------
def load_base64_image(image_path):
    image_file = Path(image_path)
    if image_file.exists():
        with open(image_file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

loader_images = [
    "otms_assets/cook_loader_1.png",
    "otms_assets/cook_loader_2.png",
    "otms_assets/cook_loader_3.png"
]

def display_rotating_loader(duration=6):
    placeholder = st.empty()
    end_time = time.time() + duration
    images_cycle = itertools.cycle(loader_images)

    while time.time() < end_time:
        img_path = next(images_cycle)
        base64_loader = load_base64_image(img_path)
        if base64_loader:
            placeholder.markdown(f"""
                <div style='text-align: center;'>
                    <img src='data:image/png;base64,{base64_loader}' style='width: 250px; height: auto;' alt='Loading...'/>
                    <p style='font-size: 18px; margin-top: 10px;'>Generating your recipe...</p>
                </div>
            """, unsafe_allow_html=True)
        time.sleep(1.2)
    placeholder.empty()

# ---------------- Recipe State ----------------
st.session_state.setdefault("recipe_blocks", {})
st.session_state.setdefault("current_block", "")
st.session_state.setdefault("recipe_ready", False)
st.session_state.setdefault("step_index", 0)
st.session_state.setdefault("steps_list", [])
st.session_state.setdefault("fun_fact", "")

# ---------------- Generate Recipe Button ----------------
if st.button("🍳 Generate Recipe"):
    if not dish_name.strip():
        st.error("Please enter a dish name to generate the recipe.")
    else:
        display_rotating_loader(duration=6)
        st.write("✅ API Key loaded:", bool(openai.api_key))

        openai.api_key = st.secrets["openai"]["api_key"]

        prompt = f"""
        Generate a detailed recipe for {dish_name.strip()} in Indian style.
        Include the following sections clearly separated and labeled:
        Ingredients
        Preparation (like marination, chopping, soaking, etc.)
        Steps (cooking instructions)
        Add a fun fact related to the dish at the end.
        Use OTMS Blends if specified.

        OTMS Blends:
        - RED Blend = Red chili–based masala
        - YELLOW Blend = Turmeric, coriander-based masala
        - GRAY Blend = Ginger garlic powder blend
        - GREEN Blend = Herb and curry leaf masala
        - BROWN Blend = Garam masala
        - WHITE Blend = Subtle base gravy masala

        User preference: {"Use OTMS Blends" if us_blends == "YES" else "No OTMS Blends"}
        """

        with st.spinner("Getting your recipe ready..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a master Indian chef using OTMS spice blends."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )

                full_recipe = response['choices'][0]['message']['content']
                normalized = full_recipe.replace("**", "").replace("__", "").strip().lower()

                sections = {"ingredients": "", "preparation": "", "steps": "", "fun_fact": ""}
                current = None
                for line in normalized.splitlines():
                    if "ingredients" in line:
                        current = "ingredients"
                        continue
                    elif "preparation" in line:
                        current = "preparation"
                        continue
                    elif "steps" in line:
                        current = "steps"
                        continue
                    elif "fun fact" in line:
                        current = "fun_fact"
                        continue
                    elif current:
                        sections[current] += line.strip() + "\n"

                steps_raw = sections["steps"].strip().split("\n")
                steps_list = [s for s in steps_raw if s.strip()]

                st.session_state.recipe_blocks = {
                    "Ingredients": sections["ingredients"].strip() or "Not found.",
                    "Preparation": sections["preparation"].strip() or "Not found.",
                    "Steps": steps_list
                }
                st.session_state.current_block = "Ingredients"
                st.session_state.recipe_ready = True
                st.session_state.step_index = 0
                st.session_state.steps_list = steps_list
                st.session_state.fun_fact = sections["fun_fact"].strip()

            except Exception as e:
                st.error(f"Something went wrong: {e}")

# ---------------- Display Recipe ----------------
if st.session_state.recipe_ready:
    block = st.session_state.current_block
    st.markdown(f"## 🍛 {dish_name.strip().title()} - {block}")

    if block == "Steps":
        steps = st.session_state.steps_list
        idx = st.session_state.step_index
        if idx < len(steps):
            st.markdown(f"**Step {idx+1} of {len(steps)}:** {steps[idx]}")
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("⬅️ Back") and idx > 0:
                    st.session_state.step_index -= 1
            with col2:
                if st.button("Next ➡️"):
                    st.session_state.step_index += 1
        else:
            st.success("🎉 Dish completed! Don't forget to garnish with coriander leaves and serve hot.")
            if st.session_state.fun_fact:
                st.info(f"🍽️ Fun Fact: {st.session_state.fun_fact}")
            if st.button("🔁 Start Over"):
                st.session_state.recipe_ready = False
    else:
        st.markdown(st.session_state.recipe_blocks.get(block, "Not available."))
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if block != "Ingredients":
                if st.button("⬅️ Back"):
                    if block == "Preparation":
                        st.session_state.current_block = "Ingredients"
        with col3:
            if block != "Steps":
                if st.button("Next ➡️"):
                    if block == "Ingredients":
                        st.session_state.current_block = "Preparation"
                    elif block == "Preparation":
                        st.session_state.current_block = "Steps"

    search_term = urllib.parse.quote(dish_name.strip())
    image_url = f"https://source.unsplash.com/600x400/?{search_term}"
    st.image(image_url, caption=f"Representative image for {dish_name.strip().title()} (via Unsplash)", use_container_width=True)
