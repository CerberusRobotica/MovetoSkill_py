import numpy as np


def calcularvetor(xf, yf, x0, y0):
    vet = np.array([xf - x0, yf - y0])
    return vet


def calculardist(xf, yf, x0, y0, xr, yr):
    a = 0
    if xf != x0:
        a = (yf - y0) / (xf - x0)
    b = -1
    c = y0 - x0 * a
    d = abs(a * xr + b * yr + c) / np.sqrt(a ** 2 + b ** 2)
    return d


def calcularnovovetor(x0, y0, xr, yr, beta, inv):
    v = np.array([xr - x0, yr - y0])
    knorm = np.sqrt(np.linalg.norm(v)**2 - beta**2)
    theta = np.arctan((yr-y0)/(xr-x0)) + inv*(np.arctan(beta/knorm) + 0.00000000000001)
    vet = np.array([knorm * np.cos(theta), knorm * np.sin(theta)])
    print(vet)
    print((knorm*np.sin(theta))/(knorm*np.cos(theta)))
    return vet


def projort(u, v):
    v1 = (np.dot(v, u) / (np.linalg.norm(u)) ** 2) * u
    return v1


def normalizar(alpha, vet):
    vet = alpha * vet / np.linalg.norm(vet)
    return vet

def angulovetores(u, v):
    return np.acos(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v)))