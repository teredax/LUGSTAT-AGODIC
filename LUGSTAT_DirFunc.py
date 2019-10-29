#Gonzalo Garcia A01281414
#Jesus Lugo A0


from LUGSTAT_TablaDeVariables import Tabla_de_Variables

class Directorio_de_Variables(object):

    def __init__(self):
        self.listaf = {}


    def addf(self, fname, ftype):
    	self.listaf[fname] = {

    	'name' : fname,
    	'ftype': ftype,
    	'fvars': Tabla_de_Variables
    	}


    def search(self, fquery):
    	return fquery in self.listaf

    def listf(self):

    	print(self.listaf)

    def getdir(self, fquery):
        if self.search(fquery) == True:
            return self.listaf[fquery]
        else:
            print("E404 \n")
            return None



def main():
    print("reee")
    test = Directorio_de_Variables()
    test.addf("func1", bool)
    test.listf()
    print("-------------")
    result=test.search("func1")
    print(result)
    print(test.getdir("func11"))

if __name__== "__main__":
  main()