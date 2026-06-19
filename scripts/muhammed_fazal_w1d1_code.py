import streamlit as st

st.title("👨‍💻 Muhammed Fazal")

st.header("About Me", divider="blue")

st.write("""
Hi! I am Muhammed Fazal.
         
I am a BCA Student who is learning Python, Data Analysis and Streamlit.
         
I enjoy building websites and dashboards.
""")

st.header("Skills", divider="green")

st.markdown("""
- **Python**
- **html**
- Web Development
- Data Analysis
""")


st.subheader(
    "Favourite Python Code",
    help="Simple Python Program"
)

st.code("""
name = "Fazal"
print("Welcome", name)
""",
language="python")

st.header("Contact", divider="orange")

st.markdown("""
📧 Email: fazal@example.com

📱 Phone: +91 255-1234567
""")

st.markdown("---")

st.caption(
    "Built with Streamlit • Day 1 Project • Muhammed Fazal"
)
