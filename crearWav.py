import numpy as np
# Se importa para generar el archivo de audio
import wave
# Se importa struct para empaquetar los valores de las muestras en hexadecimal
import struct

# Número de muestras tomadas
numeroDeMuestras = 48000
tasaDeMuestreo = 48000.0
amplitud = 16000
comptype = 'NONE'
compname = 'not compressed'
nchannels = 1
sampwidth = 2
nframes = numeroDeMuestras

def generar_archivo(salida):


    # Frencuencias
    frecuencia = 200
    frecuencia2 = 4000
    # Nombre del archivo
    salida = 'testOnda1.wav'
    # Ecuaciones
    # Se genera un vector con el valor del la ecuación del seno, para cada muestra
    # Se elimina el valor de amplitud del cálculo para añadir la amplitud a la onda resultante
    onda = [np.sin(2 * np.pi * frecuencia * x/tasaDeMuestreo) for x in range(numeroDeMuestras)]
    onda2 = [0.5 * np.sin(2 * np.pi * frecuencia2 * x/tasaDeMuestreo) for x in range(numeroDeMuestras)]
    # Se suman las dos ondas para generar la señal compuesta
    onda3 = np.array(onda) + np.array(onda2)

    # LINEAS QUE GENERAN EL WAV
    archivoSalida = wave.open(salida, 'w')
    # Se configuran los parámetros del archivo a escribir
    archivoSalida.setparams((nchannels, sampwidth, int(tasaDeMuestreo), nframes, comptype, compname))

    # Se escribe cada muestra de la onda3 en el archivo de salida
    for muestra in onda3 :
        archivoSalida.writeframes(struct.pack('h', int(muestra * amplitud)))
    # Se cierra el archivo de salida
    archivoSalida.close()

def genera_post_digitalizacion(csv):
    from numpy import genfromtxt
    array_csv = genfromtxt(csv, delimiter=',')
    # Se determina el tipo y nombre de la compresión
    # el número de canales y el ancho de muestras

    # Se abre el archivo en modo de escritura
    archivoSalida = wave.open(csv+".wav", 'w')
    # Se configuran los parámetros del archivo a escribir
    archivoSalida.setparams((nchannels, sampwidth, int(tasaDeMuestreo), nframes, comptype, compname))
    for muestra in array_csv :
        archivoSalida.writeframes(struct.pack('h', int(muestra * amplitud)))
    archivoSalida.close()
