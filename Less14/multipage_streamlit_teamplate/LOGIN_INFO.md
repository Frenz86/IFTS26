# Sistema di Login Centralizzato

## Come funziona

L'applicazione ora ha un **sistema di login centralizzato obbligatorio**. Quando accedi all'applicazione su `http://localhost:8501` (o 8502), vedrai SOLO la pagina di login.

### Flusso di autenticazione

1. **Accesso iniziale**: Quando apri l'applicazione, vedi solo il form di login
2. **Autenticazione**: Inserisci username e password
3. **Accesso completo**: Solo dopo il login vedi il menu e tutte le pagine multipage
4. **Logout**: Puoi disconnetterti in qualsiasi momento dalla sidebar

## Credenziali di test

```
Username: ciao
Password: password

Username: admin
Password: admin123

Username: user
Password: userpass
```

## Struttura del codice

### File `pag/auth.py`
Contiene tutta la logica di autenticazione:
- `init_session_state()`: Inizializza lo stato della sessione
- `login_form()`: Mostra il form di login
- `authenticate_user()`: Verifica le credenziali
- `is_logged_in()`: Controlla se l'utente è autenticato
- `get_current_user()`: Restituisce l'username corrente
- `logout()`: Disconnette l'utente

### File `app.py`
Il controllo principale avviene nella funzione `main()`:
```python
if not is_logged_in():
    login_form()
    st.stop()  # Blocca tutto se non sei loggato
```

### Pagine (`pag/*.py`)
Le pagine NON hanno più controlli di autenticazione individuali. Tutte sono protette automaticamente dal controllo centralizzato in `app.py`.

## Come aggiungere nuovi utenti

Modifica il dizionario `USERS` in `pag/auth.py`:

```python
USERS = {
    'nuovo_username': 'nuova_password',
    'altro_user': 'altra_pass',
    # ... altri utenti
}
```

## Sicurezza

⚠️ **IMPORTANTE**: Questo è un sistema di autenticazione base per ambienti di sviluppo/test.

Per produzione, considera:
- Database per gli utenti (non hardcoded)
- Hash delle password (bcrypt, argon2)
- HTTPS per la connessione
- Token di sessione
- Limiti sui tentativi di login
- Autenticazione a due fattori (2FA)

## Come personalizzare

### Cambiare il numero massimo di tentativi di login
In `pag/auth.py`, modifica la condizione:
```python
if st.session_state.authentication_state['login_attempts'] >= 3:
```

### Aggiungere pagine pubbliche (senza login)
Se vuoi che alcune pagine siano accessibili senza login, dovrai modificare `app.py` per avere una logica condizionale basata sulla pagina selezionata.
