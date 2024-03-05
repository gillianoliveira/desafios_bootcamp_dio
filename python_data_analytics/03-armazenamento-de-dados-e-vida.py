# -------------------------------------------------------------
#              Armazenamento de Dados é Vida
#--------------------------------------------------------------

# Desafio 03
# Nível: Básico

'''
DESCRIÇÃO:

Com as máquinas pesadas agrupadas estrategicamente, graças ao seu algoritmo de cálculo energético, agora a mineração está muito mais eficiente! 
Com isso, os CodeMiners logo terão que aumentar a capacidade de armazenamento de dados em seus discos de Mithril. 
Atualmente, cada máquina tem uma capacidade em teraflops e todas terão um upgrade! 
Escreva um programa que calcule a nova capacidade total de todas as máquinas após um aumento percentual específico.

ENTRADA

Dois valores inteiros positivos, representando a capacidade atual total em teraflops e o aumento percentual, separados por espaço.

SAÍDA:
A nova capacidade total em teraflops.

EXEMPLOS:

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.


| Entrada   | Saída    |
| 100 20    | 120      |
| 50 10     | 55       |
| 200 50    | 300      |

'''
# TODO: Calcule a nova capacidade do disco de Mithril
#TODO: Imprima a nova capacidade


capacidade_atual, aumento_percentual = map(int, input().split())
nova_capacidade = int(capacidade_atual + (capacidade_atual * (aumento_percentual/100)))
print(nova_capacidade)
