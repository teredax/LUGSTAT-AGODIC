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
        

    def printMemory(self):
        print("----------------------------")
        print("Global ints: ")
        for x in range(len(self.memoria[0][0])):
            print (self.getAddressFrom(0, 0, x), " = ", self.memoria[0][0][x])

        print("Global nums: ")
        for x in range(len(self.memoria[0][1])):
            print (self.getAddressFrom(0, 1, x), " = ", self.memoria[0][1][x])

        print("Global bools: ")
        for x in range(len(self.memoria[0][2])):
            print (self.getAddressFrom(0, 2, x), " = ", self.memoria[0][2][x])

        print("Global chars: ")
        for x in range(len(self.memoria[0][3])):
            print (self.getAddressFrom(0, 3, x), " = ", self.memoria[0][3][x])

        print("----------------------------")
        print("Local ints: ")
        print(self.memoria[1][0])
        for x in range(len(self.memoria[1][0])):
            print (self.getAddressFrom(1, 0, x), " = ", self.memoria[1][0][x])

        print("Local nums: ")
        for x in range(len(self.memoria[1][1])):
            print (self.getAddressFrom(1, 1, x), " = ", self.memoria[1][1][x])

        print("Local bools: ")
        for x in range(len(self.memoria[1][2])):
            print (self.getAddressFrom(1, 2, x), " = ", self.memoria[1][2][x])

        print("Local chars: ")
        for x in range(len(self.memoria[1][3])):
            print (self.getAddressFrom(1, 3, x), " = ", self.memoria[1][3][x])

        print("----------------------------")
        print("Temp ints: ")
        for x in range(len(self.memoria[2][0])):
            print (self.getAddressFrom(2, 0, x), " = ", self.memoria[2][0][x])

        print("Temp nums: ")
        for x in range(len(self.memoria[2][1])):
            print (self.getAddressFrom(2, 1, x), " = ", self.memoria[2][1][x])

        print("Temp bools: ")
        for x in range(len(self.memoria[2][2])):
            print (self.getAddressFrom(2, 2, x), " = ", self.memoria[2][2][x])

        print("Temp chars: ")
        for x in range(len(self.memoria[2][3])):
            print (self.getAddressFrom(2, 3, x), " = ", self.memoria[2][3][x])

        print("----------------------------")
        print("Const ints: ")
        for x in range(len(self.memoria[3][0])):
            print (self.getAddressFrom(3, 0, x), " = ", self.memoria[3][0][x])

        print("Const nums: ")
        for x in range(len(self.memoria[3][1])):
            print (self.getAddressFrom(3, 1, x), " = ", self.memoria[3][1][x])

        print("Const bools: ")
        for x in range(len(self.memoria[3][2])):
            print (self.getAddressFrom(3, 2, x), " = ", self.memoria[3][2][x])

        print("Const chars: ")
        for x in range(len(self.memoria[3][3])):
            print (self.getAddressFrom(3, 3, x), " = ", self.memoria[3][3][x])
        print("----------------------------")


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
    #memory.printMemory()

if __name__== "__main__":
  main()