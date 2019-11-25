#Gonzalo Garcia A01281414
#JESUS LUGO A01089769
#VERSION 21/10/2019
# Caso de prueba se pega en inputf.txt
#usando PLY (Lex / Yacc for python)

#Puntos Neurales marcados con #@1...#@2 etc

import queue as Queue
import ply.lex as lex
import ply.yacc as yacc
from LUGSTAT_DirFunc import Directorio_de_Variables
from LUGSTAT_ConsideracionesSemanticas import ConsideracionesSemanticas
from LUGSTAT_Memory import Memoria
from sklearn.cluster import KMeans
from LUGSTAT_DIRECCIONES import * #Importamos nuestras direcciones base
import statistics 
import time
import numpy as np
import pandas as pd
from sympy import Matrix
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from scipy.stats import poisson
from scipy.stats import erlang  
from scipy.stats import bernoulli
from numpy.linalg import inv
import seaborn as sb
import sys

DirectorioFunciones = Directorio_de_Variables()
ConsideracionesSemanticas = ConsideracionesSemanticas()
memory = Memoria()


FuncionActual = []
TipoActual = []
ValorArreglo = []
TemporalCounter = 0
MemoryREG = []

def findaddrfromREG(elem):
    for i in range(0, len(MemoryREG)):
        #print(elem, MemoryREG[i][2], len(MemoryREG), i, "#####")
        if MemoryREG[i][0] == elem:
            return MemoryREG[i][2]



def typetostr(element):

	#print(element)
	stringvalues = {'int', 'double', 'float', 'string', 'bool'}
	if element in stringvalues:
		return element

	else:
		if element is int:
			return 'int'
		if element is float:
			return 'double'
		if element is str:
			return 'string'
		if element is bool:
			return 'bool'


class AVAIL(object):
    def __init__(self):
        self.AvailC = 0
        self.Temp = "t"

    def next(self):
        self.AvailC+=1
        return self.Temp + str(self.AvailC)

    def reset(self):
        self.AvailC = 0




#--------------------
#Setup of Quadruples

POper = []
PilaO = []
Ptype = []
Quad = Queue.Queue()
AVAIL = AVAIL()
LineC = 0
vmcounter =0
vfcounter=0
pfcounter=0
pftypestack = []
pfboolstackcond= False
paramk =0
queryf = ""
workingtypedirectory = []
#--------------------
#Setup of Non-Linear Statements
PJumps = []
exp_type = ""
nresult = ""

def FILL(elem1, elem2):

    for i in range ( 0, Quad.qsize()):
        if Quad.queue[i][0] == elem1:
            #print("Found it!")
            #print(Quad.queue[i][0], "#", Quad.queue[i][1])
            a = Quad.queue[i][0]
            b = Quad.queue[i][1]
            c = Quad.queue[i][2]
            d = Quad.queue[i][3]
            Quad.queue[i] = (a, b, c, elem2)



InputF= open("inputf.txt", "r") 
cache=InputF.read()
reserved = {
    'if' : 'IF',
    'do' : 'DO',
    'while' : 'WHILE',
    'else' : 'ELSE',
    'read' : 'READ',
    'var' : 'VAR',
    'int' : 'INT',
    'bool': 'BOOL',
    'double' : 'DOUBLE',
    'print' : 'PRINT',
    'lugstat' : 'LUGSTAT',
    'tipo' : 'TIPO',
    'and' : 'AND',
    'or' : 'OR',
    'count' : 'COUNT',
    'countif' : 'COUNTIF',
    'plot' : 'PLOT',
    'mean' : 'MEAN',
    'median' : 'MEDIAN',
    'mode' : 'MODE', 
    'stdv' : 'STDV',
    'kmeans' : 'KMEANS',
    'derl' : 'DERL',
    'dpoi' : 'DPOI',
    'dbern' : 'DBERN',
    'ref' : 'REF',
    'rref' : 'RREF',
    'mont' : 'MONT',
    'char' : 'CHAR',
    'string': 'STRING',
    'func' : 'FUNC',
    'fx' : 'FX',
    'fy' : 'FY',
    'euler': 'EULER',
    'rotate' : 'ROTATE',
    'transpose' : 'TRANSPOSE',
    'inverse' : 'INVERSE'
           }


tokens = [
        'PLUS', 'MINUS', 'MULT','DIV','EQUALS','OPAREN', 'STRING', 
        'CPAREN', 'ID','OBRACKET', 'CBRACKET', 'GREATERTHAN', 
        'LESSTHAN', 'GRE','COLON','SCOLON','COMMA', 'NUMBER',
        'PER','EQ','LESSEQ','GREATEQ','DIFF','LCOR','RCOR',
        'COMMENT','INTEGER','NUMERIC','LOGICAL','CHARACTER','QUOTE' , 'RELOP','CTEI','CTED'
         ] + list(reserved.values())

# Tokens
#Aritmeticos
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULT   = r'\*'
t_DIV  = r'/'
t_PER = r'\%'
#Relacionales
t_RELOP = r'==|<=|>=|<|>|!='
t_GRE = r'<>'
#Asignacion
t_EQUALS  = r'\='
#Parentesis
t_OPAREN  = r'\('
t_CPAREN  = r'\)'
t_OBRACKET = r'\{'
t_CBRACKET = r'\}'
#Simbolos Especiales
t_COLON = r':'
t_SCOLON = r';'
t_COMMA = r','
#Agrupamiento
t_LCOR = r'\['
t_RCOR = r'\]' #Revisarlo
t_QUOTE = r'\"'
t_STRING = r'\".*\"'

#and or not relop ABD OR NOT 


t_ignore_COMMENT = r'\#.*'


def t_LOGICAL(t):
    r'True|False'
    return t


def t_NUMERIC(t):
    r'\d+[eE][-+]?\d+|(\.\d+|\d+\.\d+)([eE][-+]?\d+)?'
    t.value = float(t.value)              
    return t

def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Ignored characters
t_ignore = " \t"

def t_newline(t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'ID')    # Check for reserved words
     return t

    # Build the lexer
import ply.lex as lex
lexer = lex.lex()

  # Give the lexer some input
lexer.input(cache)
 
 # Tokenize
print ("Despliegue de Tokens \n")
while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     print(tok)
     
#LUGSTAT



def p_lugstat(p):
    '''
    lugstat : LUGSTAT ID SCOLON addmain lugstat2 lugstat3 mnv block
    '''

def p_addmain(p):
    '''addmain : empty'''
    DirectorioFunciones.addf(p[-2],None, 0, 0, 0, 0)
    memory.createLocalTemporal() #Creamos un contexto nuevo para main este nunca se elimina
    global currentf
    global TemporalCounter
    TemporalCounter = 0
    currentf = []
    currentf.append(p[-2])

def p_mnv(p):
    ''' mnv : empty '''
    DirectorioFunciones.addvarnum(currentf[0], vmcounter)

def p_lugstat2(p):
        '''
    lugstat2 : vars
    | empty
    '''

def p_lugstat3(p):
        '''
    lugstat3 : modules
    | modules lugstat3
    | empty'''

