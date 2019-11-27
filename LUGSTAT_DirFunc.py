#Gonzalo Garcia A01281414
#Jesus Lugo A01089769

import copy
from LUGSTAT_TablaDeVariables import Tabla_de_Variables

class Directorio_de_Variables(object):

    def __init__(self):
        self.listaf = {}


    def addf(self, fname, ftype, procstart, nparams, nvars, typeparams, params):
    	self.listaf[fname] = {
    	'name' : fname,
    	'ftype': ftype,
    	'fvars': Tabla_de_Variables(),
        'ProcS': procstart,
        'Nparams': nparams,
        'Nvars' : nvars,
        'TypeParams': typeparams,
        'Params': params
    	}


    def search(self, fquery):
    	return fquery in self.listaf

    def listf(self):
    	print(self.listaf)

    def getdir(self, fquery):
        if self.search(fquery) == True:
            return self.listaf[fquery]
        else:
            print("E404")
            return None

    def addv(self, fname, vname, vtype,loc):
        if fname in self.listaf:
            access = self.listaf[fname]
            if access['fvars'].search(vname) == True:
                print("Variable already exists")
            else:
                access['fvars'].add(vname, vtype,loc)
        else:
            print("Function does not exist")

    def addarreglo(self, fname, arreglox):
        if fname in self.listaf:
            access = self.listaf[fname]
            access['fvars'].addArr(arreglox)
        else:
            print("Function does not exist")


    def getallv(self, fname):
        if fname in self.listaf:
            access = self.listaf[fname]
            return access['fvars'].printTable()

    def releaseloc(self, fname):
        if fname in self.listaf:
            access=self.listaf[fname]
            print(access['fvars'].printTable())


    def getstartln(self, fname):
        if fname in self.listaf:
            access = self.listaf[fname]
            return access['ProcS']

    def getnparams(self, fname):
        if fname in self.listaf:
            access = self.listaf[fname]
            return access['Nparams']

    def addparams(self, fname, nparams):
        if fname in self.listaf:
            access = self.listaf[fname]
            access['Nparams'] = nparams

    def getparamtypes(self, fname):
        if fname in self.listaf:
            access = self.listaf[fname]
            access2 = copy.copy(access['TypeParams'])
            return access2
        else:
            print("E404")

    def getmemnum(self, fname, vname):
        if fname in self.listaf:
            access = self.listaf[fname]
            return access['fvars'].getmloc(vname)

    def addparamtypes(self, fname, paramstoadd):
        if fname in self.listaf:
            access  = self.listaf[fname]
            access['TypeParams'] = paramstoadd

    def addvarnum(self, fname, nvars):
        if fname in self.listaf:
            access = self.listaf[fname]
            access['Nvars'] = nvars

    def getparamsstack(self, fname):
        if fname in self.listaf:
            access = self.listaf[fname]
            return copy.copy(access['Params'])


    def addparamsstack(self, fname, params):
        if fname in self.listaf:
            access = self.listaf[fname]
            access['Params'] = params


def main():
    print("reee")
    test = Directorio_de_Variables()
    test.addf("func1", bool, 999,0,0, 0)
    test.addv("func1", "var1" , bool, 200)
    test.addv("func1", "var2" , bool, 3)
    test.getallv("func1")
    print(test.getmemnum("func1", "var1"))

if __name__== "__main__":
  main()

