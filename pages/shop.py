import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="Shop | One to Many Spices", layout="wide")

# ---------------- CSS Styling ----------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.2s ease;
    }
    .product-card:hover {
        transform: scale(1.03);
    }
    .product-title {
        font-size: 20px;
        font-weight: bold;
        margin: 10px 0 5px 0;
    }
    .product-desc {
        font-size: 14px;
        color: #555;
        margin-bottom: 8px;
    }
    .product-price {
        font-size: 16px;
        font-weight: bold;
        color: #FF3C38;
    }
    .rating {
        color: #FFC107;
        font-size: 14px;
    }
    .buy-btn {
        background-color: #FF3C38;
        color: white;
        padding: 6px 16px;
        border: none;
        border-radius: 10px;
        font-weight: bold;
        text-decoration: none;
        margin-top: 10px;
        display: inline-block;
    }
    .buy-btn:hover {
        background-color: #cc2c2a;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Helper to Load Image ----------------
def img_to_base64(path):
    try:
        return base64.b64encode(Path(path).read_bytes()).decode()
    except:
        return ""

# ---------------- Product Catalog ----------------
catalog = {
    "OTMS Blends": [
        {"name": "RED Blend", "desc": "Fiery curries and marinades.", "price": "₹149", "rating": "⭐⭐⭐⭐", "img": "otms_assets/red_blend.png"},
        {"name": "YELLOW Blend", "desc": "Ideal for dals and vegetables.", "price": "₹139", "rating": "⭐⭐⭐⭐⭐", "img": "otms_assets/yellow_blend.png"},
        {"name": "WHITE Blend", "desc": "Creamy and neutral.", "price": "₹129", "rating": "⭐⭐⭐", "img": "otms_assets/white_blend.png"},
        {"name": "GREEN Blend", "desc": "Fresh and herby.", "price": "₹139", "rating": "⭐⭐⭐⭐", "img": "otms_assets/green_blend.png"},
        {"name": "BROWN Blend", "desc": "Deep gravies & biryanis.", "price": "₹159", "rating": "⭐⭐⭐⭐", "img": "otms_assets/brown_blend.png"},
        {"name": "GRAY Blend", "desc": "Replaces ginger garlic paste.", "price": "₹149", "rating": "⭐⭐⭐⭐⭐", "img": "otms_assets/gray_blend.png"},
    ],
    "Spice Boxes": [
        {"name": "Classic Spice Box", "desc": "All 6 OTMS Blends.", "price": "₹799", "rating": "⭐⭐⭐⭐⭐", "img": "otms_assets/classic_spice_box.png"},
        {"name": "Mini Starter Kit", "desc": "Try 3 blends combo.", "price": "₹399", "rating": "⭐⭐⭐⭐", "img": "otms_assets/mini_kit.png"},
    ],
    "Kitchenware": [
        {"name": "Cast Iron Pan", "desc": "Great for even cooking.", "price": "₹999", "rating": "⭐⭐⭐⭐⭐", "img": "otms_assets/cast_iron_pan.png"},
        {"name": "Spice Grinder", "desc": "Compact & powerful.", "price": "₹699", "rating": "⭐⭐⭐", "img": "otms_assets/spice_grinder.png"},
    ],
    "Groceries": [
        {"name": "Organic Toor Dal", "desc": "High protein lentil.", "price": "₹110", "rating": "⭐⭐⭐⭐", "img": "otms_assets/toor_dal.png"},
        {"name": "Quinoa", "desc": "Healthy grain alternative.", "price": "₹180", "rating": "⭐⭐⭐", "img": "otms_assets/quinoa.png"},
    ]
}

# ---------------- Header Section ----------------
header_cols = st.columns([1, 4, 1])
with header_cols[0]:
    st.image("otms_assets/otms_logo_light.png", use_container_width=True)
with header_cols[1]:
    st.markdown("""
        <div style='text-align:center; margin-top:20px;'>
            <h1>SHOP</h1>
            <p>Explore OTMS Products & Essentials</p>
        </div>
    """, unsafe_allow_html=True)
with header_cols[2]:
    st.image("otms_assets/cookfinity_logo_light.png", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- Product Sections ----------------
for category, items in catalog.items():
    st.markdown(f"### 🛒 {category}")
    product_rows = [items[i:i+3] for i in range(0, len(items), 3)]
    for row in product_rows:
        cols = st.columns(3)
        for col, item in zip(cols, row):
            with col:
                base64_img = img_to_base64(item["img"])
                col.markdown("<div class='product-card'>", unsafe_allow_html=True)
                if base64_img:
                    col.markdown(f"<img src='data:image/png;base64,{base64_img}' width='100%' style='border-radius:12px;'/>", unsafe_allow_html=True)
                col.markdown(f"<div class='product-title'>{item['name']}</div>", unsafe_allow_html=True)
                col.markdown(f"<div class='product-desc'>{item['desc']}</div>", unsafe_allow_html=True)
                col.markdown(f"<div class='product-price'>{item['price']}</div>", unsafe_allow_html=True)
                col.markdown(f"<div class='rating'>{item['rating']}</div>", unsafe_allow_html=True)
                col.markdown(f"<a href='#' class='buy-btn'>Buy Now</a>", unsafe_allow_html=True)
                col.markdown("</div>", unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown("<br><hr><br>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>🚀 New seasonal OTMS combos launching soon!</h4>", unsafe_allow_html=True)
