# python -m spacy download en_core_web_sm
# python -m spacy download en_core_web_lg
# pip install spacy spacy-streamlit spacytextblob textblob -U

import streamlit as st

st.set_page_config(
    page_title="SpaCy NLP App",
    page_icon="🔤",
    layout="wide"
)

st.title("🔤 SpaCy NLP Multipage App")
st.markdown("---")

st.markdown("""
## Benvenuto nell'app di Natural Language Processing!

Questa applicazione dimostra diverse funzionalità di **spaCy** e **Streamlit**:

### 📄 Pagine disponibili:

1. **🔡 Tokenization** - Analizza e visualizza i token di un testo
2. **🏷️ NER (Named Entity Recognition)** - Identifica entità come persone, luoghi, date
3. **😊 Sentiment Analysis** - Analizza il sentiment di un testo con TextBlob
4. **🌳 Dependency Parser** - Visualizza le dipendenze grammaticali
5. **🔗 Word Similarity** - Confronta la similarità tra parole

---

👈 **Seleziona una pagina dal menu laterale per iniziare!**

---

### 📦 Requisiti:
```bash
pip install spacy spacy-streamlit spacytextblob textblob pandas
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_lg
python -m textblob.download_corpora
```
""")

st.sidebar.success("Seleziona una pagina sopra.")
