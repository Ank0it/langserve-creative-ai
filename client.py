import requests
import streamlit as st

def get_essay_response(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={'input': {'topic': input_text}}
    )
    return response.json()['output']['content']

def get_poem_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={'input': {'topic': input_text}}
    )
    return response.json()['output']['content']

st.title("Langchain Gemini API Demo")

# Essay Section
st.subheader("📝 Essay Generator")
essay_topic = st.text_input("Enter a topic for the essay:", key="essay")

if essay_topic:
    with st.spinner("Generating essay..."):
        try:
            essay = get_essay_response(essay_topic)
            st.write("**Essay:**")
            st.write(essay)
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Poem Section
st.subheader("🎨 Poem Generator")
poem_topic = st.text_input("Enter a topic for the poem:", key="poem")

if poem_topic:
    with st.spinner("Generating poem..."):
        try:
            poem = get_poem_response(poem_topic)
            st.write("**Poem:**")
            st.write(poem)
        except Exception as e:
            st.error(f"Error: {str(e)}")
