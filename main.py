import movetoskill
import numpy as np

x0 = 0
y0 = 0
xf = 30
yf = 30
alpha = 1
beta = 1
pos = {"xr0": 0}
for i in range(0, 5):
    pos["xr" + str(i)] = 10
    pos["yr" + str(i)] = 10 + 2*i


print(pos)
print(movetoskill.skill(x0, y0, xf, yf, pos, beta, alpha))
