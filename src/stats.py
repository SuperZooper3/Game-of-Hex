import matplotlib.pyplot as plt
import numpy as np

def plotCellCount(l):
    step = []
    for i in range(len(l)):
        step.append(i)
    cells = l
    x = np.array(step)
    y = np.array(cells)
    fig = plt.figure(figsize = (5, 5))
    plt.plot(x, y, color ='purple')
    plt.xlabel("Le step")
    plt.ylabel("Le nombre de cellules")
    plt.title("Le nombre de cellules en fonction du step")
    plt.show()

def plotAverageAge(l):
    step = []
    for i in range(len(l)):
        step.append(i)
    averages = l
    x = np.array(step)
    y = np.array(averages)
    fig = plt.figure(figsize = (5, 5))
    plt.plot(x, y, color ='pink')
    plt.xlabel("Le step")
    plt.ylabel("L'age moyen des cellules")
    plt.title("L'age des cellules en fonction du step")
    plt.show()
