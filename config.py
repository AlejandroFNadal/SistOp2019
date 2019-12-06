import os
import sys
# Devuelve la direccion completa donde se encuentra el main.py 
BASE_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

FILE_GANTT = os.path.join(BASE_PATH, 'apps', 'windows', 'Gantt.png')
FILE_MAPA = os.path.join(BASE_PATH, 'apps', 'windows', 'Mapa', 'Mapa')
FILE_TR = os.path.join(BASE_PATH, 'apps', 'windows', 'Tiempo_Retorno.png')
FILE_TE = os.path.join(BASE_PATH, 'apps', 'windows', 'Tiempo_espera.png')