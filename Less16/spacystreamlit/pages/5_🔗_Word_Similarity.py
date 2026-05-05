import spacy
import streamlit as st
from itertools import combinations
from spacy_streamlit import visualize_similarity
import pandas as pd

st.set_page_config(page_title="Word Similarity", page_icon="🔗", layout="wide")

st.title("🔗 Word Similarity")
st.markdown("Confronta la similarità semantica tra parole.")
st.markdown("---")

DEFAULT_MODEL = "en_core_web_sm"

@st.cache_resource
def load_models():
    nlp_sm = spacy.load("en_core_web_sm")
    nlp_lg = spacy.load("en_core_web_lg")
    return nlp_sm, nlp_lg

nlp, nlp_lg = load_models()

st.subheader("📊 Confronto tra due parole")
col1, col2 = st.columns(2)
with col1:
    word_1 = st.text_input('Parola 1', 'pizza', key='w1')
with col2:
    word_2 = st.text_input('Parola 2', 'fries', key='w2')

visualize_similarity(nlp_lg, (word_1, word_2))

st.markdown("---")

st.subheader("📊 Confronto tra tre parole")
col1, col2, col3 = st.columns(3)
with col1:
    word_a = st.text_input('Parola 1', 'shirt', key='wa')
with col2:
    word_b = st.text_input('Parola 2', 'jeans', key='wb')
with col3:
    word_c = st.text_input('Parola 3', 'apple', key='wc')

tokens = nlp(f"{word_a} {word_b} {word_c}")

# get combination of tokens
comb = combinations(tokens, 2)

most_similar = 0
match_tokens = None
compared_tokens = []
similarities = []

for token in list(comb):
    similarity = token[0].similarity(token[1])
    compared_tokens.append(f"{token[0].text} - {token[1].text}")
    similarities.append(round(similarity * 100, 2))
    if similarity > most_similar:
        most_similar = similarity
        match_tokens = token

if st.button('Calcola Similarità'):
    st.success(f'**{match_tokens[0]}** e **{match_tokens[1]}** sono le più simili con una similarità del **{round(most_similar*100, 2)}%**')
    
    st.write('### Risultati')
    df = pd.DataFrame({
        'Tokens': compared_tokens,
        'Similarity (%)': similarities
    }).sort_values(by='Similarity (%)', ascending=False)
    
    st.dataframe(df, use_container_width=True)
