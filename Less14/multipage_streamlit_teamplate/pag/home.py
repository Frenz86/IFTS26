import streamlit as st
from .auth import get_current_user

def main():
    st.title("🏠 Home")
    
    st.success(f"Benvenuto, **{get_current_user()}**! 👋")
    st.write("""
    Sei loggato con successo nel sistema. Puoi ora accedere a tutte le funzionalità dell'applicazione:
    
    - **📊 Data Transformation**: Elabora e trasforma i tuoi file Excel
    - **📈 Data Visualisation**: Visualizza i tuoi dati con grafici interattivi
    - **🗺️ Map**: Esplora dati geografici
    - **📜 History**: Visualizza la cronologia delle attività
    - **🔧 Utils**: Strumenti di utilità
    
    Utilizza il menu nella sidebar per navigare tra le diverse sezioni.
    """)

if __name__ == "__main__":
    main()
    
