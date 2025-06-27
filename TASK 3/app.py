import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Get in touch!!",
                   page_icon=":winking_face:",
                   layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("D:\CS TASKS\TASK 3\style.css")

# Animation
lottie_coding = load_lottieurl("https://lottie.host/05c0c55f-3c9e-4abd-971a-8e0b3a176d58/mQ2zlnFaj8.json")


# using CSS
st.markdown("""
    <style>
    h1 {font-size: 36px;}
    h2 {font-size: 30px;}
    h3 {font-size: 24px;}
    .block-container {padding-top: 2rem;}
    </style>
""", unsafe_allow_html=True)

# ---- HEADER SECTION ----
with st.container():
    col_text, col_pic = st.columns([4, 1])

    # ---------- LEFT side ----------
    with col_text:
        st.markdown("<h2>Hi, I am Ashvin 👋</h2>", unsafe_allow_html=True)
        st.markdown("<h1>Let's chit-chat through Mail!! 😎</h1>", unsafe_allow_html=True)
        st.markdown("<h3>A Growing JEE Aspirant  &  Tech Enthusiast</h3>", unsafe_allow_html=True)

        st.markdown("""
            <p style='font-size:18px;'>
            I am passionate about the growing technology in the vast world,
            which I hope will soon enter through a new horizon.
            </p>
        """, unsafe_allow_html=True)

# ---------- RIGHT side (animation) ----------
    with col_pic:
        st_lottie(lottie_coding, height=320)

# -------------------------- SECOND CONTAINER ---------------------------------------
with st.container():
    st.write("---")
    col_left, col_right = st.columns([3,2])
    
    # ---------- LEFT side ----------
    with col_left:
        st.markdown("<h2>👤 About Me</h2>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size:18px;'>
           Hello! I’m Ashvin S.M, a Grade 11 student at AVP CBSE School, Gandhinagar, with a strong interest in the field of computer science and technology. 
           My journey began with a simple “Hello World” program, and since then, I’ve been captivated by how code can be transformed into real-world solutions that make a meaningful impact.
            </p>
        """, unsafe_allow_html=True)

        st.markdown("""
            <p style='font-size:18px;'>
            I am particularly passionate about app and web development, with an eye for intuitive design and clean, functional user experiences. 
           My skills include HTML, CSS, JavaScript, Python, and C, and I continue to deepen my understanding through practical experimentation and self-driven learning.
            </p>
        """, unsafe_allow_html=True)

        st.markdown("""
            <p style='font-size:18px;'>
            As I begin exploring the world of artificial intelligence, I remain committed to building a strong foundation in both programming and problem-solving. 
           My long-term goal is to become a software engineer, contributing to thoughtful, human-centered technology that serves real-world needs.
            </p>
        """, unsafe_allow_html=True)

# -------------- RIGHT side -----------------
    with col_right:
        st.image("D:\CS TASKS\TASK 3\IMG-1.png", width=500)


# -------------------------- THRID CONTAINER (contanct) ---------------------------------------

with st.container():
    st.write("---")
    st.markdown("<h2>Wanna get in touch with me!!</h2>", unsafe_allow_html=True)
    st.markdown("<h2>Then Goahead and leave a message down bellow!! 🤝 ✌ 👇</h2>", unsafe_allow_html=True)
    st.write("###")
    contact_form = """
<form action="https://formspree.io/f/xrbkowkj" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="YOUR NAME" required>
    <input type="email" name="email" placeholder="YOUR EMAIL" required>
    <textarea name="message" placeholder="YOUR MESSAGE" required></textarea>
    <button type="submit">Send</button>
</form>
"""

left_col, right_col = st.columns(2)
with left_col:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_col:
    st.empty()