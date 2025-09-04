import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="About | One to Many Spices", layout="wide")

# ---------- helpers ----------
def img_to_base64(path: str) -> str:
    try:
        return base64.b64encode(Path(path).read_bytes()).decode()
    except Exception:
        return ""

ANIM = {
    "spicepour": "otms_assets/anim_spice_pour.gif",
    "ladle": "otms_assets/anim_ladle.gif",
    "biryani": "otms_assets/anim_biryani.gif",
    "tandoor": "otms_assets/anim_tandoor.gif",
    "cart": "otms_assets/anim_cart.gif",
    "globe": "otms_assets/anim_globe.gif",
}

# ---------- CSS (White page • Dark cards • Section accents • Watermarks on) ----------
st.markdown("""
<style>
:root{
  --page:#ffffff;
  --ink:#0b0d10;
  --muted:#475569;

  --card-deep:#0f172a;
  --card-mid:#111827;
  --card-border:rgba(255,255,255,.08);

  --soft:#e5e7eb;
  --gold:#f59e0b; /* default accent */
}

/* Page */
body, .stApp { background:var(--page)!important; color:var(--ink)!important; font-family:'Helvetica Neue',sans-serif; }
[data-testid="stSidebar"]{display:none;}
.block-container{padding-top:2rem; max-width:1100px;}

/* Section headings */
.j-head{display:flex;align-items:center;justify-content:center;margin:.5rem 0 1rem;}
.j-title{
  font-size:28px;font-weight:900;color:var(--ink);letter-spacing:.3px;text-align:center;
  position:relative;display:inline-block;padding-bottom:8px;
}
.j-title:after{
  content:"";position:absolute;left:50%;bottom:0;transform:translateX(-50%);
  width:96px;height:3px;border-radius:3px;background:var(--accent, var(--gold));
}

/* Intro (white) card */
.about-card{
  background:#fff;border:1px solid var(--soft);border-radius:18px;padding:1.6rem 1.8rem;margin-bottom:1.4rem;
  box-shadow:0 10px 24px rgba(2,8,23,.06);color:var(--ink);
}
.about-card h2{margin:0 0 .5rem 0;text-align:center;color:var(--ink);}
.about-card p{color:var(--muted);}

/* Dark slider cards — richer accent (34%) */
.j-card{
  position:relative;overflow:hidden;min-height:240px;color:#f8fafc;
  background:
    radial-gradient(120% 180% at -10% -20%, color-mix(in srgb, var(--accent, var(--gold)) 34%, transparent), transparent 55%),
    linear-gradient(180deg, var(--card-deep) 0%, var(--card-mid) 100%);
  border:1px solid var(--card-border);border-radius:22px;
  box-shadow:0 26px 64px rgba(2,8,23,.30),0 1px 0 rgba(255,255,255,.04) inset;
  padding:1.6rem 1.8rem;transition:transform .16s ease,box-shadow .16s ease;
}
.j-card:hover{transform:translateY(-2px);box-shadow:0 32px 78px rgba(2,8,23,.36),0 1px 0 rgba(255,255,255,.05) inset;}

/* Grid: media | content (watermark is a separate absolute layer) */
.j-grid{ display:grid; grid-template-columns:180px 1fr; gap:1.1rem; align-items:center; }
.j-left{display:flex;align-items:center;justify-content:center;}
.j-left img{border-radius:16px;max-height:130px;border:1px solid rgba(255,255,255,.15);background:#0d1117;}

/* Reserve space for the watermark with a % so it’s responsive */
.j-right{ margin-top:6px; padding-right:var(--wm-col, 42%); }

/* Title + underline accent */
.j-ttl{
  font-size:22px;font-weight:900;margin:.1rem 0 .35rem;color:#ffffff;letter-spacing:.1px;
  position:relative;padding-bottom:5px;
}
.j-ttl:after{
  content:"";position:absolute;left:0;bottom:0;width:60px;height:3.5px;border-radius:3px;
  background:var(--accent, var(--gold));
}
.j-dsc{color:#e6eef7;line-height:1.55;}

/* Watermark layer (right side), never trimmed, auto-sizes to its own width */
.j-wm{
  position:absolute; right:12px; top:0; bottom:0; width:var(--wm-col, 42%);
  display:flex; align-items:center; justify-content:flex-end;
  pointer-events:none; user-select:none;
  /* enable container query units (cqw/cqh) for perfect fit */
  container-type:inline-size;
}
.j-year{
  /* Fallback sizing for older browsers */
  font-size:clamp(80px, 7vw, 220px);
  /* If supported, this scales exactly to the container width */
  font-size:clamp(80px, 36cqw, 220px);
  line-height:.86;
  letter-spacing:-2px;
  color:rgba(255,255,255,.08);
  white-space:nowrap;
  text-align:right;
}

/* Prev/Next buttons */
.stButton>button{
  background:#ffffff;color:var(--ink);border:1px solid var(--soft);border-radius:12px;
  padding:.45rem .9rem;font-weight:900;box-shadow:0 2px 10px rgba(2,8,23,.06);
}
.stButton>button:hover{box-shadow:0 4px 14px rgba(2,8,23,.12);}

/* Dots */
.j-dots{display:flex;gap:.45rem;justify-content:center;margin-top:12px;}
.j-dot{width:9px;height:9px;border-radius:50%;background:#e2e8f0;border:1px solid #cbd5e1;}
.j-dot.active{
  background:radial-gradient(circle at 30% 30%, #fff, var(--accent, var(--gold)) 70%);
  border:1px solid var(--accent, var(--gold));
  box-shadow:0 0 0 4px color-mix(in srgb, var(--accent, var(--gold)) 30%, transparent);
}

/* Mobile: hide watermark & remove reserved space */
@media (max-width:820px){
  .j-right{ padding-right:0; }
  .j-wm{ display:none; }
}
</style>
""", unsafe_allow_html=True)



