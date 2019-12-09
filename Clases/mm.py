def multinivel(self,procesador,quantum):
    # se carga el proceso actual del procesador
        aux = procesador.get_proceso_actual()
        if procesador.cola1 != []:
            # Se utiliza la cola 1
            procesador.set_estadoMLQ(1)
            # Se borra la lista original
            self.purge_list()
            # se carga cola1 en cola de listos
            for x in procesador.cola1:
                self.cola_listos.append(x)
            #Se pasa a round robin con quantum 5
            self.round_robin(procesador,5)
            return self.cola_listos
        else:
            if procesador.cola2 != []: #rr 2
                #indica el numero de cola que se esta usando
                procesador.set_estadoMLQ(2) 
                self.purge_list()
                for x in procesador.cola2:
                    self.cola_listos.append(x)
                # Se llama a Round Robin y se pasa un quantum 3
                self.round_robin(procesador,3)
            else:
                if procesador.cola3!=[]:
                    # se utiliza la cola 3
                    procesador.set_estadoMLQ(3)
                    self.purge_list()
                    for x in procesador.cola3:
                        self.cola_listos.append(x)
                    # se utiliza la ultima cola por
                    #  lo tanto se llama a FCFS
                    self.fcfs(procesador)
                