def p_vars(p):
    '''
    vars : VAR vars1 
    '''
    #print("C", FuncionActual)
    global vmcounter
    global vfcounter
    global pfcounter
    global pftypestack
    global pfboolstackcond
    global Li
    global Ld
    global Lb
    global Ls
    #print("currentf: ", p[-1], " p-4", p[-4])
    if p[-4] == "lugstat":
     #Significa que vengo del main por lo tanto agrego a mi funcion main;
        for i in range(len(FuncionActual)):
                if(TipoActual[0] == 'int'):
                        if len(ValorArreglo) > 0:
                            arreglo = {
                                'name' : FuncionActual[i],
                                'inicio' : Li,
                                'final'  : Li + ValorArreglo[0] - 1,
                                'type' : TipoActual[0]
                            }
                            DirectorioFunciones.addarreglo(p[-3],arreglo)
                            for i in range(ValorArreglo[0]):
                                memory.addMemoryValue(Li,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Li, 70))
                                Li = Li + 1
                        else:     
                            DirectorioFunciones.addv(p[-3],FuncionActual[i],TipoActual[0],Li)
                            if(Li == 10000):
                                memory.addMemoryValue(Li,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Li, 70))
                                Li = Li + 1
                            else:
                                memory.addMemoryValue(Li,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Li, 70))
                                Li = Li + 1
                if(TipoActual[0] == 'double'):
                        if len(ValorArreglo) > 0:
                            arreglo = {
                                'name' : FuncionActual[i],
                                'inicio' : Ld,
                                'final'  : Ld + ValorArreglo[0] - 1,
                                'type' : TipoActual[0]
                            }
                            DirectorioFunciones.addarreglo(p[-3],arreglo)
                            for i in range(ValorArreglo[0]):
                                memory.addMemoryValue(Ld,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Ld, 70))
                                Ld = Ld + 1
                        else:     
                            DirectorioFunciones.addv(p[-3],FuncionActual[i],TipoActual[0],Ld)
                            if(Ld == 12500):
                                memory.addMemoryValue(Li,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Ld, 70))
                                Ld = Ld + 1
                            else:
                                memory.addMemoryValue(Li,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Li, 70))
                                Ld = Ld + 1
                if(TipoActual[0] == 'bool'):
                        if len(ValorArreglo) > 0:
                            arreglo = {
                                'name' : FuncionActual[i],
                                'inicio' : Lb,
                                'final'  : Lb + ValorArreglo[0] - 1,
                                'type' : TipoActual[0]
                            }
                            DirectorioFunciones.addarreglo(p[-3],arreglo)
                            for i in range(ValorArreglo[0]):
                                memory.addMemoryValue(Lb,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Lb, 70))
                                Lb = Lb + 1
                        else:     
                            DirectorioFunciones.addv(p[-3],FuncionActual[i],TipoActual[0],Lb)
                            if(Lb == 15000):
                                memory.addMemoryValue(Lb,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Lb, 70))
                                Lb = Lb + 1
                            else:
                                memory.addMemoryValue(Lb,70)
                                Lb = Lb + 1
                if(TipoActual[0] == 'string'):
                        if len(ValorArreglo) > 0:
                            arreglo = {
                                'name' : FuncionActual[i],
                                'inicio' : Ls,
                                'final'  : Ls + ValorArreglo[0] - 1,
                                'type' : TipoActual[0]
                            }
                            DirectorioFunciones.addarreglo(p[-3],arreglo)
                            for i in range(ValorArreglo[0]):
                                memory.addMemoryValue(Ls,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Ls, 70))
                                Ls = Ls + 1
                        else:     
                            DirectorioFunciones.addv(p[-3],FuncionActual[i],TipoActual[0],Ls)
                            if(Ls == 12500):
                                memory.addMemoryValue(Ls,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Ls, 70))
                                Ls = Ls + 1
                            else:
                                memory.addMemoryValue(Ls,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Ls, 70))
                                Ls = Ls + 1
                vmcounter+=1
                #print(FuncionActual[i], "@#!#!@")
        Li = 10000
        Ld = 12500
        Lb = 15000
        Ls = 17500
        FuncionActual.clear()
        TipoActual.clear()
        ValorArreglo.clear()
    else:
        if p[-1] == '(': #Vengo desde FUNC soy parte de una funcion
            #print(currentf, "$@#$@#")
            for i in range(len(FuncionActual)):
                if(TipoActual[0] == 'int'):
                        if len(ValorArreglo) > 0:
                            arreglo = {
                                'name' : FuncionActual[i],
                                'inicio' : Li,
                                'final'  : Li + ValorArreglo[0] - 1,
                                'type' : TipoActual[0]
                            }
                            DirectorioFunciones.addarreglo(p[-5],arreglo)
                            for i in range(ValorArreglo[0]):
                                memory.addMemoryValue(Li,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Li, 70))

                                Li = Li + 1
                        else:     
                            DirectorioFunciones.addv(p[-5],FuncionActual[i],TipoActual[0],Li)
                            memory.addMemoryValue(Li,70)
                            MemoryREG.append((FuncionActual[i],TipoActual[0], Li, 70))
                            Li = Li + 1
                if(TipoActual[0] == 'double'):
                        if len(ValorArreglo) > 0:
                            arreglo = {
                                'name' : FuncionActual[i],
                                'inicio' : Ld,
                                'final'  : Ld + ValorArreglo[0] - 1,
                                'type' : TipoActual[0]
                            }
                            DirectorioFunciones.addarreglo(p[-5],arreglo)
                            for i in range(ValorArreglo[0]):
                                memory.addMemoryValue(Ld,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Ld, 70))
                                Ld = Ld + 1
                        else:     
                            DirectorioFunciones.addv(p[-5],FuncionActual[i],TipoActual[0],Ld)
                            memory.addMemoryValue(Ld,70)
                            MemoryREG.append((FuncionActual[i],TipoActual[0], Ld, 70))
                            Ld = Ld + 1
                if(TipoActual[0] == 'bool'):
                        if len(ValorArreglo) > 0:
                            arreglo = {
                                'name' : FuncionActual[i],
                                'inicio' : Lb,
                                'final'  : Lb + ValorArreglo[0] - 1,
                                'type' : TipoActual[0]
                            }
                            DirectorioFunciones.addarreglo(p[-5],arreglo)
                            for i in range(ValorArreglo[0]):
                                memory.addMemoryValue(Lb,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Lb, 70))
                                Lb = Lb + 1
                        else:     
                            DirectorioFunciones.addv(p[-5],FuncionActual[i],TipoActual[0],Lb)
                            memory.addMemoryValue(Lb,70)
                            MemoryREG.append((FuncionActual[i],TipoActual[0], Lb, 70))
                            Lb = Lb + 1
                if(TipoActual[0] == 'string'):
                        if len(ValorArreglo) > 0:
                            arreglo = {
                                'name' : FuncionActual[i],
                                'inicio' : Ls,
                                'final'  : Ls + ValorArreglo[0] - 1,
                                'type' : TipoActual[0]
                            }
                            DirectorioFunciones.addarreglo(p[-5],arreglo)
                            for i in range(ValorArreglo[0]):
                                memory.addMemoryValue(Ls,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Ls, 70))
                                Ls = Ls + 1
                        else:     
                            DirectorioFunciones.addv(p[-5],FuncionActual[i],TipoActual[0],Ls)
                            memory.addMemoryValue(Ls,70)
                            MemoryREG.append((FuncionActual[i],TipoActual[0], Ls, 70))
                            Ls = Ls + 1
                pfcounter+=1
                #print(TipoActual[0], " of type")
                #print(p[-1], "fds")
                pftypestack.append(TipoActual[0])
                #print(pfcounter, "params!")
            FuncionActual.clear()
            TipoActual.clear()
            Li = 10000
            Ld = 12500
            Lb = 15000
            Ls = 17500
    
    if p[-1] == ";":
     #N linea de Variables (Usualmente de otro tipo) 
     #VER DONDE METEMOS CONTEXTO PARA AGREGAR MEMORY VALUE O EN CUALQUIER OTRO CASO HACERLO HASTA MAQUINA VIRTUAL 
        for i in range(len(FuncionActual)):
                    if(TipoActual[0] == 'int'):
                        if len(ValorArreglo) > 0:
                            arreglo = {
                                'name' : FuncionActual[i],
                                'inicio' : Li,
                                'final'  : Li + ValorArreglo[0] - 1,
                                'type' : TipoActual[0]
                            }
                            DirectorioFunciones.addarreglo(currentf[-1],arreglo)
                            for i in range(ValorArreglo[0]):
                                memory.addMemoryValue(Li,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Li, 70))
                                Li = Li + 1
                        else:     
                            DirectorioFunciones.addv(currentf[-1],FuncionActual[i],TipoActual[0],Li)
                            memory.addMemoryValue(Li,70)
                            MemoryREG.append((FuncionActual[i],TipoActual[0], Li, 70))
                            Li = Li + 1
                    if(TipoActual[0] == 'double'):
                        if len(ValorArreglo) > 0:
                            arreglo = {
                                'name' : FuncionActual[i],
                                'inicio' : Ld,
                                'final'  : Ld + ValorArreglo[0] - 1,
                                'type' : TipoActual[0]
                            }
                            DirectorioFunciones.addarreglo(currentf[-1],arreglo)
                            for i in range(ValorArreglo[0]):
                                memory.addMemoryValue(Ld,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Ld, 70))
                                Ld = Ld + 1
                        else:     
                            DirectorioFunciones.addv(currentf[-1],FuncionActual[i],TipoActual[0],Ld)
                            memory.addMemoryValue(Ld,70)
                            MemoryREG.append((FuncionActual[i],TipoActual[0], Ld, 70))
                            Ld = Ld + 1
                    if(TipoActual[0] == 'bool'):
                        if len(ValorArreglo) > 0:
                            arreglo = {
                                'name' : FuncionActual[i],
                                'inicio' : Lb,
                                'final'  : Lb + ValorArreglo[0] - 1,
                                'type' : TipoActual[0]
                            }
                            DirectorioFunciones.addarreglo(currentf[-1],arreglo)
                            for i in range(ValorArreglo[0]):
                                memory.addMemoryValue(Lb,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Lb, 70))
                                Lb = Lb + 1
                        else:     
                            DirectorioFunciones.addv(currentf[-1],FuncionActual[i],TipoActual[0],Lb)
                            memory.addMemoryValue(Lb,70)
                            MemoryREG.append((FuncionActual[i],TipoActual[0], Lb, 70))
                            Lb = Lb + 1
                    if(TipoActual[0] == 'string'):
                        if len(ValorArreglo) > 0:
                            arreglo = {
                                'name' : FuncionActual[i],
                                'inicio' : Ls,
                                'final'  : Ls + ValorArreglo[0] - 1,
                                'type' : TipoActual[0]
                            }
                            DirectorioFunciones.addarreglo(currentf[-1],arreglo)
                            for i in range(ValorArreglo[0]):
                                memory.addMemoryValue(Ls,70)
                                MemoryREG.append((FuncionActual[i],TipoActual[0], Ls, 70))
                                Ls = Ls + 1
                        else:     
                            DirectorioFunciones.addv(currentf[-1],FuncionActual[i],TipoActual[0],Ls)
                            memory.addMemoryValue(Ls,70)
                            MemoryREG.append((FuncionActual[i],TipoActual[0], Ls, 70))
                            Ls = Ls + 1           
                    if currentf[-1] != currentf[0] and pfboolstackcond == True:
                       # print("FS@@@@@@@@@@@@@@@@@@@@@@@@D", TipoActual[0], FuncionActual[i])
                        #print("regular function var, not a param", FuncionActual[i])
                        #print(p[1], "#@#@#@#@##")
                        pftypestack.append(TipoActual[0])
                        pfcounter+=1
                    if currentf[-1] != currentf[0] and pfboolstackcond == False:
                        #print("FS#######################D", TipoActual[0], FuncionActual[i])
                        vfcounter+=1
                        #print(vfcounter, "vars of f!")  
                    #print(vfcounter, "im going in! first line", FuncionActual[i])
                    #print("STATUS:", currentf)
        FuncionActual.clear()
        TipoActual.clear() 
        ValorArreglo.clear()
    if p[-1] == ')': # Variables locales de una FUNC EN CASO DE NECESITARLO AQUI CREAR UN CONTEXTO NUEVO LA PRIMERA VEZ QUE SE ENTRE AQUI  
        for i in range(len(FuncionActual)):
                if(TipoActual[0] == 'int'):
                    DirectorioFunciones.addv(currentf[-1],FuncionActual[i],TipoActual[0],Li)
                    #memory.addMemoryValue(Li,70)
                    Li = Li + 1
                if(TipoActual[0] == 'double'):
                    DirectorioFunciones.addv(currentf[-1],FuncionActual[i],TipoActual[0],Ld)
                    #memory.addMemoryValue(Ld,70)
                    Ld = Ld + 1
                if(TipoActual[0] == 'bool'):
                    DirectorioFunciones.addv(currentf[-1],FuncionActual[i],TipoActual[0],Lb)
                    #memory.addMemoryValue(Lb,70)
                    Lb = Lb + 1
                if(TipoActual[0] == 'string'):
                    DirectorioFunciones.addv(currentf[-1],FuncionActual[i],TipoActual[0],Ls)
                    #memory.addMemoryValue(Ls,70)
                    Ls = Ls + 1            
                vfcounter+=1
                #print(vfcounter, "im going in! first line", FuncionActual[i])
                #print("regular function var, not a param", FuncionActual[i])
        Li = 10000
        Ld = 12500
        Lb = 15000
        Ls = 17500
        FuncionActual.clear()
        TipoActual.clear()
        ValorArreglo.clear()

           

