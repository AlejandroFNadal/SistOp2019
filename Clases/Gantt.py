import matplotlib.pyplot as plt


class Gantt:

    def gantt(self, cubo, procesos):
        #p = procesos[0]
        #p2 = procesos[1]
        # Declaring a figure "gnt" 
        fig, gnt = plt.subplots() 

        
        # Setting labels for x-axis and y-axis 
        gnt.set_xlabel('Tiempo') 
        gnt.set_ylabel('Procesos') 
  
        # Setting Y-axis limits 
        gnt.set_ylim(0, 80) 
  
        # Setting X-axis limits 
        gnt.set_xlim(0, 160) 

<<<<<<< HEAD
=======
        # Setting ticks on y-axis 
        gnt.set_yticks([15, 25, 35])
         
>>>>>>> master

        # Setting graph attribute 
        gnt.grid(True)

        # Declaring a bar in schedule 
        #gnt.broken_barh([(p.tiempo_arribo, 10)], (30, 9), facecolors =('tab:orange'))
        #gnt.broken_barh([(p.tiempo_arribo+10, 10)], (30, 9), facecolors =('tab:blue'))
        print("hola")
        eje_x = []

        clk=0
        e_x =0
        e_y =1
        y= 10
        eje_x= []
        eje_x_labels = []
        eje_y= []
        eje_y_labels = []
        for i in cubo:
            col =0
<<<<<<< HEAD
            
            eje_x_labels.append(str(e_x))
            eje_x.append(clk)
            #eje_y_labels.append(str(e_y))
            eje_y.append(y)
=======
            eje_x.append(str(clk))
            
>>>>>>> master
            for x in i:
                
                if x[1]==5: #En estado ejecucion
                    gnt.broken_barh([(clk, 10)], (col, 10), facecolors =('tab:orange'))
                elif x[1]==3: #En estado bloqueado
                    gnt.broken_barh([(clk, 10)], (col, 10), facecolors =('tab:red'))
                col +=10
                #e_y +=1
                
          
            clk +=10
            e_x +=1
            y +=10
        
        for i in procesos:
            print("Proceso numero: "+ str(e_y))
            eje_y_labels.append(str(e_y))
            e_y +=1    
          
        # Setting ticks on x-axis 
        gnt.set_xticks(eje_x)
        gnt.set_xticklabels(eje_x_labels)

        # Setting ticks on y-axis 
        gnt.set_yticks(eje_y) 
        # Labelling tickes of y-axis 
        gnt.set_yticklabels(eje_y_labels)


        print("holaaa")
<<<<<<< HEAD
        plt.savefig("C:\SistOperativo\SistOp2019\proc7.png")
=======
        #gnt.set_xticklabels(eje_x)
        plt.savefig("D:\Desktop\pyqt\SistOp2019\proc8.png")
>>>>>>> master
