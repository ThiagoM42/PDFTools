import streamlit as st
from streamlit_option_menu import option_menu

import menu_extrair

st.set_page_config(
    page_title='PDFTools',
    page_icon=':page_facing_up',
    layout='wide'
)
_, col2, _ = st.columns(3)

with col2:
    st.title('PDFTools')
    st.markdown("""
    
    ### Escolha a opção desejada abaixo:
    """)

entradas_menu = {
    'Pegar Questões': 'file-earmark-pdf-fill',
    'Extrair página': 'file-earmark-pdf-fill',
    'Combinar PDFs': 'plus-square-fill',
    "Adicionar maraca d´água": 'droplet-fill',
    'Imagens para pdf': 'file-earmark-richtext-fill',
    'Excel para PDF': 'file-earmark-spreadsheet-fill',
}
escolha = option_menu(
    menu_title=None,
    orientation='horizontal',
    options=list(entradas_menu.keys()),
    icons=list(entradas_menu.values()),
    default_index=0
)

_ , col2, _ = st.columns(3)
with col2:
    if escolha == 'Pegar Questões':
       menu_extrair.exibir_menu_extrair(coluna=col2)
    else:
        st.warning('Implementar')
    #
    # if escolha == 'Combinar PDFs':
    #     st.write('Combinar PDFs')