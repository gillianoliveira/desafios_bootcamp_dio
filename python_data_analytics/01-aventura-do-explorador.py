# -------------------------------------------------------------
#                     AVENTURA DO EXPLORADOR
#--------------------------------------------------------------

# Desafio 01
# Nível: Básico

'''
# DESAFIO: 
Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes. Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é desvendando seus caminhos por meio de um código em Python. Prepare-se para a "Aventura do Explorador"!

ENTRADA:
Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade de passos que o explorador deve dar na floresta. .


SAÍDA:
O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. Utilize um laço de repetição para simular os passos do explorador. A cada passo, imprima uma mensagem informando a distância percorrida até o momento.


EXEMPLOS:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada    Saída
2          Explorador: 1 passo
           Explorador: 2 passos
           
3          Explorador: 1 passo
           Explorador: 2 passos

0          Nenhum passo dado na floresta.
'''

# SOLUÇÂO

quantidade_de_passos = int(input())

if quantidade_de_passos > 0:
    palavra_passos = ""
    for i in range(quantidade_de_passos):
        i += 1
        if i == 1:
            print(f"Explorador: {i} passo")
        else:
            print(f"Explorador: {i} passos")
else:
    print("Nenhum passo dado na floresta.")