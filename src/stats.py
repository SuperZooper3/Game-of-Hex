import matplotlib.pyplot as plt

def plotCellCount(l):
    step = []
    for i in range(len(l)):
        step.append(i)
    cells = l
    fig = plt.figure(figsize = (5, 5))
    plt.plot(step, cells, color ='purple', width = 0.4)
    plt.xlabel("Le step")
    plt.ylabel("Le nombre de cellules")
    plt.title("Le nombre de cellules en fonction du step")
    plt.show()

def plotAverageAge(l):
    step = []
    for i in range(len(l)):
        step.append(i)
    averages = l
    fig = plt.figure(figsize = (5, 5))
    plt.bar(step, averages, color ='pink', width = 0.4)
    plt.xlabel("Le step")
    plt.ylabel("L'age moyen des cellules")
    plt.title("L'age des cellules en fonction du step")
    plt.show()
