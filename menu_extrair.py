import tempfile
import re
from pathlib import Path
import PyPDF2
import streamlit as st


def exibir_menu_extrair(coluna):
    dados_pdf = []
    with coluna:
        st.markdown("""
        #Extrair página PDF
        
        Escolha um arquivo PDF para extrair uma página:
        """)

        arquivo_pdf = st.file_uploader(
            label='Selecione o arquivo PDF',
            type='pdf',
            accept_multiple_files=False
        )

        if arquivo_pdf:
            botoes_desativados = False
        else:
            botoes_desativados = True

        numero_pagina_start = st.number_input('Página incial da extração', min_value=1, disabled=botoes_desativados)
        numero_pagina_final = st.number_input('Página final da extração', min_value=1, disabled=botoes_desativados)

        clicou_processar = st.button(
            'Clique para processar o arquivo PDF...',
            use_container_width=True,
            disabled=botoes_desativados
        )
        if clicou_processar:
            container = st.container(border=True)
            dados_pdf = extrair_pagina_pdf(arquivo_pdf=arquivo_pdf, numero_pagina_start=numero_pagina_start)
            if dados_pdf is None:
                st.warning(f'PDF não possui página de número {numero_pagina_start}!')
                return
            input_area(dados_pdf, container)

def input_area(dados_pdf, container):
    for i, question in enumerate(dados_pdf):
        container.text_area(f'Questão {i + 1}', question, 400, on_change=proc, key=i, args=(i, dados_pdf))

def proc(key, dados_pdf):
    dados_pdf[key] = st.session_state[key]
    container = st.container(border=True)
    button = container.button('Next step', on_click=match_question_alternative, args=dados_pdf)
    input_area(dados_pdf, container)

def extrair_pagina_pdf(arquivo_pdf, numero_pagina_start):
    questions = []
    pdf_reader = PyPDF2.PdfReader(arquivo_pdf)
    total_page = len(pdf_reader.pages)
    # pattern = r'\d{2}\. .*?\n(?:[A-D]\) .+?\.\n)+'
    # pattern = r'^\d+\.\s+.*,\s*(A\).+?)(B\).+?)(C\).+?)(D\).+?)$'
    # pattern = r'\d+\..*?(?=\d+\.|$)'
    pattern = r'\d+\..*?(?=\n\d+\.\s|$)'
    for num_page in range(numero_pagina_start, total_page+1):
        # print(num_page)
        try:
            page = pdf_reader.pages[num_page-1]

            text = page.extract_text() + "0) end a)"
            page_questions = re.findall(r'^\s?\d?\d\)+[\sa-zA-Zà-úÀ-Ú0-9.(),:;!?-]{1,}?\s{1,}?(?=\s?\d?\d\))', text, flags=re.M)
            if not page_questions:
                text = page.extract_text()
                page_questions = re.findall(pattern, text, re.DOTALL)
                # page_questions = re.findall(r'^\d{2}\.+[\sa-zA-Zà-úÀ-Ú0-9.(),:;!?"\'\,(\d)-]{1,}?\s{1,}?(?=\s?\d?\d\))', text, flags=re.M)

            # tem que retornar um array para cada questão
            # return page_questions
            questions.extend(page_questions)
            # print(questions)
            # questions
            # questions = list(filter(lambda el: re.match(r'A\)', el, flags=re.M), questions))
            # questions = list(filter(lambda el: print(re.match(r'A\)', el, flags=re.M)), questions))
            questions = list(filter(lambda el: len(re.findall(r'[Aa]\)', el))>0, questions))
        except IndexError:
            print('Error')

    return questions


def match_question_alternative(dados_pdf):
    print(dados_pdf)
    container = st.container(border=True)
    # container.write(dados)
    # input_area(dados_pdf, container, '')