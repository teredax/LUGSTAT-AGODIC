#LUGSTAT
#VERSION 21/10/2019

class Tabla_de_Variables(object):

    def __init__(self):
        self.lista = {}

    #se usa
    def add(self,vid,vtype,memoryloc = 0): #vid = variable id, vtype = variable type 
        self.lista[vid] = {
            'name' : vid, #manejamos el id como el nombre
            'type' : vtype,
            'memoryloc': memoryloc
        }

    def addArr(self,variableArr):
        self.lista[variableArr['name']] = variableArr 

    def search(self,vid):
        return vid in self.lista.keys()

    def get(self,vid):
        if self.search(vid): #Buscamos si existe 
            return self.lista[vid] #En ese caso regresamos variable completa
        else:
            return None
    
    def getbyName(self):
        return self.lista

    def getbyType(self):
        return sorted(self.lista, key=lambda k: k['type'])

    def printTable(self):
        print(self.lista.items())
