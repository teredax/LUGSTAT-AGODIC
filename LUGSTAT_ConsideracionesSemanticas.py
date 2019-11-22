#Consideraciones Semanticas
#
#    tipo : INT
#    | BOOL 
#    | DOUBLE
#    | STRING
#    | CHAR
#    Aritmeticos
#t_PLUS    = r'\+'
#t_MINUS   = r'-'
#t_MULT   = r'\*'
#t_DIV  = r'/'
#t_PER = r'\%'
#Relacionales
#t_RELOP = r'==|<|>|<=|>=|!='
#t_GRE = r'<>'
#Asignacion
#t_EQUALS  = r'\='

class ConsideracionesSemanticas ():

        def __init__(self):
            self.Consideracion = {
                #INT
                'int' : { 'int': { #Entero y Entero
                    '+' : 'int', '-' : 'int', '*' : 'int', '/' : 'int', '%' : 'int', '=' : 'int',
                    '==' : 'bool', '<' : 'bool', '>' : 'bool', '<=' : 'bool', '>=' : 'bool','!=' : 'bool','<>' : 'bool',
                },
                'double' : { #Entero y doble
                    '+' : 'double', '-' : 'double', '*' : 'double', '/' : 'double', '%' : 'int', '=' : 'int',
                    '==' : 'bool', '<' : 'bool', '>' : 'bool', '<=' : 'bool', '>=' : 'bool','!=' : 'bool','<>' : 'bool',
                },
                'bool' : { #Entero y bool
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'char' : { #Entero y bool
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'string' : { #Entero y bool
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                }
                 },

                #DOUBLE
                 'double' : { 'int': { #doble y Entero
                    '+' : 'double', '-' : 'double', '*' : 'double', '/' : 'double', '%' : 'double', '=' : 'double',
                    '==' : 'bool', '<' : 'bool', '>' : 'bool', '<=' : 'bool', '>=' : 'bool','!=' : 'bool','<>' : 'bool',
                },
                'double' : { #doble y doble
                    '+' : 'double', '-' : 'double', '*' : 'double', '/' : 'double', '%' : 'double', '=' : 'double',
                    '==' : 'bool', '<' : 'bool', '>' : 'bool', '<=' : 'bool', '>=' : 'bool','!=' : 'bool','<>' : 'bool',
                },
                'bool' : { #doble y bool
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'char' : { #doble y char
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'string' : { #doble y string
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                }
                 },

                #BOOL
                 'bool' : { 'int': { #bool y Entero
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'double' : { #bool y doble
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'bool' : { #bool y bool
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'bool',
                    '==' : 'bool', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'bool','<>' : 'error',
                },
                'char' : { #bool y char
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'string' : { #bool y string
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                }
                 },

                #CHAR
                 'char' : { 'int': { #CHAR y Entero
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'double' : { #CHAR y doble
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'bool' : { #CHAR y bool
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'char' : { #CHAR y CHAR
                    '+' : 'char', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'char',
                    '==' : 'bool', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'bool','<>' : 'error',
                },
                'string' : { #CHAR y String
                    '+' : 'string', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error', #Revisar == y != como bools ?
                }
                 },

                #String
                 'String' : { 'int': { #String y Entero
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'double' : { #String y doble
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'bool' : { #String y bool
                    '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'error', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'error','<>' : 'error',
                },
                'char' : { #String y char
                    '+' : 'string', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'error',
                    '==' : 'bool', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'bool','<>' : 'error',  #Revisar == y != como bools ?
                },
                'string' : { #String y String
                    '+' : 'string', '-' : 'error', '*' : 'error', '/' : 'error', '%' : 'error', '=' : 'string',
                    '==' : 'bool', '<' : 'error', '>' : 'error', '<=' : 'error', '>=' : 'error','!=' : 'bool','<>' : 'error',
                }
                 }

            }

        def get_tipo(self, Izq, Der, operador):
            return self.Consideracion[Izq][Der][operador]

def main():
    print("reee")
    test = ConsideracionesSemanticas()
    print(test.get_tipo('int', 'bool', '*'))

if __name__== "__main__":
  main()
