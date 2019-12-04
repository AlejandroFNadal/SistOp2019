import sqlite3
from sqlite3 import Error
from Clases.Procesador import *

from crearDB import Presets, Proceso, Particiones
# Este main solo representa una prueba de las clases existentes, no se
# planea implementar de esta forma.
if __name__ == '__main__':
   
    preset=Presets()
    preset.id=1
    preset.descripcion="MV"
    preset.tamMemoria=100
    preset.sistOpMem=10
    preset.fija_variable="variable"
    preset.cant_part=6
    preset.algoritmo_as=2#1 bf,2ff,3wf
    Core = Procesador()
    #Preset de prueba y procesos de prueba
    
    proc1=Proceso()
    proc1.id_proc=1
    proc1.id_batch=1
    proc1.tam_proc=10
    proc1.prioridad=1
    proc1.rafagaCPU= "C1"
    proc1.tiempo_arribo=1

    proc2=Proceso()
    proc2.id_proc=2
    proc2.id_batch=1
    proc2.tam_proc=10
    proc2.prioridad=1
    proc2.rafagaCPU= "C10-E2-C42-C1-E2-C52"
    proc2.tiempo_arribo=4

    proc3=Proceso()
    proc3.id_proc=3
    proc3.id_batch=1
    proc3.tam_proc=10
    proc3.prioridad=2
    proc3.rafagaCPU="C3-E2-C22"
    proc3.tiempo_arribo=3
    
    proc4=Proceso()
    proc4.id_proc=4
    proc4.id_batch=1
    proc4.tam_proc=10
    proc4.prioridad=2
    proc4.rafagaCPU= "C1-E2-C99"
    proc4.tiempo_arribo=4

    part1=Particiones()
    part1.id_part=1
    part1.batch=1
    part1.tam_part=30
    part1.dir_ini=11
    part1.dir_fin=31

    part2=Particiones()
    part2.id_part=2
    part2.batch=2
    part2.tam_part=60
    part2.dir_ini=31
    part2.dir_fin=71
    
    part3=Particiones()
    part3.id_part=3
    part3.batch=2
    part3.tam_part=60
    part3.dir_ini=71
    part3.dir_fin=131
    procesos=[proc1,proc2,proc3]
    particiones=[part1,part2]


    Core.Simular(preset,procesos,particiones,3,2)

    #simular(preset,procesos,particiones,alg_planificacion,quantum)

    #alg_planificacion 
    # 0 = FCFS , 1 = RR , 2 = PRIORIDADES , 3 = MQL , 4 = SJF , 5 = SRTF 

