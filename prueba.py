#!/usr/bin/env python3

# Autor: Zamudio Romero Ariel Rodolfo
# email: zamromxd@gmail.com
# GNU/GPL License

import matplotlib.pyplot as plt
import sys


def dynamicPlot(ax, filename, fila, columna):
    with open(filename) as f:
        data = f.readlines()
    I = []
    X = []
    labelr, labelx0, _ = ((data[0])[1:]).split(",")
    for line in data:
        if "#" not in line[0]:
            i, x = map(float, line.split())
            I.append(i)
            X.append(x)
    ax[fila, columna].plot(I, X)
    ax[fila, columna].scatter(I, X, marker="o")
    ax[fila, columna].set_title(labelr + "," + labelx0)


fig, ax = plt.subplots(2, 2)
fila, columna = 0, 0
for arg in sys.argv[1:]:
    dynamicPlot(ax, arg, fila, columna)
    fila += 1
    if fila == 2:
        columna += 1
        fila = 0
plt.xlabel("Time")
plt.ylabel("x")
fig.set_facecolor("lightsteelblue")
plt.grid()
plt.show()
