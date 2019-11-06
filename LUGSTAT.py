#Gonzalo Garcia A01281414
#JESUS LUGO A01089769
#VERSION 21/10/2019
# Caso de prueba se pega en inputf.txt
#usando PLY (Lex / Yacc for python)


import queue as Queue
import ply.lex as lex
import ply.yacc as yacc
from LUGSTAT_DirFunc import Directorio_de_Variables

DirectorioFunciones = Directorio_de_Variables()

FuncionActual = []
TipoActual = []


#--------------------
#Setup of Quadruples

POper = []
PilaO = []
Ptype = []
q = Queue.Queue()
#--------------------


InputF= open("inputf.txt", "r") 
cache=InputF.read()
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
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
    'func' : 'FUNC',
    'fx' : 'FX',
    'fy' : 'FY',
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
t_RELOP = r'==|<|>|<=|>=|!='
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
    lugstat : LUGSTAT ID SCOLON addmain lugstat2 lugstat3 block
    '''

def p_addmain(p):
    '''addmain : empty'''
    DirectorioFunciones.addf(p[-2],None)
    global currentf
    currentf = p[-2]

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

    #print("currentf: ", p[-1])
    if p[-4] == "lugstat":
     #Significa que vengo del main por lo tanto agrego a mi funcion main;
        for i in range(len(FuncionActual)):
                DirectorioFunciones.addv(p[-3],FuncionActual[i],TipoActual[0])
        FuncionActual.clear()
        TipoActual.clear()
    else:
        if p[-1] == '(': #Vengo desde FUNC soy parte de una funcion
            global currentf
            currentf = p[-5]
            for i in range(len(FuncionActual)):
                DirectorioFunciones.addv(p[-5],FuncionActual[i],TipoActual[0])
            FuncionActual.clear()
            TipoActual.clear()
    
    if p[-1] == ";": #N linea de Variables (Usualmente de otro tipo)
        for i in range(len(FuncionActual)):
            DirectorioFunciones.addv(currentf,FuncionActual[i],TipoActual[0])
        FuncionActual.clear()
        TipoActual.clear() 

    if p[-1] == ')': # Variables locales de una FUNC
        #print("12321",FuncionActual)
        for i in range(len(FuncionActual)):
            DirectorioFunciones.addv(currentf,FuncionActual[i],TipoActual[0])
        FuncionActual.clear()
        TipoActual.clear() 
           

def p_vars1(p):
    ''' 
    vars1 : ID COMMA vars1
    | ID COLON tipo SCOLON lugstat2
    | ID asign2 COLON tipo SCOLON
    | ID asign2 COMMA vars1
    '''
    
    #print("vars: ",p[1],p[2],p[3])
    if p[2] == ":":

        TipoActual.append(p[3]) #Guardamos tipo actual
        if p[1] not in FuncionActual:
            FuncionActual.append(p[1])
    else:
        FuncionActual.append(p[1])
        if p[3] != "None" and p[3] not in FuncionActual:
            FuncionActual.append(p[3]) #Ultimo Recorrido guardamos posicion final 

        p[0] = p[3] #Matener informacion

    if p[3] == ":":
        TipoActual.append(p[4]) #En caso de tener valores de arreglo ejem test4[] Update a futuro. 
    else:
        pass
    
    p[0] = p[1]

    #print(FuncionActual)

def p_savename(p):
    '''savename : empty'''

def p_modules(p):
    '''
    modules : FUNC ID COLON tipo addfunction OPAREN modules2 CPAREN modules2 block'''
    
def p_addfunction(p):
    '''addfunction : empty'''
    p[0] = p[-3]
    DirectorioFunciones.addf(p[-3],p[-1])
    #Agregamos la funcion al tener los datos de tipo y datos 


def p_modules2(p):
    '''
    modules2 : vars
    | empty'''
    p[0] = p[1]
    

def p_block(p):
    '''
    block : OBRACKET block2 CBRACKET
    '''
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
    '''escrt : PRINT OPAREN expresion CPAREN SCOLON
	| PRINT OPAREN CPAREN SCOLON
    | PRINT OPAREN ID escrt2 CPAREN SCOLON
    | PRINT OPAREN STRING CPAREN SCOLON
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

def p_cond(p):
    '''cond : IF OPAREN expresion CPAREN block SCOLON
    | IF OPAREN expresion CPAREN block ELSE block SCOLON
    '''

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

def p_exp(p):
    '''
    exp : termino
    | termino PLUS exp
    | termino MINUS exp
    '''

    #print("exp",p[-1])
    #POper.append(p[-1])



def p_termino(p):
    '''
    termino : factor
    | factor MULT termino
    | factor DIV termino
    '''
    #print("term",p[-1])
    #POper.append(p[-1])



def p_factor(p):
    '''
    factor : OPAREN expresion CPAREN 
    | PLUS varcte
    | MINUS varcte
    | varcte
    '''
    #print("facctor",p[1])

    # @1
    #print("!@#",p[-4])
    #print("!@#",p[-1])
    #PilaO.append()

def p_varcte(p):
    '''
    varcte : ID
    | ID asign2
    | NUMERIC
    | NUMBER
    '''
    if float(p[1]).is_integer():
        print("soy entero ", p[1])
    else:
        print("soy flotante ",p[1])
    print(p[-10])


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
    '''

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
    mmmfunc : ID 
    | OBRACKET  mmmarray CBRACKET
	| OBRACKET mmmarray CBRACKET COMMA mmmfunc
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
 

 # Build the parser
print ("Parsing . . . \n")
parser = yacc.yacc()
result = parser.parse(cache)


print("Variables lugstat MAIN \n")
DirectorioFunciones.getallv("lugstattest")
print("\n")
print("Variables de Modulo Prueba \n")
DirectorioFunciones.getallv("prueba")