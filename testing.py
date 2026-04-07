import streamlit as st
import calendar
from datetime import datetime

st.markdown(
    """
    <head>
        <meta name="google-site-verification" content="<meta name="google-site-verification" content="w86RdQgR9US_r7V4OengDvxUfTtiJ3MMYt6_fcJZWdM" />" />
    </head>
    """, 
    unsafe_allow_html=True
)

# Page configuration
st.set_page_config(page_title="Pro Calendar", page_icon="📅", layout="centered")

# Custom CSS for Gradient Background and Glassmorphism
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #2d2d44 100%);
        color: white;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff4b2b, #ff416c);
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 30px;
        font-weight: bold;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(255, 75, 43, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(255, 75, 43, 0.6);
    }
    .calendar-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        font-family: 'Courier New', Courier, monospace;
        color: #00ffcc;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown("<h1 style='text-align: center; color: #00ffcc;'>✨ Interactive Calendar</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Created by Dheeraj Prajapat</p>", unsafe_allow_html=True)

# Layout: Sidebar or Columns for Inputs

yy = st.number_input("Year", min_value=1900, max_value=2100, value=2026)
    
    
# Month selection with names instead of numbers
month_names = list(calendar.month_name)
mm_name = st.selectbox("Month", month_names, index=3) # Default April
mm = month_names.index(mm_name) + 1

# Generate Button
if st.button("Generate Calendar 🚀"):
    cal_data = calendar.month(yy, mm)
    
    st.markdown("---")
    st.markdown(f"<h3 style='text-align: center;'>📅 {mm_name} {yy}</h3>", unsafe_allow_html=True)
    
    # Styled Calendar Output
    st.code(cal_data, language='text')
    
    st.balloons() # Visual effect for fun!

else:
    st.info("Select Year and Month, then click 'Generate'")
