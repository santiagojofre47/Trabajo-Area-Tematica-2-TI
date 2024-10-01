from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Arbol import Nodo

class Nodo:
    id: int
    char: str
    valor: int
    izq: Nodo
    der: Nodo
    def __init__(self, id: int, caracter:str):
        self.id = id
        self.char = caracter
        if caracter == "nuevo":
            self.valor = 0
        else:
            self.valor = 1
        self.izq = None
        self.der = None
    
    def agregar(self, caracter:str):
        if caracter == self.char:
            self.valor += 1
            return True
        elif self.char == "":
            if self.izq.agregar(caracter):
                self.valor += 1
                return True
            elif self.der.agregar(caracter):
                self.valor += 1
                return True
        else:
            return False
    
    def listar(self, lista:list[tuple[Nodo,str]], camino:str):
        for indice, elemento in enumerate(lista):
            if len(elemento[1]) < len(camino) or (len(elemento[1]) == len(camino) and elemento[1] > camino):
                lista.insert(indice, (self, camino))
                if self.char == "":
                    self.izq.listar(lista, camino + "0")
                    self.der.listar(lista, camino + "1")
                break
        else:
            lista.append((self, camino))
            if self.char == "":
                self.izq.listar(lista, camino + "0")
                self.der.listar(lista, camino + "1")
        cadena = ""
        for nodo, camino in lista:
            cadena += f"{nodo.char}, {nodo.valor}, {camino} | "
            # print(cadena)
    

    def arreglar_contadores(self):
        if self.char != "":
            return self.valor
        else:
            self.valor = self.izq.arreglar_contadores() + self.der.arreglar_contadores()
            return self.valor
    

    def get_codigo(self, char:str) -> str | None:
        if self.char == char:
            return ""
        elif self.char == "":
            cod_izq = self.izq.get_codigo(char)
            cod_der = self.der.get_codigo(char)
            if cod_izq != None:
                return "0" + cod_izq
            elif cod_der != None:
                return "1" + cod_der
        return None

    
    







class ArbolHuffmanDinamico:
    ascii_dict = {chr(i): format(i, '08b') for i in range(32, 127)}
    raiz: Nodo
    nuevo: Nodo
    id_actual: int
    def __init__(self):
        self.id_actual = 0
        self.raiz = Nodo(self.id_actual, "nuevo")
        self.id_actual += 1
        self.nuevo = self.raiz
    
    def agregar(self, caracter:str):
        if not self.raiz.agregar(caracter):
            self.nuevo.char = ""
            self.nuevo.valor = 1
            self.nuevo.der = Nodo(self.id_actual, caracter)
            self.id_actual += 1
            self.nuevo.izq = Nodo(self.id_actual, "nuevo")
            self.id_actual += 1
            self.nuevo = self.nuevo.izq
            return True
        
    
    def ordenar(self):
        lista:list[tuple[Nodo, str]] = []
        self.raiz.listar(lista, "")
        ordenada = True
        for i in range(len(lista)-1):
            if lista[i][0].valor > lista[i+1][0].valor:
                ordenada = False
                break
        if ordenada:
            return True
        cant = len(lista)
        for i in range(cant-1):
            actual = lista[i]
            sig = lista[i+1]
            if actual[0].valor > sig[0].valor:
                indice_primero = i
                break
        
        j = indice_primero + 1
        while j < cant and lista[j][0].valor == lista[j+1][0].valor:
            j += 1
        
        if j == cant:
            raise Exception("Error")
        
        indice_ultimo = j
        
        camino_padre_primero = lista[indice_primero][1][:-1]

        i = 0
        while lista[i][1] != camino_padre_primero:
            i += 1
        indice_padre_primero = i
        
        

        camino_padre_ultimo = lista[indice_ultimo][1][:-1]
        i = 0
        while lista[i][1] != camino_padre_ultimo:
            i += 1
        indice_padre_ultimo = i

        primero = lista[indice_primero][0]
        segundo = lista[indice_ultimo][0]
        padre_primero = lista[indice_padre_primero][0]
        padre_ultimo = lista[indice_padre_ultimo][0]

        if padre_primero.izq.id == primero.id:
            if padre_ultimo.izq.id == segundo.id:
                padre_primero.izq = segundo
                padre_ultimo.izq = primero
            elif padre_ultimo.der.id == segundo.id:
                padre_primero.izq = segundo
                padre_ultimo.der = primero
        elif padre_primero.der.id == primero.id:
            if padre_ultimo.izq.id == segundo.id:
                padre_primero.der = segundo
                padre_ultimo.izq = primero
            elif padre_ultimo.der.id == segundo.id:
                padre_primero.der = segundo
                padre_ultimo.der = primero
        else:
            raise Exception("Error encontrando padres")

        
        self.raiz.arreglar_contadores()
        
        self.ordenar()


    def codificar(self, cadena:str):
        nueva = ""
        for caracter in cadena:
            codigo = self.raiz.get_codigo(caracter)
            if codigo == None:
                nueva += self.raiz.get_codigo("nuevo")
                nueva += self.ascii_dict[caracter]
            else:
                nueva += codigo
            self.agregar(caracter)
            self.raiz.arreglar_contadores()
            self.ordenar()
        return nueva
    

if __name__ == "__main__":
    arbol = ArbolHuffmanDinamico()
    print(arbol.codificar("COMOQUIERESQUETEQUIERA SIQUIENQUIEROQUEMEQUIERA"))