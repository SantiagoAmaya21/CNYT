import math


def sumaCplx(c1, c2):
    return (c1[0] + c2[0] , c1[1] + c2[1])


def restaCplx(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])


def multiplicarCplx(c1=[], c2=[]):
    return (c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c2[0] * c1[1])


def dividirCplx(c1, c2):
    denominador = (c2[0] ** 2) + (c2[1] ** 2)
    return (((c1[0] * c2[0]) + (c1[1] * c2[1])) / denominador, ((c2[0] * c1[1]) - (c1[0] * c2[1])) / denominador)


def moduloCplx(c):
    magnitud = round(math.sqrt((c[0] ** 2) + (c[1] ** 2)), 4)
    return magnitud


def conjugadoCplx(c):
    return (c[0], -c[1])


def convertirCoordenadas(c, modelo=""):
    if modelo.lower() == "cartesiano":
        return (c[0] * math.cos(c[1]), c[0] * math.sin(c[1]))
    elif modelo.lower() == "polar":
        rho = moduloCplx(c)
        theta = calcularFaseCplx(c)
        return (rho, theta)
    raise Exception("Solo se pueden hacer conversiones a polar o cartesiano!")


def calcularFaseCplx(c):
    return round(math.atan2(c[1], c[0]), 4)



