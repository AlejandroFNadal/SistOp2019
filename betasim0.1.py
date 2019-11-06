import sqlite3
from sqlite3 import Error
from Clases.Procesador import *

from crearDB import Presets, Proceso
# Este main solo representa una prueba de las clases existentes, no se
# planea implementar de esta forma.
if __name__ == '__main__':
   
    preset=Presets()
    preset.id=1
    preset.descripcion="Ej1"
    preset.tamMemoria=150
    preset.sistOpMem=10
    preset.fija_variable="variable"
    preset.cant_part=5
    preset.algoritmo_as=2
    Core = Procesador()
    #Preset de prueba y procesos de prueba
    
    proc1=Proceso()
    proc1.id_proc=1
    proc1.id_batch=1
    proc1.tam_proc=40
    proc1.prioridad=2
    proc1.rafagaCPU="E1-S1-C2"
    proc1.tiempo_arribo=3

    proc2=Proceso()
    proc2.id_proc=2
    proc2.id_batch=1
    proc2.tam_proc=30
    proc2.prioridad=3
    proc2.rafagaCPU="E2-C3"
    proc2.tiempo_arribo=2

    proc3=Proceso()
    proc3.id_proc=3
    proc3.id_batch=1
    proc3.tam_proc=20
    proc3.prioridad=3
    proc3.rafagaCPU="E4-C5"
    proc3.tiempo_arribo=1
    
    procesos=[proc1,proc2,proc3]
    particiones=[]

    Core.Simular(preset,procesos,particiones)
