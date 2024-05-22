import streamlit as st
import pandas as pd
import pyperclip


col3, col4 = st.columns([0.5, 0.5])
def add_gabarito(question):
    print('PASSOU AKI')
    # num_question = question['num_questao']
    # print(num_question)

try:
    dados_gabarito = []
    questoes = [
        {
            "num_questao": "01",
            "enunciado": [
                "01. De acordo com o Texto 1 , quanto ao uso de tecnologias,  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "mais da metade das empresas brasileiras só utilizam a Inteligência Artificial.",
                    "response": False
                },
                {
                    "alternativa": "menos da metade das empresas brasileiras utilizam a Inteligência Artificial.",
                    "response": False
                },
                {
                    "alternativa": "metade das empresas brasileiras não utilizam a Inteligência Artificial.",
                    "response": False
                },
                {
                    "alternativa": "metade das empresas brasileiras já utilizam a Inteligência Artificial",
                    "response": False
                }
            ],
            "texto": [
                "Texto 1"
            ],
            "figura": ""
        },
        {
            "num_questao": "02",
            "enunciado": [
                "02. O propósito comunicativo dominante no Texto 1  é \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "discutir impactos da Inteligência Artificial no mundo dos negócios brasileiro.",
                    "response": False
                },
                {
                    "alternativa": "refletir sobre o uso adequado da Inteligência Artificial nas empresas brasileiras.",
                    "response": False
                },
                {
                    "alternativa": "analisar o papel da Inteligência Artificial na automação nas fábricas brasileiras.",
                    "response": False
                },
                {
                    "alternativa": "informar sobre o avanço do uso da Inteligência Artificial no mercado brasileiro",
                    "response": False
                }
            ],
            "texto": [
                "Texto 1"
            ],
            "figura": ""
        },
        {
            "num_questao": "03",
            "enunciado": [
                "03. O Texto 1   é predominantemente  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "narrativo por relatar um fato recente de interesse da sociedade: uso da Inteligência Artificial.",
                    "response": False
                },
                {
                    "alternativa": "argumentativo por defender um ponto de vista sobre o uso da Inteligência Artificial.",
                    "response": False
                },
                {
                    "alternativa": "narrativo por contar como se deu a entrada da Inteligência Artificial nas empresas brasileiras.",
                    "response": False
                },
                {
                    "alternativa": "argumentativo por se contrapor ao uso da Inteligência Artificial nas empresas brasileiras",
                    "response": False
                }
            ],
            "texto": [
                "Texto 1"
            ],
            "figura": ""
        },
        {
            "num_questao": "04",
            "enunciado": [
                "04. Quanto à configuração do gênero, o Texto 1  é um(a)  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "reportagem.",
                    "response": False
                },
                {
                    "alternativa": "comentário.",
                    "response": False
                },
                {
                    "alternativa": "notícia.",
                    "response": False
                },
                {
                    "alternativa": "editorial.  \n \nConsidere o trecho para responder às questões de 05 a 11.  \n \n \nA tecnologia é, (",
                    "response": False
                },
                {
                    "alternativa": "cada vez mais (",
                    "response": False
                },
                {
                    "alternativa": ", (",
                    "response": False
                },
                {
                    "alternativa": "uma aliada (",
                    "response": False
                },
                {
                    "alternativa": "para as empresas de variados setores e portes. \nUma pesquisa global recente da IBM mostrou que (",
                    "response": False
                },
                {
                    "alternativa": "41% das empresas brasileira s utilizam alguma forma \nde Inteligência Artificial em seu dia a dia. Os dados coletados demonstram que (",
                    "response": False
                },
                {
                    "alternativa": "houve um “crescimento \nconsiderável” (",
                    "response": False
                },
                {
                    "alternativa": "na adoção da tecnologia no cenário pós -pandemia, uma vez que (",
                    "response": False
                },
                {
                    "alternativa": "foram muitos os \ndesafios causados pela Covid -19",
                    "response": False
                }
            ],
            "texto": [
                "figura"
            ],
            "figura": ""
        },
        {
            "num_questao": "05",
            "enunciado": [
                "05. Em relação à sua organização, o parágrafo é formado por  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "três períodos e seis orações.",
                    "response": False
                },
                {
                    "alternativa": "dois períodos e quatro orações.",
                    "response": False
                },
                {
                    "alternativa": "um único período e seis orações.",
                    "response": False
                },
                {
                    "alternativa": "quatro períodos e cinco orações",
                    "response": False
                }
            ],
            "texto": [
                "figura"
            ],
            "figura": ""
        },
        {
            "num_questao": "06",
            "enunciado": [
                "06. A expressão CADA VEZ MAIS  (2) assume valor de uma locução  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "prepositiva.",
                    "response": False
                },
                {
                    "alternativa": "conjuntiva.",
                    "response": False
                },
                {
                    "alternativa": "adverbial.",
                    "response": False
                },
                {
                    "alternativa": "adjetiva",
                    "response": False
                }
            ],
            "texto": [
                "figura"
            ],
            "figura": ""
        },
        {
            "num_questao": "07",
            "enunciado": [
                "07. Quanto ao uso das vírgulas  marcadas por (1) e (3), é correto afirmar que  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "isolam adjunto adverbial.",
                    "response": False
                },
                {
                    "alternativa": "isolam um adjunto adnominal.",
                    "response": False
                },
                {
                    "alternativa": "separam expressão com função de vocativo.",
                    "response": False
                },
                {
                    "alternativa": "separam uma expressão com função de aposto",
                    "response": False
                }
            ],
            "texto": [
                "figura"
            ],
            "figura": ""
        },
        {
            "num_questao": "08",
            "enunciado": [
                "08. O uso do vocábulo ALIADA  (4) deixa implícita a informação de que a tecnologia  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "contribui para o crescimento econômico das empresas.",
                    "response": False
                },
                {
                    "alternativa": "garante o desenvolvimento sustentável e os lucros das empresas.",
                    "response": False
                },
                {
                    "alternativa": "contribui com a automação dos serviços e com o aumento do desemprego.",
                    "response": False
                },
                {
                    "alternativa": "mudou as relações de trabalho nas empresas, informatizando os serviços",
                    "response": False
                }
            ],
            "texto": [
                "figura"
            ],
            "figura": ""
        },
        {
            "num_questao": "09",
            "enunciado": [
                "09. Nas ocorrências (5) e (6), o elemento linguístico QUE , respectivamente, tem valor de  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "pronome e conjunção.",
                    "response": False
                },
                {
                    "alternativa": "conjun ção e conjunção.",
                    "response": False
                },
                {
                    "alternativa": "preposição e interjeição.",
                    "response": False
                },
                {
                    "alternativa": "substantivo e advérbio",
                    "response": False
                }
            ],
            "texto": [
                "figura"
            ],
            "figura": ""
        },
        {
            "num_questao": "10",
            "enunciado": [
                "10. Em “CRESCIMENTO CONSIDERÁVEL”  (7), as aspas foram usadas para  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "marcar uma informação irônica.",
                    "response": False
                },
                {
                    "alternativa": "demarcar uma citação indireta.",
                    "response": False
                },
                {
                    "alternativa": "demarcar uma citação direta.",
                    "response": False
                },
                {
                    "alternativa": "enfatizar uma informação importa nte",
                    "response": False
                }
            ],
            "texto": [
                "figura"
            ],
            "figura": ""
        },
        {
            "num_questao": "11",
            "enunciado": [
                "11. O elemento linguístico UMA VEZ QUE  (8) introduz uma ideia de  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "causa em relação a algo que já foi discutido no texto.",
                    "response": False
                },
                {
                    "alternativa": "concessão em relação a algo que ainda será dito no texto.",
                    "response": False
                },
                {
                    "alternativa": "conclusão em relação às ideias discutidas ao longo do texto.",
                    "response": False
                },
                {
                    "alternativa": "consequência das ideias apresentadas ao longo do texto",
                    "response": False
                }
            ],
            "texto": [
                "figura"
            ],
            "figura": ""
        },
        {
            "num_questao": "12",
            "enunciado": [
                "12. De acordo com o Texto 2 , é correto afirmar que  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "possivelmente, o ChatGPT  resolverá os problemas de escrita na escola",
                    "response": False
                },
                {
                    "alternativa": "historicamente, o ChatGPT  é a plataforma que se desenvolveu mais rápido.",
                    "response": False
                },
                {
                    "alternativa": "atualmente, a Inteligência Artificial simplifica os problemas da humanidade.",
                    "response": False
                },
                {
                    "alternativa": "futuramente, a humanidade não precisará mais da Inteligência Artificial",
                    "response": False
                }
            ],
            "texto": [
                "Texto 2"
            ],
            "figura": ""
        },
        {
            "num_questao": "13",
            "enunciado": [
                "13. Sobre o Texto 3 , é correto afirmar que  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "a maioria dos brasileiros afirmou já usar a Inteligência Artificial.",
                    "response": False
                },
                {
                    "alternativa": "a confiança dos brasileiros na Inteligência Artificial é a maior do mundo.",
                    "response": False
                },
                {
                    "alternativa": "o Brasil é um dos países onde a tecnologia tem um alto índ ice de aceitação.",
                    "response": False
                },
                {
                    "alternativa": "o Brasil é um dos quatro países que mais produzem tecnologia no mundo",
                    "response": False
                }
            ],
            "texto": [
                "Texto 3"
            ],
            "figura": ""
        },
        {
            "num_questao": "14",
            "enunciado": [
                "14. Quanto à configuração genérica, os textos 2 e 3, respectivamente, são  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "tirinha e tabela.",
                    "response": False
                },
                {
                    "alternativa": "anedota e tabela.",
                    "response": False
                },
                {
                    "alternativa": "charge e infográfico",
                    "response": False
                },
                {
                    "alternativa": "cartum e infográfico",
                    "response": False
                }
            ],
            "texto": [
                "figura"
            ],
            "figura": ""
        },
        {
            "num_questao": "15",
            "enunciado": [
                "15. Os textos 1, 2 e 3 apresentam em comum o  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "tipo textual.",
                    "response": False
                },
                {
                    "alternativa": "gênero textual.",
                    "response": False
                },
                {
                    "alternativa": "registro informal.",
                    "response": False
                },
                {
                    "alternativa": "recorte temático",
                    "response": False
                }
            ],
            "texto": [
                "texto"
            ],
            "figura": ""
        },
        {
            "num_questao": "16",
            "enunciado": [
                "16. O Texto 1  mostra que 41% das empresas brasileiras utilizam alguma forma de Inteligência Artificial em \nseu dia a dia. Considerando -se que existam 21 milhões de empresas no Brasil, a quantidade de \ncorporações com uso dessa tecnologia é  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "8.400.000.",
                    "response": False
                },
                {
                    "alternativa": "8.610.000.",
                    "response": False
                },
                {
                    "alternativa": "12.390.000.",
                    "response": False
                },
                {
                    "alternativa": "12.600.000",
                    "response": False
                }
            ],
            "texto": [
                "Texto 1"
            ],
            "figura": ""
        },
        {
            "num_questao": "17",
            "enunciado": [
                "17. De acordo com o Texto 1 , U$ 504 milhões equivale a cerca de R$ 2,61 bilhões. Sendo assim, é possível \nafirmar que a cotação do dólar, em reais, aproximadamente, foi de  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "R$ 5,12.",
                    "response": False
                },
                {
                    "alternativa": "R$ 5,24.",
                    "response": False
                },
                {
                    "alternativa": "R$ 5,18.",
                    "response": False
                },
                {
                    "alternativa": "R$ 5,30",
                    "response": False
                }
            ],
            "texto": [
                "Texto 1"
            ],
            "figura": ""
        },
        {
            "num_questao": "18",
            "enunciado": [
                "18. Tomando por base os valores  percentuais presente s nas barras do Texto 3 , a média aritmética da \naceitação nos 10 países que mais confiam em inteligência artificial é de  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "47,7%.",
                    "response": False
                },
                {
                    "alternativa": "53,2%.",
                    "response": False
                },
                {
                    "alternativa": "63,1%.",
                    "response": False
                },
                {
                    "alternativa": "43,9",
                    "response": False
                }
            ],
            "texto": [
                "Texto 3"
            ],
            "figura": ""
        },
        {
            "num_questao": "19",
            "enunciado": [
                "19. A leitura do Texto 3  permite afirmar que a diferença entre os percentuais do país qu e mais aceita e do \nque menos aceita (dentre os 10 com maior aceitação) a Inteligência Artificial é  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "41%.",
                    "response": False
                },
                {
                    "alternativa": "40%.",
                    "response": False
                },
                {
                    "alternativa": "39%.",
                    "response": False
                },
                {
                    "alternativa": "42",
                    "response": False
                }
            ],
            "texto": [
                "Texto 3"
            ],
            "figura": ""
        },
        {
            "num_questao": "20",
            "enunciado": [
                "20. Considerando que, no Texto 3 , as barras representantes dos percentuais de aceitação da Inteligência \nArtificial possuem áreas proporcionais ao seu respectivo percentual e que a barra referente à Índia \n(primeira posição) é um retângulo de dimensões 0,8 cm x 4 cm, é possível afirmar que a barra de \nCingapura (quinta posição) é um retângulo de área igual a  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "2,22 cm2.",
                    "response": False
                },
                {
                    "alternativa": "3,02 cm2.",
                    "response": False
                },
                {
                    "alternativa": "1,92 cm2.",
                    "response": False
                },
                {
                    "alternativa": "3,20 cm2",
                    "response": False
                }
            ],
            "texto": [
                "Texto 3"
            ],
            "figura": ""
        },
        {
            "num_questao": "21",
            "enunciado": [
                "21. De acordo com os dados apresentados no Texto 3 , a moda dos percentuais de aceitação nos 10 países \nque mais confiam na inteligência artificial é de  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "42,5%.",
                    "response": False
                },
                {
                    "alternativa": "54,5%.",
                    "response": False
                },
                {
                    "alternativa": "26%.",
                    "response": False
                },
                {
                    "alternativa": "34",
                    "response": False
                }
            ],
            "texto": [
                "Texto 3"
            ],
            "figura": ""
        },
        {
            "num_questao": "22",
            "enunciado": [
                "22. Em um número natural, formado por três algarismos, o dígito da centena é 4, o da dezena é 6 e o da \nunidade é Y, formando o número 46Y. Sabendo que esse número é múltiplo de 3, o produto dos valores \nque Y pode assumir é  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "10.",
                    "response": False
                },
                {
                    "alternativa": "40.",
                    "response": False
                },
                {
                    "alternativa": "20.",
                    "response": False
                },
                {
                    "alternativa": "80",
                    "response": False
                }
            ],
            "texto": [
                "Texto 3"
            ],
            "figura": ""
        },
        {
            "num_questao": "23",
            "enunciado": [
                "23. Considere que uma determinada pessoa estava estudando probabilidade com auxílio do aplicativo \nCHATGPT, e fez o questionamento apresentado na Figura 1 abaixo:  \n \nFigura 1  \n \n \n \n \nFonte: Aplicativo CHATGPT.  \n \nApós essa mensagem, o aplicativo CHATGPT respondeu, c orretamente, que a probabilidade, nessa \nsituação, corresponderia a  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "2/3.",
                    "response": False
                },
                {
                    "alternativa": "4/5.",
                    "response": False
                },
                {
                    "alternativa": "1/3.",
                    "response": False
                },
                {
                    "alternativa": "1/2",
                    "response": False
                }
            ],
            "texto": [
                "Figura 1",
                "Figura 1"
            ],
            "figura": ""
        },
        {
            "num_questao": "24",
            "enunciado": [
                "24. De acordo com o Texto 1, a estimativa do investimento realizado por companhias brasileiras em \nInteligência Artificial, no ano de 2022, foi de U$ 504 milhões, o que representa um aumento de 28% em \nrelação ao ano anterior. Dessa forma, no ano de 2021, em valores estimados, o investimento teria sido \nequivalente a  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "U$ 363 .880.000,00.",
                    "response": False
                },
                {
                    "alternativa": "U$ 402 .290.000,00.",
                    "response": False
                },
                {
                    "alternativa": "U$ 393 .750.000,00.",
                    "response": False
                },
                {
                    "alternativa": "U$ 355 .438.000,00",
                    "response": False
                }
            ],
            "texto": [
                "Texto 1"
            ],
            "figura": ""
        },
        {
            "num_questao": "25",
            "enunciado": [
                "25. Para a construção de uma microempresa de treinamento em programas e recursos de Inteligência \nArtificial, foi utilizado um terreno retangular, cujo comprimento é de 5 m maior do que a largura e a área \nigual a 300 m2. A soma dos lados desse terreno retangular é  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "70 m.",
                    "response": False
                },
                {
                    "alternativa": "60 m.",
                    "response": False
                },
                {
                    "alternativa": "54 m.",
                    "response": False
                },
                {
                    "alternativa": "72 m",
                    "response": False
                }
            ],
            "texto": [
                "Texto 1"
            ],
            "figura": ""
        },
        {
            "num_questao": "25",
            "enunciado": [],
            "alternatives": [
                {
                    "alternativa": "70 m.",
                    "response": False
                },
                {
                    "alternativa": "60 m.",
                    "response": False
                },
                {
                    "alternativa": "54 m.",
                    "response": False
                },
                {
                    "alternativa": "72 m",
                    "response": False
                }
            ],
            "texto": [
                "Texto 1"
            ],
            "figura": ""
        },
        {
            "num_questao": "27",
            "enunciado": [
                "27. Um jovem estudante pretende ir ao Vale do Silício, localizado nos Estados Unidos, para fazer um curso \nsobre Inteligência Artificial. Contudo, as distâncias nas estradas do país são marcadas em milhas. Como \nele está acostumado a utilizar os valores em quilô metros e quer entender melhor as distâncias locais, \nanalisa uma placa, indicando que a cidade aonde ele deseja chegar, está a 92 milhas de distância. \nSabendo que 1 quilômetro é equivalente a cerca de 0,62 milhas, é correto afirmar que a distância a ser \npercorrida por ele, em quilômetros, aproximadamente, é de  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "155.",
                    "response": False
                },
                {
                    "alternativa": "132.",
                    "response": False
                },
                {
                    "alternativa": "126.",
                    "response": False
                },
                {
                    "alternativa": "148",
                    "response": False
                }
            ],
            "texto": [
                "Texto 1"
            ],
            "figura": ""
        },
        {
            "num_questao": "28",
            "enunciado": [
                "28. Para empreender, no ramo de Inteligência Artificial, um recém -formado na área de TI (Tecnologia da \nInformação) pretende adquirir um empréstimo com um amigo. A condição acordada e ntre eles garantiu \num valor de 25 mil reais, valor a ser pago ao final de dois anos, com taxa de juros simples de 1% ano \nmês. Desse modo, ao final desse tempo, ele terá pago um valor total de  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "R$ 30.000,00 .",
                    "response": False
                },
                {
                    "alternativa": "R$ 31.000,00 .",
                    "response": False
                },
                {
                    "alternativa": "R$ 29.000,00 .",
                    "response": False
                },
                {
                    "alternativa": "R$ 28.000,00",
                    "response": False
                }
            ],
            "texto": [
                "Texto 1"
            ],
            "figura": ""
        },
        {
            "num_questao": "29",
            "enunciado": [
                "29. Segun do o Texto 1 , os investimentos em Inteligência Artificial aumentaram 28% entre 2021 e 2022. Esse \npercentual de 28%, na forma de fração, pode ser representado como  \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "7/25.",
                    "response": False
                },
                {
                    "alternativa": "7/20.",
                    "response": False
                },
                {
                    "alternativa": "13/21.",
                    "response": False
                },
                {
                    "alternativa": "1/4",
                    "response": False
                }
            ],
            "texto": [
                "Texto 1"
            ],
            "figura": ""
        },
        {
            "num_questao": "30",
            "enunciado": [
                "30. Uma empresa de Inteligência Artificial (IA) montou a logomarca abaixo apresentada para divulgação e \ndistribuição de panfletos: um retângulo representando a letra “i” e um triângulo representando a letra “a”, \nconforme Figura 2. Para impressão das logomarcas , serão utilizadas folhas de 210 mm x 312,5  mm, \nconsiderando um desperdício de exatamente 20%. Partindo desses dados, a quantidade de logomarcas \nque será possível imprimir em cada folha é  \n \n \nFigura 2  \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \nFonte : Elaboração Própria.  \n \n \n"
            ],
            "alternatives": [
                {
                    "alternativa": "13.",
                    "response": False
                },
                {
                    "alternativa": "14.",
                    "response": False
                },
                {
                    "alternativa": "11.",
                    "response": False
                },
                {
                    "alternativa": "12",
                    "response": False
                }
            ],
            "texto": [
                "Figura 2",
                "Figura 2"
            ],
            "figura": ""
        }
    ]
    # gabarito = [
    #   {
    #     "questao": 1,
    #     "resposta": "B"
    #   },
    #   {
    #     "questao": 2,
    #     "resposta": "C"
    #   },
    # {
    #     "questao": 3,
    #     "resposta": "C"
    # },
    # ]
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
            gabarito_copiado = st.text_area('adicionar gabarito aqui, copiar e colar', height=320)
            gabarito_copiado = gabarito_copiado.replace(" ", "").replace("\n", "")
            for indice, caractere in enumerate(gabarito_copiado):
                dados_gabarito.append({'questao': indice+1, 'resposta': caractere})
            # print(gabarito_copiado)
            df = pd.DataFrame(dados_gabarito)
            st.session_state['gabarito_pd'] = dados_gabarito
            df.set_index("questao", inplace =True)

        edited_df = st.data_editor(df, num_rows="dynamic")

    if st.button('Copiar para a área de transferência'):
        df_str = edited_df.to_csv(index=True, sep='\t')
        pyperclip.copy(df_str)
        st.success("Dados copiados para a área de transferência!")

except:
    st.warning('Nenhum gabarito por enquanto')

