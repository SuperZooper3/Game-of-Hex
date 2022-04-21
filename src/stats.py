import matplotlib.pyplot as plt
import numpy as np

def plotCellCount(l):
    cells = l
    x = np.array(list(range(len(l))))
    y = np.array(cells)
    plt.plot(x, y, color ='purple')
    plt.xlabel("Le pas")
    plt.ylabel("Le nombre de cellules")
    plt.title("Le nombre de cellules en fonction du pas")
    plt.fill_between(x= x, y1= y, color= "purple",alpha= 0.2)
    plt.show()

def plotAverageAge(l):
    averages = l
    x = np.array(list(range(len(l))))
    y = np.array(averages)
    plt.plot(x, y, color ='darkblue')
    plt.xlabel("Le pas")
    plt.ylabel("L'age moyen des cellules")
    plt.title("L'age moyen des cellules en fonction du pas")
    plt.fill_between(x= x, y1= y, color= "b",alpha= 0.2)

    plt.show()

def plotNewCellCount(l):
    ncc = l
    x = np.array(list(range(len(l))))
    y = np.array(ncc)
    plt.plot(x, y, color ='red')
    plt.xlabel("Le pas")
    plt.ylabel("Le nombre de nouvelles cellules")
    plt.title("Le nombre de nouvelles cellules en fonction du pas")
    plt.fill_between(x= x, y1= y, color= "red",alpha= 0.2)
    plt.show()