def p_vars1(p):
    ''' 
    vars1 : ID COMMA vars1
    | ID COLON tipo SCOLON lugstat2
    | ID LCOR NUMBER RCOR COLON tipo SCOLON lugstat2
    | ID LCOR NUMBER RCOR COLON tipo SCOLON 
    | ID LCOR NUMBER RCOR LCOR NUMBER RCOR COLON tipo SCOLON lugstat2
    | ID LCOR NUMBER RCOR LCOR NUMBER RCOR COLON tipo SCOLON 
    | ID asign2 COLON tipo SCOLON
    | ID asign2 COMMA vars1
    '''
    
    #print("vars: ",p[1],p[2],p[3])
    if p[2] == ":":                
        TipoActual.append(p[3]) #Guardamos tipo actual
        if p[1] not in FuncionActual:
            FuncionActual.append(p[1])
    elif p[2] == "[":
        if p[5]== "[":
            TipoActual.append(p[9])
            ValorArreglo.append(p[3] * p[6])
            if p[1] not in FuncionActual:
                FuncionActual.append(p[1])#En caso de tener valores de arreglo ejem test4[] Update a futuro. 
        else:
            TipoActual.append(p[6]) 
            ValorArreglo.append(p[3])
            if p[1] not in FuncionActual:
                FuncionActual.append(p[1])#En caso de tener valores de arreglo ejem test4[] Update a futuro. 
            p[0] = p[3]

    else:
        FuncionActual.append(p[1])
        if p[3] != "None" and p[3] not in FuncionActual:
            FuncionActual.append(p[3]) #Ultimo Recorrido guardamos posicion final 
        p[0] = p[3] #Matener informacion
    
    p[0] = p[1]

    #print(FuncionActual)

def p_savename(p):
    '''savename : empty'''

def p_modules(p):
    '''
    modules : FUNC ID COLON tipo mn1 OPAREN  modules2 mn2 CPAREN modules2 mn3 funblock mn7'''


#@mn1
def p_mn1(p):
    '''mn1 : empty'''
    global pfboolstackcond
    quad = ("INIT", p[-3])
    Quad.put(quad)
    p[0] = p[-3]
    DirectorioFunciones.addf(p[-3],p[-1], LineC+1, 0 , 0, 0)
    currentf.append(p[-3])
    pfboolstackcond = True

    #Agregamos la funcion al tener los datos de tipo y datos 


def p_mn7(p):
    '''mn7 : empty'''

    global currentf
    global TemporalCounter
    global pftypestack
    quad = (LineC+1, "END", currentf[-1])
    Quad.put(quad)
    print("STATUS1:", currentf)
    currentf.pop()

    #pftypestack = []

    print("STATUS2:", currentf)
    TemporalCounter = 0
    #DirectorioFuncionedef p_savename(p):
    '''savename : empty'''


def p_mn2(p):
    '''mn2 : '''
    global pfcounter
    global pftypestack
    global pfboolstackcond
    #print(pfcounter, "fff")
    DirectorioFunciones.addparams(currentf[-1], pfcounter)
    pfcounter =0
    #print(pftypestack, "mn21")
    DirectorioFunciones.addparamtypes(currentf[-1], pftypestack)
    pftypestack = []
    pfboolstackcond = False


def p_mn3(p):
    '''mn3 : empty'''
    global vfcounter
    DirectorioFunciones.addvarnum(currentf[-1], vfcounter)

    vfcounter=0

def p_funccall(p):
    ''' funccall : ID OPAREN fcn1 expresion fcn2 funccall2 CPAREN fcn3 '''


def p_fcn1(p):
    ''' fcn1 : empty'''
    global LineC
    #print(p[-2])
    if DirectorioFunciones.search(p[-2]):
        LineC+=1
        quad = (LineC+1, "ERA", p[-2])
        Quad.put(quad)

    else:
        print("Function being summoned does not exist!")
        sys.exit()

    global queryf
    global workingtypedirectory
    queryf = p[-2]
    print("queryff " , queryf)
    workingtypedirectory = DirectorioFunciones.getparamtypes(queryf)
    #print(workingtypedirectory, "@#$@#")
    


