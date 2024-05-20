import streamlit as st
import pandas as pd
import pyperclip

col3, col4 = st.columns([0.5, 0.5])
try:
    dados_gabarito = []
    if st.session_state['gabarito']:
        with col3:
            gabarito = st.session_state['gabarito']
            # text_area(f'Questão {i + 1}', question, 400, disabled=True)
            st.text_area('Gabarito', gabarito, 320)
        with col4:
            gabarito_copiado = st.text_area('adicionar gabarito aqui, copiar e colar', height=320)
            gabarito_copiado = gabarito_copiado.replace(" ", "").replace("\n", "")
            for indice, caractere in enumerate(gabarito_copiado):
                dados_gabarito.append({'Questão': indice+1, 'Alternativa': caractere})
            # print(gabarito_copiado)
            df = pd.DataFrame(dados_gabarito)
            df.set_index("Questão", inplace =True)

        edited_df = st.data_editor(df, num_rows="dynamic")

    if st.button('Copiar para a área de transferência'):
        df_str = edited_df.to_csv(index=True, sep='\t')
        pyperclip.copy(df_str)
        st.success("Dados copiados para a área de transferência!")
except:
    st.warning('Nenhum gabarito por enquanto')
