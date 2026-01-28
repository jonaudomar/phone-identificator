import streamlit as st
import time

st.title('Vérificateur de spam téléphonique')

prospection = ['0162', '0163', '0270', '0271', '0377', '0378', '0424', '0425', '0568', '0569', '0948', '0949', '09475', '09476', '09477', '09478', '09479']

def appelant_normalized(number: str) -> str:
    """
    Nettoie la chaine de caractères du préfixe télphonique et des caractères non numériques.
    """
    value = ''.join(c for c in number if c.isdigit())

    if value.startswith('33'):
        value = '0' + value[2:]

    if value.startswith('0033'):
        value = '0' + value[4:]

    return value

def is_spam(appelant:str):
    """
    Cette fonction vérifie si un numéro est probablement un appel commercial indésirable.
    """
    spam = False

    for prefixe in prospection:
        if appelant.startswith(prefixe):
            spam = True
            break
    return 'spam' if spam else 'tout va bien'

numero = st.text_input("Entrez un numéro de téléphone à 10 chiffres :")
numero = appelant_normalized(numero)

if len(numero) != 10:
    st.warning("Le numéro doit contenir exactement 10 chiffres ci-dessus.")
elif len(numero) == 10:
    st.success("Numéro valide ✅")
    st.success("Cliquez sur 'Vérifier' pour poursuivre l'analyse anti-spam.")

    if st.button('Vérifier', type='primary'):
        with st.spinner("Wait for it...", show_time=True):
            time.sleep(1.7)

        if is_spam(numero) == 'spam':
            st.error('Ceci est très probablement un spam !')
        else:
            st.success('Ce numéro semble fiable')