def p_fcn2(p):
    ''' fcn2 : empty'''
    global paramk
    global LineC

    argT = Ptype.pop()
    argT = typetostr(argT)
    argF = PilaO.pop()
    #print(pftypestack, '#@$')
    print(queryf)
    getp = workingtypedirectory
    #print(getp, "getppp")
    argP = getp.pop()
    #print(DirectorioFunciones.getparamtypes(queryf), "#@$#$@@#%$^&$^#")
    print(argT, argP, argF)
    if argT == argP:
        paramk+=1
        LineC+=1
        quad = (LineC+1, "PARAM", argF, "param"+str(paramk))
        Quad.put(quad)
    else:
        print("Arguement and Function Parameter type Mismatch!")
        sys.exit()

def p_fcn3(p):
    '''fcn3 : empty '''
    #print(DirectorioFunciones.getnparams(p[-7]), "$#@")
    #print(paramk)
    global LineC
    global paramk
    if DirectorioFunciones.getnparams(p[-7]) != paramk:
        print("Inconsistent number of arguements:parameters for function ", p[-7])
        sys.exit()
    else:
        LineC+=1
        quad = (LineC+1, "GOSUB", p[-7], DirectorioFunciones.getstartln(p[-7]))
        Quad.put(quad)

    queryf = ""
    paramk= 0

def p_funccall2(p):
    ''' funccall2 : COMMA expresion fcn2 funccall2
    | empty '''
    

def p_modules2(p):
    '''
    modules2 : vars
    | empty'''
    p[0] = p[1]

def p_funblock(p):
    '''
    funblock : OBRACKET block2 CBRACKET
    '''   
def p_block(p):
    '''
    block : OBRACKET block2 CBRACKET
    '''
    global currentf
    global TemporalCounter
    print("STATUS:", currentf)
    currentf.pop()
    TemporalCounter = 0
    print("STATUS:", currentf)
    
def p_block2(p):
    '''
    block2 : estatuto
    | estatuto block2
    | empty'''

def p_tipo(p):
    '''
    tipo : INT
    | BOOL 
    | DOUBLE
    | STRING
    | CHAR
    '''
    p[0] = p[1]

def p_estatuto(p):
    '''
    estatuto : asign
    | cond 
    | escrt
    | plot
    | count
    | countif
    | metodos
    | dwhile
    | readln
    | funccall
    '''

def p_asign(p):
    '''
    asign : ID EQUALS expresion SCOLON
    | ID EQUALS ID SCOLON
    | ID EQUALS ID asign2 SCOLON
    | ID asign2 EQUALS ID SCOLON
    | ID asign2 EQUALS expresion SCOLON
    | ID asign2 EQUALS ID asign2 SCOLON
    '''
    #print("!@#",p[1], p[2])

    if p[2] is '=' or p[3] is '=':
        
        if p[2] is '=':
            POper.append(p[2])
        else:
            POper.append(p[3])

        #print("equals",p[3])

    PilaO.append(p[1])
    #print(p[1], "@@@@@@@@@@@@@@@@@@@@@@@@")
    if type(p[1]) is int or type(p[1]) is float:
        Ptype.append(type(p[1]))
    else:
        print("Looking in var table for type")
        #print(currentf, "#$#@$")
        index=DirectorioFunciones.getdir(currentf[-1])
        tar=index['fvars'].get(p[1])
        #print(tar, "@#$@#$@#$@#$@#$@#$")

        if tar == None:
            print("Variable not found locally. Checking global scope..")
            index=DirectorioFunciones.getdir(currentf[0])
            tar=index['fvars'].get(p[1])

        if tar == None:
            print("Variable doesn't exist!")
            sys.exit()
        else:
            tarfilter = tar['type']
            #print(tar['type'], "#$@$@@#$")
            #print("tarfilter",tarfilter)
            Ptype.append(tarfilter)


    if POper:
        if POper[-1] == '=':
            rOP = PilaO.pop()
            rTY = Ptype.pop()
            rTY = typetostr(rTY)
            lOP = PilaO.pop()
            lTY = Ptype.pop()
            lTY = typetostr(lTY)
            oOP = POper.pop()
            global LineC
            LineC +=1
            fTY = ConsideracionesSemanticas.get_tipo(lTY, rTY, oOP)
            print("Your Quad is: ", "Line : [[", LineC, "]]" , lOP, rTY, rOP, lTY, oOP, fTY)
            if fTY != 'error':
                quad = (oOP, lOP, rOP)
                Quad.put(quad)

                # if any operand were a temporal space return it to AVAIL??
                #Next....
            else:
                print("Type Mismatch1")   
                sys.exit() 


def p_asign2(p):
    '''
    asign2 : LCOR expresion RCOR asign3
    | LCOR varcte RCOR asign3 
    '''

def p_asign3(p):
    '''
    asign3 : LCOR expresion RCOR
    | LCOR varcte RCOR 
    | empty'''


def p_escrt(p):
    '''escrt : PRINT OPAREN ID en3 escrt2 CPAREN SCOLON
    | PRINT OPAREN expresion en1 CPAREN SCOLON
    | PRINT OPAREN STRING CPAREN en2 SCOLON
    | PRINT OPAREN STRING  escrt2 CPAREN en2 SCOLON
    '''

def p_escrt2(p):
    '''escrt2 : COMMA escrt3
    | empty
    '''

def p_escrt3(p):
    '''escrt3 : ID escrt2
    | ID
    | STRING escrt2 escrt2
    '''

def p_en1(p):
    '''en1 : empty'''
    output = PilaO.pop()
    #print("PrintOut", output)
    global LineC
    LineC+=1
    quad = ("PRINT", output)
    Quad.put(quad)

def p_en2(p):
    '''en2 : empty'''
    outputstr = p[-2]
    quad  = ("PRINT", outputstr)
    global LineC
    LineC+=1
    Quad.put(quad)

def p_en3(p):
    '''en3 : empty'''
    print("Checking if variable to print exists", p[-1])
    index=DirectorioFunciones.getdir(currentf[-1])
    tar=index['fvars'].get(p[-1])

    if tar == None:
        print("Variable not found locally. Checking global scope..")
        index=DirectorioFunciones.getdir(currentf[0])
        tar=index['fvars'].get(p[-1])

    if tar == None:
        print("Variable doesn't exist!")
        sys.exit()
    else:
        output = p[-1]
        global LineC
        LineC+=1
        quad = ("READ", output)
        Quad.put(quad)





def p_cond(p):
    '''cond : IF OPAREN expresion cn1 CPAREN ifblock SCOLON cn2
    | IF OPAREN expresion cn1 CPAREN ifblock ELSE cn3 ifblock SCOLON cn2
    '''

def p_cn1(p):
    '''cn1 : empty'''
    exp_type = Ptype.pop()
    #print(exp_type)
    exp_type = typetostr(exp_type)
    global LineC
    LineC +=1
    if exp_type != 'bool':
        print("Type Mismatch2!")
        sys.exit()
    else:
        res = PilaO.pop()
        PJumps.append(LineC)
        print("Your Quad is: [[", LineC, "]]", "GOTOF", res, 0)
        quad = (LineC, "GOTOF", res, 0)
        Quad.put(quad)


def p_cn2(p):
    '''cn2 : empty'''
    cend = PJumps.pop()
    print(LineC+1, "----Im exiting the if into this line----")
    FILL(cend, LineC+1)
    #print(Quad.queue)

def p_cn3(p):
    '''cn3 : empty'''
    global LineC
    LineC +=1
    quad = (LineC, "GOTO", 0, 0)
    Quad.put(quad)
    print("Your Quad is: [[", LineC, "]]", "GOTO", 0, 0)
    false = PJumps.pop()
    PJumps.append(LineC)
    FILL(false, LineC+1)
    #print(LineC+1, "----Im exiting the else into this line----")
    #print(Quad.queue)
def p_ifblock(p):
    '''
    ifblock : OBRACKET ifblock2 CBRACKET
    '''    
def p_ifblock2(p):
    '''
    ifblock2 : estatuto
    | estatuto ifblock2
    | empty'''

def p_count(p):
    'count : COUNT OPAREN ID COMMA varcte COMMA varcte CPAREN SCOLON'

def p_countif(p):
    'countif : COUNTIF OPAREN ID COMMA varcte COMMA varcte COMMA cond CPAREN SCOLON'

def p_plot(p):
    '''plot : PLOT OPAREN xyfunc CPAREN SCOLON
    | PLOT OPAREN plot2 CPAREN SCOLON
    '''
