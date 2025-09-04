# cook.py — OTMS (white theme + categories strip + watermark-safe recipe pane)

import base64, datetime, json, re, smtplib, ssl, urllib.parse
from email.message import EmailMessage
from pathlib import Path
import streamlit as st

# ======================== Page & Theme ========================
st.set_page_config(page_title="Cook | One to Many Spices", layout="wide")
ACCENT_RED = "#FF3C38"

st.markdown(
    f"""
<style>
:root {{
  --accent-red:{ACCENT_RED};
  --page:#ffffff; --ink:#111827; --muted:#475569;
  --border:#e5e7eb; --shadow:0 10px 24px rgba(2,8,23,.08);
}}
/* Optional local fonts (drop your files into otms_assets/fonts/) */
@font-face {{
  font-family:'LeJourSerif';
  src: url('/otms_assets/fonts/LeJourSerif.woff2') format('woff2');
  font-display:swap;
}}
@font-face {{
  font-family:'TTInterphaseMono';
  src: url('/otms_assets/fonts/TTInterphaseMono.woff2') format('woff2');
  font-display:swap;
}}
/* Base */
[data-testid="stSidebar"]{{display:none!important}}
body,.stApp,.block-container,.main{{background:var(--page)!important;color:var(--ink)!important;font-family:'Helvetica Neue',sans-serif}}
.block-container{{max-width:1200px;padding-top:.6rem}}
/* Top-right buttons */
.top-right-btns{{position:absolute;top:12px;right:22px;z-index:1000;display:flex;gap:8px}}
.otms-btn{{background:#ff3c38;color:#fff;border:none;border-radius:12px;padding:8px 16px;font-weight:800;font-size:12px;cursor:pointer;box-shadow:var(--shadow)}}
.otms-btn.secondary{{background:#004aad}}
.otms-btn:hover{{filter:brightness(.97)}}
/* Header row */
.header-wrap{{display:grid;grid-template-columns:180px 1fr 220px;align-items:center;gap:16px;margin:8px 0 10px}}
.header-center{{text-align:center}}
.header-center h1{{font-family:'LeJourSerif', 'Playfair Display', serif;font-size:64px;letter-spacing:.08em;margin:.1rem 0 .25rem}}
.header-center p{{font-family:'TTInterphaseMono','ui-monospace','SFMono-Regular',Menlo,monospace;color:var(--ink);opacity:.85;margin:.2rem 0}}
/* White cards / panels */
.header-card,.panel{{background:#fff;border:1px solid var(--border);border-radius:16px;padding:14px 18px;box-shadow:var(--shadow)}}
.header-card{{text-align:center;margin:8px 0 16px}}
.panel{{margin:6px 0 12px}}
/* Labels */
.hint-chip{{display:inline-block;padding:6px 10px;border-radius:10px;background:#f8fafc;border:1px solid var(--border);color:#0f172a;font-weight:700;margin-bottom:6px}}
.label{{display:block;margin:6px 0 6px;font-weight:800;color:#0f172a;text-transform:uppercase;letter-spacing:.4px}}
/* Buttons */
.stButton > button[kind="primary"]{{width:100%;background:var(--accent-red);color:#fff;border-radius:12px;font-weight:800;padding:12px 18px;border:1px solid #bf2a26}}
.stButton > button:not([kind="primary"]){{width:100%;background:#fff;color:#111827;border-radius:10px;border:1px solid var(--border);font-weight:700;padding:10px 12px;box-shadow:0 4px 12px rgba(2,8,23,.04)}}
.stButton > button:not([kind="primary"]):hover{{background:#f8fafc}}
.stButton > button:disabled{{opacity:.9!important;color:#94a3b8!important;background:#f1f5f9!important;border:1px solid var(--border)!important}}
/* Tabs */
.stTabs [role="tablist"]{{border-bottom:1px solid var(--border)}}
.stTabs [role="tab"]{{color:#64748b;font-weight:700}}
.stTabs [aria-selected="true"]{{color:#111827;border-bottom:3px solid var(--accent-red)}}
/* Read-aloud + chips */
.rl-btn,.fact{{background:#fff;border:1px solid var(--border);border-radius:12px;box-shadow:0 4px 12px rgba(2,8,23,.04)}}
.rl-btn{{width:100%;padding:10px 14px;color:#111827;font-weight:700;cursor:pointer}}
.rl-btn:hover{{background:#f8fafc}}
.fact{{padding:14px 16px;color:#334155}}
hr.sep{{border:none;border-top:1px solid var(--border);margin:12px 0}}
/* Category strip */
#cats{{scroll-margin-top:20px}}
.cat-strip{{display:flex;gap:24px;align-items:center;justify-content:center;flex-wrap:wrap;margin:2px 0 10px}}
.cat-card{{display:flex;flex-direction:column;align-items:center;gap:8px}}
.cat-img{{width:84px;height:84px;border-radius:50%;border:1px solid var(--border);box-shadow:0 6px 16px rgba(2,8,23,.08);background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.cat-img img{{width:100%;height:100%;object-fit:contain;animation:spin 18s linear infinite}}
.cat-img:hover img{{animation-duration:8s}}
.cat-label{{font-weight:900;letter-spacing:.03em}}
@keyframes spin{{from{{transform:rotate(0deg)}}to{{transform:rotate(360deg)}}}}
/* Dish list (Block 4) */
.grid{{display:grid;grid-template-columns:repeat(2, minmax(0,1fr));gap:14px}}
.dish{{background:#fff;border:1px solid var(--border);border-radius:12px;padding:12px 14px;box-shadow:0 4px 12px rgba(2,8,23,.04)}}
.dish a{{text-decoration:none;color:#111827;font-weight:800}}
/* Shop link */
.shop-link{{display:flex;justify-content:center;margin:16px 0}}
</style>
""",
    unsafe_allow_html=True,
)

