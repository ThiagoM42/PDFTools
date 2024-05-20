import tempfile
import re
from pathlib import Path
import PyPDF2
import streamlit as st

def input_area(dados_pdf, container):
    for i, question in enumerate(dados_pdf):
        # container.text_area(f'Questão {i + 1}', question, 400, on_change=proc, key=i, args=(i, dados_pdf))
        container.text_area(f'Questão {i + 1}', question, 400, disabled=True)

def extrair_pagina_pdf(arquivo_pdf, numero_pagina_start):
    questions = []
    pdf_reader = PyPDF2.PdfReader(arquivo_pdf)
    total_page = len(pdf_reader.pages)
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
def extrair_pagina_pdf_gabarito(arquivo_pdf, num_page):
    pdf_reader = PyPDF2.PdfReader(arquivo_pdf)
    total_page = len(pdf_reader.pages)
    try:
        page = pdf_reader.pages[num_page - 1]
        text = page.extract_text()
        return text
    except IndexError:
        print('Error')

col1, col2 = st.columns([0.7, 0.3])

st.title('PDFTools')

st.markdown("""
#Extrair página PDF

Escolha um arquivo PDF para extrair uma página:
""")

arquivo_pdf = st.file_uploader(
    label='Selecione o arquivo PDF de questões',
    type='pdf',
    accept_multiple_files=False
)
numero_pagina_start = st.number_input('Página incial da extração', min_value=1)
# numero_pagina_final = st.number_input('Página final da extração', min_value=1)
# if arquivo_pdf:1
#     botoes_desativados = False
# else:
#     botoes_desativados = True

arquivo_pdf_gabarito = st.file_uploader(
    label='Selecione o arquivo PDF do gabarito',
    type='pdf',
    accept_multiple_files=False
)
numero_pagina_extract = st.number_input('Escolha uma página para ser extraido os dados', min_value=1)

if arquivo_pdf:
    container = st.container(border=True)
    dados_pdf = extrair_pagina_pdf(arquivo_pdf=arquivo_pdf, numero_pagina_start=numero_pagina_start)
    st.session_state['dados_pdf'] = dados_pdf
    if dados_pdf is None:
        st.warning(f'PDF não possui página de número {numero_pagina_start}!')
        # return
    input_area(dados_pdf, container)

if arquivo_pdf_gabarito:
    container = st.container(border=True)
    dados_pdf_gabarito = extrair_pagina_pdf_gabarito(arquivo_pdf=arquivo_pdf_gabarito, num_page=numero_pagina_extract)
    st.session_state['gabarito'] = dados_pdf_gabarito
    if dados_pdf_gabarito is None:
        st.warning(f'PDF não possui página de número {numero_pagina_extract}!')
    # print(dados_pdf_gabarito)
    # input_area(dados_pdf, container)