def p_plot2(p):
    '''
    plot2 : LCOR varcte COMMA varcte RCOR
    | LCOR varcte COMMA varcte RCOR COMMA plot2
    | empty
    '''

def p_xyfunc(p):
    '''xyfunc : FX EQUALS exp SCOLON xyfunc
    | FY EQUALS exp SCOLON xyfunc
    | empty
    '''

#RE REVISAR DIAGRAMA
def p_expresion(p):
    '''expresion : exp 
    | expresion RELOP exp 
    '''
    #@9
    relopindex = {'>', '<', '>=','<=', '!=', '=='}
    if POper:
        if POper[-1] in relopindex:
            #print("im going in")
            rOP = PilaO.pop()
            rTY = Ptype.pop()
            rTY = typetostr(rTY)
            lOP = PilaO.pop()
            lTY = Ptype.pop()
            lTY = typetostr(lTY)
            oOP = POper.pop()
            global LineC
            global Ti
            global Td
            global Tb
            global Ts
            LineC +=1
            fTY = ConsideracionesSemanticas.get_tipo(lTY, rTY, oOP)
            print("Your Quad is: ", "Line : [[", LineC, "]]" , lOP, rTY, rOP, lTY, oOP, fTY)
            if fTY != 'error':
                RFI = AVAIL.next()
                if fTY == 'int':
                    DirectorioFunciones.addv(currentf[-1],RFI, fTY,Ti)
                    memory.addMemoryValue(Ti,74)
                    MemoryREG.append((RFI, fTY, Ti, 0))
                    quad = (oOP, rOP, lOP, RFI, Ti)
                    Quad.put(quad)
                    PilaO.append(RFI)
                    Ti = Ti + 1
                if fTY == 'double':
                    DirectorioFunciones.addv(currentf[-1],RFI, fTY,Td)
                    memory.addMemoryValue(Td,74)
                    quad = (oOP, rOP, lOP, RFI, Td)
                    MemoryREG.append((RFI, fTY, Td, 0))
                    Quad.put(quad)
                    PilaO.append(RFI)
                    Td = Td + 1
                if fTY == 'bool':
                    DirectorioFunciones.addv(currentf[-1],RFI, fTY,Tb)
                    memory.addMemoryValue(Tb,74)
                    MemoryREG.append((RFI, fTY, Tb, 0))
                    quad = (oOP, rOP, lOP, RFI, Tb)
                    Quad.put(quad)
                    PilaO.append(RFI)
                    Tb = Tb + 1
                if fTY == 'string':
                    DirectorioFunciones.addv(currentf[-1],RFI, fTY,Ts)
                    memory.addMemoryValue(Ts,74)
                    MemoryREG.append((RFI, fTY, Ts, 0))
                    quad = (oOP, rOP, lOP, RFI, Ts)
                    Quad.put(quad)
                    PilaO.append(RFI)
                    Ts = Ts + 1
                Ptype.append(fTY)
                #Ver en que momento borrar liberar temporales
    			# if any operand were a temporal space return it to AVAIL??
    			#Next....
            else:
                print("Type Mismatch3!")
                sys.exit()


def p_exp(p):
    '''
    exp : termino
    | termino PLUS exp
    | termino MINUS exp
    '''
    #@8
    relopindex = {'>', '<', '>=', '<=', '!=', '=='}
    #print(p[-1])
    if p[-1] in relopindex:
        POper.append(p[-1])
        #print("I put in", p[-1])

    #@2
    if p[-1] is '+' or p[-1] is '-':
    	POper.append(p[-1])
    	#print("plusminus",p[-1])

    #@4
    if POper:
    	if POper[-1] == '+' or POper[-1] == '-':
            rOP = PilaO.pop()
            rTY = Ptype.pop()
            rTY = typetostr(rTY)
            lOP = PilaO.pop()
            lTY = Ptype.pop()
            lTY = typetostr(lTY)
            oOP = POper.pop()
            global LineC
            global Ti
            global Td
            global Tb
            global Ts
            LineC +=1
            fTY = ConsideracionesSemanticas.get_tipo(lTY, rTY, oOP)
            print("Your Quad is: ", "Line : [[", LineC, "]]" , lOP, rTY, rOP, lTY, oOP, fTY)
            if fTY != 'error':
                RFI = AVAIL.next()
                if fTY == 'int':
                    DirectorioFunciones.addv(currentf[-1],RFI, fTY,Ti)
                    memory.addMemoryValue(Ti,74)
                    MemoryREG.append((RFI, fTY, Ti, 0))
                    quad = (oOP, rOP, lOP, RFI, Ti)
                    Quad.put(quad)
                    PilaO.append(RFI)
                    Ti = Ti + 1
                if fTY == 'double':
                    DirectorioFunciones.addv(currentf[-1],RFI, fTY,Td)
                    memory.addMemoryValue(Td,74)
                    MemoryREG.append((RFI, fTY, Td, 0))
                    quad = (oOP, rOP, lOP, RFI, Td)
                    Quad.put(quad)
                    PilaO.append(RFI)
                    Td = Td + 1
                if fTY == 'bool':
                    DirectorioFunciones.addv(currentf[-1],RFI, fTY,Tb)
                    memory.addMemoryValue(Tb,74)
                    MemoryREG.append((RFI, fTY, Tb, 0))
                    quad = (oOP, rOP, lOP, RFI, Tb)
                    Quad.put(quad)
                    PilaO.append(RFI)
                    Tb = Tb + 1
                if fTY == 'string':
                    DirectorioFunciones.addv(currentf[-1],RFI, fTY,Ts)
                    memory.addMemoryValue(Ts,74)
                    MemoryREG.append((RFI, fTY, Ts, 0))
                    quad = (oOP, rOP, lOP, RFI, Ts)
                    Quad.put(quad)
                    PilaO.append(RFI)
                    Ts = Ts + 1
                Ptype.append(fTY)
                # if any operand were a temporal space return it to AVAIL??
                #Next....
            else:
                print("Type Mismatch4!")
                sys.exit()



def p_termino(p):
    '''
    termino : factor
    | factor MULT termino
    | factor DIV termino
    '''



    #@3
    if p[-1] is '*' or p[-1] is '/':
    	POper.append(p[-1])
    	#print("muldiv",p[-1])
   
    #@5
    if POper:
    	if POper[-1] == '*' or POper[-1] == '/':
            rOP = PilaO.pop()
            rTY = Ptype.pop()
            rTY = typetostr(rTY)
            lOP = PilaO.pop()
            lTY = Ptype.pop()
            lTY = typetostr(lTY)
            oOP = POper.pop()
            global LineC
            global Ti
            global Td
            global Tb
            global Ts
            LineC +=1
            fTY = ConsideracionesSemanticas.get_tipo(lTY, rTY, oOP)
            print("Your Quad is: ", "Line : [[", LineC, "]]" , lOP, rTY, rOP, lTY, oOP, fTY)
            if fTY != 'error':
                RFI = AVAIL.next()
                if fTY == 'int':
                    DirectorioFunciones.addv(currentf[-1],RFI, fTY,Ti)
                    memory.addMemoryValue(Ti,74)
                    MemoryREG.append((RFI, fTY, Ti, 0))
                    quad = (oOP, rOP, lOP, RFI, Ti)
                    Quad.put(quad)
                    PilaO.append(RFI)
                    Ti = Ti + 1
                if fTY == 'double':
                    DirectorioFunciones.addv(currentf[-1],RFI, fTY,Td)
                    memory.addMemoryValue(Td,74)
                    MemoryREG.append((RFI, fTY, Td, 0))
                    quad = (oOP, rOP, lOP, RFI, Td)
                    Quad.put(quad)
                    PilaO.append(RFI)
                    Td = Td + 1 
                Ptype.append(fTY)
                # if any operand were a temporal space return it to AVAIL??
                #Next....
            else:
                print("Type Mismatch5!")
                sys.exit()


def p_factor(p):
    '''
    factor : OPAREN expresion CPAREN 
    | varcte
    '''
    #print("factor", p[1], p[-1])

    #@6
    if (p[-1] == '('):
    	POper.append("|")
    	#pls help? no se si va a faltar un reset para que ignore lo que esta antes

    #@7
    if (p[-1] == ')'):
    	POper.pop()

