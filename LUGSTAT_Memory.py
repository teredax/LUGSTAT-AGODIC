#Mapeo de locaciones
#Mantener 2,500 por tipo 

from LUGSTAT_DIRECCIONES import * #Importamos nuestras direcciones base

class Memoria:

    def __init__(self):     
        self.createMemory()

    def createMemory(self): #      G               L             T              C  
        self.memoria =      [[{},{},{},{}], [[{},{},{},{}]],[[{},{},{},{}]],[{},{},{},{}]] 


    def addMemoryValue (self,direccion,valor):
        if abs(direccion) // 10000 == 0: #Guardamos valor en Globales
            self.memoria[0][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500] = valor # [Nivel es decir GLTC] [Tipo de variable][Index de variable]
        elif abs(direccion) // 10000 == 1: #Guardamos valor en Locales
            self.memoria[1][-1][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500] = valor #Agregamos un -1 ya que existe una local y una temporal por cada funcion
        elif abs(direccion) // 10000 == 2: #Guardamos valor en Temporales
            #print("se agrego a temp en la direccion", direccion)
            self.memoria[2][-1][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500] = valor #Agregamos un -1 ya que existe una local y una temporal por cada funcion
        elif abs(direccion) // 10000 == 3: #Guardamos valor en Constantes
            #print("se agrego a const en la direccion", direccion)
            self.memoria[3][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500] = valor #Crear funcion de no poder sobre escribir constantes

    def addActualMemoryContext (self,direccion,valor):
        if abs(direccion) // 10000 == 1: #Guardamos valor en Locales
            self.memoria[1][-1][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500] = valor #Agregamos un -1 ya que existe una local y una temporal por cada funcion
        elif abs(direccion) // 10000 == 2: #Guardamos valor en Temporales
            #print("se agrego a temp en la direccion", direccion)
            self.memoria[2][-1][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500] = valor #Agregamos un -1 ya que existe una local y una temporal por cada funcion

    def addOldMemoryContext (self,direccion,valor):
        if abs(direccion) // 10000 == 1: #Guardamos valor en Locales
            self.memoria[1][-2][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500] = valor #Agregamos un -1 ya que existe una local y una temporal por cada funcion
        elif abs(direccion) // 10000 == 2: #Guardamos valor en Temporales
            print("se agrego a temp en la direccion", direccion)
            self.memoria[2][-2][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500] = valor #Agregamos un -1 ya que existe una local y una temporal por cada funcion

    def getAddressFrom(self, nivel, tipo, index): #Donde nivel es = global [0], local[1], temporal [3], constante [4] 
        return nivel * 10000 + tipo * 2500 + index


    def getActualContextValue(self, direccion):
        if abs(direccion) // 10000 == 0: #Guardamos valor en Globales
            return self.memoria[0][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500]
        elif abs(direccion) // 10000 == 1: #Guardamos valor en Locales
            return self.memoria[1][-1][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500]
        elif abs(direccion) // 10000 == 2:
            return self.memoria[2][-1][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500]
        elif abs(direccion) // 10000 == 3: #Guardamos valor en Constantes
            return self.memoria[3][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500]

        else:
            print("Address not found")

    def getOldContextValue(self, direccion):
        if abs(direccion) // 10000 == 0: #Guardamos valor en Globales
            return self.memoria[0][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500]
        elif abs(direccion) // 10000 == 1: #Guardamos valor en Locales
            return self.memoria[1][-2][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500]
        elif abs(direccion) // 10000 == 2:
            return self.memoria[2][-2][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500]
        elif abs(direccion) // 10000 == 3: #Guardamos valor en Constantes
            return self.memoria[3][((abs(direccion) % 10000) // 2500)][(abs(direccion) % 10000) % 2500]

        else:
            print("Address not found")

    def freeFunctionMemory(self):
        self.memoria[1].pop() #Al terminar una funcion eliminamos las variables locales
        self.memoria[2].pop() #Al terminar una funcion eliminamos las variables Temporales

    def createLocalTemporal(self):
        self.memoria[1].append([{},{},{},{}]) #Al crear una funcion siempre crear una nueva direccion
        self.memoria[2].append([{},{},{},{}]) #Al crear una funcion eliminamos las variables Temporales

    def getType(self,direccion):
        if((abs(direccion) % 10000) // 2500) == 0: 
            return "int"
        elif ((abs(direccion) % 10000) // 2500) == 1: 
            return "double" 
        elif ((abs(direccion) % 10000) // 2500) == 2: 
            return "bool" 
        elif ((abs(direccion) % 10000) // 2500) == 3: 
           return "string" 

    def getBase(self,direccion):
        if abs(direccion) // 10000 == 0: 
            if((abs(direccion) % 10000) // 2500) == 0: 
                return 0
            elif ((abs(direccion) % 10000) // 2500) == 1: 
                return 2500 
            elif ((abs(direccion) % 10000) // 2500) == 2: 
                return 5000 
            elif ((abs(direccion) % 10000) // 2500) == 3: 
                return 7500 
        elif abs(direccion) // 10000 == 1: 
            if((abs(direccion) % 10000) // 2500) == 0: 
                return 10000
            elif ((abs(direccion) % 10000) // 2500) == 1: 
                return 12500 
            elif ((abs(direccion) % 10000) // 2500) == 2: 
                return 15000 
            elif ((abs(direccion) % 10000) // 2500) == 3: 
                return 17500 
        elif abs(direccion) // 10000 == 2: 
            if((abs(direccion) % 10000) // 2500) == 0: 
                return 20000
            elif ((abs(direccion) % 10000) // 2500) == 1: 
                return 225000 
            elif ((abs(direccion) % 10000) // 2500) == 2: 
                return 25000 
            elif ((abs(direccion) % 10000) // 2500) == 3:
                return 27500 
        elif abs(direccion) // 10000 == 3: 
            if((abs(direccion) % 10000) // 2500) == 0: 
                return 30000
            elif ((abs(direccion) % 10000) // 2500) == 1: 
                return 32500 
            elif ((abs(direccion) % 10000) // 2500) == 2:
                return 35000 
            elif ((abs(direccion) % 10000) // 2500) == 3: 
                return 37500 

def main():
    memory = Memoria()
    print(memory.getType(37500))

if __name__== "__main__":
  main()