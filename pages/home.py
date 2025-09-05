# pages/home.py — OTMS Home (pure-link navigation with robust router)
from pathlib import Path
import base64, urllib.parse
import streamlit as st

st.set_page_config(page_title="OTMS | Home", layout="wide")

ACCENT = "#FF3C38"; BORDER = "#e5e7eb"; INK = "#0f172a"

# ---------- helpers ----------
def b64file(p: Path) -> str:
    try:
        return base64.b64encode(p.read_bytes()).decode()
    except Exception:
        return ""

def img_src(local_path: str, fallback_kw: str = "indian food") -> str:
    p = Path(local_path)
    b = b64file(p)
    if b:
        ext = (p.suffix or ".png").lstrip(".")
        return f"data:image/{ext};base64,{b}"
    return f"https://source.unsplash.com/900x600/?{urllib.parse.quote(fallback_kw)}"

def _get_params():
    # Streamlit >=1.30 has st.query_params; fallback to experimental for older
    try:
        qp = dict(st.query_params)  # returns dict[str, str]
        # normalize to lists for consistent access
        return {k: [v] if isinstance(v, str) else v for k, v in qp.items()}
    except Exception:
        return st.experimental_get_query_params()

def _first(params, key, default=""):
    v = params.get(key)
    if not v:
        return default
    return v[0] if isinstance(v, list) else v

def _to_bool(val):
    if isinstance(val, bool): return val
    s = str(val).strip().lower()
    return s in {"1","true","yes","y","on"}

def _set_cook_state_from_params(params):
    dish = _first(params, "dish", "").strip()
    cat  = _first(params, "cat", "").strip()
    auto = _to_bool(_first(params, "auto", "0"))
    st.session_state["cook_dish"] = dish
    st.session_state["cook_cat"]  = cat
    st.session_state["cook_auto"] = auto
    st.session_state["cook_from_home"] = True

def _switch_any(candidates):
    # Try multiple plausible paths (case/placement differences across projects)
    for target in candidates:
        try:
            st.switch_page(target)
            return
        except Exception:
            continue
    # If nothing matched, show a concise hint and stop
    st.error("Navigation target not found. Make sure the destination file exists:\n"
             + " /pages/" + " or /" + " • ".join(candidates))
    st.stop()

# Map short names from ?page=... to likely file paths
PAGE_TARGETS = {
    "cook":   ["pages/cook.py", "cook.py", "Cook.py", "pages/Cook.py"],
    "learn":  ["pages/learn.py", "learn.py", "Learn.py", "pages/LEARN.py"],
    "engage": ["pages/engage.py","engage.py","Engage.py","pages/Engage.py"],
    "shop":   ["pages/shop.py", "shop.py", "Shop.py", "pages/Shop.py"],
    "signin": ["pages/signin.py","signin.py","SignIn.py","pages/SignIn.py"],
    "collab": ["pages/collab.py","collab.py","Collab.py","pages/Collab.py"],
    "home":   ["pages/home.py","home.py","Home.py","pages/Home.py"],
}

# ---------- ROUTER: handle query params and jump BEFORE rendering UI ----------
_params = _get_params()
_requested = _first(_params, "page", "").strip().lower()

if _requested and _requested != "home":
    if _requested == "cook":
        _set_cook_state_from_params(_params)
    _switch_any(PAGE_TARGETS.get(_requested, []))

