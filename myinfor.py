import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Welcome to My Portfolio", layout="wide")

# --- Custom CSS for Background Image & Bottom-Aligned Text ---
page_bg_img = """
<style>
/* Full-page Background Image */
.stApp {
    background-image: url("https://cdn.pixilart.com/photos/large/a93749a9418029b.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Container to hold the text at the bottom */
.bottom-text-container {
    position: fixed;
    bottom: 20px; /* Adjust this value to move text higher or lower */
    left: 50%;
    transform: translateX(-50%);
    background: rgba(0, 0, 0, 0.6); /* Dark semi-transparent background */
    padding: 10px 20px;
    border-radius: 10px;
    text-align: center;
    width: 80%;
}

/* Styling for Text */
.bottom-text {
    color: white;
    font-size: 22px;
    font-weight: bold;
    text-shadow: 3px 3px 5px rgba(0,0,0,0.7);
}
</style>
"""

# Apply the CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Bottom-Aligned Text ---
st.markdown(
    """
    <div class="bottom-text-container">
        <p class="bottom-text">🚀 Explore my projects, skills, and experience in Data Science & Analytics.</p>
        <p class="bottom-text">🔍 Stay curious, keep learning, and build amazing things!</p>
    </div>
    """,
    unsafe_allow_html=True
)
