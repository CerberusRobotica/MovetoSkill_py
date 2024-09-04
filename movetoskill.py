import numpy as np

import VetOp
import testecolisao
from VetOp import calcularvetor


def skill(x0, y0, xf, yf, pos, beta, alpha):
    vet = VetOp.calcularvetor(xf, yf, x0, y0)
    if testarcolisoes(x0, y0, vet, pos, beta):
        vet = pathfinding(x0, y0, xf, yf, pos, beta)
    vet = VetOp.normalizar(alpha, vet)
    return vet



def pathfinding(x0, y0, xf, yf, pos, beta):
    vetores = []
    print(vetores)
    for i in range(int(len(pos)/2)):
        xr = pos.get("xr" + str(i))
        yr = pos.get("yr" + str(i))
        vet = VetOp.calcularnovovetor(x0, y0, xr, yr, beta, 1)
        if not testarcolisoes(x0, y0, vet, pos, beta):
            vetores.append(vet)
    for i in range(int(len(pos)/2)):
        xr = pos.get("xr" + str(i))
        yr = pos.get("yr" + str(i))
        vet = VetOp.calcularnovovetor(x0, y0, xr, yr, beta, -1)
        if not testarcolisoes(x0, y0, vet, pos, beta):
            vetores.append(vet)
    vet = calcularvetor(xf, yf, x0, y0)
    angulosvet = []
    for i in range(0, len(vetores)):
        angulosvet.append(VetOp.angulovetores(vetores[i], vet))
    j = 0
    for i in range(1, len(vetores)):
        if abs(angulosvet[i]) < abs(angulosvet[j]):
            j = i
    vet = vetores[j]

    return vet


def testarcolisoes(x0, y0, vet, pos, beta):
    for i in range(0, int(len(pos)/2)):
        xr = pos.get("xr" + str(i))
        yr = pos.get("yr" + str(i))
        if testecolisao.teste(vet, x0, y0, xr, yr, beta):
            return 1
    return 0