# ---------- CSS ----------
st.markdown(
    f"""
<style>
:root {{ --accent:{ACCENT}; --ink:{INK}; --border:{BORDER}; }}
[data-testid="stSidebar"]{{display:none!important}}
.block-container{{max-width:1200px;padding-top:.6rem}}
body,.stApp,.main{{background:#fff;color:var(--ink)}}

/* header */
.header{{display:grid;grid-template-columns:170px 1fr 230px;align-items:center;gap:16px;margin:.2rem 0 .4rem}}
.header h1{{font-size:28px;margin:.2rem 0 .2rem;letter-spacing:.02em;font-weight:900}}
.header p{{opacity:.92;margin:.1rem 0;font-size:14px}}
.top-right{{display:flex;justify-content:flex-end;gap:8px}}
.btn{{background:var(--accent);color:#fff;border:none;border-radius:12px;padding:8px 14px;
     font-weight:800;box-shadow:0 8px 18px rgba(255,60,56,.15);cursor:pointer;text-decoration:none;display:inline-block}}
.btn.secondary{{background:#004aad}}

/* search + spice chart */
.search-row{{display:grid;grid-template-columns:1fr 220px;gap:20px;margin:.2rem 0 1rem;align-items:center}}
.searchbox{{position:relative}}
.searchbox input{{width:100%;height:46px;border:1px solid var(--border);border-radius:100px;padding:0 52px 0 20px;font-size:16px;font-weight:600;outline:none}}
.searchbox button.search{{position:absolute;right:6px;top:6px;height:34px;border-radius:100px;background:#0ea5e9;border:0;color:#fff;font-weight:800;padding:0 14px;cursor:pointer}}
.searchbox form{{margin:0}} /* remove default gap */

/* spice pill (rotating icon + label under) */
.spice-pill{{display:flex;flex-direction:column;align-items:center;gap:6px}}
.spice-circle{{width:54px;height:54px;border:1px solid var(--border);border-radius:999px;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 16px rgba(2,8,23,.08);background:#fff}}
.spice-circle img{{width:42px;height:42px;border-radius:50%;animation:spin 16s linear infinite}}
.spice-label a{{display:inline-block;padding:9px 14px;border:1px solid var(--border);border-radius:999px;font-weight:900;text-decoration:none;color:var(--ink);box-shadow:0 6px 16px rgba(2,8,23,.06)}}
.spice-label a:hover{{background:#f8fafc}}
@keyframes spin{{from{{transform:rotate(0)}}to{{transform:rotate(360deg)}}}}

/* modal (pure :target for spice chart) */
#spicechart{{display:none}}
.modal{{position:fixed;inset:0;background:rgba(15,23,42,.55);display:none;align-items:center;justify-content:center;z-index:9999}}
.modal .box{{position:relative;background:#fff;border:1px solid var(--border);border-radius:16px;padding:14px;max-width:920px;width:92%;box-shadow:0 20px 40px rgba(2,8,23,.2)}}
.modal .box img{{width:100%;height:auto;border-radius:12px;border:1px solid var(--border)}}
.modal .close{{position:absolute;top:10px;right:12px;background:#fff;border:1px solid var(--border);border-radius:8px;font-weight:900;padding:6px 10px;text-decoration:none;color:#111}}
#spicechart:target.modal{{display:flex}}

/* categories marquee */
.marquee-wrap{{overflow:hidden;border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:10px 0;margin:.2rem 0 1rem}}
.track{{display:flex;gap:26px;align-items:center;animation:slide 28s linear infinite;will-change:transform}}
.cat{{display:flex;flex-direction:column;align-items:center;gap:6px;min-width:92px}}
.cat a{{text-decoration:none;color:inherit}}
.cat .pic{{width:72px;height:72px;border-radius:50%;border:1px solid var(--border);box-shadow:0 6px 16px rgba(2,8,23,.08);overflow:hidden;background:#fff;display:flex;align-items:center;justify-content:center}}
.cat .pic img{{width:100%;height:100%;object-fit:contain;animation:spin 18s linear infinite}}
.cat .lab{{font-weight:900;font-size:11px;letter-spacing:.04em;text-align:center}}
@keyframes slide{{from{{transform:translateX(0)}}to{{transform:translateX(-50%)}}}}

/* row 2 */
.row-2{{display:grid;grid-template-columns:1.2fr .8fr;gap:20px;margin:2px 0 14px}}
.banner{{position:relative;height:260px;border-radius:18px;border:1px solid var(--border);overflow:hidden;box-shadow:0 16px 34px rgba(2,8,23,.1)}}
.banner img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;animation:fade 8s infinite}}
.banner img:nth-child(1){{animation-delay:0s}}
.banner img:nth-child(2){{animation-delay:2s}}
.banner img:nth-child(3){{animation-delay:4s}}
.banner img:nth-child(4){{animation-delay:6s}}
@keyframes fade{{0%{{opacity:0}} 8%{{opacity:1}} 42%{{opacity:1}} 50%{{opacity:0}} 100%{{opacity:0}}}}
.blend{{background:#fff;border:1px solid var(--border);border-radius:18px;padding:14px;box-shadow:0 10px 20px rgba(2,8,23,.08)}}
.blend a{{display:block}} /* whole card clickable */

/* row 3 */
.row-3{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:6px 0 12px}}
.ld-grid{{display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:auto;gap:14px}}
.ld-grid a{{display:block;border-radius:16px;box-shadow:0 10px 24px rgba(2,8,23,.10);overflow:hidden;border:1px solid var(--border);background:#fff}}
.ld-grid img{{width:100%;height:auto;display:block}}
.ld-grid .shop{{grid-column:1 / span 2}}
.week img{{width:100%;height:auto;border-radius:14px;border:1px solid var(--border)}}
.week .btn-line{{margin-top:10px}}

/* mobile */
@media (max-width: 840px){{
  .header{{grid-template-columns:120px 1fr 0}}
  .search-row{{grid-template-columns:1fr}}
  .row-2{{grid-template-columns:1fr}}
  .row-3{{grid-template-columns:1fr}}
  .ld-grid{{grid-template-columns:1fr}}
  .ld-grid .shop{{grid-column:auto}}
}}
</style>
""",
    unsafe_allow_html=True,
)

