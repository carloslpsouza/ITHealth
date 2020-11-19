import os

def leRanking():
    f = open('ranking', 'r')
    ranking = f.readlines()
    f.close()
    return ranking
    #print(ranking)

def atualizaRanking(nomeJogador, tempo, pontos):
    pontos = int(pontos)
    f = open('ranking', 'r')
    ranking = f.readlines()
    f.close()
    #print(ranking)
    for i in range(3):
        indice = (i * 3)
        pts = ranking[indice]
        pts = int(pts[:-1])

        if pontos >= pts:
            ranking.insert(indice, str(pontos)+'\n')
            ranking.insert(indice+1, str(nomeJogador)+'\n')
            ranking.insert(indice+2, str(tempo)+'\n')
            break
    if len(ranking) > 9:
        ranking.pop(9)
        ranking.pop(10)
        ranking.pop()

    os.remove('ranking')
    f = open('ranking', 'x')
    f = open('ranking', 'a')
    for i in range(9):
        f.write(str(ranking[i]))

    f.close()

    #print(ranking)

leRanking()