# ======================== Assets / Helpers ========================
BASE_DIR = Path(__file__).resolve().parents[1]


def b64file(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode() if p.exists() else ""
# Inline logo once
LOGO_B64 = b64file(Path("otms_assets/otms_logo_light.png"))

def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.strip().lower())

# Loader assets (if you use them)
LOADER_B64 = [b64file(Path("otms_assets") / f"cook_loader_{i}.png") for i in range(1, 6)]
PLACEHOLDER_B64 = b64file(Path("otms_assets/food_placeholder.jpg")) or b64file(Path("otms_assets/cook_loader_1.png"))

def loader_html() -> str:
    if not any(LOADER_B64):
        return '<div class="loader-stack"><div class="loader-cap">Generating…</div></div>'
    imgs = "".join(f'<img class="f{i+1}" src="data:image/png;base64,{b}"/>' for i, b in enumerate(LOADER_B64) if b)
    return f'<div class="loader-stack">{imgs}<div class="loader-cap">Generating your recipe…</div></div>'

def resilient_dish_img(name: str) -> str:
    slug = slugify(name)
    locals_ = [Path(f"otms_assets/dishes/{slug}{ext}") for ext in (".jpg",".png",".webp")]
    local = next((b64file(p) for p in locals_ if p.exists()), "")
    unsplash = f"https://source.unsplash.com/800x500/?{urllib.parse.quote(name)}"
    picsum = "https://picsum.photos/800/500?blur=1"
    src = f"data:image/*;base64,{local}" if local else unsplash
    return f"""<img src="{src}"
         onerror="if(this.src.indexOf('unsplash')>-1){{this.src='{picsum}';}}
                  else{{this.onerror=null;this.src='data:image/png;base64,{PLACEHOLDER_B64}';}}"
         style="width:100%;height:auto;border-radius:12px;border:1px solid #e5e7eb" />"""

