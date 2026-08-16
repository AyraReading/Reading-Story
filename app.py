import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Little Reader AI", page_icon="📖")
st.title("📖 Little Reader AI")

api_key = st.text_input("Enter your Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if st.button("Generate New Story"):
            with st.spinner("Generating story..."):
                response = model.generate_content('Write a short, simple, 5-sentence story for a child learning to read.')
                st.session_state['story'] = response.text
    except Exception as e:
        st.error(f"Error: {e}")

if 'story' in st.session_state:
    st.success("Here is your story:")
    st.write(st.session_state['story'])
