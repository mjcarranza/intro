#1
def combinaciones(lista1, lista2):
    if isinstance(lista1, list) and isinstance(lista2, list):
        return combinaciones_aux1(lista1, lista2)
    else: return "Error"

def combinaciones_aux1(lista1, lista2):
    if lista2 == []:
        return [] + combinaciones_aux2(lista1[1:], lista2)
    else: return ([lista1[0] * lista2[0]] + combinaciones_aux(lista1,
                                                              lista2[1:]))
def combinaciones_aux2(lista1, lista2):
    if lista2 == []:
        return [] + combinaciones_aux3(lista1[1:], lista2)
    else: return ([lista1[0] * lista2[0]] + combinaciones_aux2(lista1,
                                                               lista2[1:]))
def combinaciones_aux3(lista1, lista2):
    if lista2 == []:
        return []
    else: return[lista1[0] * lista2[0]] + combinaciones_aux3(lista1, lista2[1:])

#2

import math
def std(lista, avg):
    if isinstance(lista, list) and isinstance(avg, list):
        return std_aux(lista, avg)
    else: return "Error"

def std_aux(lista, avg):
    if lista == []:
        return 0
    else:
        return((math.sqrt(lista[0] - avg[0] / len(lista) - 1)) +
               std_aux(lista[1:], avg[1:]))


#3

def zScore(listaX, S, avg):
    if isinstance(listaX, list):
        return zScore_aux(listaX, S, avg)
    else: return "Error"

def zScore_aux(listaX, S, avg):
    if listaX == []:
        return []
    else:
        return [(listaX[0] - avg) / S] + zScore_aux(listaX[1:], S, avg)

#4

def rScore(Zx, Zy):
    if isinstance(Zx, list) and isinstance(Zy, list):
        return rScore_aux(Zx, Zy)
    else: return "Error"

def rScore_aux(Zx, Zy):
    if Zx == [] and Zy == []:
        return 0
    else:
        return (((Zx[0] * Zy[0]) / len(Zy) - 1) +
                rScore_aux(Zx[1:], Zy[1:]))