# ---------------- Category data ----------------
CATS = [
    ("THALI","otms_assets/cat_thali.png", [
        "South Indian Thali","North Indian Thali","Andhra Meals","Mini Meals","Gujarati Thali","Rajasthani Thali"
    ]),
    ("BIRYANI","otms_assets/cat_biryani.png", [
        "Chicken Biryani","Veg Dum Biryani","Paneer Biryani","Hyderabadi Mutton Biryani","Egg Biryani","Prawn Biryani"
    ]),
    ("TIFFINS","otms_assets/cat_tiffins.png", [
        "Idli Sambar","Masala Dosa","Upma","Medu Vada","Pesarattu","Poori Bhaji"
    ]),
    ("SEA FOOD","otms_assets/cat_seafood.png", [
        "Prawn Masala","Fish Fry","Fish Curry","Crab Masala","Prawn Pulao","Tawa Fish"
    ]),
    ("VEG","otms_assets/cat_veg.png", [
        "Aloo Gobi","Bhindi Fry","Paneer Butter Masala","Kadai Paneer","Baingan Bharta","Chole Masala"
    ]),
    ("TANDOOR","otms_assets/cat_tandoor.png", [
        "Chicken Tikka","Paneer Tikka","Tandoori Roti","Malai Tikka","Tandoori Chicken","Veg Seekh"
    ]),
    ("RICE","otms_assets/cat_rice.png", [
        "Jeera Rice","Veg Pulao","Curd Rice","Tomato Rice","Lemon Rice","Ghee Rice"
    ]),
    ("NON VEG","otms_assets/cat_nonveg.png", [
        "Chicken Fry","Pepper Chicken","Mutton Curry","Chicken Chettinad","Andhra Chicken","Keema Masala"
    ]),
    ("EGG","otms_assets/cat_egg.png", [
        "Egg Curry","Egg Fried Rice","Egg Bhurji","Masala Omelette","Egg Roast","Anda Ghotala"
    ]),
    ("INDO CHINESE","otms_assets/cat_indochinese.png", [
        "Veg Manchurian","Gobi Manchurian","Chicken Lollipop","Hakka Noodles","Schezwan Rice","Chilli Chicken"
    ]),
    ("SNACKS","otms_assets/cat_snacks.png", [
        "Samosa","Pakora","Mirchi Bajji","Cutlet","Onion Rings","Bhel Puri"
    ]),
]

# ======================== Query Params / State ========================
try:
    qp = st.query_params  # Streamlit >= 1.30
    get_q = lambda k: qp.get(k)
except Exception:
    get_q = lambda k: st.experimental_get_query_params().get(k, [None])[0]

cat_q = get_q("cat")
dish_q = get_q("dish")

st.session_state.setdefault("dish_name", "")
st.session_state.setdefault("category", None)
st.session_state.setdefault("pending", False)
st.session_state.setdefault("recipe_ready", False)
st.session_state.setdefault("step_idx", 1)

if dish_q:
    st.session_state["dish_name"] = dish_q
if cat_q:
    st.session_state["category"] = cat_q

