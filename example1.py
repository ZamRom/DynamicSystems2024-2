#!/usr/bin/env python3

# Autor: Zamudio Romero Ariel Rodolfo
# email: zamromxd@gmail.com
# GNU/GPL License

import sys

#x0 = 2 # 1) Initial condition
x0 = float(sys.argv[1])
x = x0
print(f'#x0={x0},x=x+1')
print('#i\tx_i')
print(f'0\t{x}')
for i in range(100-1): #2) iterate
    x = x + 1.0  # 3) matematical expression (recursive)
    print(f"{i+1}\t{x}")