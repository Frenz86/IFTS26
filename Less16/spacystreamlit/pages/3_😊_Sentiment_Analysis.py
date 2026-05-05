import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import streamlit as st

st.set_page_config(page_title="Sentiment Analysis", page_icon="😊", layout="wide")

st.title("😊 Sentiment Analysis")
st.markdown("Analizza il sentiment di un testo usando TextBlob.")
st.markdown("---")

DEFAULT_MODEL = "en_core_web_sm"
DEFAULT_TEXT = 'I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy.'

@st.cache_resource
def load_nlp():
    nlp = spacy.load(DEFAULT_MODEL)
    nlp.add_pipe('spacytextblob')
    return nlp

nlp = load_nlp()
raw_text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200)

if st.button("Analyze Sentiment"):
    doc = nlp(raw_text)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Polarity", round(doc._.blob.polarity, 2))
        st.caption("Range: -1 (negativo) a +1 (positivo)")
    
    with col2:
        st.metric("Subjectivity", round(doc._.blob.subjectivity, 2))
        st.caption("Range: 0 (oggettivo) a 1 (soggettivo)")