# ---------- page header ----------
st.title("ABOUT US")

# ---------- Our Story ----------
st.markdown("""
<div class="about-card">
  <h2>Our Story</h2>
  <p>
    One to Many Spices (OTMS) was born out of a simple yet powerful idea:
    one spice box, endless possibilities. We believe cooking should be effortless,
    creative, and deeply connected to culture and memories. With our curated blends,
    anyone can create authentic Indian dishes and global fusions without the complexity
    of sourcing dozens of spices.
  </p>
</div>
""", unsafe_allow_html=True)

# ---------- Data with accents + watermarks ----------
# Accents:
ACCENT_JOURNEY = "#F59E0B"   # saffron / OTMS gold
ACCENT_WHY     = "#FF6A3D"   # paprika
ACCENT_MISSION = "#22C55E"   # emerald
ACCENT_VISION  = "#3B82F6"   # sapphire

JOURNEY = [
    {"year":"2019","title":"From kitchen trials to a bold idea",
     "desc":"Weekend cook-ups turned into a mission: one spice box that could power a full thali—without 25 jars on the counter.",
     "gif":ANIM["spicepour"], "emoji":"🧂", "accent":ACCENT_JOURNEY},
    {"year":"2023","title":"Six signature OTMS blends",
     "desc":"RED, WHITE, YELLOW, BROWN, GREEN, GRAY—refined so recipes become a formula, not guesswork.",
     "gif":ANIM["ladle"], "emoji":"🥄", "accent":ACCENT_JOURNEY},
    {"year":"2024","title":"AI-assisted recipes meet real kitchens",
     "desc":"Prototype app launches to generate detailed, stepwise recipes and swap single spices for OTMS blends.",
     "gif":ANIM["biryani"], "emoji":"🍛", "accent":ACCENT_JOURNEY},
    {"year":"2025","title":"From project to brand",
     "desc":"Company incorporation in India, packaging R&D, and the first ‘Populu Dabba’ pilots with inner-lid spice charts.",
     "gif":ANIM["tandoor"], "emoji":"🔥", "accent":ACCENT_JOURNEY},
]

WHY = [
    {"wm":"WHY OTMS","title":"One box, full thali",
     "desc":"RED • WHITE • YELLOW • BROWN • GREEN • GRAY—cover 90%+ daily cooking with predictable ratios.",
     "gif":ANIM["spicepour"], "emoji":"❓", "accent":ACCENT_WHY},
    {"wm":"COOKFINITY","title":"AI recipes that fit your kitchen",
     "desc":"Detailed steps, voice guidance, multi-language support—and blends appear on top of the ingredients list.",
     "gif":ANIM["biryani"], "emoji":"🍛", "accent":ACCENT_WHY},
    {"wm":"DESIGN","title":"Designed for speed & delight",
     "desc":"Inner-lid spice charts, refill logic, and ‘Populu Dabba’ that looks great on the counter.",
     "gif":ANIM["cart"], "emoji":"🛒", "accent":ACCENT_WHY},
]

