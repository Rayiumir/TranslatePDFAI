import streamlit as st
import fitz
import time
from huggingface_hub import InferenceClient

st.title('Translate PDF')
st.markdown("""...""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Yor PDF", type="pdf")
buttonTranslate = st.button("Translate")

if uploaded_file and buttonTranslate:
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in range(len(pdf)):
        pages = pdf[page]
        text = pages.get_text('text')
        client = InferenceClient(
            model = "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
            api_key= ""
        )
        completion = client.chat.completions.create(
            messages=[
                {
                    'role' : 'system',
                    'content' : 'translate all texts into fluent Persian'
                },
                {
                    'role' : 'user',
                    'content' : text
                }
            ]
        )

        st.markdown(completion.choices[0].message.content)
        time.sleep(3)