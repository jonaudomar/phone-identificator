import streamlit as st
import time

st.title('Vérificateur de spam')

prospection = ['0162', '0163', '0270', '0271', '0377', '0378', '0424', '0425', '0568', '0569', '0948', '0949', '09475', '09476', '09477', '09478', '09479']

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


numero = st.text_input('Entrez un numéro de téléphone à 10 chiffres :')

if st.button('Vérifier', type='primary'):
    with st.spinner("Wait for it...", show_time=True):
        time.sleep(1.7)

    if is_spam(numero) == 'spam':
        st.warning('Ceci est très probablement un spam !')
    else:
        st.success('Ce numéro semble fiable')
