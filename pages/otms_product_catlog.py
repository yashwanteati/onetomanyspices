# Creating a dummy product catalog with multiple categories
import pandas as pd

product_catalog = pd.DataFrame([
    {"Category": "OTMS Blends", "Name": "RED Blend", "Description": "Perfect for fiery curries and marinades.", "Price": "$5.99", "Rating": "4.8"},
    {"Category": "OTMS Blends", "Name": "YELLOW Blend", "Description": "Bright, aromatic for dals and veggies.", "Price": "$5.99", "Rating": "4.7"},
    {"Category": "OTMS Blends", "Name": "WHITE Blend", "Description": "Creamy base masala without strong color.", "Price": "$5.99", "Rating": "4.6"},
    {"Category": "OTMS Blends", "Name": "GREEN Blend", "Description": "Fresh punch for greens and chutneys.", "Price": "$5.99", "Rating": "4.8"},
    {"Category": "OTMS Blends", "Name": "BROWN Blend", "Description": "Bold earthy notes for gravies, biryanis.", "Price": "$5.99", "Rating": "4.9"},
    {"Category": "OTMS Blends", "Name": "GRAY Blend", "Description": "Replaces ginger garlic paste effectively.", "Price": "$5.99", "Rating": "4.7"},

    {"Category": "Spice Boxes", "Name": "OTMS Premium 6-Pack", "Description": "Complete spice set in a gift box.", "Price": "$29.99", "Rating": "5.0"},
    {"Category": "Spice Boxes", "Name": "OTMS Sampler Pack", "Description": "Mini spice jars to try all blends.", "Price": "$14.99", "Rating": "4.6"},

    {"Category": "Kitchenware", "Name": "Cast Iron Tawa", "Description": "Perfect for rotis and dosas.", "Price": "$24.99", "Rating": "4.5"},
    {"Category": "Kitchenware", "Name": "Spice Storage Organizer", "Description": "Keeps all blends neat & fresh.", "Price": "$19.99", "Rating": "4.7"},

    {"Category": "Groceries", "Name": "Toor Dal - 1kg", "Description": "Premium quality lentils.", "Price": "$3.49", "Rating": "4.9"},
    {"Category": "Groceries", "Name": "Basmati Rice - 5kg", "Description": "Long-grain aged basmati rice.", "Price": "$11.99", "Rating": "5.0"},
])

import ace_tools as tools; tools.display_dataframe_to_user(name="OTMS Product Catalog", dataframe=product_catalog)
