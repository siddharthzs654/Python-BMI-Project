from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt

def graphs(h, w):
    #Creating Coordinates For Graoh
    allheight=[0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.25]



    underweight=[]
    for i in range(0,len(allheight)):
        temp=(18.5)*allheight[i]*allheight[i]
        underweight.append(round(temp,2))


    normalweight=[]
    for i in range(0,len(allheight)):
        temp=(24.5)*allheight[i]*allheight[i]
        normalweight.append(round(temp,2))



    overweight=[]
    for i in range(0,len(allheight)):
        temp=(29.9)*allheight[i]*allheight[i]
        overweight.append(round(temp,2)) 



    obese=[]
    for i in range(0,len(allheight)):
        temp=(40)*allheight[i]*allheight[i]
        obese.append(round(temp,2))



    #Plotting Graph
    plt.plot([],[],color='g',label='Underweight',linewidth=5)
    plt.plot([],[],color='c',label='Normal',linewidth=5)
    plt.plot([],[],color='r',label='Overweight',linewidth=5)
    plt.plot([],[],color='b',label='Obesity',linewidth=5)
    plt.plot([],[],color='k',label='Your Health',linewidth=5)
    plt.stackplot(allheight,underweight,normalweight,overweight,obese,colors=['g','c','r','b'])
    plt.legend()
    plt.grid()
    plt.xlabel('Height(m)')
    plt.ylabel('Weight(Kg)')
    plt.scatter(h,w,color='k')
    
    plt.savefig('data.png')
