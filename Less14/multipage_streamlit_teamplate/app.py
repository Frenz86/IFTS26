import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import importlib
#import joblib
import os
from pag.auth import init_session_state, is_logged_in, login_form, logout, get_current_user

st.set_page_config(
                    page_title="Template Project",
                    page_icon=Image.open("img/icon_site.png"),
                    layout="wide",
                    )


def get_pages():

    PAGES = 'pag' # cartella con le pagine, non usare pages!!!
    pages = []
    icons = []
    modules = []
    
    BLACKLIST_FILES = ['__init__', 'test','auth','utils']  # aggiungi qui i file da escludere    
    # page_order = []
    page_order = ['home', 'history', 'datavisualisation', 'map', 'data','titanic']

    files = [f[:-3] for f in os.listdir(PAGES) if f.endswith('.py') and f[:-3] not in BLACKLIST_FILES]
    files.sort(key=lambda x: page_order.index(x) if x in page_order else len(page_order))
    
    # Mapping icon 
    icon_mapping = {
                    'home': 'bi-house',
                    'history': 'bi-hourglass-split',
                    'datavisualisation': 'bi-card-image',
                    'map': 'bi-map',
                    'data': 'bi-database-down',
                    }
    
    for file in files:
        page_name = file.capitalize()
        pages.append(page_name)        
        icons.append(icon_mapping.get(file, 'bi-file'))        
        module = importlib.import_module(f'{PAGES}.{file}')
        modules.append(module)
    return pages, icons, modules

pages, icons, modules = get_pages()

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
                        "title": title,
                        "function": function
                        })

    def main():
        # Inizializza il sistema di autenticazione
        init_session_state()
        
 
        if not is_logged_in():
            # Mostra solo il form di login
            st.title("Template Project")
            login_form()
            st.stop()  # Ferma l'esecuzione qui se non sei loggato
        

        with st.sidebar:
            # Logo + titolo in cima alla sidebar
            col_logo, col_title = st.columns([1, 3], vertical_alignment="center")
            with col_logo:
                st.image("img/icon_site.png", width=50)
            with col_title:
                st.markdown("### Template Project")
            st.caption("Il tuo spazio di lavoro")
            st.markdown("---")

            # Menu di navigazione
            app = option_menu(
                                menu_title="Menu",
                                options=pages,
                                icons=icons,
                                menu_icon="bi-list",
                                default_index=0,
                                styles={
                                        "container": {"padding": "5!important", "background-color": "transparent"},
                                        "icon": {"color": "inherit", "font-size": "23px"},
                                        "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px"},
                                        "nav-link-selected": {"color": "black", "background-color": "#9ac280"}
                                        }
                                        )

            # Sezione utente in fondo alla sidebar
            st.markdown("---")
            current_user = get_current_user()
            st.markdown(f"#### 👋 Ciao, **{current_user}**!")
            st.caption("Buon lavoro 🚀")
            if st.button("🚪 Logout", type="secondary", use_container_width=True):
                logout()

        selected_index = pages.index(app)
        modules[selected_index].main()

if __name__ == "__main__":
    MultiApp.main()