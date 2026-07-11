import streamlit as st
from ollama import Client

# creat client instace (very inpmortant)

client = Client(host="http://localhost:11434")
st.set_page_config(
    page_title="custom LLM model by prakash senapati - ollama",
    layout= "centered"


)

st.title("Mr.prakash senapati - ollama app")

prompt = st.text_area("Enter your prompt here:", height=200)

if st.button("Generate Response"):
    if prompt.strip() == "":
        st.warning("please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat(
                model="qwen2.5:3b",
                messages=[
                    {"role": "user", "content": prompt}
                ]

            )
            st.success("Response generated successfully!")
            st.write(response["message"]["content"])