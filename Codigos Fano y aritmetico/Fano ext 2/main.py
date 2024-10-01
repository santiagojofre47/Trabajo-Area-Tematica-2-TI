from arbol import arbol
def concat(dict):
    if len(dict) != 0:
        nuevo = {}
        for key1 in dict:
            for key2 in caracteres:
                nuevo[key1+key2] = dict[key1]*caracteres[key2]
        return nuevo
    else:
        return caracteres
if __name__ == "__main__":
    caracteres = {"A":4/26,
                  "L":4/26,
                  "O":4/26,
                  "B":2/26,
                  "C":2/26,
                  "I":2/26,
                  "P":2/26,
                  "T":2/26,
                  "V":2/26,
                  "U":1/26,
                  "N":1/26
                }
    """caracteres = {
        "E":10/46,
        "Q":7/46,
        "U":7/46,
        "I":6/46,
        "R":4/46,
        "O":3/46,
        "S":2/46,
        "M":2/46,
        "A":2/46,
        "C":1/46,
        "T":1/46,
        "N":1/46
    }"""
    cadena = "PABLOPABLITOCLAVOUNCLAVITO"
    print(f"Long sin compilar: {len(cadena)*8}")
    """exti = {}"""
    
    """for i in range(1,5):
        exti = concat(exti)
        extiord = sorted(exti.items(), key= lambda x:x[1], reverse=True)
        raizi = arbol(extiord)
        raizi.resolver()
        codigo = ""

        for j in range(0,len(cadena)-i+1,i+1):
            print(cadena[j:j+i])
            codigo += raizi.get_codigo(cadena[j:j+i])
        
        print(f"Long compilando con ext{i}: {len(codigo)}")"""



    ext2 = concat(caracteres)
    
    
    
    ext2 = sorted(ext2.items(), key= lambda x:x[1], reverse=True)
    
    c = sorted(caracteres.items(), key= lambda x:x[1], reverse=True)   
    
    

    
    raizext1 = arbol(c)
    raizext1.resolver()

    raizext2 = arbol(ext2)
    raizext2.resolver()

   

    codigoext1 = ""
    codigoext2 = ""
    

    for i in range(len(cadena)):
        codigoext1 += raizext1.get_codigo(cadena[i])

    for i in range(0,len(cadena)-2,2):
        codigoext2 += raizext2.get_codigo(cadena[i:i+2])

   
   

    print(codigoext2)
    print(codigoext1)
    
    print(f"Long compilando con ext1: {len(codigoext1)}")
    print(f"porcentaje de compresión ext1: {len(codigoext1)/(len(cadena)*8)}")
    print(f"Long compilando con ext2: {len(codigoext2)}")
    print(f"porcentaje de compresión ext2: {len(codigoext2)/(len(cadena)*8)}")
    


        



    
    