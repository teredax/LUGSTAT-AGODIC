#Gonzalo Garcia A01281414
#Jesus Lugo A01089769
# Caso de prueba se pega en inputf.txt
#usando PLY (Lex / Yacc for python)



import ply.lex as lex
import ply.yacc as yacc

InputF= open("/Users/lugo/Documents/Clases/Compiladores/CompiladoresAgoDic/inputf.txt", "r") 
cache=InputF.read()
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'program' :'PROGRAM',
    'var' : 'VAR',
    'int' : 'INT',
    'bool': 'BOOL',
    'string':'STRING',
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
    'stdv' : 'STDV',
    'kmeans' : 'KMEANS',
    'derl' : 'DERL',
    'dpoi' : 'DPOI',
    'dbern' : 'DBERN',
    'ref' : 'REF',
    'rref' : 'RREF',
    'mont' : 'MONT',
    'xyfunction' : 'XYFUNCTION' ,
    'char' : 'CHAR',
    'func' : 'FUNC'
           }


tokens = [
        'PLUS', 'MINUS', 'MULT','DIV','EQUALS','OPAREN', 'STRING', 
        'CPAREN', 'ID','OBRACKET', 'CBRACKET', 'GREATERTHAN', 
        'LESSTHAN', 'GRE','COLON','SCOLON','COMMA', 'NUMBER',
        'PER','EQ','LESSEQ','GREATEQ','DIFF','LCOR','RCOR',
        'COMMENT','INTEGER','NUMERIC','LOGICAL','CHARACTER','QUOTE' , 'RELOP','CTEI','CTED','X','Y','MODE','ROTATE','TRANSPOSE','INVERSE'
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
t_STRING = r'\"[+-@#$^&*?!a-z/\s/A-Z][a-z/\s/A-Z0-9+-@#$^&*?!:]*\"'

#and or not relop ABD OR NOT 


t_ignore_COMMENT = r'\#.*'

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

#Tengo duda contra el diagrama por tanta recursion
def p_vars(p):
    '''
    vars : VAR vars3 COLON tipo SCOLON vars4
    '''

#Apoya a hacer el ciclo de variables
def p_vars1(p):
    '''
    vars1 : CTEI COMMA vars1
    | CTEI empty
    | empty '''

def p_vars2(p):
    '''
    vars2 : LCOR vars1 RCOR vars2
    | empty '''

def p_vars3(p):
    '''
    vars3 : ID COMMA vars3
    | ID vars2
    '''

def p_vars4(p):
    '''
    vars4 : vars3
    | empty'''


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
    asign : ID asign2 EQUALS expresion SCOLON
    | ID asign2 EQUALS ID asign2 SCOLON
    '''
def p_asign2(p):
    '''
    asign2 : LCOR expresion RCOR asign2
    | LCOR CTEI RCOR asign2
    | empty
    '''

def p_escrt(p):
    '''escrt : PRINT OPAREN expresion CPAREN SCOLON
	| PRINT OPAREN CPAREN SCOLON
	| PRINT OPAREN QUOTE ID QUOTE CPAREN SCOLON
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
    'count : COUNT ID CPAREN COMMA CTEI COMMA CTEI OPAREN SCOLON'

def p_countif(p):
    'countif : COUNTIF OPAREN ID COMMA CTEI COMMA CTEI COMMA cond OPAREN SCOLON'

def p_plot(p):
    '''plot : PLOT OPAREN func CPAREN SCOLON
    | PLOT OPAREN plot2 CPAREN SCOLON
    '''
def p_plot2(p):
    '''
    plot2 : LCOR plot3 COMMA plot3 RCOR plot2
    | LCOR plot3 COMMA plot3 RCOR
    '''

def p_plot3(p):
    '''
    plot3 : CTEI
    | CTED'''

def p_func(p):
    '''func : X EQUALS exp func2 SCOLON
    | Y EQUALS exp func2 SCOLON
    '''

def p_func2(p):
    '''
    func2 : func
    | empty
    '''

#RE REVISAR DIAGRAMA
def p_expresion(p):
    '''expresion : exp 
    | RELOP exp 
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
    factor : PLUS varcte
    | MINUS varcte
    | OPAREN expresion CPAREN
    '''

def p_varcte(p):
    '''
    varcte : ID
    | NUMBER
    | DOUBLE
    '''

def p_metodos(p):
    '''
    metodos : MEAN OPAREN metodos2 CPAREN SCOLON
    | MEDIAN OPAREN metodos2 CPAREN SCOLON
    | MODE OPAREN metodos2 CPAREN SCOLON
    | STDV OPAREN metodos2 CPAREN SCOLON
    | KMEANS OPAREN metodos2 CPAREN SCOLON
    | REF OPAREN metodos2 CPAREN SCOLON
    | RREF OPAREN metodos2 CPAREN SCOLON
    | MONT OPAREN metodos2 CPAREN SCOLON
    | DERL OPAREN ID COMMA ID COMMA ID CPAREN SCOLON
    | DBERN OPAREN ID COMMA ID COMMA ID CPAREN SCOLON
    | DPOI OPAREN ID COMMA ID CPAREN SCOLON
    | TRANSPOSE OPAREN metodos2 CPAREN SCOLON
    | INVERSE OPAREN metodos2 CPAREN SCOLON
    | ROTATE OPAREN metodos2 CPAREN SCOLON
    '''
def p_metodos2(p):
    '''
    metodos2 : ID 
    | metodos3
    '''
def p_metodos3(p):
    '''
    metodos3 : LCOR metodos4 RCOR metodos3
    | LCOR metodos4 RCOR
    '''

def p_metodos4(p):
    '''
    metodos4 : CTEI COMMA metodos4
    | CTEI COMMA
    | CTED COMMA metodos4
    | CTED COMMA
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
#[][] [2] trial[1] Corrected
#Need to check asignacion still not working
# test2 = (1+1); doesn't work. . . 
# test2 = 1+1; doesn't work. . .
# test2 = 1 + test doesn't work . . .
