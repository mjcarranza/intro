#tarea busqueda binaria

class buscar(object):
    def __init__(self):
        pass
    def busqueda(self, num, lista):
        if isinstance(num, int) and isinstance(lista, list):
            return self.busqueda_aux(num, lista, len(lista)//2, len(lista))
        else: return "error"
    def busqueda_aux(self, num, lista, indice, n):
        if len(lista) < indice:
            return -1
        elif lista[indice] == num:
            return indice
        elif lista[indice]  > num:
            return self.busqueda_aux(num, lista, n//2 , indice)
        else: return self.busqueda_aux(num, lista, n - indice,  indice + n // 2)


lista=[1,2,3,4,5,6,7]
num=6
s=buscar()
print(s.busqueda(num, lista))
