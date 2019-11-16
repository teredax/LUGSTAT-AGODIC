
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CBRACKET CHAR CHARACTER COLON COMMA COMMENT COUNT COUNTIF CPAREN CTED CTEI DBERN DERL DIFF DIV DO DOUBLE DPOI ELSE EQ EQUALS FUNC FX FY GRE GREATEQ GREATERTHAN ID IF INT INTEGER INVERSE KMEANS LCOR LESSEQ LESSTHAN LOGICAL LUGSTAT MEAN MEDIAN MINUS MODE MONT MULT NUMBER NUMERIC OBRACKET OPAREN OR PER PLOT PLUS PRINT QUOTE RCOR READ REF RELOP ROTATE RREF SCOLON STDV STRING TIPO TRANSPOSE VAR WHILE\n    lugstat : LUGSTAT ID SCOLON addmain lugstat2 lugstat3 block\n    addmain : empty\n    lugstat2 : vars\n    | empty\n    \n    lugstat3 : modules\n    | modules lugstat3\n    | empty\n    vars : VAR vars1 \n     \n    vars1 : ID COMMA vars1\n    | ID COLON tipo SCOLON lugstat2\n    | ID asign2 COLON tipo SCOLON\n    | ID asign2 COMMA vars1\n    savename : empty\n    modules : FUNC ID COLON tipo addfunction OPAREN modules2 CPAREN modules2 blockaddfunction : empty\n    modules2 : vars\n    | empty\n    block : OBRACKET block2 CBRACKET\n    \n    block2 : estatuto\n    | estatuto block2\n    | empty\n    tipo : INT\n    | BOOL \n    | DOUBLE\n    | STRING\n    | CHAR\n    \n    estatuto : asign\n    | cond \n    | escrt\n    | plot\n    | count\n    | countif\n    | metodos\n    | dwhile\n    | readln\n    \n    asign : ID EQUALS expresion SCOLON\n    | ID EQUALS ID SCOLON\n    | ID EQUALS ID asign2 SCOLON\n    | ID asign2 EQUALS ID SCOLON\n    | ID asign2 EQUALS expresion SCOLON\n    | ID asign2 EQUALS ID asign2 SCOLON\n    \n    asign2 : LCOR expresion RCOR asign3\n    | LCOR varcte RCOR asign3 \n    \n    asign3 : LCOR expresion RCOR\n    | LCOR varcte RCOR \n    | emptyescrt : PRINT OPAREN ID en3 escrt2 CPAREN SCOLON\n    | PRINT OPAREN expresion en1 CPAREN SCOLON\n    | PRINT OPAREN STRING CPAREN en2 SCOLON\n    escrt2 : COMMA escrt3\n    | empty\n    escrt3 : ID escrt2\n    | ID\n    | STRING escrt2 escrt2\n    en1 : emptyen2 : emptyen3 : emptycond : IF OPAREN expresion cn1 CPAREN ifblock SCOLON cn2\n    | IF OPAREN expresion cn1 CPAREN ifblock ELSE cn3 ifblock SCOLON cn2\n    cn1 : emptycn2 : emptycn3 : empty\n    ifblock : OBRACKET ifblock2 CBRACKET\n    \n    ifblock2 : estatuto\n    | estatuto ifblock2\n    | emptycount : COUNT OPAREN ID COMMA varcte COMMA varcte CPAREN SCOLONcountif : COUNTIF OPAREN ID COMMA varcte COMMA varcte COMMA cond CPAREN SCOLONplot : PLOT OPAREN xyfunc CPAREN SCOLON\n    | PLOT OPAREN plot2 CPAREN SCOLON\n    \n    plot2 : LCOR varcte COMMA varcte RCOR\n    | LCOR varcte COMMA varcte RCOR COMMA plot2\n    | empty\n    xyfunc : FX EQUALS exp SCOLON xyfunc\n    | FY EQUALS exp SCOLON xyfunc\n    | empty\n    expresion : exp \n    | expresion RELOP exp \n    \n    exp : termino\n    | termino PLUS exp\n    | termino MINUS exp\n    \n    termino : factor\n    | factor MULT termino\n    | factor DIV termino\n    \n    factor : OPAREN expresion CPAREN \n    | varcte\n    \n    varcte : ID\n    | ID asign2\n    | NUMERIC\n    | NUMBER\n    \n    dwhile : DO wn1 wblock WHILE OPAREN dwhileconds CPAREN wn2 SCOLON \n    wn1 : emptywn2 : empty\n    wblock : OBRACKET block2 CBRACKET   \n    \n    dwhileconds : expresion dwhileconds\n    | expresion AND dwhileconds\n    | expresion OR dwhileconds\n    | empty\n     readln : READ OPAREN ID rn1 CPAREN SCOLON rn1 : empty \n    metodos : MEAN OPAREN mmmfunc CPAREN SCOLON\n    | MEDIAN OPAREN mmmfunc CPAREN SCOLON\n    | MODE OPAREN mmmfunc CPAREN SCOLON\n    | STDV OPAREN mmmfunc CPAREN SCOLON\n    | KMEANS OPAREN varcte COMMA mmmfunc CPAREN SCOLON\n    | DERL OPAREN expfunc CPAREN SCOLON\n    | DBERN OPAREN expfunc CPAREN SCOLON\n    | DPOI OPAREN expfunc2 CPAREN SCOLON\n    | TRANSPOSE OPAREN mmmfunc CPAREN SCOLON\n    | INVERSE OPAREN mmmfunc CPAREN SCOLON\n    | ROTATE OPAREN mmmfunc CPAREN SCOLON\n    | REF OPAREN mmmfunc CPAREN SCOLON\n    | RREF OPAREN mmmfunc CPAREN SCOLON\n    | MONT OPAREN mmmfunc CPAREN SCOLON\n    \n    expfunc : ID COMMA ID COMMA ID\n    | varcte COMMA varcte COMMA varcte\n    \n    expfunc2 : ID COMMA ID\n    | varcte COMMA varcte\n    \n    mmmfunc : ID \n    | OBRACKET  mmmarray CBRACKET\n\t| OBRACKET mmmarray CBRACKET COMMA mmmfunc\n\t| empty \n    \n    mmmarray : varcte\n    | varcte COMMA mmmarray\n    | empty\n    empty :'
    
