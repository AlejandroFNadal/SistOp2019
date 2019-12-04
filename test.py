import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

"""
plt.axis([0, 10, 0, 1])

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(1)
"""

# Declaring a figure "gnt" 
fig, gnt = plt.subplots() 


# Setting Y-axis limits 
gnt.set_ylim(0, 50) 
  
# Setting X-axis limits 
gnt.set_xlim(0, 160) 

# Setting labels for x-axis and y-axis 
gnt.set_xlabel('TIEMPO') 
gnt.set_ylabel('procesos') 

# Setting ticks on y-axis 
gnt.set_yticks([15]) 
# Labelling tickes of y-axis 
gnt.set_yticklabels(['p'])

# Setting graph attribute 
gnt.grid(True) 

ALT = (15, 9)

PROCESOS = [
    {'descripcion': 'SO',
     'tamanios':[(0, 10)],
     'altura': ALT,
     'color': ('tab:red'), },
    
    {'descripcion': 'P1','tamanios':[(10, 25)],
     'altura': ALT,
     'color': ('tab:blue'), },
    
    {'descripcion': 'P2','tamanios':[(35, 5)],
     'altura': ALT,
     'color': '#0f0f0f', },
    
    
    {'descripcion': 'P3','tamanios':[(40, 10)],
     'altura': ALT,
     'color': '#0f0f0f', },

    {'descripcion': 'P1','tamanios':[(50, 25)],
     'altura': ALT,
     'color': '#0f0f0f', },
]

mod = 10%10
print("modulo = "+str(mod))


leyenda = []
for proceso in PROCESOS:
    gnt.broken_barh(proceso['tamanios'], proceso['altura'], color=proceso['color']) 
    leyenda.append(mpatches.Patch(color=proceso['color'], label=proceso['descripcion']))
    #plt.pause(1.5)

plt.legend(handles=leyenda)


plt.show()