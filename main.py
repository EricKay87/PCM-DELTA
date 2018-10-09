from crearWav import *
from leerWav import retorno
import numpy as np


nombre_archivo = "testOnda1.wav"
sensibilidad = 255


def PCM():
    lista_onda = retorno(nombre_archivo)
    valor_min = (lista_onda.min())
    valor_max = (lista_onda.max())
    lista_onda = lista_onda.tolist()
    diferencia = abs((valor_max - valor_min) / sensibilidad)
    lista_aprox = []
    for x in range(sensibilidad):
        lista_aprox.append(valor_min + (diferencia * x))
    PCM = aproxima(lista_onda, lista_aprox)
    lista_a_csv(PCM,"PCM.csv")
    print("digitalizacion PCM - correcta")
    genera_post_digitalizacion("PCM.csv")
    return PCM


def DELTA():
    lista_onda = retorno(nombre_archivo)
    DELTA_lista=[]
    if lista_onda[0]>0:
        DELTA_lista.append(1)
    for valor in range(1,len(lista_onda)):
        if lista_onda[valor]>lista_onda[valor-1]:
            DELTA_lista.append(1)
        else:
            DELTA_lista.append(0)
    lista_a_csv(DELTA_lista,"DELTA_BIN.csv")
    lista_delta_final=[]
    acumulador=0
    for valor in range(len(DELTA_lista)):
        if DELTA_lista[valor]==1:
            acumulador=acumulador+(1.48/3)
            #con45

        else:
            acumulador = acumulador - (1.48/3)
        lista_delta_final.append(acumulador)
    lista_a_csv(lista_delta_final, "DELTA.csv")
    print("digitalizacion DELTA - correcta")
    genera_post_digitalizacion("DELTA.csv")
    return lista_delta_final






def plot(original,pcm,delta):
    import matplotlib.pyplot as plt
    # LINEAS QUE GENERAN EL GRÁFICO
    # Se genera la recta de la primera onda
    grafico = plt.plot(original, label='ORIGINAL')
    # Se genera la recta de la segunda onda
    grafico2 = plt.plot(pcm, label='PCM')
    # Se genera el gráfico de la onda resultante
    grafico3 = plt.plot(delta, label='DELTA')
    # Se agrega un título al gráfico
    plt.title('Señal mostrada')
    # Se muestra la leyenda para identificar las ondas
    plt.legend()

    plt.show()






def lista_a_csv(lista,nombre_archivo):
    np.savetxt(nombre_archivo, lista, delimiter=",", fmt='%s')

def aproxima(lista_continua, lista_discreta):
    lista_procesada = []
    for num_cont in lista_continua:
        min = 1000
        for num_dis in range(len(lista_discreta)):
            if abs(num_cont - lista_discreta[num_dis]) < min:
                min = abs(num_cont - lista_discreta[num_dis])
                indice = num_dis
        lista_procesada.append(lista_discreta[indice])
    return lista_procesada


plot(retorno(nombre_archivo),PCM(),DELTA())