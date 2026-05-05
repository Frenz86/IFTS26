import spacy
import streamlit as st
from spacy_streamlit import visualize_parser

st.set_page_config(page_title="Dependency Parser", page_icon="🌳", layout="wide")

st.title("🌳 Dependency Parser")
st.markdown("Visualizza le dipendenze grammaticali del testo.")
st.markdown("---")

DEFAULT_MODEL = "en_core_web_sm"
DEFAULT_TEXT = "Bill Gates is not the CEO of Microsoft anymore"

raw_text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200)
nlp = spacy.load(DEFAULT_MODEL)
doc = nlp(raw_text)

if st.button('Visualizza Parser'):
    visualize_parser(doc)