# ---------- header ----------
logo = img_src("otms_assets/otms_logo_light.png", "spices logo")
st.markdown(
    (
        '<div class="header">'
        f'  <div><img src="{logo}" style="width:150px;height:auto"/></div>'
        '  <div>'
        '     <h1>Cook your favorite recipes 🫰🫰</h1>'
        '     <p>Home and restaurant-quality dishes with our OTMS blends. Enter a dish, '
        '        generate the recipe, and follow step-by-step process……</p>'
        '  </div>'
        '  <div class="top-right">'
        '     <a class="btn" href="?page=signin">Sign In / Create Account</a>'
        '     <a class="btn secondary" href="?page=collab">COLLAB with OTMS</a>'
        '  </div>'
        '</div>'
    ),
    unsafe_allow_html=True,
)

# ---------- search + spice chart (GET form, no JS) ----------
left, right = st.columns([1, 0.38])
with left:
    spice_icon = img_src("otms_assets/icon_spice.png", "spices")
    st.markdown(
        f"""
<div class="search-row">
  <div class="searchbox">
    <form method="get">
      <input type="hidden" name="page" value="cook"/>
      <input type="hidden" name="auto" value="1"/>
      <input name="dish" placeholder="Eg: Palak Paneer"/>
      <button class="search" type="submit">Search</button>
    </form>
  </div>
  <div class="spice-pill">
    <div class="spice-circle"><img src="{spice_icon}" alt="spice"/></div>
    <div class="spice-label"><a href="#spicechart">OTMS SPICE CHART</a></div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

with right:
    chart = img_src("otms_assets/otms_spice_chart.png", "spice chart")
    st.markdown(
        (
            '<div id="spicechart" class="modal">'
            '  <div class="box">'
            '     <a href="#" class="close">✕</a>'
            f'     <img src="{chart}" alt="OTMS Spice Chart"/>'
            '  </div>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

# ---------- categories marquee (pure <a> links) ----------
CATS = [
    ("THALI","otms_assets/cat_thali.png"),
    ("BIRYANI","otms_assets/cat_biryani.png"),
    ("TIFFINS","otms_assets/cat_tiffins.png"),
    ("SEA FOOD","otms_assets/cat_seafood.png"),
    ("VEG","otms_assets/cat_veg.png"),
    ("TANDOOR","otms_assets/cat_tandoor.png"),
    ("RICE","otms_assets/cat_rice.png"),
    ("NON VEG","otms_assets/cat_nonveg.png"),
    ("EGG","otms_assets/cat_egg.png"),
    ("INDO CHINESE","otms_assets/cat_indochinese.png"),
    ("SNACKS","otms_assets/cat_snacks.png"),
]
items = CATS + CATS
html_parts = ['<div class="marquee-wrap"><div class="track">']
for name, icon in items:
    icon_url = img_src(icon, name)
    href = f'?page=cook&cat={urllib.parse.quote(name)}&auto=1#cats'
    html_parts.append(
        f'<div class="cat">'
        f'  <a href="{href}" target="_self">'
        f'    <div class="pic"><img src="{icon_url}" alt="{name}"/></div>'
        f'    <div class="lab">{name}</div>'
        f'  </a>'
        f'</div>'
    )
html_parts.append('</div></div>')
st.markdown("".join(html_parts), unsafe_allow_html=True)

# ---------- row 2: banner rotator + blend of month ----------
banners = [img_src(f"otms_assets/home_banner_{i}.png", "spice blend") for i in range(1,5)]
l2, r2 = st.columns([1.2, .8], gap="large")
with l2:
    if banners:
        imgs = "".join([f'<img src="{b}"/>' for b in banners])
        st.markdown(f'<div class="banner">{imgs}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="banner" style="display:flex;align-items:center;justify-content:center;color:#64748b">No banner images</div>', unsafe_allow_html=True)

with r2:
    jar = img_src("otms_assets/blend_of_the_month.png", "spice jar")
    st.markdown(
        (
            f'<div class="blend"><a href="?page=shop" target="_self">'
            f'  <img src="{jar}" alt="Blend of the Month" '
            '       style="width:100%;max-height:160px;object-fit:contain;'
            '              border:1px dashed #fde68a;border-radius:12px;background:#fffbeb" />'
            '  <div style="font-size:12px;color:#64748b;margin-top:6px">'
            '     Tap to shop this blend and see recipes.'
            '  </div>'
            '</a></div>'
        ),
        unsafe_allow_html=True,
    )

# ---------- row 3: Learn / Dine / Shop cards + recipe of the week ----------
l3, r3 = st.columns([1,1], gap="large")

with l3:
    learn_img = img_src("otms_assets/learn_card.png","learn OTMS")
    dine_img  = img_src("otms_assets/dine_card.png","engage")  # ensure file exists
    shop_img  = img_src("otms_assets/shop_card.png","shop")
    st.markdown(
        (
            '<div class="ld-grid">'
            f'  <a href="?page=learn"  target="_self"><img src="{learn_img}" alt="LEARN"/></a>'
            f'  <a href="?page=engage" target="_self"><img src="{dine_img}"  alt="ENGAGE"/></a>'
            f'  <a class="shop" href="?page=shop" target="_self"><img src="{shop_img}" alt="SHOP"/></a>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

with r3:
    hero = img_src("otms_assets/recipe_of_week.png","mutton curry")
    week_dish = "Mutton Curry"
    dish_q = urllib.parse.quote(week_dish)
    st.markdown(f'<div class="week"><img src="{hero}" alt="Recipe of the Week"/></div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="btn-line">'
        f'  <a class="btn" style="display:block;text-align:center;border-radius:10px" '
        f'     href="?page=cook&dish={dish_q}&auto=1" target="_self">Cook {week_dish} ➜</a>'
        f'</div>',
        unsafe_allow_html=True,
    )
