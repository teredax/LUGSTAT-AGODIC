# CompiladoresAgoDic
Repositorio para nuestro proyecto para la clase de compiladores

 __        __    __   ______    ______   ________  ______   ________ 
/  |      /  |  /  | /      \  /      \ /        |/      \ /        |
$$ |      $$ |  $$ |/$$$$$$  |/$$$$$$  |$$$$$$$$//$$$$$$  |$$$$$$$$/ 
$$ |      $$ |  $$ |$$ | _$$/ $$ \__$$/    $$ |  $$ |__$$ |   $$ |   
$$ |      $$ |  $$ |$$ |/    |$$      \    $$ |  $$    $$ |   $$ |   
$$ |      $$ |  $$ |$$ |$$$$ | $$$$$$  |   $$ |  $$$$$$$$ |   $$ |   
$$ |_____ $$ \__$$ |$$ \__$$ |/  \__$$ |   $$ |  $$ |  $$ |   $$ |   
$$       |$$    $$/ $$    $$/ $$    $$/    $$ |  $$ |  $$ |   $$ |   
$$$$$$$$/  $$$$$$/   $$$$$$/   $$$$$$/     $$/   $$/   $$/    $$/    
                                                                     
                                                                    

Manual de usuario 

Pre requisitos:
Dependencias necesarias para versión funcional del código
Numpy que usamos como np
Pandas que usamos como pd
Matplotlib que usamos como plt
Sklearn.datasets
Sklearn clusters
Scipy.stats
Seabron que usamos como sb
Sympy 

La instalación de estas dependencias se hacen de la siguiente manera 
pip/ppip3 install nombre_dependencia desde consola.
Es necesario tener una versión de python 3.0 o mayor instalada. 
Ejecución
Es necesario contar con el archivo inputf.txt, aquí es donde tendremos nuestro código, para la lectura de un input diferente es necesario reemplazar el nombre del archivo por el que se desea compilar dentro de LUGSTAT.py en dondé en la linea 117 encontraremos InputF
#Aquí se ingresa el archivo a compilar
InputF= open("inputf.txt", "r")

Para ejecutar el programa solo es necesario el comando pyhton3/py LUGSTAT.py
Tipos de variables
Int
Double
Bool
String

Manejo de Sintaxis:

Main
----------------------------------------------------

LUGSTAT es el token de inicio para lugstat.
ID es el nombre de el main
SCOLON es ;
Lugstat2 es la función que va a las variables
Lugstat3 es la función que va a los módulos
lugstat : LUGSTAT ID SCOLON lugstat2 lugstat3 block

lugstat mimain;
var mivar1 : int;
func mifunc : int (param1: int;) {}
{}
Variables
----------------------------------------------------

“vars1” es la gramática para definir variables, brinca desde la regla vars donde esta el token “var” asign2 llama a la regla de declaracion de arreglos y matrices.

LUGSTAT solo permite declaraciones genéricas. 
Estas declaraciones se pueden juntar en una sola con commas si son del mismo tipo.
vars : VAR vars1 

vars1 : ID COMMA vars1
    | ID COLON tipo SCOLON lugstat2
    | ID asign2 COLON tipo SCOLON
    | ID asign2 COMMA vars1


----------------------------------------------------
Ejemplo
----------------------------------------------------
    
var mivar1 : int;
var mibool1, mibool2 :bool;
var midouble1, midobule2 :double;

Funciones
----------------------------------------------------
Modules es la declaración de los módulos o funciones adicionales. Inicia con FUNC
ID es el nombre del módulo
Tipo es el tipo de retorno

modules2 manda a llamar la declaración de variables, primero para parámetros luego las variables locales de la función. 

Funblock es el bloque de la función. 
modules : FUNC ID COLON tipo OPAREN  modules2 CPAREN modules2 funblock 


----------------------------------------------------
Ejemplo
----------------------------------------------------

func mifunc : int (param1: int;)
var mivlocal1: int;
{}

Bloques
----------------------------------------------------
Los bloques son estatutos rodeados por brackets.

Dentro de los estatutos están todas las funciones y operaciones. 
block : OBRACKET block2 CBRACKET

 '''
block2 : estatuto
| estatuto block2
| empty'''


Estatutos basicos
----------------------------------------------------

Estos son los estatutos básicos, cada uno manda a su regla.  
Entre ellos están el de asignación, las condiciones, estructura, do while, llamada a función y al read line. 


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


