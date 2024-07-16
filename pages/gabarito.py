import streamlit as st
import pandas as pd
import pyperclip
import re

col3, col4 = st.columns([0.5, 0.5])
def add_gabarito(question):
    print('PASSOU AKI')
    # num_question = question['num_questao']
    # print(num_question)

try:
    dados_gabarito = []
    alternatives = ['A', 'B', 'C', 'D', 'E']

    if st.session_state['gabarito']:
        if st.button('Associar ao questionário'):
            questoes = st.session_state['questoes']
            for indice, question in enumerate(questoes):
                # print(indice)
                num_question = int(question['num_questao'])
                gabarito_ = st.session_state['gabarito_pd']
                alternative = list(filter(lambda x: x['questao'] == num_question, gabarito_))
                if alternative:
                    response_gabarito = alternative[0]["resposta"]
                    index = alternatives.index(response_gabarito)
                    if index>= 0:
                        print(index)
                        question['alternatives'][index]["response"] = True
            # st.json(first)
        with col3:
            gabarito = st.session_state['gabarito']
            # text_area(f'Questão {i + 1}', question, 400, disabled=True)
            st.text_area('Gabarito', gabarito, 320)
        with col4:
            # print(st.session_state['gabarito_pd'])
            # if st.session_state['gabarito_pd']:
            #     gabarito_copiado = st.text_area('adicionar gabarito aqui, copiar e colar', st.session_state['gabarito_pd'], height=320)
            # else:
            #     gabarito_copiado = st.text_area('adicionar gabarito aqui, copiar e colar', height=320)

            gabarito_copiado = st.text_area('adicionar gabarito aqui, copiar e colar', 
                                            height=320)            
            gabarito_copiado = gabarito_copiado.replace(" ", "").replace("\n", "")
            i=0
            for indice, caractere in enumerate(gabarito_copiado):
                caractere =  re.findall(r'[a-zA-Z]', caractere)
                if(caractere):
                    dados_gabarito.append({'questao': i+1, 'resposta': caractere}) 
                    i=i+1               
            # print(gabarito_copiado)
            df = pd.DataFrame(dados_gabarito)
            st.session_state['gabarito_pd'] = dados_gabarito
            df.set_index("questao", inplace =True)
        if(st.session_state['gabarito_pd']):            
            edited_df = st.data_editor(df, num_rows="dynamic")
        print(len(dados_gabarito))

            # df = pd.DataFrame(st.session_state['gabarito_pd'])
            # df.set_index("questao", inplace =True)
            # edited_df = st.data_editor(df, num_rows="dynamic")

    if st.button('Copiar para a área de transferência'):
        df_str = edited_df.to_csv(index=True, sep='\t')
        pyperclip.copy(df_str)
        st.success("Dados copiados para a área de transferência!")

except:
    st.warning('Nenhum gabarito por enquanto')

