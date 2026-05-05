import spacy
import spacy_streamlit
import streamlit as st

st.set_page_config(page_title="Tokenization", page_icon="🔡", layout="wide")

st.title("🔡 Tokenization")
st.markdown("Analizza e visualizza i token di un testo.")
st.markdown("---")

DEFAULT_MODEL = "en_core_web_sm"
DEFAULT_TEXT = "this is a test"

nlp = spacy.load(DEFAULT_MODEL)
raw_text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200)
doc = nlp(raw_text)

if st.button("Tokenize"):
    spacy_streamlit.visualize_tokens(doc)
