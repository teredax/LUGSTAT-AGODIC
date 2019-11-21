#Mapeo de locaciones
#Mantener 2,500 por tipo 
#Codigo G = global L = Local T = Temporales C = Constantes + Tipo i = int, d = double, bool = b, string = s 

#Globales
Gi = 0
Gd = 2500
Gb = 5000
Gs = 7500
#Locales
Li = 10000
Ld = 12500
Lb = 15000
Ls = 17500
#Temporales
Ti = 20000
Td = 22500
Tb = 25000
Ts = 27500
#Constantes
Ci = 30000
Cd = 32500
Cb = 35000
Cs = 37500

class Memoria:

    def __init__(self):     
        self.createMemory()

    def createMemory(self):  #      G               L               T              C  
        self.memoria =      [[{},{},{},{}], [{},{},{},{}],[{},{},{},{}],[{},{},{},{}]] 
    
    def addMemoryValue (self,direccion,valor):
        if direccion // 10000 == 0: #Guardamos valor en Globales
            self.memoria[0][((direccion % 10000) // 2500)][(direccion % 10000) % 2500] = valor
        elif direccion // 10000 == 1: #Guardamos valor en Locales
            self.memoria[1][((direccion % 10000) // 2500)][(direccion % 10000) % 2500] = valor
        elif direccion // 10000 == 2: #Guardamos valor en Temporales
            self.memoria[2][((direccion % 10000) // 2500)][(direccion % 10000) % 2500] = valor
        elif direccion // 10000 == 3: #Guardamos valor en Constantes
            self.memoria[3][((direccion % 10000) // 2500)][(direccion % 10000) % 2500] = valor #Crear funcion de no poder sobre escribir constantes

    def getAddressFrom(self, nivel, tipo, index):
        return nivel * 10000 + tipo * 2500 + index

    def getValue(self, direccion):
        if direccion // 10000 == 0: #Guardamos valor en Globales
            return self.memoria[0][((direccion % 10000) // 2500)][(direccion % 10000) % 2500]
        elif direccion // 10000 == 1: #Guardamos valor en Locales
            return self.memoria[1][((direccion % 10000) // 2500)][(direccion % 10000) % 2500]
        elif direccion // 10000 == 2: #Guardamos valor en Temporales
            return self.memoria[2][((direccion % 10000) // 2500)][(direccion % 10000) % 2500]
        elif direccion // 10000 == 3: #Guardamos valor en Constantes
            return self.memoria[3][((direccion % 10000) // 2500)][(direccion % 10000) % 2500]
    


def main():
    memory = Memoria()
    memory.addMemoryValue(0, 5)
    memory.addMemoryValue(2500, 5.0)
    memory.addMemoryValue(5000, True)
    memory.addMemoryValue(7500, "Perro Global")
    memory.addMemoryValue(10000, 5)
    memory.addMemoryValue(12500, 5.0)
    memory.addMemoryValue(15000, True)
    memory.addMemoryValue(17500, "Perro Local")
    memory.addMemoryValue(20000, 5)
    memory.addMemoryValue(22500, 5.0)
    memory.addMemoryValue(25000, True)
    memory.addMemoryValue(27500, "Perro Temporal")
    memory.addMemoryValue(30000, 5)
    memory.addMemoryValue(32500, 5.0)
    memory.addMemoryValue(35000, True)
    memory.addMemoryValue(37500, "Perro Constante")
    print(memory.getValue(17500))

if __name__== "__main__":
  main()