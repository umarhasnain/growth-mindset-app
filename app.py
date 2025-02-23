import streamlit as st

# Title of the app
st.title("Growth Mindset Challenge")

# Introduction
st.write("""
A **growth mindset** is the belief that abilities can be developed through effort, learning, and persistence.
Embrace challenges, learn from mistakes, and keep improving!
""")

# User Interaction
name = st.text_input("Enter your name:", "")
if name:
    st.write(f"Welcome, {name}! Let's develop a growth mindset together.")

# Challenge for the User
challenge = st.selectbox(
    "Choose a mindset challenge for today:",
    ["Practice Gratitude", "Learn from a Mistake", "Stay Persistent", "Seek Feedback"]
)

st.write(f"Your challenge today: **{challenge}**. Keep going!")

# Inspirational Quote
st.success("💡 *Your abilities grow as you learn. Keep pushing forward!*")