def p_varcte(p):
    '''
    varcte : ID
    | ID asign2
    | NUMERIC
    | NUMBER
    | LOGICAL
    '''
    localvar = 'Const'
    global TemporalCounter
    global Ci
    global Cd
    global Cb
    global Cs

    if type(p[1]) is int or type(p[1]) is float: # Verifica primero si es un id o constante
    	if float(p[1]).is_integer():
            localvar += currentf[-1]
            localvar += str(TemporalCounter)
            DirectorioFunciones.addv(currentf[-1],localvar,"int",Ci)
            TemporalCounter = TemporalCounter + 1
            memory.addMemoryValue(Ci,p[1])
            Ci = Ci + 1
            
    	else:
            localvar += currentf[-1]
            localvar += str(TemporalCounter)
            DirectorioFunciones.addv(currentf[-1],localvar,"double",Cd)
            TemporalCounter = TemporalCounter + 1
            memory.addMemoryValue(Cd,p[1])
            Cd = Cd + 1

    #print("vcte",p[1], type(p[1]))
    
    #@1
    if p[1] == 'True' or p[1] == 'False':
        #print("hi!")
        Ptype.append('bool')
        PilaO.append(p[1])
    else:
        if type(p[1]) is int or type(p[1]) is float:
            Ptype.append(type(p[1]))
            PilaO.append(p[1])
        else:
            print("Looking in var table for type")
            #print(currentf, "#$#@$")
            index=DirectorioFunciones.getdir(currentf[-1])
            tar=index['fvars'].get(p[1])

            if tar == None:
                print("Variable not found locally. Checking global scope..")
                index=DirectorioFunciones.getdir(currentf[0])
                tar=index['fvars'].get(p[1])

            if tar == None:
                print("Variable doesn't exist!")
                sys.exit()
            else:
                tarfilter = tar['type']
                #print("tarfilter",tarfilter)
                Ptype.append(tarfilter)
                PilaO.append(p[1])
        #print(index)

def p_dwhile(p):
    '''
    dwhile : DO wn1 wblock WHILE OPAREN dwhileconds CPAREN wn2 SCOLON 
    '''
def p_wn1(p):
    '''wn1 : empty'''
    global LineC
    PJumps.append(LineC+1)
    quad = ("DO", LineC+1)
    Quad.put(quad)
    LineC+=1
def p_wn2(p):
    '''wn2 : empty'''
    exp_type = Ptype.pop()
    exp_type = typetostr(exp_type)
    if exp_type != 'bool':
        print("Type Mismatch6!")
        sys.exit()
    else:
        res = PilaO.pop()
        doloopstart = PJumps.pop()
        print("Your Quad is: ", LineC+1, "GOTOV", doloopstart)
        quad = (LineC+1, "GOTOV", doloopstart)
        Quad.put(quad)

def p_wblock(p):
    '''
    wblock : OBRACKET block2 CBRACKET   
    '''

def p_dwhileconds(p):
    '''
    dwhileconds : expresion dwhileconds
    | expresion AND dwhileconds
    | expresion OR dwhileconds
    | empty
    '''

def p_readln(p):
    ''' readln : READ OPAREN ID rn1 CPAREN SCOLON '''

def p_rn1(p):
    '''rn1 : empty '''
    print("Checking if variable to read and write onto exists")
    index=DirectorioFunciones.getdir(currentf[-1])
    tar=index['fvars'].get(p[-1])

    if tar == None:
        print("Variable not found locally. Checking global scope..")
        index=DirectorioFunciones.getdir(currentf[0])
        tar=index['fvars'].get(p[-1])

    if tar == None:
        print("Variable doesn't exist!")
        sys.exit()
    else:
        output = p[-1]
        global LineC
        LineC+=1
        quad = ("READ", output)
        Quad.put(quad)


def p_metodos(p):
    '''
    metodos : MEAN OPAREN mmmfunc CPAREN SCOLON
    | MEDIAN OPAREN mmmfunc CPAREN SCOLON
    | MODE OPAREN mmmfunc CPAREN SCOLON
    | STDV OPAREN mmmfunc CPAREN SCOLON
    | KMEANS OPAREN varcte COMMA mmmfunc CPAREN SCOLON
    | DERL OPAREN expfunc CPAREN SCOLON
    | DBERN OPAREN expfunc CPAREN SCOLON
    | DPOI OPAREN expfunc2 CPAREN SCOLON
    | TRANSPOSE OPAREN mmmfunc CPAREN SCOLON
    | INVERSE OPAREN mmmfunc CPAREN SCOLON
    | ROTATE OPAREN mmmfunc CPAREN SCOLON
    | REF OPAREN mmmfunc CPAREN SCOLON
    | RREF OPAREN mmmfunc CPAREN SCOLON
    | MONT OPAREN mmmfunc CPAREN SCOLON
    | EULER OPAREN CPAREN SCOLON
    '''
    output = p[-1]
    global LineC
    LineC+=1
    print(p[1])
    quad = (p[1].upper(), output)
    Quad.put(quad)

def p_expfunc(p):
    '''
    expfunc : ID COMMA ID COMMA ID
    | varcte COMMA varcte COMMA varcte
    '''

def p_expfunc2(p):
    '''
    expfunc2 : ID COMMA ID
    | varcte COMMA varcte
    '''

def p_mmmfunc(p):
    '''
    mmmfunc : LCOR RCOR
	| LCOR mmmarray RCOR COMMA mmmfunc
    | LCOR mmmarray RCOR
    | ID
	| empty 
    '''

def p_mmmarray(p):
    '''
    mmmarray : varcte
    | varcte COMMA mmmarray
    | empty
    '''

def p_empty(p):
 'empty :'
 pass

 
 # Error rule for syntax errors
def p_error(p):
     print("Syntax error in input!")
 

 # Build the parseroh 
print ("Parsing . . . \n")
parser = yacc.yacc()
result = parser.parse(cache)

print("tu quadruplo resultante es:")
print(Quad.queue)

print("")
print("Variables lugstat MAIN \n")
DirectorioFunciones.getallv("lugstattest")
print("\n")

print("Variables prueba \n")
DirectorioFunciones.getallv("prueba")

print("Probando Memoria")
#print(memory.getCurrentContextValue(10000))

print("")
#print(MemoryREG)

