#-------------------------------------
# Dragão
# Desafios Intermediários Formação Python Developer
# Desafio 1 de 3
# Realizado em: 15-05-2024


# Desafio
# Daenerys é a khaleesi dos Dothraki. Juntamente com Drogon, eles vão atrás do Tyrion, para tentar dominar Westeros. Ela possui, além do seu dragãozinho, um rastreador que mede o nível de energia de qualquer ser vivo. Todos os seres com o nível menor ou igual a 8000, ela considera como se fosse um inseto. Quando passa deste valor, que foi o caso do Drogon, ela se espanta e grita “Mais de 8000”. Baseado nisso, utilize a mesma tecnologia e analise o nível de energia dos seres vivos.

# Entrada
# A primeira linha contém um número inteiro C relativo ao número de casos de teste. Em seguida, haverá C linhas, com um número inteiro N (100 <= N <= 100000) relativo ao nível de energia de um ser vivo.

# Saída
# Para cada valor lido, imprima o texto correspondente.


C = int(input())
niveis_de_energia = []

for i in range (C):
    nivel_energia = int(input())
    niveis_de_energia.append(nivel_energia)
  
for i in niveis_de_energia:
    if i > 8000:
        print('Mais de 8000!')
    else:
        print('Inseto!')
  