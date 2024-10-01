from nodo import nodo

class arbol:
    __raiz = None
    __codigos = {}

    def __init__(self,grupo) -> None:
        self.__raiz = nodo(grupo,"")
        self.__codigos = {}

    def resolver(self):
        self.__raiz.dividir()
        self.InOrden(self.__raiz,"")
        
        
    def get_pab(self):
        print(self.__codigos["PAB"])    
    
    def InOrden(self,SubArbol,codigo):
        if SubArbol != None:
            self.InOrden(SubArbol.get_hijoizq(),codigo+SubArbol.get_codigo())
            self.InOrden(SubArbol.get_hijoder(),codigo+SubArbol.get_codigo())
            if len(SubArbol.get_grupo()) == 1:
                self.__codigos[SubArbol.get_grupo()[0][0]] = SubArbol.get_codigo()

    def get_codigo(self,num):
        return self.__codigos[num]