Asignacion
----------------------------------------------------
LUGSTAT permite varios tipos de asignación, ya sea el resultado de una expresión, igualar variables, igualar el contenido de un arreglo y operaciones de arreglos en general.
'''
asign : ID EQUALS expresion SCOLON
| ID EQUALS ID SCOLON
| ID EQUALS ID asign2 SCOLON
| ID asign2 EQUALS ID SCOLON
| ID assign2 EQUALS expresion SCOLON
| ID asign2 EQUALS ID asign2 SCOLON
'''


----------------------------------------------------
Ejemplo
----------------------------------------------------

Var1 = 1+1*(100/10);
Var1 = Var2;
Var1 = Arr1[1];
Arr1[2+1] = Arr2[3+i];
. . .
Arr1[2] = 1*3;



Escritura
----------------------------------------------------

El estatuto de escritura de LUGSTAT escrt permite juntar predicados con commas y imprimirlos, ya sean variables, expresiones  o strings. 
'''escrt : PRINT OPAREN ID escrt2 CPAREN SCOLON
| PRINT OPAREN expresion CPAREN SCOLON
| PRINT OPAREN STRING CPAREN SCOLON
'''
----------------------------------------------------
Ejemplo
----------------------------------------------------

Print (var1);
print(var1, var2);
print(1+1);
print(“hola mundo!”);


Condiciones
----------------------------------------------------


LUGSTAT soporta estatutos condicionales tipo IF y IF - ELSE para expresiones con operadores relacionales == , < ,> ,<= ,>= ,!=
'''cond : IF OPAREN expresion CPAREN ifblock SCOLON
| IF OPAREN expresion CPAREN ifblock ELSE ifblock SCOLON
'''

----------------------------------------------------
Ejemplo
----------------------------------------------------


If (a > b) {};
. . .
If (a > b) {} else {};

Expresiones
----------------------------------------------------


El manejo de expresiones de LUGSTAT está basado en el de littleduck2019. 
'''expresion : exp 
    | expresion RELOP exp 
'''

'''exp : termino
    | termino PLUS exp
    | termino MINUS exp
'''

'''termino : factor
    | factor MULT termino
    | factor DIV termino
'''

'''factor : OPAREN expresion CPAREN 
    | varcte
'''

'''varcte : ID
    | ID asign2
    | NUMERIC
    | NUMBER
'''



Do-While
----------------------------------------------------

La manera que hace lugstat sus ciclos es usando DO - WHILE
'''dwhile : DO wblock WHILE OPAREN dwhileconds CPAREN SCOLON 
'''


Read Line
----------------------------------------------------

LUGSTAT soporta inputs por el usuario usando la función read, lee y asigna a la variable lo que se leyó. 

''' readln : READ OPAREN ID CPAREN SCOLON '''


read(k);

Funciones especiales
----------------------------------------------------

mean(Arreglo de enteros); 
--@Función que imprime el promedio de una lista, recibe como parámetro un arreglo de enteros. 

median(Arreglo de enteros); 
--@Función que imprime la mediana de una lista, recibe como parámetro un arreglo de enteros. 

mode(Arreglo de enteros); 
--@Función que imprime la moda de una lista, recibe como parámetro un arreglo de enteros. 

stdv(Arreglo de enteros); 
--@Función que regresa la mediana de una lista, recibe como parámetro un arreglo de enteros. 

kmeans(Nclusters,Arreglo de enteros); 
--@Función que genera una gráfica a partir del número de clusters, recibe como parámetro un entero y un arreglo de enteros. 

derl(i1,i2,i3); 
--@Función que genera una gráfica a partir de los parámetros con distribución de erlang, recibe como parámetro tres entero y un arreglo de enteros. 

dbern(Nclusters,Arreglo de enteros); 
--@Función que genera una gráfica con distribución de bernoulli a partir del tamaño y esperanza, recibe como parámetro un entero y un doble. 

dpoi(Nclusters,Arreglo de enteros); 
--@Función que genera una gráfica con distribución poisson a partir del tamaño y esperanza, recibe como parámetro un entero y un doble. 

transpose(Matriz de enteros); 
--@Función que despliega una matriz  en su forma transpuesta recibe como parámetro una matriz de enteros o dobles. 

inverse(Matriz de enteros); 
--@Función que despliega una matriz  en su forma inversa recibe como parámetro una matriz de enteros o dobles. 

rotate(Matriz de enteros); 
--@Función que despliega una matriz  en su forma rotada recibe como parámetro una matriz de enteros o dobles. 