MISSION = [
    {"wm":"MISSION","title":"Make home cooking effortless",
     "desc":"Turn complex masalas into simple formulas—measure, mix, cook. Less time guessing, more time enjoying.",
     "gif":ANIM["ladle"], "emoji":"🥄", "accent":ACCENT_MISSION},
    {"wm":"AUTHENTIC","title":"Real flavors, no shortcuts",
     "desc":"Blends crafted to honor regional tastes—from Andhra heat to North-Indian richness—without 20 spice jars.",
     "gif":ANIM["spicepour"], "emoji":"🧂", "accent":ACCENT_MISSION},
    {"wm":"EMPOWER","title":"From first-timers to pros",
     "desc":"Clear steps, visual cues, and OTMS blends make consistent, restaurant-quality food achievable for all.",
     "gif":ANIM["biryani"], "emoji":"🍛", "accent":ACCENT_MISSION},
]

VISION = [
    {"wm":"VISION","title":"Food × Tech × Culture",
     "desc":"A seamless loop of blends, recipes, and community—Where AI-guided cooking meets family traditions.",
     "gif":ANIM["globe"], "emoji":"🌍", "accent":ACCENT_VISION},
    {"wm":"COMMUNITY","title":"Learn, share, co-create",
     "desc":"Creators publish kits, families remix recipes, and the best ideas become official OTMS packs.",
     "gif":ANIM["cart"], "emoji":"🛒", "accent":ACCENT_VISION},
    {"wm":"SUSTAIN","title":"Smart packaging, less waste",
     "desc":"Refill-first boxes and durable jars—designed to be reused, not discarded.",
     "gif":ANIM["tandoor"], "emoji":"🔥", "accent":ACCENT_VISION},
]

def render_slider(title: str, items: list, state_key: str, accent: str):
    if state_key not in st.session_state:
        st.session_state[state_key] = 0
    idx = st.session_state[state_key]

    lc, hc, rc = st.columns([1, 6, 1])
    with lc:
        if st.button("←", key=f"prev_{state_key}"):
            st.session_state[state_key] = (idx - 1) % len(items)
            idx = st.session_state[state_key]
    with hc:
        st.markdown(
            f'<div class="j-head"><div class="j-title" style="--accent:{accent}">{title}</div></div>',
            unsafe_allow_html=True
        )
    with rc:
        if st.button("→", key=f"next_{state_key}"):
            st.session_state[state_key] = (idx + 1) % len(items)
            idx = st.session_state[state_key]

    m = items[idx]
    gif_path = m.get("gif", "")
    gif_b64 = base64.b64encode(Path(gif_path).read_bytes()).decode() if gif_path and Path(gif_path).exists() else ""
    img_html = (f'<img src="data:image/gif;base64,{gif_b64}" alt="anim" />' if gif_b64
                else f'<div style="font-size:84px;line-height:1;text-align:center;">{m.get("emoji","✨")}</div>')

    wm = m.get("year") or m.get("wm", "")
    # Reserve exact column width based on watermark length
    n = len(wm)
    wm_space = 300 if n <= 4 else 360 if n <= 8 else 420   # px for third grid column
    wm_size  = 160 if n <= 4 else 150 if n <= 8 else 140   # px font size
    wm_html = f'<div class="j-wm"><div class="j-year">{wm}</div></div>' if wm else ""

    card_html = f"""
    <div class="j-card" style="--accent:{m.get('accent', accent)};">
      <div class="j-grid" style="--wm-space:{wm_space}px; --wm-size:{wm_size}px;">
        <div class="j-left">{img_html}</div>
        <div class="j-right">
          <div class="j-ttl">{m['title']}</div>
          <div class="j-dsc">{m['desc']}</div>
        </div>
        {wm_html}
      </div>
    </div>
    <div class="j-dots" style="--accent:{m.get('accent', accent)}">
      {''.join([f'<div class="j-dot {"active" if i==idx else ""}"></div>' for i in range(len(items))])}
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)



# ---------- Render sections ----------
render_slider("The OTMS Journey", JOURNEY, "journey_idx", ACCENT_JOURNEY)
render_slider("Why OTMS?", WHY, "why_idx", ACCENT_WHY)
render_slider("Our Mission", MISSION, "mission_idx", ACCENT_MISSION)
render_slider("Our Vision", VISION, "vision_idx", ACCENT_VISION)

# --- Back & Home ---
st.markdown("""
<div class="button-group">
    <a href="/shop" target="_self"><button class="back-btn">⬅️ Back to LEARN</button></a>
    <a href="/" target="_self"><button class="home-btn">🏡 Home</button></a>
</div>
""", unsafe_allow_html=True)
