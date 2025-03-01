import streamlit as st
import subprocess

# Install required package
subprocess.run(["pip", "install", "-q", "-U", "google-genai"], check=True)

from google import genai

# Streamlit UI
st.title("AI-Powered Career Path Generator")

# User Input
name = st.text_input("Enter your name:")
years_experience = st.number_input("Enter your years of experience:", min_value=0, step=1)

# Generate Career Path
if st.button("Generate Career Path"):
    if name and years_experience >= 0:
        client = genai.Client(api_key="your-api-key")
        prompt = (f"As an expert career guide counselor, make a detailed career path for me. My name is {name}, "
                  f"I am interested in MERN stack development, and I have {years_experience} years of experience.")
        response = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
        
        st.subheader("Career Path Recommendation:")
        st.write(response.text)
    else:
        st.warning("Please enter a valid name and years of experience.")
