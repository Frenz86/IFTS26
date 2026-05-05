import spacy
import spacy_streamlit
import streamlit as st

st.set_page_config(page_title="NER", page_icon="🏷️", layout="wide")

st.title("🏷️ Named Entity Recognition")
st.markdown("Identifica entità come persone, luoghi, date nel testo.")
st.markdown("---")

DEFAULT_MODEL = "en_core_web_sm"
DEFAULT_TEXT = """
Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. 
Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. 
They incorporated Google as a California privately held company on September 4, 1998, in California. Google was then reincorporated in Delaware on October 22, 2002.
"""

text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200)
doc = spacy_streamlit.process_text(DEFAULT_MODEL, text)
nlp = spacy.load(DEFAULT_MODEL)
labels = list(nlp.get_pipe("ner").labels)

spacy_streamlit.visualize_ner(
    doc,
    labels=labels,
    show_table=False,
    title="Persons, dates and locations",
)

st.text(f"Analyzed using spaCy model {DEFAULT_MODEL}")