print("Maq V. INIT.")
#print(Quad.qsize(), "$#$#$#$")
WhileCond = False
operationstack = []
backup = []
funcstack = []
while Quad.empty() == False:
    opbasicas = {'+', '-', '*', '/'}
    opasign = {'='}
    relopindex = {'>', '<', '>=', '<=', '!=', '=='}
    # Caso operacion
    ActualQ = Quad.get()
    if ActualQ[0] in opbasicas:
        OPP = ActualQ[0]
        LOP = ActualQ[1]
        ROP = ActualQ[2]
        RT = ActualQ[3]
        MM = ActualQ[4]
        #print(OPP, LOP, ROP, RT)

        if OPP == '+':
            # Si ambos son constantes nadamas hace la operacion sin tener que acceder a memoria por su valor
            if type(LOP) is int or type(LOP) is float:
                if type(ROP) is int or type(ROP) is float:
                    res = LOP + ROP
                    memory.addMemoryValue(MM, res)
                    #print(memory.getValue(20000))
                else:
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    res = LOP + addrv
                    memory.addMemoryValue(MM, res)

            else:
                if type(ROP) is int or type(ROP) is float:
                # El primer valor no es cte pero el segundo si
                    #print(LOP)
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    res = ROP + addrv
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(20000))

                else:
                    print("Both vars")
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    LOPV = addrv
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    ROPV = addrv
                    res = LOPV + ROPV
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(20000))
                    # Ninguno es un cte

        if OPP == '*':
            # Si ambos son constantes nadamas hace la operacion sin tener que acceder a memoria por su valor
            if type(LOP) is int or type(LOP) is float:
                if type(ROP) is int or type(ROP) is float:
                    res = LOP * ROP
                    memory.addMemoryValue(MM, res)
                    #print(memory.getValue(20000))
                else:
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    res = LOP * addrv
                    memory.addMemoryValue(MM, res)

            else:
                if type(ROP) is int or type(ROP) is float:
                # El primer valor no es cte pero el segundo si
                    #print(LOP)
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    res = ROP * addrv
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(20000))

                else:
                    #print("Both vars")
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    LOPV = addrv
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    ROPV = addrv
                    res = LOPV * ROPV
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(20000))
                    # Ninguno es un CTED


        if OPP == '-':
            # Si ambos son constantes nadamas hace la operacion sin tener que acceder a memoria por su valor
            if type(LOP) is int or type(LOP) is float:
                if type(ROP) is int or type(ROP) is float:
                    res =  ROP - LOP
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(20000))
                else:
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    res =  addrv - LOP
                    memory.addMemoryValue(MM, res)

            else:
                if type(ROP) is int or type(ROP) is float:
                # El primer valor no es cte pero el segundo si
                    #print(LOP)
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    res = ROP - addrv
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(20000))

                else:
                    print("Both vars")
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    LOPV = addrv
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    ROPV = addrv
                    res =  ROPV - LOPV
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(20000))
                    # Ninguno es un cte

        if OPP == '/':
            if type(LOP) is int or type(LOP) is float:
                if type(ROP) is int or type(ROP) is float:
                    res =  ROP / LOP
                    memory.addMemoryValue(MM, res)
                    print(memory.getActualContextValue(20000))
                else:
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    res =  addrv / LOP
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(20000))

            else:
                if type(ROP) is int or type(ROP) is float:
                # El primer valor no es cte pero el segundo si
                    #print(LOP)
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    res = ROP / addrv
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(20000))

                else:
                    print("Both vars")
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    LOPV = addrv
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    ROPV = addrv
                    res =  ROPV / LOPV
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(20000))
                    # Ninguno es un cte

    if ActualQ[0] in opasign:
        OPP = ActualQ[0]
        LOP = ActualQ[1]
        ROP = ActualQ[2]
        #print(OPP, LOP, ROP)

        #print("Both vars")
        if type(LOP) is int or type(LOP) is float:
            addr = findaddrfromREG(ROP)
            memory.addMemoryValue(addr, LOP)
        else:
            addr = findaddrfromREG(LOP)
            #print(addr)
            addrv = memory.getActualContextValue(addr)
            LOPV = addrv
            addr = findaddrfromREG(ROP)
            memory.addMemoryValue(addr, LOPV)

        #print(memory.getActualContextValue(10001))

    if ActualQ[0] == "PRINT":
        #print(type(ActualQ[1]))
        check = ActualQ[1]
        if check[0] is "\"":
            aux = ActualQ[1]
            aux.strip('\"')
            print(aux[1:-1])
        else:
            LOP = ActualQ[1]
            addr = findaddrfromREG(LOP)
            #print(addr)
            addrv = memory.getActualContextValue(addr)
            print(addrv)

    if ActualQ[0] in relopindex:
        OPP = ActualQ[0]
        LOP = ActualQ[1]
        ROP = ActualQ[2]
        RT = ActualQ[3]
        MM = ActualQ[4]

        if ActualQ[0] == '<':
        #print(OPP, LOP, ROP, RT)
            if type(LOP) is int or type(LOP) is float:
                if type(ROP) is int or type(ROP) is float:
                    res = ROP < LOP
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))
                else:
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    res = addrv < LOP
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))

            else:
                if type(ROP) is int or type(ROP) is float:
                # El primer valor no es cte pero el segundo si
                    #print(LOP)
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    res = ROP < addrv
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))

                else:
                    print("Both vars")
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    LOPV = addrv
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    ROPV = addrv
                    res = ROPV < LOPV
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))
                    # Ninguno es un cte

        if ActualQ[0] == '>':
        #print(OPP, LOP, ROP, RT)
            if type(LOP) is int or type(LOP) is float:
                if type(ROP) is int or type(ROP) is float:
                    res = ROP > LOP
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))
                else:
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    res = addrv > LOP
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))

            else:
                if type(ROP) is int or type(ROP) is float:
                # El primer valor no es cte pero el segundo si
                    #print(LOP)
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    res = ROP > addrv
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))

                else:
                    print("Both vars")
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    LOPV = addrv
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    ROPV = addrv
                    res = ROPV > LOPV
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))
                    # Ninguno es un cte

        if ActualQ[0] == '>=':
            if type(LOP) is int or type(LOP) is float:
                if type(ROP) is int or type(ROP) is float:
                    res = ROP >= LOP
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))
                else:
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    res = addrv >= LOP
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))

            else:
                if type(ROP) is int or type(ROP) is float:
                # El primer valor no es cte pero el segundo si
                    #print(LOP)
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    res = ROP >= addrv
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))

                else:
                    print("Both vars")
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    LOPV = addrv
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    ROPV = addrv
                    res = ROPV >= LOPV
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))
                    # Ninguno es un cte

        if ActualQ[0] == '<=':
            if type(LOP) is int or type(LOP) is float:
                if type(ROP) is int or type(ROP) is float:
                    res = ROP <= LOP
                    memory.addMemoryValue(MM, res)
                    print(memory.getActualContextValue(25000))
                else:
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    res = addrv <= LOP
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))

            else:
                if type(ROP) is int or type(ROP) is float:
                # El primer valor no es cte pero el segundo si
                    #print(LOP)
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    res = ROP <= addrv
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))

                else:
                    print("Both vars")
                    addr = findaddrfromREG(LOP)
                    addrv = memory.getActualContextValue(addr)
                    LOPV = addrv
                    addr = findaddrfromREG(ROP)
                    addrv = memory.getActualContextValue(addr)
                    ROPV = addrv
                    res = ROPV <= LOPV
                    memory.addMemoryValue(MM, res)
                    #print(memory.getActualContextValue(25000))
                    # Ninguno es un cte

        #print("hi!")
        if WhileCond == True and res == True:
            #print("We're supposed to loop here!", operationstack)
            while Quad.empty() == False:
                backup.append(Quad.get())

            #print("Quad emptied into aux,", backup)
            for i in range(0, len(operationstack)):
                Quad.put(operationstack[i])
            #print("Added pending operations to quad", Quad.queue)
            for i in range(0, len(backup)):
                Quad.put(backup[i])
            #print("Added original quad behind pending operations", Quad.queue)

        if WhileCond == True and res == False:
            WhileCond = False
       
    if ActualQ[1] == "GOTOF":
        #print("gotofcond")
        LOP = ActualQ[2]
        #print(LOP)        
        addr = findaddrfromREG(LOP)
        #print(addr)
        addrv = memory.getActualContextValue(addr)
        LOPV = addrv
        #print(LOPV)
        advance = ActualQ[3] - ActualQ[0]
        #print(advance)
        if LOPV == False:
            for i in range (0, advance-1):
                trash =Quad.get()
                #print(trash)
        #print("skip complete")

    if ActualQ[0] == "READ":
            LOP = ActualQ[1]
            addr = findaddrfromREG(LOP)
            tmem = memory.getType(addr)
            userinput = input()

            if(tmem == 'int' or tmem == 'double'):
                if userinput.isdigit():
                    rfy = "int"
                    if(tmem == "double"):
                        rfy = "double"
                        userinput = float(userinput)
                        print("Mi input doble es ",userinput)
                else:
                    try: #Controlamos si es un doble 
                        float(userinput)
                        rfy = "double"
                    except ValueError:
                        rfy = 'error'
            else:
                if userinput == 'True' or userinput == 'False':
                    rfy = 'bool'
                else:
                    rfy = typetostr(type(userinput))
                #print(rfy, "@")
            #print(tmem)
            #print(rfy)
            if tmem == rfy:
                memory.addMemoryValue(addr, userinput)
            else:
                print("Input and variable Type Mismatch!")
                sys.exit()
                #print(memory.getActualContextValue(10001))
                


    if ActualQ[0] == "DO":
        operationstack.append(ActualQ)
        i=0
        while(ActualQ[1] != "GOTOV"):
            ActualQ = Quad.queue[i]
            operationstack.append(ActualQ)
            i+=1
            #print(ActualQ, "#@#@")
        #print(operationstack, "This will be repeated")
        WhileCond = True



    if ActualQ[0] == "INIT":
        funcstack.append(ActualQ)
        i=0
        while(ActualQ[1] != "END"):
            ActualQ = Quad.get()
            funcstack.append(ActualQ)
        print(funcstack, "CurrentFunctions in stack")

    if ActualQ[1] == "ERA":
        memory.createLocalTemporal()
        key = ActualQ[2]
        print("Function Call to", key)
#        fbackup = []
#        fbackup.append(ActualQ)
#        while(Quad.empty() == False):
#            fbackup.append(Quad.get())
            # se vacia el quadruplo a backup    


