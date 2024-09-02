import io
import streamlit as st
from captcha.image import ImageCaptcha
from PIL import Image
import string
import random
import time

st.logo(
    "media/icons8-robot-96.png",
    link="https://capxax.streamlit.app/",
    icon_image="media/icons8-robot-48.png",
)

import streamlit as st

st.set_page_config(
    page_title="Capxax",
    page_icon="media/icons8-robot-48.png",
)

# Define the characters to generate captcha text
alphabets = string.ascii_letters + string.digits

# Function to generate random captcha text
def generate_random_text(length=4):
    return ''.join(random.choice(alphabets) for _ in range(length))

# Function to generate a captcha image from the text
def generate_captcha_image(captcha_text):
    image = ImageCaptcha(width=150, height=90)
    buf = io.BytesIO()
    image.write(captcha_text, buf, format='jpeg')
    buf.seek(0)
    im = Image.open(buf)
    return im

# Initialize session state for captcha text and image
if 'captcha_text' not in st.session_state:
    st.session_state['captcha_text'] = generate_random_text()

if 'captcha_image' not in st.session_state:
    # Add a progress bar for captcha generation
    progress_bar = st.progress(0)
    st.write("Generating captcha image...")
    # Simulate progress
    for i in range(100):
        time.sleep(0.01)  # Simulate some processing time
        progress_bar.progress(i + 1)
    st.session_state['captcha_image'] = generate_captcha_image(st.session_state['captcha_text'])
    progress_bar.empty()  # Remove progress bar after completion

# Display title with emoji
st.title("**CAPXAX 🤖**", help='Generate captcha image')

# Display captcha image
captcha_image_placeholder = st.image(st.session_state['captcha_image'], use_column_width=True)

# Input for captcha text
captcha_input = st.text_input("Enter the characters you see:")

# Button to submit captcha input
if st.button("**Submit**"):
    if captcha_input.strip().lower() == st.session_state['captcha_text'].lower():
        st.success("Captcha Verified!")
        new_captcha_text = generate_random_text()
        # Add a progress bar for captcha generation
        progress_bar = st.progress(0)
        st.write("Generating new captcha image...")
        # Simulate progress
        for i in range(100):
            time.sleep(0.01)  # Simulate some processing time
            progress_bar.progress(i + 1)
        new_captcha_image = generate_captcha_image(new_captcha_text)
        st.session_state['captcha_text'] = new_captcha_text
        st.session_state['captcha_image'] = new_captcha_image
        captcha_image_placeholder.image(st.session_state['captcha_image'], use_column_width=True)
        progress_bar.empty()  # Remove progress bar after completion
    else:
        st.warning("Incorrect Characters! Please try again.")

footer_html = """<div style='text-align: center;'>
  <p>Developed with ❤️ by Sayam</p>
</div>"""
st.markdown(footer_html, unsafe_allow_html=True)
