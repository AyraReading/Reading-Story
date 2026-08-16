import streamlit as st
import openai

st.set_page_config(page_title="Little Reader AI", page_icon="📖")
st.title("📖 Little Reader AI")

api_key = st.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    try:
        client = openai.OpenAI(api_key=api_key)
        
        if st.button("Generate New Story"):
            with st.spinner("Generating story for Ayra..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": "Write a short, simple, 5-sentence story for a child learning to read."}]
                )
                st.session_state['story'] = response.choices[0].message.content
    except Exception as e:
        st.error(f"API Error: {e}")

if 'story' in st.session_state:
    st.success("Here is your story:")
    st.write(st.session_state['story'])
