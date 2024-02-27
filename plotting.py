#!/usr/bin/env python3

# Autor: Zamudio Romero Ariel Rodolfo
# email: zamromxd@gmail.com
# GNU/GPL License

import matplotlib.pyplot as plt

def dynamicPlot(ax,filename):
    with open(filename) as f:
        data = f.readlines()
    I = []
    X = []
    label,_ = ((data[0])[1:]).split(',')
    for line in data:
        if "#" not in line[0]:
            i, x = map(float, line.split())
            I.append(i)
            X.append(x)
    ax.plot(I, X, label=label)

# fig = plt.figure()
fig,ax = plt.subplots()
dynamicPlot(ax,'data1.dat')
dynamicPlot(ax, "data2.dat")
dynamicPlot(ax, "data0.dat")
plt.legend()
plt.show()
