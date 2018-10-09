amplitud = 16000
def retorno(nombreArchivo):
    import wave
    import struct
    import numpy as np


    # Amplitud

    archivoEntrada = wave.open(nombreArchivo, 'r')
    # Se obtiene el número de muestras del archivo
    frames = archivoEntrada.getnframes()
    # Se leen las muestras
    data = archivoEntrada.readframes(frames)
    # Se cierra el archivo
    archivoEntrada.close()
    # Se descomprimen los datos de hexadecimal a numérico
    data = struct.unpack('{n}h'.format(n=frames), data)
    # Se convierten los datos de una lista de python a un
    # arreglo de numpy
    data = np.array(data)
    # Se divide por el valor de amplitud para obtener las señales originales
    data = data / amplitud
    return data

def plot():
    nombreArchivo = 'testOnda1.wav'

    archivoEntrada = wave.open(nombreArchivo, 'r')
    # Se obtiene el número de muestras del archivo
    frames = archivoEntrada.getnframes()
    # Se leen las muestras
    data = archivoEntrada.readframes(frames)
    # Se cierra el archivo
    archivoEntrada.close()
    # Se descomprimen los datos de hexadecimal a numérico
    data = struct.unpack('{n}h'.format(n=frames), data)
    # Se convierten los datos de una lista de python a un
    # arreglo de numpy
    data = np.array(data)
    # Se divide por el valor de amplitud para obtener las señales originales
    data = data / amplitud
    # Se grafica la onda resultante
    grafico = plt.plot(data, label='data')
    # Se agrega un título al gráfico
    plt.title('Señal mostrada')
    # Se muestra la leyenda del gráfico
    plt.legend()
    # Se agrega el gráfico
    plt.show()

