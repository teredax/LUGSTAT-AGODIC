#Gonzalo Garcia A01281414
#Jesus Lugogo   A01089769


class Tabla_de_Variables(object):

    def __init__(self):
        self.lista = {}

    #se usa
    def add(self,vname,vtype,memoryloc = 0):  
        self.lista[vname] = {
            'name' : vname,
            'type' : vtype,
            'memoryloc': memoryloc
        }

    def addArr(self,variableArr):
        self.lista[variableArr['name']] = variableArr #Revisar como agregar o controlar el uso de id unicos

    def search(self,vname):
        return vname in self.lista

    def get(self,vname):
        if self.search(vname): #Buscamos si existe 
            return self.lista[vname] #En ese caso regresamos variable completa
        else:
            return None
    
    def getbyName(self):
        return self.lista

    def getbyType(self):
        return sorted(self.lista, key=lambda k: k['type'])

    def printTable(self):
        print(self.lista.items())

