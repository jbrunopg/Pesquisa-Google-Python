from googlesearch import *
from googlesearch import search


#Texto da pesquisa

query = 'Python'

#Resultado da busca e a lista com os resultados

result = list(search(query, lang='pt-br', num_results=5))

# Resultado Buscas

print(result)