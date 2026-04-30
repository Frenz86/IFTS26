import streamlit as st

# Configurazione utenti (in un'applicazione reale, questi dovrebbero essere in un database)
USERS = {
    'ciao': 'password',
    'admin': 'admin123',
    'user': 'userpass'
}

def init_session_state():
    """Inizializza lo stato della sessione per l'autenticazione"""
    if 'authentication_state' not in st.session_state:
        st.session_state.authentication_state = {
            'logged_in': False,
            'username': '',
            'login_attempts': 0
        }

def login_form():
    """Mostra il form di login centralizzato con layout centrato"""

    # Crea colonne per centrare il form (layout non wide)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)

        # Logo + titolo centrati
        logo_col1, logo_col2, logo_col3 = st.columns([1, 1, 1])
        with logo_col2:
            st.image("img/icon_site.png", width=100)

        st.markdown(
            "<h1 style='text-align: center; margin-bottom: 0;'>Template Project</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='text-align: center; color: gray; margin-top: 0;'>Bentornato! Accedi per continuare.</p>",
            unsafe_allow_html=True,
        )
        st.markdown("---")

        with st.form("login_form"):
            st.subheader("🔐 Accesso")
            username = st.text_input("👤 Username", placeholder="Inserisci il tuo username")
            password = st.text_input("🔒 Password", type="password", placeholder="Inserisci la tua password")
            submit_button = st.form_submit_button("🚀 Accedi", type="primary", use_container_width=True)

            if submit_button:
                if authenticate_user(username, password):
                    st.session_state.authentication_state['logged_in'] = True
                    st.session_state.authentication_state['username'] = username
                    st.session_state.authentication_state['login_attempts'] = 0
                    st.success("✅ Login effettuato con successo!")
                    st.rerun()
                else:
                    st.session_state.authentication_state['login_attempts'] += 1
                    st.error("❌ Username o password non corretti!")

                    if st.session_state.authentication_state['login_attempts'] >= 3:
                        st.warning("⚠️ Troppi tentativi di login falliti. Riprova più tardi.")

        # Credenziali di test in modo più discreto, sotto il form
        with st.expander("ℹ️ Credenziali di test (demo)"):
            st.code("ciao / password\nadmin / admin123\nuser / userpass", language=None)

def authenticate_user(username, password):
    """Verifica le credenziali dell'utente"""
    return username in USERS and USERS[username] == password

def logout():
    """Effettua il logout dell'utente"""
    st.session_state.authentication_state['logged_in'] = False
    st.session_state.authentication_state['username'] = ''
    st.session_state.authentication_state['login_attempts'] = 0
    st.rerun()

def is_logged_in():
    """Controlla se l'utente è loggato"""
    return st.session_state.authentication_state.get('logged_in', False)

def get_current_user():
    """Restituisce l'username dell'utente corrente"""
    return st.session_state.authentication_state.get('username', '')