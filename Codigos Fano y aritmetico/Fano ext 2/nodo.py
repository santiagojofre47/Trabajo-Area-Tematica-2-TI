class nodo:
    __codigo = str 
    __hijoizq = None
    __hijoder = None
    __grupo = list
    __sumatoria = 0

    def __init__(self, grupo, codigo) -> None:
        self.__grupo = grupo
        self.__codigo = codigo
        self.__hijoder = None
        self.__hijoizq = None
        self.__sumatoria = 0
        for i in range(len(self.__grupo)):
            self.__sumatoria += self.__grupo[i][1]
    
    def set_hijoder(self,nodo):
        self.__hijoder = nodo
    
    def get_hijoizq(self,nodo):
        self.__hijoizq = nodo
    
    def get_hijoizq(self):
        return self.__hijoizq

    def get_hijoder(self):
        return self.__hijoder
    
    def set_grupo(self,grupo):
        self.__grupo = grupo
    
    def get_grupo(self):
        return self.__grupo

    def set_codigo(self,codigo):
        self.__codigo = codigo
    
    def get_codigo(self):
        return self.__codigo

    def dividir(self):
        if len(self.__grupo) > 1:
            temp = self.__grupo.copy()
            sum = 0
            GrupoProbGreater = []
            GrupoProbLesser = []
            
            while sum < (self.__sumatoria/2): 
                sum += temp[0][1]
                GrupoProbGreater.append(temp[0])
                temp.pop(0)
                if sum + temp[0][1] > (self.__sumatoria/2):
                    break
                
            GrupoProbLesser = temp
            self.__hijoizq= nodo(GrupoProbLesser,self.__codigo+"1")
            self.__hijoder = nodo(GrupoProbGreater,self.__codigo+"0")
            self.__hijoder.dividir()
            self.__hijoizq.dividir()
        
            
       
    