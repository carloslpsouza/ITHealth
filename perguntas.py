from random import randint, sample
import os

global bloco_pergunta, resposta, qtds_perguntas, qtds_linhas, aleatorio

def selecionaQuestao(bloco):
    global bloco_pergunta, resposta
    f = open('perguntas', 'r')
    bloco_pergunta = f.readlines()
    pergunta = bloco_pergunta[bloco]
    opc_a = bloco_pergunta[bloco + 1]
    opc_b = bloco_pergunta[bloco + 2]
    opc_c = bloco_pergunta[bloco + 3]
    opc_d = bloco_pergunta[bloco + 4]
    complexidade = bloco_pergunta[bloco + 5]
    resposta = bloco_pergunta[bloco + 6]
    return pergunta[:-1], opc_a[:-1], opc_b[:-1], opc_c[:-1], opc_d[:-1], complexidade[:-1], resposta[:-1]

    f.close()

def aleatorio():
    global qtds_perguntas, qtds_linhas, aleatorio
    f = open('perguntas', 'r')
    qtds_linhas = len(f.readlines())
    qtds_perguntas = int(qtds_linhas/7)
    f.close()
    aleatorio = []
    for i in range(qtds_perguntas):
      n = 0
      while (n in aleatorio):
        n = randint(0,qtds_perguntas-1)
      aleatorio.append(n)
    return aleatorio