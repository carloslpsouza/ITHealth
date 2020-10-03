import time
import threading

global segundos
global minutos
global horas
segundos = 0
minutos = 0
horas = 0

def crono():
    global segundos
    global minutos
    global horas
    segundos = int(segundos)
    minutos = int(minutos)
    horas = int(horas)
    if segundos == 59:
        segundos = -1
        minutos += 1
        if minutos == 59:
            minutos = -1
            horas += 1
        return crono()
    else:
        segundos += 1
        time.sleep(1)
        return crono()

tempo_corrido = threading.Thread(target=crono, args=())
tempo_corrido.start()

def tempoCorrido():
    tempo = str("Tempo:  {:02d}:{:02d}:{:02d}".format(horas, minutos, segundos))
    return tempo

