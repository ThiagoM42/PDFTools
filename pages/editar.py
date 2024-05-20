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
    st.button('Next step.', on_click=match_question_alternative)

def proc(key, dados_pdf):
    dados_pdf[key] = st.session_state[key]
    input_area(dados_pdf)

def match_question_alternative():
    questoes = []
    num_questao = 0
    alternatives_arr_map = []
    dados_pdf = st.session_state['dados_pdf']
    padrao = re.compile(r'^\d{1,}?[.)]+[\sa-zA-Zà-úÀ-Ú0-9.(),%“”""''$;/:-]{1,}?\s{1,}?(?=[aA][\)\.])', flags=re.M)
    for i, question in enumerate(dados_pdf):
        # st.text_area(f'Questão {i + 1}', question, 400, on_change=proc, key=i, args=(i, dados_pdf))
        enunciado = padrao.findall(question)
        # print(enunciado)
        if enunciado:
            num_questao = re.findall(r'\d{1,}', enunciado[0], flags=re.M)
            if num_questao:
                num_questao = num_questao[0]
            # print(enunciado)
            alternatives = re.findall(r'^\s?[a-zA-Z]+\)+[\sa-zA-Zà-úÀ-Ú0-9.(),%“”""''$;/:-]+\w', question, flags=re.M)
            # print(alternatives)
            if alternatives:
                alternatives_arr = re.split('\w\)', *alternatives)
                alternatives_arr.pop(0)
                alternatives_arr_map = list(map(lambda x: x.strip(), alternatives_arr))
                print(alternatives_arr_map)
                # print(
                #     "*************************************************************************************************************************************")

            else:
                print(f'não houve match {i}')
        obj_question = {'num_questao': num_questao, 'enunciado': enunciado, 'alternatives': alternatives_arr_map}
        questoes.append(obj_question)
    print(questoes)
    st.session_state['questoes'] = questoes
    print("*************************************************************************************************************************************")

try:
    if st.session_state['dados_pdf']:
        dados_pdf = st.session_state['dados_pdf']
        input_area(dados_pdf)
    # else:
    #     st.write('Nenhum dado para ser editado')
except:
    st.warning('Nenhum dado para ser editado por enquanto!!!')
