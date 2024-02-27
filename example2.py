#!/usr/bin/env python3

# Autor: Zamudio Romero Ariel Rodolfo
# email: zamromxd@gmail.com
# GNU/GPL License

import sys

# x0 = 2 # 1) Initial condition
x0 = float(sys.argv[2])
r = float(sys.argv[1])
ran = int(sys.argv[3])
x = x0
print(f"#r={r},x0={x0},x=rx(1-x)")
print("#i\tx_i")
print(f"0\t{x}")
for i in range(ran - 1):  # 2) iterate
    x = r*x*(1-x)  # 3) matematical expression (recursive)
    print(f"{i+1}\t{x}")
