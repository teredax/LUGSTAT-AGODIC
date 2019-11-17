#Gonzalo Garcia A01281414
#Jesus Lugo A01089769


from LUGSTAT_TablaDeVariables import Tabla_de_Variables

class Directorio_de_Variables(object):

    def __init__(self):
        self.listaf = {}


    def addf(self, fname, ftype, procstart, nparams, nvars):
    	self.listaf[fname] = {
    	'name' : fname,
    	'ftype': ftype,
    	'fvars': Tabla_de_Variables(),
        'ProcS': procstart,
        'Nparams': nparams,
        'Nvars' : nvars 
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
            #print ("Function exists")
            access = self.listaf[fname]
            if access['fvars'].search(vname) == True:
                print("Variable already exists")
            else:
                access['fvars'].add(vname, vtype,loc)
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
            #print (access['Nparams'])
            return access['Nparams']

    def addparams(self, fname, nparams):
        if fname in self.listaf:
            access = self.listaf[fname]
            access['Nparams'] = nparams
            #print(access['Nparams'])



    def addvarnum(self, fname, nvars):
        if fname in self.listaf:
            access = self.listaf[fname]
            access['Nvars'] = nvars
            #print(access['Nvars'])



def main():
    print("reee")
    test = Directorio_de_Variables()
    test.addf("func1", bool, 999,0,0)
    test.addv("func1", "var1" , bool)
    test.addv("func1", "var2" , bool)
    test.getallv("func1")
    test.releaseloc("func1")

if __name__== "__main__":
  main()

