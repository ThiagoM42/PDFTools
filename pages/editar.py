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
    for i, question in enumerate(dados_pdf):
        st.text_area(f'Questão {i + 1}', question, 400, on_change=proc, key=i, args=(i, dados_pdf))

def proc(key, dados_pdf):
    dados_pdf[key] = st.session_state[key]
    container = st.container(border=True)
    button = container.button('Next step', on_click=match_question_alternative)
    input_area(dados_pdf)

def match_question_alternative():
    # enunciado = re.findall(r'^\s?\d+\)+[\sa-zA-Zà-úÀ-Ú0-9.(),:-]{1,}?\s{1,}?(?=a\))', dados_pdf[0], flags=re.M)
    dados_pdf = st.session_state['dados_pdf']
    padrao = re.compile(r'^\d+\.\s+.*,\s*(A\).+?)(B\).+?)(C\).+?)(D\).+?)$', re.DOTALL)
    match = padrao.match(dados_pdf[0])
    enunciado = match.group(0)
    opcao_a = match.group(1)
    print(enunciado.split('A)')[0])
    print("Opção A:", opcao_a)
    # container = st.container(border=True)
    # container.write(dados)
    # input_area(dados_pdf, container, '')

try:
    if st.session_state['dados_pdf']:
        dados_pdf = st.session_state['dados_pdf']
        input_area(dados_pdf)
    # else:
    #     st.write('Nenhum dado para ser editado')
except:
    st.warning('Nenhum dado para ser editado por enquanto!!!')
