import Clases.Procesador
import Clases.Procesos

cola1=[]
cola2=[]
cola3=[]

Core2= Procesador()

preset=Presets()
    preset.id=1
    preset.descripcion="Ej1"
    preset.tamMemoria=140
    preset.sistOpMem=10
    preset.fija_variable="variable"
    preset.cant_part=5
    preset.algoritmo_as=2#1 bf,2ff,3wf

    proc1=Proceso()
    proc1.id_proc=1
    proc1.id_batch=1
    proc1.tam_proc=10
    proc1.prioridad=2
    proc1.rafagaCPU="C1-E1-C2"
    proc1.tiempo_arribo=1

    proc2=Proceso()
    proc2.id_proc=2
    proc2.id_batch=1
    proc2.tam_proc=20
    proc2.prioridad=3
    proc2.rafagaCPU="C2-E2-C7"
    proc2.tiempo_arribo=2

    proc3=Proceso()
    proc3.id_proc=3
    proc3.id_batch=1
    proc3.tam_proc=50
    proc3.prioridad=3
    proc3.rafagaCPU="C1-E5-C9"
    proc3.tiempo_arribo=3
    
    proc4=Proceso()
    proc4.id_proc=4
    proc4.id_batch=1
    proc4.tam_proc=25
    proc4.prioridad=3
    proc4.rafagaCPU="C5"
    proc4.tiempo_arribo=5