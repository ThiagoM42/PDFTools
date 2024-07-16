import streamlit as st
import re

def input_area(dados_pdf):
    html_str = f"""
    <style>
    p.a {{
      font: bold 25px Courier;
    }}
    </style>
    <p class="a">Tem {len(dados_pdf)} questões</p>
    """

    st.markdown(html_str, unsafe_allow_html=True)
    st.button('Next step', on_click=match_question_alternative)
    for i, question in enumerate(dados_pdf):
        st.text_area(f'Questão {i + 1}', question, 400, on_change=proc, key=i, args=(i, dados_pdf))
        col1, col2 = st.columns([0.5, 0.5])
        with col1:
            st.button(f'Adicionar questão após a {i + 1}', type="secondary", on_click=add_question, args=(i, dados_pdf))
        with col2:
            st.button(f'Remover Questão {i + 1}', type="primary", on_click=remove_question, args=(i, dados_pdf))
        # st.button(f'Remover Questão {i + 1}', key=i, on_click=remove_question, args=(i, dados_pdf), type="secondary")
    st.button('Next step.', on_click=match_question_alternative)

def proc(key, dados_pdf):
    print(st.session_state[key])
    dados_pdf[key] = st.session_state[key]
    st.session_state['dados_pdf'] = dados_pdf
    input_area(dados_pdf)

def add_question(key, dados_pdf):
    dados_pdf.insert(key+1, '')
    st.session_state['dados_pdf'] = dados_pdf
    input_area(dados_pdf)

def remove_question(key, dados_pdf):
    dados_pdf.pop(key)
    st.session_state['dados_pdf'] = dados_pdf
    input_area(dados_pdf)

def match_question_alternative():
    questoes = []
    num_questao = 0
    texto = ''
    figura = ''
    alternatives_arr_map = []
    dados_pdf = st.session_state['dados_pdf']
    padrao = re.compile(r'^\d{1,}?[.)]+[\sa-zA-Zà-úÀ-Ú0-9.(),%“”""?°ºª!''$;/:-]{1,}?\s{1,}?(?=[aA][\)\.])', flags=re.M)
    for i, question in enumerate(dados_pdf):
        # st.text_area(f'Questão {i + 1}', question, 400, on_change=proc, key=i, args=(i, dados_pdf))
        try:
            enunciado = padrao.findall(question)
            # print(enunciado)
            if enunciado:
                num_questao = re.findall(r'\d{1,}', enunciado[0], flags=re.M)
                if num_questao:
                    num_questao = num_questao[0]
                # print(enunciado)
                alternatives = re.findall(r'^\s?[a-zA-Z]+\)+[\sa-zA-Zà-úÀ-Ú0-9.(),%“”""?°ºª!''$;/:-]+\w', question, flags=re.M)                
                if re.findall(r'texto+\s*\d*', enunciado[0], flags=re.I):
                    texto = re.findall(r'texto+\s*\d*', enunciado[0], flags=re.I)
                elif re.findall(r'parágrafo+\s*\d*', enunciado[0], flags=re.I):
                    texto = re.findall(r'parágrafo+\s*\d*', enunciado[0], flags=re.I)
                elif re.findall(r'trecho+\s*\d*', enunciado[0], flags=re.I):
                    texto = re.findall(r'trecho+\s*\d*', enunciado[0], flags=re.I)
                else:
                    texto=""
                if re.findall(r'figura+\s*\d*', enunciado[0], flags=re.I):
                    figura = re.findall(r'figura+\s*\d*', enunciado[0], flags=re.I)
                elif re.findall(r'imagem+\s*\d*', enunciado[0], flags=re.I):
                    figura = re.findall(r'imagem+\s*\d*', enunciado[0], flags=re.I)
                else:
                    figura=""
                if alternatives:
                    alternatives_arr = re.split('\w\)', *alternatives)
                    alternatives_arr.pop(0)
                    alternatives_arr_map = list(map(lambda x: {'alternativa': x.strip(), 'response': False}, alternatives_arr))
                else:
                    print(f'não houve match {i}')
        except:
            st.error(f'Houve um erro na questão {i+1}', icon="🚨")
        obj_question = {'num_questao': num_questao, 'enunciado': enunciado, 'alternatives': alternatives_arr_map, "texto": texto, "figura": figura, 'name_file': st.session_state['name_file']}
        questoes.append(obj_question)
    # print(questoes)
    st.session_state['questoes'] = questoes
    # print("*************************************************************************************************************************************")

try:
    if st.session_state['dados_pdf']:
        dados_pdf = st.session_state['dados_pdf']
        input_area(dados_pdf)
    # else:
    #     st.write('Nenhum dado para ser editado')
except:
    st.warning('Nenhum dado para ser editado por enquanto!!!')