# ======================== Header (1) ========================
st.markdown("""
<div class="top-right-btns">
    <button class="otms-btn" onclick="window.location.href='/signin'">Sign In / Create Account</button>
    <button class="otms-btn secondary" onclick="window.location.href='/collab'">COLLAB with OTMS</button>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f"""
<div class="header-wrap">
  <div>
    <img src="data:image/png;base64,{LOGO_B64}" style="width:160px;height:auto" />
  </div>
  <div class="header-center">
     <h1>COOK</h1>
     <p>Home and restaurant-quality dishes with our blends. Enter a dish, generate the recipe,
        and order ingredients and follow step-by-step with voice....</p>
  </div>
  <div></div>
</div>
""",
    unsafe_allow_html=True,
)



# ======================== Category strip (2) — FIXED ========================
cards_html = ""
for name, img, _ in CATS:
    img_b64 = b64file(Path(img)) or ""
    src = f"data:image/png;base64,{img_b64}" if img_b64 else "https://picsum.photos/84"
    # NOTE: no leading spaces at line starts below
    cards_html += (
    f'<div class="cat-card">'
    f'  <a href="?cat={urllib.parse.quote(name)}#cats" title="{name}" target="_self">'
    f'    <div class="cat-img"><img src="{src}" alt="{name}"/></div>'
    f'  </a>'
    f'  <div class="cat-label">{name}</div>'
    f'</div>'
)



st.markdown(
    f'<div id="cats" class="cat-strip">{cards_html}</div>',
    unsafe_allow_html=True,
)

# ======================== Hint / Overview Card ========================
st.markdown(
    "<div class='header-card'>Cook restaurant-quality dishes with our blends. "
    "Enter a dish, generate the recipe, and follow step-by-step with voice.</div>",
    unsafe_allow_html=True,
)

# ======================== Layout: Left (3) + Right (4) ========================
left, right = st.columns([6, 6], gap="large")

# ---------- Left Inputs (3)
with left:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("<div class='hint-chip'>💡 Try “Paneer Butter Masala”, “Veg Pulao”, “Chicken Fry”.</div>", unsafe_allow_html=True)

    st.markdown("<span class='label'>🍽️ What dish would you like to cook today?</span>", unsafe_allow_html=True)
    dish_name = st.text_input("", value=st.session_state["dish_name"], key="dish_input", placeholder="e.g., Chili Paneer")
    st.session_state["dish_name"] = dish_name

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<span class='label'>🌶️ Use OTMS Blends?</span>", unsafe_allow_html=True)
        blends_choice = st.radio("", ["✅ YES", "❌ NO"], index=0, horizontal=True)
        use_blends = blends_choice.startswith("✅")
    with c2:
        st.markdown("<span class='label'>🔊 Voice Language</span>", unsafe_allow_html=True)
        LANG2CODE = {"English":"en-US","Hindi":"hi-IN","Telugu":"te-IN","Tamil":"ta-IN","Marathi":"mr-IN","Kannada":"kn-IN"}
        lang_label = st.selectbox("", list(LANG2CODE.keys()), index=0)
        lang_code = LANG2CODE[lang_label]

    st.markdown("<hr class='sep'/>", unsafe_allow_html=True)
    col_gen, col_reset = st.columns([2, 1])
    with col_gen:
        gen_clicked = st.button("🔎  Generate Recipe", type="primary", use_container_width=True)
    with col_reset:
        reset_clicked = st.button("↩️  Reset", use_container_width=True)

    st.toggle("🖼️ Show dish image", value=False, key="show_img")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- State utilities
def sig(): return f"{dish_name.strip().lower()}|{use_blends}|{lang_label}"

if reset_clicked:
    for k in ["ingredients_text","about_text","preparation_text","steps_list","fun_fact",
              "recipe_ready","last_sig","step_idx","pending"]:
        st.session_state.pop(k, None)
    st.session_state["dish_name"] = ""
    st.session_state["category"] = None
    st.rerun()

# -------- OpenAI (optional)
try:
    import openai  # type: ignore
except ModuleNotFoundError:
    openai = None

def build_prompt():
    return f"""
Write a complete Indian recipe for "{dish_name.strip()}".

Headings (use exactly these):
Ingredients
About
Preparation
Steps
Fun Fact

Rules:
- OTMS Blends: {"ENABLED" if use_blends else "DISABLED"}.
- If DISABLED: do NOT mention OTMS or the word "blend" anywhere.
- If ENABLED: pick at most TWO blends that truly fit this dish (no laundry list).
- Ingredients: one bullet per line with quantities.
- About: 3–6 vivid sentences (no instructions or numbered lines).
- Steps: 8–12 crisp, numbered steps.
- Fun Fact: 1 playful, specific line.

OTMS reference:
RED (chili-forward), YELLOW (turmeric-coriander), GRAY (ginger-garlic powder),
GREEN (herb & curry leaf), BROWN (garam masala), WHITE (subtle base gravy).
""".strip()

@st.cache_data(show_spinner=False, ttl=3600)
def parse_sections(text: str):
    lines = text.splitlines()
    sections = {"ingredients": [], "about": [], "preparation": [], "steps": [], "fun_fact": []}
    current = None
    step_num = re.compile(r"^\s*\d+[\).\s-]+")
    def head(s: str):
        s = s.lower().strip()
        if "ingredient" in s: return "ingredients"
        if s.startswith("about") or "story" in s: return "about"
        if "preparation" in s or s == "prep": return "preparation"
        if "step" in s or "method" in s or "direction" in s: return "steps"
        if "fun fact" in s or s.startswith("tip"): return "fun_fact"
        return None
    for raw in lines:
        l = raw.strip()
        if not l: continue
        h = head(l)
        if h: current = h; continue
        if current == "about" and step_num.match(l):
            current = "steps"
        if current: sections[current].append(l)
    steps = [step_num.sub("", s).strip() for s in sections["steps"]]
    def nz(s): return re.sub(r"```(?:[a-zA-Z0-9_-]+)?\n?", "", "\n".join(s)).replace("```","").strip()
    return nz(sections["ingredients"]), nz(sections["about"]), nz(sections["preparation"]), steps, nz(sections["fun_fact"]).replace("Fun Fact","").strip(":- \n")

def trim_blends(ingredients_text: str, use_blends: bool, max_blends: int = 2) -> str:
    if not ingredients_text: return ingredients_text
    lines = [l for l in ingredients_text.splitlines() if l.strip()]
    if not use_blends:
        lines = [l for l in lines if "OTMS" not in l.upper() and "BLEND" not in l.upper()]
        return "\n".join(lines)
    kept, out = 0, []
    for l in lines:
        if "OTMS" in l.upper() or "BLEND" in l.upper():
            if kept < max_blends: out.append(l); kept += 1
        else: out.append(l)
    return "\n".join(out)

@st.cache_data(show_spinner=False)
def ingredients_to_rows(text: str):
    rows = []
    for line in text.splitlines():
        l = line.strip().lstrip("-•").strip()
        if not l: continue
        qty, item = "", l
        if " - " in l:
            left, right = [x.strip() for x in l.split(" - ", 1)]
            if re.search(r"\d|\b(tsp|tbsp|cup|cups|ml|g|kg|pinch|clove|slice|piece|pieces)\b", right, re.I):
                item, qty = left, right
            else:
                item, qty = right, left
        else:
            m = re.match(r"^([\d/.\s+-]+(?:tsp|tbsp|cup|cups|ml|g|kg|pinch|clove|slice|piece|pieces)?)\s+(.*)$", l, re.I)
            if m: qty, item = m.group(1).strip(), m.group(2).strip()
        rows.append({"Ingredient": item, "Qty": qty})
    return rows

def speak_button(text: str, lang_code: str = "en-US", key: str = "tts"):
    safe = json.dumps(text)
    st.markdown(
        f"""
        <button id="btn-{key}" class="rl-btn">🔊 Read Aloud</button>
        <script>
        (function(){{
          function say(txt, lang) {{
            if (!window.speechSynthesis) {{ alert("Speech not supported on this browser."); return; }}
            window.speechSynthesis.getVoices();
            const u = new SpeechSynthesisUtterance(txt);
            u.lang = lang; u.rate = 1.0; u.volume = 1.0;
            window.speechSynthesis.cancel(); window.speechSynthesis.speak(u);
          }}
          const btn = document.getElementById("btn-{key}");
          if (btn) {{
            window.speechSynthesis.onvoiceschanged = function(){{}};
            btn.onclick = () => say({safe}, "{lang_code}");
          }}
        }})();
        </script>
    """,
        unsafe_allow_html=True,
    )

def generate_recipe():
    try:
        import openai  # type: ignore
    except ModuleNotFoundError:
        st.error("OpenAI SDK not installed. Run: pip install openai"); st.stop()
    key = st.secrets.get("openai", {}).get("api_key")
    if not key:
        st.error("Missing OpenAI key in .streamlit/secrets.toml"); st.stop()
    openai.api_key = key
    prompt = build_prompt()
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role":"system","content":"You are a precise Indian chef who writes reliable, engaging recipes using OTMS blends only when asked."},
            {"role":"user","content":prompt},
        ],
        temperature=0.5, max_tokens=1050,
    )
    text = resp["choices"][0]["message"]["content"].strip()
    ing, about, prep, steps, fact = parse_sections(text)
    ing = trim_blends(ing, use_blends, max_blends=2)
    st.session_state.update({
        "ingredients_text": ing, "about_text": about, "preparation_text": prep,
        "steps_list": steps, "fun_fact": fact, "recipe_ready": True,
        "last_sig": sig(), "step_idx": 1,
    })

# Generate click
if 'gen_clicked' in locals() and gen_clicked:
    if not st.session_state["dish_name"].strip():
        st.error("Please enter a dish name first.")
    else:
        st.session_state["pending"] = True
        st.session_state["recipe_ready"] = False
        st.rerun()

# ======================== Right column (4) ========================
with right:
    area = st.empty()

    # If a category was chosen and we don't have a recipe pending/shown, show the dish list
    show_cat_list = bool(st.session_state.get("category")) and not st.session_state.get("pending") and not st.session_state.get("recipe_ready")

    if show_cat_list:
        with area.container():
            cat_name = st.session_state["category"]
            dishes = next((d for n, _, d in CATS if n == cat_name), [])
            st.markdown(f"### {cat_name.title()}")
            st.markdown('<div class="grid">', unsafe_allow_html=True)
            for d in dishes:
                href = f"?cat={urllib.parse.quote(cat_name)}&dish={urllib.parse.quote(d)}#cats"
                st.markdown(f'<div class="dish"><a href="{href}">{d}</a></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            st.info("Tip: click a dish to fill the input on the left, then press **Generate Recipe**.")

    elif st.session_state.get("pending"):
        with area.container():
            with st.status("Cooking up your recipe…", expanded=True):
                st.markdown(loader_html(), unsafe_allow_html=True)
                generate_recipe()
        st.session_state["pending"] = False
        st.rerun()

    elif st.session_state.get("recipe_ready"):
        with area.container():
            title = st.session_state["dish_name"].strip().title() or "Your Dish"
            st.markdown(f"## {title}")

            tabs = st.tabs(["About", "Ingredients", "Preparation", "Steps", "Fun Fact"])

            with tabs[0]:
                st.markdown(st.session_state.get("about_text") or "_No story yet — try generating again._")
                speak_button(st.session_state.get("about_text",""), lang_code=lang_code, key="about")

            with tabs[1]:
                rows = ingredients_to_rows(st.session_state.get("ingredients_text",""))
                if rows: st.dataframe(rows, use_container_width=True, hide_index=True)
                else: st.markdown(st.session_state.get("ingredients_text") or "_No ingredients found._")
                if use_blends:
                    st.caption("✅ Using OTMS blends. Tip: GRAY can replace ginger–garlic paste for speed.")
                speak_button(st.session_state.get("ingredients_text",""), lang_code=lang_code, key="ing")

            with tabs[2]:
                st.markdown(st.session_state.get("preparation_text") or "_No preparation steps found._")
                speak_button(st.session_state.get("preparation_text",""), lang_code=lang_code, key="prep")

            with tabs[3]:
                steps = st.session_state.get("steps_list", [])
                if steps:
                    n = len(steps); idx = st.session_state.get("step_idx", 1)
                    st.markdown(f"**Step {idx} of {n}**"); st.write(steps[idx - 1])
                    c_back, c_next = st.columns(2)
                    with c_back:
                        if st.button("⬅️ Back", use_container_width=True, disabled=(idx <= 1), key="back"):
                            st.session_state["step_idx"] = max(1, idx - 1); st.rerun()
                    with c_next:
                        if st.button("Next ➡️", use_container_width=True, disabled=(idx >= n), key="next"):
                            st.session_state["step_idx"] = min(n, idx + 1); st.rerun()
                    speak_button(f"Step {idx} of {n}. {steps[idx-1]}", lang_code=lang_code, key="steps")
                else:
                    st.info("No steps found.")

            with tabs[4]:
                if st.session_state.get("fun_fact"):
                    st.markdown(f"<div class='fact'>{st.session_state['fun_fact']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='fact'>No fun fact found.</div>", unsafe_allow_html=True)

            if st.session_state.get("show_img") and st.session_state["dish_name"].strip():
                st.markdown("<hr class='sep'/>", unsafe_allow_html=True)
                st.markdown(resilient_dish_img(st.session_state["dish_name"]), unsafe_allow_html=True)

            # Feedback + download + home
            st.markdown("<hr class='sep'/>", unsafe_allow_html=True)
            st.markdown("### Rate & Share Feedback")
            stars = st.slider("How was this recipe?", 1, 5, 5, 1, key="rating")
            fb = st.text_area("Share any notes (what worked, what you'd change)")

            full_text = (
                f"""{title}

Ingredients
-----------
{st.session_state.get('ingredients_text','')}

About
-----
{st.session_state.get('about_text','')}

Preparation
-----------
{st.session_state.get('preparation_text','')}

Steps
-----
"""
                + "\n".join([f"{i+1}. {s}" for i, s in enumerate(st.session_state.get("steps_list", []))])
                + (("\n\nFun Fact\n--------\n" + st.session_state.get("fun_fact","")) if st.session_state.get("fun_fact") else "")
            )

            ratings_path = BASE_DIR / "recipe_ratings.json"
            fb_path = BASE_DIR / "recipe_feedback.json"

            def robust_append_json(path: Path, payload: dict):
                path.parent.mkdir(parents=True, exist_ok=True)
                data = []
                if path.exists():
                    try:
                        loaded = json.loads(path.read_text())
                        if isinstance(loaded, list): data = loaded
                        elif isinstance(loaded, dict):
                            if "entries" in loaded and isinstance(loaded["entries"], list):
                                loaded["entries"].append(payload); path.write_text(json.dumps(loaded, indent=2)); return
                            else: data = [loaded]
                    except Exception: data = []
                data.append(payload); path.write_text(json.dumps(data, indent=2))

            def try_send_email(subject: str, body: str):
                smtp = st.secrets.get("smtp"); ifnot = "SMTP not configured"
                if not smtp: return False, ifnot
                try:
                    msg = EmailMessage(); msg["Subject"]=subject; msg["From"]=smtp["user"]; msg["To"]="onetomanyspices@gmail.com"; msg.set_content(body)
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL(smtp.get("host","smtp.gmail.com"), int(smtp.get("port",465)), context=context) as server:
                        server.login(smtp["user"], smtp["password"]); server.send_message(msg)
                    return True, None
                except Exception as e: return False, str(e)

            c_submit, c_copy, c_dl = st.columns([1,1,1])
            with c_submit:
                if st.button("✅ Submit Feedback", use_container_width=True):
                    ts = datetime.datetime.utcnow().isoformat()
                    robust_append_json(ratings_path, {"dish": title, "stars": stars, "when": ts})
                    if fb.strip(): robust_append_json(fb_path, {"dish": title, "feedback": fb.strip(), "when": ts})
                    subject = f"OTMS Recipe Feedback — {title} ({stars}/5)"
                    email_body = f"{subject}\n\n{fb.strip() or '(no notes)'}\n\n---\nFull recipe:\n\n{full_text}"
                    sent, err = try_send_email(subject, email_body)
                    if sent: st.success("Thanks! Saved locally and emailed to onetomanyspices@gmail.com ✅")
                    else:
                        mailto = ("mailto:onetomanyspices@gmail.com?"
                                  f"subject={urllib.parse.quote(subject)}&"
                                  f"body={urllib.parse.quote(email_body[:2000])}")
                        st.info("Saved locally." if err=="SMTP not configured" else "Saved locally (email failed).")
                        st.markdown(f"[📧 Send with your email app]({mailto})")

            with c_copy:
                st.markdown(
                    f"""
                    <button class="rl-btn" id="copy-recipe">📋 Copy Recipe</button>
                    <script>
                    (function(){{
                      const btn=document.getElementById("copy-recipe");
                      if(btn) btn.onclick=async()=>{{try{{await navigator.clipboard.writeText({json.dumps(full_text)});btn.innerText="✅ Copied!";setTimeout(()=>btn.innerText="📋 Copy Recipe",1400);}}catch(e){{}}}};
                    }})();
                    </script>
                    """,
                    unsafe_allow_html=True,
                )
            with c_dl:
                st.download_button("⬇️ Download .txt", data=full_text, file_name=f"{slugify(title)}.txt",
                                   mime="text/plain", use_container_width=True)

            # Bottom links: Shop + Home
            st.markdown("<hr class='sep'/>", unsafe_allow_html=True)
            st.markdown('<div class="shop-link"><a href="/shop" class="rl-btn" style="text-decoration:none;text-align:center">🛒 Visit the OTMS Shop</a></div>', unsafe_allow_html=True)
            try:
                st.page_link("pages/home.py", label="🏠 Home", icon="🏠")
            except Exception:
                st.markdown('<div class="shop-link"><a href="/" class="rl-btn" style="text-decoration:none;text-align:center">🏠 Home</a></div>', unsafe_allow_html=True)

    else:
        with area.container():
            st.info("Choose a category above to browse dishes, or enter a dish and click **Generate Recipe**.")
            st.write("Tabs will show **About, Ingredients, Preparation, Steps,** and **Fun Fact** once generated.")
