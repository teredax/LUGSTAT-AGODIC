#Gonzalo Garcia A01281414
#JESUS LUGO A01089769
#VERSION 21/10/2019
# Caso de prueba se pega en inputf.txt
#usando PLY (Lex / Yacc for python)



import ply.lex as lex
import ply.yacc as yacc

InputF= open("/Users/lugo/Documents/Clases/Compiladores/CompiladoresAgoDic/inputf.txt", "r") 
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
    lugstat : LUGSTAT ID SCOLON lugstat2 lugstat3 block
    '''

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
    vars : VAR vars1 COLON tipo SCOLON
    '''

def p_vars1(p):
    '''
    vars1 : ID
    | ID COMMA vars1
    | ID asign2
    | ID asign2 COMMA vars1
    '''

def p_modules(p):
    '''
    modules : FUNC ID COLON tipo OPAREN modules2 CPAREN modules2 block'''

def p_modules2(p):
    '''
    modules2 : vars
    | empty'''


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

def p_termino(p):
    '''
    termino : factor
    | factor MULT termino
    | factor DIV termino
    '''



def p_factor(p):
    '''
    factor : OPAREN expresion CPAREN 
    | PLUS varcte
    | MINUS varcte
    | varcte
    '''

def p_varcte(p):
    '''
    varcte : ID
    | ID asign2
    | NUMERIC
    | NUMBER
    '''

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
print(result)


# Patch notes - - - - - - - - - - - - - -

#Need to check asignacion
# test2 = (1+1); doesn't work. . . 
# test2 = 1+1; doesn't work. . .
# test2 = 1 + test doesn't work . . .
