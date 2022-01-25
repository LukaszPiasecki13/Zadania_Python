from threading import Thread
import time
import numpy as np
import matplotlib.pyplot as plt


def histogram1():
    global x1
    x1 = np.random.normal(size=1000000)

def histogram2():
    global x2
    x2 = np.random.normal(size=1000000)
def histogram3():
    global x3
    x3 = np.random.normal(size=1000000)
def histogram4():
    global x4
    x4 = np.random.normal(size=1000000)
def plot():
    plt.subplot(2, 2, 1)
    plt.hist(x1, color="k")
    plt.subplot(2, 2, 2)
    plt.hist(x2, color="r")
    plt.subplot(2, 2, 3)
    plt.hist(x3, color="g")
    plt.subplot(2, 2, 4)
    plt.hist(x4, color="y")

    plt.draw()
    plt.show()



hist1 = Thread(target=histogram1)
hist1.start()
print("histogram 1 zostal uruchomiony \n")
hist2 = Thread(target=histogram2)
hist2.start()
print("histogram 2 zostal uruchomiony \n")
hist3 = Thread(target=histogram3)
hist3.start()
print("histogram 3 zostal uruchomiony \n")
hist4 = Thread(target=histogram4)
hist4.start()
print("histogram 4 zostal uruchomiony \n")

print("plot zostal uruchomiony\n")
plot = Thread(target=plot)
plot.start()


