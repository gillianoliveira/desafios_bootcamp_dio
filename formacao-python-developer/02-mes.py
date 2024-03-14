# -------------------------------------------------------------
#              Mês
#--------------------------------------------------------------

# Desafio 02
# Nível: Básico

'''
DESAFIO:
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

ENTRADA;
A entrada contém um único valor inteiro.


SAÍDA:
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.
'''

month = int(input())

months_dict = {
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}

if month >= 1 and month <= 12:
  print(months_dict[month])
