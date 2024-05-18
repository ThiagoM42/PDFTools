import re

# Padrão regex para capturar uma questão objetiva com 5 alternativas
# padrao_regex = r'\b\d+\.\s.*?(?:\n[A-E]\..*?)+'
padrao_regex = r'\d+\..+?\(A\).+?\(B\).+?\(C\).+?\(D\).+?\(E\)'

# Exemplo de texto de um PDF contendo uma questão objetiva com 5 alternativas
texto_pdf = """
1. Qual é a capital do Brasil?
   A. Rio de Janeiro
   B. São Paulo
   C. Brasília
   D. Belo Horizonte
   E. Salvador
2. Quem escreveu a peça "Hamlet"?
   A. William Shakespeare
   B. Miguel de Cervantes
   C. Charles Dickens
   D. Jane Austen
   E. Oscar Wilde
"""

# Encontrar todas as questões objetivas com 5 alternativas no texto do PDF
matches = re.findall(padrao_regex, texto_pdf)

# Imprimir as correspondências encontradas
for match in matches:
    print(match)