import requests
import streamlit as st
import os

# Use deployed API URL
API_URL = os.getenv("API_URL", "https://langserve-creative-ai.onrender.com")

def get_essay_response(input_text):
    try:
        response = requests.post(
            f"{API_URL}/essay/invoke",
            json={'input': {'topic': input_text}},
            timeout=30
        )
        response.raise_for_status()
        return response.json()['output']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def get_poem_response(input_text):
    try:
        response = requests.post(
            f"{API_URL}/poem/invoke",
            json={'input': {'topic': input_text}},
            timeout=30
        )
        response.raise_for_status()
        return response.json()['output']['content']
    except Exception as e:
        return f"Error: {str(e)}"

st.set_page_config(page_title="LangServe Creative AI", page_icon="✨")

st.title("✨ LangServe Creative AI")
st.markdown("*Transform Ideas into Essays & Poems with AI Magic* 🎭")

# Essay Section
st.subheader("📝 Essay Generator")
essay_topic = st.text_input("Enter a topic for the essay:", key="essay", placeholder="e.g., Artificial Intelligence")

if essay_topic:
    with st.spinner("🤖 Generating essay..."):
        essay = get_essay_response(essay_topic)
        st.markdown("### Your Essay:")
        st.write(essay)
        st.divider()

# Poem Section
st.subheader("🎨 Poem Generator")
poem_topic = st.text_input("Enter a topic for the poem:", key="poem", placeholder="e.g., Nature")

if poem_topic:
    with st.spinner("✍️ Crafting poem..."):
        poem = get_poem_response(poem_topic)
        st.markdown("### Your Poem:")
        st.write(poem)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center'>
    <p>Powered by <b>Google Gemini 2.5</b> • <b>LangChain</b> • <b>FastAPI</b></p>
    <p><a href='https://langserve-creative-ai.onrender.com/docs' target='_blank'>📚 API Documentation</a></p>
</div>
""", unsafe_allow_html=True)
