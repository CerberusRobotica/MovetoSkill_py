import numpy as np
import VetOp


def teste(vet, x0, y0, xr, yr, beta):
    xf, yf = vet + np.array([x0, y0])
    if VetOp.calculardist(xf, yf, x0, y0, xr, yr) >= beta:
        return 0
    v = np.array([xr - x0, yr - y0])
    v1 = VetOp.projort(vet, v)
    r = np.linalg.norm(v - v1)
    w = np.sqrt(np.abs(beta ** 2 - r ** 2))
    if np.linalg.norm(v1) > np.linalg.norm(vet) + w:
        return 0
    else:
        return 1