_lr_action_items = {'LUGSTAT':([0,],[2,]),'$end':([1,17,78,],[0,-1,-18,]),'ID':([2,10,14,18,21,24,26,28,29,30,31,32,33,34,35,36,68,71,72,73,74,75,76,77,80,82,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,108,109,110,111,112,113,114,115,117,120,130,135,155,161,162,163,164,165,166,167,168,169,170,171,173,185,186,188,189,197,199,200,203,204,218,220,221,224,229,230,233,236,238,239,240,241,243,246,247,250,251,252,253,254,255,256,262,263,264,266,271,272,276,277,278,281,282,284,286,288,291,293,303,308,309,311,312,329,331,332,334,335,],[3,16,20,37,16,72,37,-27,-28,-29,-30,-31,-32,-33,-34,-35,16,-77,-87,-89,-90,-79,-82,72,118,72,122,131,132,134,134,134,134,72,142,142,146,134,134,134,134,134,134,156,-126,72,-126,-88,72,72,72,72,-86,174,72,72,37,72,-42,-46,-78,-43,-80,-81,-83,-84,-85,-37,-36,72,72,72,72,134,244,72,248,72,-38,-39,-40,269,-69,-70,72,-101,72,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,72,-44,-45,-41,37,-48,-49,72,72,134,304,72,72,-99,-126,37,-47,-105,72,72,-58,-61,-67,-91,-126,-59,-68,]),'SCOLON':([3,61,62,63,64,65,66,71,72,73,74,75,76,106,108,110,111,117,118,119,162,163,164,165,166,167,168,169,170,172,174,175,182,183,184,190,194,195,196,198,201,202,205,206,207,208,209,210,219,226,227,228,231,232,258,262,263,265,267,280,306,315,319,321,322,326,333,],[4,105,-22,-23,-24,-25,-26,-77,-87,-89,-90,-79,-82,160,-126,-126,-88,-86,171,173,-42,-46,-78,-43,-80,-81,-83,-84,-85,218,220,221,-126,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,271,272,-56,273,274,286,-44,-45,288,293,303,-126,-63,329,331,-93,332,335,]),'VAR':([4,5,6,105,215,287,],[-126,10,-2,10,10,10,]),'FUNC':([4,5,6,7,8,9,12,15,60,78,105,107,159,160,325,],[-126,-126,-2,14,-3,-4,14,-8,-9,-18,-126,-12,-10,-11,-14,]),'OBRACKET':([4,5,6,7,8,9,11,12,13,15,19,57,60,78,87,88,89,90,95,96,97,98,99,100,101,102,105,107,159,160,197,222,260,261,278,287,289,310,313,314,325,],[-126,-126,-2,-126,-3,-4,18,-5,-7,-8,-6,-126,-9,-18,135,135,135,135,135,135,135,135,135,135,155,-92,-126,-12,-10,-11,135,266,-16,-17,135,-126,-126,18,266,-62,-14,]),'CPAREN':([8,9,15,60,71,72,73,74,75,76,84,87,88,89,90,95,96,97,98,99,100,105,107,108,110,111,116,117,121,122,123,124,125,126,129,133,134,136,137,138,139,141,144,145,148,149,150,151,152,153,156,159,160,162,163,164,165,166,167,168,169,170,176,177,178,179,180,181,197,213,214,215,223,225,237,242,248,249,256,259,260,261,262,263,268,269,270,273,274,278,283,284,285,288,294,295,296,297,298,299,300,302,304,305,307,308,309,311,312,317,318,323,324,327,328,330,332,334,],[-3,-4,-8,-9,-77,-87,-89,-90,-79,-82,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-126,-12,-126,-126,-88,170,-86,-126,-87,-126,182,183,184,-73,190,-119,-122,194,195,196,198,201,202,205,206,207,208,209,210,-126,-10,-11,-42,-46,-78,-43,-80,-81,-83,-84,-85,222,-60,-126,-57,226,-55,-126,258,-100,-126,267,-51,-120,280,-117,-118,-126,287,-16,-17,-44,-45,-50,-53,-126,-126,-126,-126,306,-126,-98,-126,-52,-126,-74,-76,-75,-71,319,-121,-115,-116,-95,-126,-126,-58,-61,-54,-126,-96,-97,-72,-73,333,-126,-59,]),'COMMA':([16,23,72,73,74,108,110,111,122,131,132,140,142,143,146,147,162,163,165,178,179,187,192,225,234,235,237,244,245,262,263,268,269,270,294,295,299,301,317,],[21,68,-87,-89,-90,-126,-126,-88,-126,188,189,197,199,200,203,204,-42,-46,-43,224,-57,233,238,-51,276,277,278,281,282,-44,-45,-50,224,224,-52,224,318,320,-54,]),'COLON':([16,20,23,108,110,162,163,165,262,263,],[22,59,67,-126,-126,-42,-46,-43,-44,-45,]),'LCOR':([16,37,72,84,108,110,118,122,142,146,174,318,],[24,24,24,130,161,161,24,24,24,24,24,130,]),'CBRACKET':([18,25,26,27,28,29,30,31,32,33,34,35,36,72,73,74,79,108,110,111,135,155,162,163,165,171,173,191,192,193,212,218,220,221,229,230,236,238,239,240,241,243,246,247,250,251,252,253,254,255,262,263,264,266,271,272,279,286,288,290,291,292,293,303,311,312,316,329,331,332,334,335,],[-126,78,-19,-21,-27,-28,-29,-30,-31,-32,-33,-34,-35,-87,-89,-90,-20,-126,-126,-88,-126,-126,-42,-46,-43,-37,-36,237,-123,-125,257,-38,-39,-40,-69,-70,-101,-126,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-44,-45,-41,-126,-48,-49,-124,-99,-126,315,-64,-66,-47,-105,-58,-61,-65,-67,-91,-126,-59,-68,]),'IF':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,320,329,331,332,334,335,],[38,38,-27,-28,-29,-30,-31,-32,-33,-34,-35,38,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,38,-48,-49,-99,-126,38,-47,-105,-58,-61,38,-67,-91,-126,-59,-68,]),'PRINT':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[39,39,-27,-28,-29,-30,-31,-32,-33,-34,-35,39,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,39,-48,-49,-99,-126,39,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'PLOT':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[40,40,-27,-28,-29,-30,-31,-32,-33,-34,-35,40,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,40,-48,-49,-99,-126,40,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'COUNT':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[41,41,-27,-28,-29,-30,-31,-32,-33,-34,-35,41,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,41,-48,-49,-99,-126,41,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'COUNTIF':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[42,42,-27,-28,-29,-30,-31,-32,-33,-34,-35,42,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,42,-48,-49,-99,-126,42,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'MEAN':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[43,43,-27,-28,-29,-30,-31,-32,-33,-34,-35,43,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,43,-48,-49,-99,-126,43,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'MEDIAN':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[44,44,-27,-28,-29,-30,-31,-32,-33,-34,-35,44,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,44,-48,-49,-99,-126,44,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'MODE':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[45,45,-27,-28,-29,-30,-31,-32,-33,-34,-35,45,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,45,-48,-49,-99,-126,45,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'STDV':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[46,46,-27,-28,-29,-30,-31,-32,-33,-34,-35,46,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,46,-48,-49,-99,-126,46,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'KMEANS':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[47,47,-27,-28,-29,-30,-31,-32,-33,-34,-35,47,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,47,-48,-49,-99,-126,47,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'DERL':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[48,48,-27,-28,-29,-30,-31,-32,-33,-34,-35,48,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,48,-48,-49,-99,-126,48,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'DBERN':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[49,49,-27,-28,-29,-30,-31,-32,-33,-34,-35,49,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,49,-48,-49,-99,-126,49,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'DPOI':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[50,50,-27,-28,-29,-30,-31,-32,-33,-34,-35,50,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,50,-48,-49,-99,-126,50,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'TRANSPOSE':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[51,51,-27,-28,-29,-30,-31,-32,-33,-34,-35,51,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,51,-48,-49,-99,-126,51,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'INVERSE':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[52,52,-27,-28,-29,-30,-31,-32,-33,-34,-35,52,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,52,-48,-49,-99,-126,52,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'ROTATE':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[53,53,-27,-28,-29,-30,-31,-32,-33,-34,-35,53,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,53,-48,-49,-99,-126,53,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'REF':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[54,54,-27,-28,-29,-30,-31,-32,-33,-34,-35,54,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,54,-48,-49,-99,-126,54,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'RREF':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[55,55,-27,-28,-29,-30,-31,-32,-33,-34,-35,55,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,55,-48,-49,-99,-126,55,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'MONT':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[56,56,-27,-28,-29,-30,-31,-32,-33,-34,-35,56,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,56,-48,-49,-99,-126,56,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'DO':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[57,57,-27,-28,-29,-30,-31,-32,-33,-34,-35,57,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,57,-48,-49,-99,-126,57,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'READ':([18,26,28,29,30,31,32,33,34,35,36,155,171,173,218,220,221,229,230,236,239,240,241,243,246,247,250,251,252,253,254,255,264,266,271,272,286,288,291,293,303,311,312,329,331,332,334,335,],[58,58,-27,-28,-29,-30,-31,-32,-33,-34,-35,58,-37,-36,-38,-39,-40,-69,-70,-101,-102,-103,-104,-106,-107,-108,-109,-110,-111,-112,-113,-114,-41,58,-48,-49,-99,-126,58,-47,-105,-58,-61,-67,-91,-126,-59,-68,]),'INT':([22,59,67,],[62,62,62,]),'BOOL':([22,59,67,],[63,63,63,]),'DOUBLE':([22,59,67,],[64,64,64,]),'STRING':([22,59,67,83,224,],[65,65,65,124,270,]),'CHAR':([22,59,67,],[66,66,66,]),'NUMERIC':([24,71,72,73,74,75,76,77,80,82,83,91,92,93,94,108,109,110,111,112,113,114,115,117,120,130,135,161,162,163,164,165,166,167,168,169,170,185,186,188,189,200,204,233,238,256,262,263,276,277,282,284,308,309,],[73,-77,-87,-89,-90,-79,-82,73,73,73,73,73,73,73,73,-126,73,-126,-88,73,73,73,73,-86,73,73,73,73,-42,-46,-78,-43,-80,-81,-83,-84,-85,73,73,73,73,73,73,73,73,73,-44,-45,73,73,73,73,73,73,]),'NUMBER':([24,71,72,73,74,75,76,77,80,82,83,91,92,93,94,108,109,110,111,112,113,114,115,117,120,130,135,161,162,163,164,165,166,167,168,169,170,185,186,188,189,200,204,233,238,256,262,263,276,277,282,284,308,309,],[74,-77,-87,-89,-90,-79,-82,74,74,74,74,74,74,74,74,-126,74,-126,-88,74,74,74,74,-86,74,74,74,74,-42,-46,-78,-43,-80,-81,-83,-84,-85,74,74,74,74,74,74,74,74,74,-44,-45,74,74,74,74,74,74,]),'OPAREN':([24,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,62,63,64,65,66,71,72,73,74,75,76,77,80,82,83,104,108,109,110,111,112,113,114,115,117,120,157,158,161,162,163,164,165,166,167,168,169,170,185,186,211,256,262,263,284,308,309,],[77,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,-22,-23,-24,-25,-26,-77,-87,-89,-90,-79,-82,77,77,77,77,-126,-126,77,-126,-88,77,77,77,77,-86,77,215,-15,77,-42,-46,-78,-43,-80,-81,-83,-84,-85,77,77,256,77,-44,-45,77,77,77,]),'EQUALS':([37,81,108,110,127,128,162,163,165,262,263,],[80,120,-126,-126,185,186,-42,-46,-43,-44,-45,]),'RCOR':([69,70,71,72,73,74,75,76,108,110,111,117,162,163,164,165,166,167,168,169,170,216,217,262,263,275,],[108,110,-77,-87,-89,-90,-79,-82,-126,-126,-88,-86,-42,-46,-78,-43,-80,-81,-83,-84,-85,262,263,-44,-45,299,]),'RELOP':([69,70,71,72,73,74,75,76,108,110,111,116,117,118,119,121,122,123,162,163,164,165,166,167,168,169,170,172,174,175,216,217,219,262,263,284,],[109,-86,-77,-87,-89,-90,-79,-82,-126,-126,-88,109,-86,-87,109,109,-87,109,-42,-46,-78,-43,-80,-81,-83,-84,-85,-88,-87,109,109,-86,-88,-44,-45,109,]),'MULT':([70,72,73,74,76,108,110,111,117,118,122,162,163,165,170,172,174,217,219,262,263,],[-86,-87,-89,-90,114,-126,-126,-88,-86,-87,-87,-42,-46,-43,-85,-88,-87,-86,-88,-44,-45,]),'DIV':([70,72,73,74,76,108,110,111,117,118,122,162,163,165,170,172,174,217,219,262,263,],[-86,-87,-89,-90,115,-126,-126,-88,-86,-87,-87,-42,-46,-43,-85,-88,-87,-86,-88,-44,-45,]),'PLUS':([70,72,73,74,75,76,108,110,111,117,118,122,162,163,165,168,169,170,172,174,217,219,262,263,],[-86,-87,-89,-90,112,-82,-126,-126,-88,-86,-87,-87,-42,-46,-43,-83,-84,-85,-88,-87,-86,-88,-44,-45,]),'MINUS':([70,72,73,74,75,76,108,110,111,117,118,122,162,163,165,168,169,170,172,174,217,219,262,263,],[-86,-87,-89,-90,113,-82,-126,-126,-88,-86,-87,-87,-42,-46,-43,-83,-84,-85,-88,-87,-86,-88,-44,-45,]),'AND':([71,72,73,74,75,76,108,110,111,117,162,163,164,165,166,167,168,169,170,262,263,284,],[-77,-87,-89,-90,-79,-82,-126,-126,-88,-86,-42,-46,-78,-43,-80,-81,-83,-84,-85,-44,-45,308,]),'OR':([71,72,73,74,75,76,108,110,111,117,162,163,164,165,166,167,168,169,170,262,263,284,],[-77,-87,-89,-90,-79,-82,-126,-126,-88,-86,-42,-46,-78,-43,-80,-81,-83,-84,-85,-44,-45,309,]),'FX':([84,273,274,],[127,127,127,]),'FY':([84,273,274,],[128,128,128,]),'WHILE':([154,257,],[211,-94,]),'ELSE':([265,315,],[289,-63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lugstat':([0,],[1,]),'addmain':([4,],[5,]),'empty':([4,5,7,12,18,26,57,84,87,88,89,90,95,96,97,98,99,100,104,105,108,110,121,122,123,135,155,156,178,182,197,215,238,256,266,269,270,273,274,278,284,287,288,289,291,295,306,308,309,318,332,],[6,9,13,13,27,27,102,129,136,136,136,136,136,136,136,136,136,136,158,9,163,163,177,179,181,193,27,214,225,228,136,261,193,285,292,225,225,297,297,136,285,261,312,314,292,225,322,285,285,328,312,]),'lugstat2':([5,105,],[7,159,]),'vars':([5,105,215,287,],[8,8,260,260,]),'lugstat3':([7,12,],[11,19,]),'modules':([7,12,],[12,12,]),'vars1':([10,21,68,],[15,60,107,]),'block':([11,310,],[17,325,]),'asign2':([16,37,72,118,122,142,146,174,],[23,81,111,172,111,111,111,219,]),'block2':([18,26,155,],[25,79,212,]),'estatuto':([18,26,155,266,291,],[26,26,26,291,291,]),'asign':([18,26,155,266,291,],[28,28,28,28,28,]),'cond':([18,26,155,266,291,320,],[29,29,29,29,29,330,]),'escrt':([18,26,155,266,291,],[30,30,30,30,30,]),'plot':([18,26,155,266,291,],[31,31,31,31,31,]),'count':([18,26,155,266,291,],[32,32,32,32,32,]),'countif':([18,26,155,266,291,],[33,33,33,33,33,]),'metodos':([18,26,155,266,291,],[34,34,34,34,34,]),'dwhile':([18,26,155,266,291,],[35,35,35,35,35,]),'readln':([18,26,155,266,291,],[36,36,36,36,36,]),'tipo':([22,59,67,],[61,104,106,]),'expresion':([24,77,80,82,83,120,161,256,284,308,309,],[69,116,119,121,123,175,216,284,284,284,284,]),'varcte':([24,77,80,82,83,91,92,93,94,109,112,113,114,115,120,130,135,161,185,186,188,189,200,204,233,238,256,276,277,282,284,308,309,],[70,117,117,117,117,140,143,143,147,117,117,117,117,117,117,187,192,217,117,117,234,235,245,249,275,192,117,300,301,305,117,117,117,]),'exp':([24,77,80,82,83,109,112,113,120,161,185,186,256,284,308,309,],[71,71,71,71,71,164,166,167,71,71,231,232,71,71,71,71,]),'termino':([24,77,80,82,83,109,112,113,114,115,120,161,185,186,256,284,308,309,],[75,75,75,75,75,75,75,75,168,169,75,75,75,75,75,75,75,75,]),'factor':([24,77,80,82,83,109,112,113,114,115,120,161,185,186,256,284,308,309,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'wn1':([57,],[101,]),'xyfunc':([84,273,274,],[125,296,298,]),'plot2':([84,318,],[126,327,]),'mmmfunc':([87,88,89,90,95,96,97,98,99,100,197,278,],[133,137,138,139,148,149,150,151,152,153,242,302,]),'expfunc':([92,93,],[141,144,]),'expfunc2':([94,],[145,]),'wblock':([101,],[154,]),'addfunction':([104,],[157,]),'asign3':([108,110,],[162,165,]),'cn1':([121,],[176,]),'en3':([122,],[178,]),'en1':([123,],[180,]),'mmmarray':([135,238,],[191,279,]),'rn1':([156,],[213,]),'escrt2':([178,269,270,295,],[223,294,295,317,]),'en2':([182,],[227,]),'modules2':([215,287,],[259,310,]),'ifblock':([222,313,],[265,326,]),'escrt3':([224,],[268,]),'dwhileconds':([256,284,308,309,],[283,307,323,324,]),'ifblock2':([266,291,],[290,316,]),'cn2':([288,332,],[311,334,]),'cn3':([289,],[313,]),'wn2':([306,],[321,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lugstat","S'",1,None,None,None),
  ('lugstat -> LUGSTAT ID SCOLON addmain lugstat2 lugstat3 block','lugstat',7,'p_lugstat','LUGSTAT.py',212),
  ('addmain -> empty','addmain',1,'p_addmain','LUGSTAT.py',216),
  ('lugstat2 -> vars','lugstat2',1,'p_lugstat2','LUGSTAT.py',227),
  ('lugstat2 -> empty','lugstat2',1,'p_lugstat2','LUGSTAT.py',228),
  ('lugstat3 -> modules','lugstat3',1,'p_lugstat3','LUGSTAT.py',233),
  ('lugstat3 -> modules lugstat3','lugstat3',2,'p_lugstat3','LUGSTAT.py',234),
  ('lugstat3 -> empty','lugstat3',1,'p_lugstat3','LUGSTAT.py',235),
  ('vars -> VAR vars1','vars',2,'p_vars','LUGSTAT.py',239),
  ('vars1 -> ID COMMA vars1','vars1',3,'p_vars1','LUGSTAT.py',275),
  ('vars1 -> ID COLON tipo SCOLON lugstat2','vars1',5,'p_vars1','LUGSTAT.py',276),
  ('vars1 -> ID asign2 COLON tipo SCOLON','vars1',5,'p_vars1','LUGSTAT.py',277),
  ('vars1 -> ID asign2 COMMA vars1','vars1',4,'p_vars1','LUGSTAT.py',278),
  ('savename -> empty','savename',1,'p_savename','LUGSTAT.py',304),
  ('modules -> FUNC ID COLON tipo addfunction OPAREN modules2 CPAREN modules2 block','modules',10,'p_modules','LUGSTAT.py',308),
  ('addfunction -> empty','addfunction',1,'p_addfunction','LUGSTAT.py',312),
  ('modules2 -> vars','modules2',1,'p_modules2','LUGSTAT.py',320),
  ('modules2 -> empty','modules2',1,'p_modules2','LUGSTAT.py',321),
  ('block -> OBRACKET block2 CBRACKET','block',3,'p_block','LUGSTAT.py',327),
  ('block2 -> estatuto','block2',1,'p_block2','LUGSTAT.py',338),
  ('block2 -> estatuto block2','block2',2,'p_block2','LUGSTAT.py',339),
  ('block2 -> empty','block2',1,'p_block2','LUGSTAT.py',340),
  ('tipo -> INT','tipo',1,'p_tipo','LUGSTAT.py',344),
  ('tipo -> BOOL','tipo',1,'p_tipo','LUGSTAT.py',345),
  ('tipo -> DOUBLE','tipo',1,'p_tipo','LUGSTAT.py',346),
  ('tipo -> STRING','tipo',1,'p_tipo','LUGSTAT.py',347),
  ('tipo -> CHAR','tipo',1,'p_tipo','LUGSTAT.py',348),
  ('estatuto -> asign','estatuto',1,'p_estatuto','LUGSTAT.py',354),
  ('estatuto -> cond','estatuto',1,'p_estatuto','LUGSTAT.py',355),
  ('estatuto -> escrt','estatuto',1,'p_estatuto','LUGSTAT.py',356),
  ('estatuto -> plot','estatuto',1,'p_estatuto','LUGSTAT.py',357),
  ('estatuto -> count','estatuto',1,'p_estatuto','LUGSTAT.py',358),
  ('estatuto -> countif','estatuto',1,'p_estatuto','LUGSTAT.py',359),
  ('estatuto -> metodos','estatuto',1,'p_estatuto','LUGSTAT.py',360),
  ('estatuto -> dwhile','estatuto',1,'p_estatuto','LUGSTAT.py',361),
  ('estatuto -> readln','estatuto',1,'p_estatuto','LUGSTAT.py',362),
  ('asign -> ID EQUALS expresion SCOLON','asign',4,'p_asign','LUGSTAT.py',367),
  ('asign -> ID EQUALS ID SCOLON','asign',4,'p_asign','LUGSTAT.py',368),
  ('asign -> ID EQUALS ID asign2 SCOLON','asign',5,'p_asign','LUGSTAT.py',369),
  ('asign -> ID asign2 EQUALS ID SCOLON','asign',5,'p_asign','LUGSTAT.py',370),
  ('asign -> ID asign2 EQUALS expresion SCOLON','asign',5,'p_asign','LUGSTAT.py',371),
  ('asign -> ID asign2 EQUALS ID asign2 SCOLON','asign',6,'p_asign','LUGSTAT.py',372),
  ('asign2 -> LCOR expresion RCOR asign3','asign2',4,'p_asign2','LUGSTAT.py',429),
  ('asign2 -> LCOR varcte RCOR asign3','asign2',4,'p_asign2','LUGSTAT.py',430),
  ('asign3 -> LCOR expresion RCOR','asign3',3,'p_asign3','LUGSTAT.py',435),
  ('asign3 -> LCOR varcte RCOR','asign3',3,'p_asign3','LUGSTAT.py',436),
  ('asign3 -> empty','asign3',1,'p_asign3','LUGSTAT.py',437),
  ('escrt -> PRINT OPAREN ID en3 escrt2 CPAREN SCOLON','escrt',7,'p_escrt','LUGSTAT.py',441),
  ('escrt -> PRINT OPAREN expresion en1 CPAREN SCOLON','escrt',6,'p_escrt','LUGSTAT.py',442),
  ('escrt -> PRINT OPAREN STRING CPAREN en2 SCOLON','escrt',6,'p_escrt','LUGSTAT.py',443),
  ('escrt2 -> COMMA escrt3','escrt2',2,'p_escrt2','LUGSTAT.py',447),
  ('escrt2 -> empty','escrt2',1,'p_escrt2','LUGSTAT.py',448),
  ('escrt3 -> ID escrt2','escrt3',2,'p_escrt3','LUGSTAT.py',452),
  ('escrt3 -> ID','escrt3',1,'p_escrt3','LUGSTAT.py',453),
  ('escrt3 -> STRING escrt2 escrt2','escrt3',3,'p_escrt3','LUGSTAT.py',454),
  ('en1 -> empty','en1',1,'p_en1','LUGSTAT.py',458),
  ('en2 -> empty','en2',1,'p_en2','LUGSTAT.py',467),
  ('en3 -> empty','en3',1,'p_en3','LUGSTAT.py',475),
  ('cond -> IF OPAREN expresion cn1 CPAREN ifblock SCOLON cn2','cond',8,'p_cond','LUGSTAT.py',499),
  ('cond -> IF OPAREN expresion cn1 CPAREN ifblock ELSE cn3 ifblock SCOLON cn2','cond',11,'p_cond','LUGSTAT.py',500),
  ('cn1 -> empty','cn1',1,'p_cn1','LUGSTAT.py',504),
  ('cn2 -> empty','cn2',1,'p_cn2','LUGSTAT.py',520),
  ('cn3 -> empty','cn3',1,'p_cn3','LUGSTAT.py',527),
  ('ifblock -> OBRACKET ifblock2 CBRACKET','ifblock',3,'p_ifblock','LUGSTAT.py',540),
  ('ifblock2 -> estatuto','ifblock2',1,'p_ifblock2','LUGSTAT.py',544),
  ('ifblock2 -> estatuto ifblock2','ifblock2',2,'p_ifblock2','LUGSTAT.py',545),
  ('ifblock2 -> empty','ifblock2',1,'p_ifblock2','LUGSTAT.py',546),
  ('count -> COUNT OPAREN ID COMMA varcte COMMA varcte CPAREN SCOLON','count',9,'p_count','LUGSTAT.py',549),
  ('countif -> COUNTIF OPAREN ID COMMA varcte COMMA varcte COMMA cond CPAREN SCOLON','countif',11,'p_countif','LUGSTAT.py',552),
  ('plot -> PLOT OPAREN xyfunc CPAREN SCOLON','plot',5,'p_plot','LUGSTAT.py',555),
  ('plot -> PLOT OPAREN plot2 CPAREN SCOLON','plot',5,'p_plot','LUGSTAT.py',556),
  ('plot2 -> LCOR varcte COMMA varcte RCOR','plot2',5,'p_plot2','LUGSTAT.py',560),
  ('plot2 -> LCOR varcte COMMA varcte RCOR COMMA plot2','plot2',7,'p_plot2','LUGSTAT.py',561),
  ('plot2 -> empty','plot2',1,'p_plot2','LUGSTAT.py',562),
  ('xyfunc -> FX EQUALS exp SCOLON xyfunc','xyfunc',5,'p_xyfunc','LUGSTAT.py',566),
  ('xyfunc -> FY EQUALS exp SCOLON xyfunc','xyfunc',5,'p_xyfunc','LUGSTAT.py',567),
  ('xyfunc -> empty','xyfunc',1,'p_xyfunc','LUGSTAT.py',568),
  ('expresion -> exp','expresion',1,'p_expresion','LUGSTAT.py',573),
  ('expresion -> expresion RELOP exp','expresion',3,'p_expresion','LUGSTAT.py',574),
  ('exp -> termino','exp',1,'p_exp','LUGSTAT.py',604),
  ('exp -> termino PLUS exp','exp',3,'p_exp','LUGSTAT.py',605),
  ('exp -> termino MINUS exp','exp',3,'p_exp','LUGSTAT.py',606),
  ('termino -> factor','termino',1,'p_termino','LUGSTAT.py',648),
  ('termino -> factor MULT termino','termino',3,'p_termino','LUGSTAT.py',649),
  ('termino -> factor DIV termino','termino',3,'p_termino','LUGSTAT.py',650),
  ('factor -> OPAREN expresion CPAREN','factor',3,'p_factor','LUGSTAT.py',688),
  ('factor -> varcte','factor',1,'p_factor','LUGSTAT.py',689),
  ('varcte -> ID','varcte',1,'p_varcte','LUGSTAT.py',704),
  ('varcte -> ID asign2','varcte',2,'p_varcte','LUGSTAT.py',705),
  ('varcte -> NUMERIC','varcte',1,'p_varcte','LUGSTAT.py',706),
  ('varcte -> NUMBER','varcte',1,'p_varcte','LUGSTAT.py',707),
  ('dwhile -> DO wn1 wblock WHILE OPAREN dwhileconds CPAREN wn2 SCOLON','dwhile',9,'p_dwhile','LUGSTAT.py',752),
  ('wn1 -> empty','wn1',1,'p_wn1','LUGSTAT.py',755),
  ('wn2 -> empty','wn2',1,'p_wn2','LUGSTAT.py',758),
  ('wblock -> OBRACKET block2 CBRACKET','wblock',3,'p_wblock','LUGSTAT.py',772),
  ('dwhileconds -> expresion dwhileconds','dwhileconds',2,'p_dwhileconds','LUGSTAT.py',777),
  ('dwhileconds -> expresion AND dwhileconds','dwhileconds',3,'p_dwhileconds','LUGSTAT.py',778),
  ('dwhileconds -> expresion OR dwhileconds','dwhileconds',3,'p_dwhileconds','LUGSTAT.py',779),
  ('dwhileconds -> empty','dwhileconds',1,'p_dwhileconds','LUGSTAT.py',780),
  ('readln -> READ OPAREN ID rn1 CPAREN SCOLON','readln',6,'p_readln','LUGSTAT.py',784),
  ('rn1 -> empty','rn1',1,'p_rn1','LUGSTAT.py',787),
  ('metodos -> MEAN OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',809),
  ('metodos -> MEDIAN OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',810),
  ('metodos -> MODE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',811),
  ('metodos -> STDV OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',812),
  ('metodos -> KMEANS OPAREN varcte COMMA mmmfunc CPAREN SCOLON','metodos',7,'p_metodos','LUGSTAT.py',813),
  ('metodos -> DERL OPAREN expfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',814),
  ('metodos -> DBERN OPAREN expfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',815),
  ('metodos -> DPOI OPAREN expfunc2 CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',816),
  ('metodos -> TRANSPOSE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',817),
  ('metodos -> INVERSE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',818),
  ('metodos -> ROTATE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',819),
  ('metodos -> REF OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',820),
  ('metodos -> RREF OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',821),
  ('metodos -> MONT OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',822),
  ('expfunc -> ID COMMA ID COMMA ID','expfunc',5,'p_expfunc','LUGSTAT.py',827),
  ('expfunc -> varcte COMMA varcte COMMA varcte','expfunc',5,'p_expfunc','LUGSTAT.py',828),
  ('expfunc2 -> ID COMMA ID','expfunc2',3,'p_expfunc2','LUGSTAT.py',833),
  ('expfunc2 -> varcte COMMA varcte','expfunc2',3,'p_expfunc2','LUGSTAT.py',834),
  ('mmmfunc -> ID','mmmfunc',1,'p_mmmfunc','LUGSTAT.py',839),
  ('mmmfunc -> OBRACKET mmmarray CBRACKET','mmmfunc',3,'p_mmmfunc','LUGSTAT.py',840),
  ('mmmfunc -> OBRACKET mmmarray CBRACKET COMMA mmmfunc','mmmfunc',5,'p_mmmfunc','LUGSTAT.py',841),
  ('mmmfunc -> empty','mmmfunc',1,'p_mmmfunc','LUGSTAT.py',842),
  ('mmmarray -> varcte','mmmarray',1,'p_mmmarray','LUGSTAT.py',847),
  ('mmmarray -> varcte COMMA mmmarray','mmmarray',3,'p_mmmarray','LUGSTAT.py',848),
  ('mmmarray -> empty','mmmarray',1,'p_mmmarray','LUGSTAT.py',849),
  ('empty -> <empty>','empty',0,'p_empty','LUGSTAT.py',853),
]
