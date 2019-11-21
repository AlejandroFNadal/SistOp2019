import matplotlib.pyplot as plt


class Gantt:

    def gantt(self, cubo):
        #p = procesos[0]
        #p2 = procesos[1]
        # Declaring a figure "gnt" 
        fig, gnt = plt.subplots() 

        # Setting ticks on y-axis 
        gnt.set_yticks([15, 25, 35]) 
        # Labelling tickes of y-axis 
        gnt.set_yticklabels(['1', '2', '3'])

        # Setting labels for x-axis and y-axis 
        gnt.set_xlabel('Tiempo') 
        gnt.set_ylabel('Procesos') 
  
        # Setting Y-axis limits 
        gnt.set_ylim(0, 50) 
  
        # Setting X-axis limits 
        gnt.set_xlim(0, 160) 

        # Setting ticks on y-axis 
        gnt.set_yticks([15, 25, 35])

        # Setting graph attribute 
        gnt.grid(True)

        # Declaring a bar in schedule 
        #gnt.broken_barh([(p.tiempo_arribo, 10)], (30, 9), facecolors =('tab:orange'))
        #gnt.broken_barh([(p.tiempo_arribo+10, 10)], (30, 9), facecolors =('tab:blue'))
        print("hola")
        clk=0
        for i in cubo:
            col =0
            for x in i:
                if x[1]==5: #En estado ejecucion
                    gnt.broken_barh([(clk, 10)], (col+10, 9), facecolors =('tab:orange'))
                elif x[1]==3: #En estado bloqueado
                    gnt.broken_barh([(clk, 10)], (col+10, 9), facecolors =('tab:red'))
                col +=10
            clk +=10
        print("holaaa")
        plt.savefig("D:\Desktop\pyqt\SistOp2019\proc7.png")