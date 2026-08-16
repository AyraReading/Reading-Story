import streamlit as st
from google import genai

st.set_page_config(page_title="Little Reader AI", page_icon="📖")
st.title("📖 Little Reader AI")

api_key = st.text_input("Enter your Gemini API Key", type="password")

if api_key:
    try:
        client = genai.Client(api_key=api_key)
        
        if st.button("Generate New Story"):
            with st.spinner("Generating story..."):
                response = client.models.generate_content(
                    model='gemini-1.5-flash-8b',
                    contents='Write a short, simple, 5-sentence story for a child learning to read.'
                )
                st.session_state['story'] = response.text
    except Exception as e:
        st.error(f"Error: {e}")

if 'story' in st.session_state:
    st.success("Here is your story:")
    st.write(st.session_state['story'])
