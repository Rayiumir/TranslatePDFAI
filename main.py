import streamlit as st
import fitz

st.title('Translate PDF')
st.markdown("""...""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Yor PDF", type="pdf")
buttonTranslate = st.button("Translate")

if uploaded_file and buttonTranslate:
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in range(len(pdf)):
        pages = pdf[page]
        st.markdown(page.get_text('text'))
