import streamlit as st
import os
from dotenv import load_dotenv
import openai
# Load environment variables from .env file
load_dotenv()
# Set OpenAI API configurations
openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)

from langchain.chat_models import ChatOpenAI


def generate_response(prompt, temperature):
    chat_model = ChatOpenAI(temperature=temperature, model_kwargs={"engine":"GPT3-5"}) 
    text = prompt
    return chat_model.predict(text)


def main():
    st.title("LangChain Response Generator")

    # User input prompt
    user_input = st.text_area("Enter your prompt:")

    # Temperature slider
    temperature = st.slider("Select temperature:", 0.1, 1.0, 0.5, 0.1)

    if st.button("Generate Response"):
        if user_input:
            response = generate_response(user_input, temperature)
            st.write("Generated Response:")
            st.write(response)
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
