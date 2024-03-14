# -------------------------------------------------------------
#              Tuitando
#--------------------------------------------------------------

# Desafio 01
# Nível: Básico


'''
DESAFIO:
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

ENTRADA:
A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

SAÍDA:
A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

'''
T = input()

entrada = len(T)
  
if entrada > 140:
  print("MUTE")
else:
  print("TWEET")