#todo 
#verificar multiples do whiles ? 
#print(1) no werky, falta hacer un tipo de verificacion alli, los demas prints si jalan


    if ActualQ[0] == 'MEAN':
        #Meter arreglo, como data, ver como procesar en los quads
        data1 = [19, 46, 21, 18, 30]
        x = statistics.mean(data1) 
        print("Mean ",x)

    if ActualQ[0] == 'MEDIAN':
        #Meter arreglo, como data, ver como procesar en los quads
        data1 = [19, 46, 21, 18, 30]
        x = statistics.median(data1)
        print("Median ",x)

    if ActualQ[0] == 'MODE':
        data1 = [19, 46, 21, 18, 30]
        x = statistics.mode(data1)
        print("Mode ",x) 

    if ActualQ[0] == 'STDV':
        #Meter arreglo, como data, ver como procesar en los quads
        data1 = [19, 46, 21, 18, 30]
        x = statistics.stdev(data1)
        print("Standar Derivation ",x) 

    if ActualQ[0] == 'KMEANS':
        #Metemos conjunto de datos 1 y conjunto de datos 2 y numero de clusters
        df = pd.DataFrame({
            'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
            'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
        })


        kmeans = KMeans(n_clusters=3)
        kmeans.fit(df)

        labels = kmeans.predict(df)
        centroids = kmeans.cluster_centers_

        colmap = {1: 'r', 2: 'g', 3: 'b'}

        fig = plt.figure(figsize=(5, 5))

        colors = (list(map(lambda x: colmap[x+1], labels)))

        plt.scatter(df['x'], df['y'], color=colors, alpha=0.5, edgecolor='k')
        for idx, centroid in enumerate(centroids):
            plt.scatter(*centroid, color=colmap[idx+1])
        plt.xlim(0, 80)
        plt.ylim(0, 80)
        plt.show()
        plt.clf()

    if ActualQ[0] == 'DERL':

        #Creamos una variable random continua
        numargs = erlang.numargs 
        [a] = [0.6, ] * numargs 
        rv = erlang(a) 
        
        quantile = np.arange (0.01, 1, 0.1) 
   
        # Random Variates 
        R = erlang.rvs(a, scale = 2,  size = 10) 

        # PDF 
        R = erlang.pdf(a, quantile, loc = 0, scale = 1) 

        distribution = np.linspace(0, np.minimum(rv.dist.b, 5)) 
        
        plot = plt.plot(distribution, rv.pdf(distribution)) 
        plt.title("Erlang")

        plt.show()
        plt.clf()

    if ActualQ[0] == 'DBERN':

        #QUE ES LO QUE ASIGNAMOS, SIZE, PROBABILIDAD Y QUE MAS ?

        data_bern = bernoulli.rvs(size=1000,p=0.6)
        ax = sb.distplot(data_bern,
                        kde=True,
                        color='crimson',
                        hist_kws={"linewidth": 25,'alpha':1})
        ax.set(xlabel='Bernouli', ylabel='Frequency')
        plt.show()
        plt.clf()

    if ActualQ[0] == 'DPOI':


        #metemos mu y size uwu
        data_binom = poisson.rvs(mu=4, size=10000)
        ax = sb.distplot(data_binom,
                        kde=True,
                        color='green',
                        hist_kws={"linewidth": 25,'alpha':1})
        ax.set(xlabel='Poisson', ylabel='Frequency')
        plt.show()
        plt.clf()

    if ActualQ[0] == 'TRANSPOSE':
        matrix=[[1,2,3],[4,5,6]] 
        print(matrix) 
        print("\n") 
        print(np.transpose(matrix))  #Solo neceistamos la matriz con numpu ya hacemos transpose

    if ActualQ[0] == 'INVERSE':
        matrix = np.array([[1,1,1],[0,2,5],[2,5,-1]]) 
        print(matrix) 
        print("\n") 
        print(inv(matrix))  #Solo neceistamos la matriz con numpu ya hacemos transpose

    if ActualQ[0] == 'ROTATE':

        mat =[  
            [1,  2,  3,  4 ], 
            [5,  6,  7,  8 ], 
            [9,  10, 11, 12 ], 
            [13, 14, 15, 16 ]   
        ] 
  
        top = 0
        bottom = len(mat)-1
    
        left = 0
        right = len(mat[0])-1
    
        while left < right and top < bottom: 
    
            # Store the first element of next row, 
            # this element will replace first element of 
            # current row 
            prev = mat[top+1][left] 
    
            # Move elements of top row one step right 
            for i in range(left, right+1): 
                curr = mat[top][i] 
                mat[top][i] = prev 
                prev = curr 
    
            top += 1
    
            # Move elements of rightmost column one step downwards 
            for i in range(top, bottom+1): 
                curr = mat[i][right] 
                mat[i][right] = prev 
                prev = curr 
    
            right -= 1
    
            # Move elements of bottom row one step left 
            for i in range(right, left-1, -1): 
                curr = mat[bottom][i] 
                mat[bottom][i] = prev 
                prev = curr 
    
            bottom -= 1
    
            # Move elements of leftmost column one step upwards 
            for i in range(bottom, top-1, -1): 
                curr = mat[i][left] 
                mat[i][left] = prev 
                prev = curr 
    
            left += 1

        for row in mat: 
                print (row)

    if ActualQ[0] == 'REF':
        A = np.array([[60, 91, 26], [60, 3, 75], [45, 90, 31]], dtype='float')
        b = np.array([1, 0, 0])

        Ab = np.hstack([A, b.reshape(-1, 1)])

        n = len(b)

        for i in range(n):
            a = Ab[i]

            for j in range(i + 1, n):
                b = Ab[j]
                m = a[i] / b[i]
                Ab[j] = a - m * b

        for i in range(n - 1, -1, -1):
            Ab[i] = Ab[i] / Ab[i, i]
            a = Ab[i]

            for j in range(i - 1, -1, -1):
                b = Ab[j]
                m = a[i] / b[i]
                Ab[j] = a - m * b

        x = Ab[:, 3]
        print("REF",x)

    if ActualQ[0] == 'RREF':
        M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]]) 

        M_rref = M.rref()   

        print("RREF", M_rref)

    if ActualQ[0] == 'MONT':
        M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]]) 

        M_rref = M.rref()   

        print("Montante", M_rref)

    if ActualQ[0] == 'EULER':
        print('J.G., 2019           __gggrgM**M#mggg__')
        print('                __wgNN@"B*P""mp""@d#"@N#Nw__')
        print('              _g#@0F_a*F#  _*F9m_ ,F9*__9NG#g_')
        print('           _mN#F  aM"    #p"    !q@    9NL "9#Qu_')
        print('          g#MF _pP"L  _g@"9L_  _g""#__  g"9w_ 0N#p')
        print('        _0F jL*"   7_wF     #_gF     9gjF   "bJ  9h_')
        print('       j#  gAF    _@NL     _g@#_      J@u_    2#_  #_')
        print('      ,FF_#" 9_ _#"  "b_  g@   "hg  _#"  !q_ jF "*_09_')
        print('      F N"    #p"      Ng@       `#g"      "w@    "# t')
        print('     j p#    g"9_     g@"9_      gP"#_     gF"q    Pb L')
        print('     0J  k _@   9g_ j#"   "b_  j#"   "b_ _d"   q_ g  ##')
        print('     #F  `NF     "#g"       "Md"       5N#      9W"  j#')
        print('     #k  jFb_    g@"q_     _*"9m_     _*"R_    _#Np  J#')
        print('     tApjF  9g  J"   9M_ _m"    9%_ _*"   "#  gF  9_jNF')
        print('      k`N    "q#       9g@        #gF       ##"    #"j')
        print('      `_0q_   #"q_    _&"9p_    _g"`L_    _*"#   jAF,"')
        print('       9# "b_j   "b_ g"    *g _gF    9_ g#"  "L_*"qNF')
        print('        "b_ "#_    "NL      _B#      _I@     j#" _#"')
        print('          NM_0"*g_ j""9u_  gP  q_  _w@ ]_ _g*"F_g@')                
        print('           "NNh_ !w#_   9#g"    "m*"   _#*" _dN@"')
        print('              9##g_0@q__ #"4_  j*"k __*NF_g#@P"')
        print('                "9NN#gIPNL_ "b@" _2M"Lg#N@F"')
        print('                    ""P@*NN#gEZgNN@#@P""')


