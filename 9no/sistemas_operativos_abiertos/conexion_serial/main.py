from juego import Juego
import sys
try:
    import serial  # Python2
except ImportError:
    from serial3 import *  # Python3

entrada = sys.argv
jugador = str(entrada[1])
puerto = str(entrada[2])
conexion = serial.Serial(puerto, 38400, timeout=1)
numero = int(entrada[3])

juego = Juego(jugador, conexion, numero)