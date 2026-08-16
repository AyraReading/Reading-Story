import streamlit as st
import openai

st.set_page_config(page_title="Little Reader AI", page_icon="📖")
st.title("📖 Little Reader AI")

api_key = st.text_input("Enter your OpenAI API Key", type="password")

if not api_key:
    st.warning("Please enter your OpenAI API key to start!")
else:
    client = openai.OpenAI(api_key=api_key)

    if st.button("Generate New Story"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Write a short, simple, 5-sentence story for a 7-year-old child to practice reading."}]
        )
        st.session_state['story'] = response.choices[0].message.content

    if 'story' in st.session_state:
        st.write(st.session_state['story'])
