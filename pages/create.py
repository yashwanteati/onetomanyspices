import streamlit as st

st.set_page_config(page_title="Create | One to Many Spices", layout="wide")

# ---------------- Hide Sidebar ----------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .activity-card {
        background-color: white;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.2s ease;
    }
    .activity-card:hover {
        transform: scale(1.03);
    }
    .activity-title {
        font-size: 22px;
        font-weight: bold;
        margin: 12px 0 8px 0;
    }
    .activity-desc {
        font-size: 14px;
        color: #666;
        margin-bottom: 10px;
    }
    .activity-btn {
        background-color: #FF3C38;
        color: white;
        padding: 8px 18px;
        border: none;
        border-radius: 10px;
        font-weight: bold;
        text-decoration: none;
    }
    .activity-btn:hover {
        background-color: #cc2c2a;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
header_cols = st.columns([1, 4, 1])
with header_cols[0]:
    st.image("otms_assets/otms_logo_light.png", use_container_width=True)
with header_cols[1]:
    st.markdown("""
        <div style='text-align: center; margin-top: 20px;'>
            <h1 style='font-size: 48px;'>CREATE</h1>
            <p style='font-size: 18px; color: #555;'>Experiment, innovate, and share your unique dishes with OTMS blends.</p>
        </div>
    """, unsafe_allow_html=True)
with header_cols[2]:
    st.image("otms_assets/cookfinity_logo_light.png", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- Activities ----------------
activity_cols = st.columns(3)

with activity_cols[0]:
    st.markdown("""
        <div class="activity-card">
            <div class="activity-title">🧪 Try Custom Recipes</div>
            <div class="activity-desc">
                Pick OTMS blends and let our AI suggest creative recipes for you!
            </div>
            <a href="#" class="activity-btn">Try It</a>
        </div>
    """, unsafe_allow_html=True)

with activity_cols[1]:
    st.markdown("""
        <div class="activity-card">
            <div class="activity-title">📷 Showcase Your Creation</div>
            <div class="activity-desc">
                Upload your innovative dish using OTMS blends. We’ll spotlight the best!
            </div>
            <a href="#" class="activity-btn">Upload</a>
        </div>
    """, unsafe_allow_html=True)

with activity_cols[2]:
    st.markdown("""
        <div class="activity-card">
            <div class="activity-title">🎨 Design Your Own Blend</div>
            <div class="activity-desc">
                Got a creative blend idea? Submit your version and get feedback!
            </div>
            <a href="#" class="activity-btn">Submit Idea</a>
        </div>
    """, unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown("<br><hr><br>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>✨ Your creations power the OTMS movement. Keep innovating!</h4>", unsafe_allow_html=True)
