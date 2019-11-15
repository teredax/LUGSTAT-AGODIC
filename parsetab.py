
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CBRACKET CHAR CHARACTER COLON COMMA COMMENT COUNT COUNTIF CPAREN CTED CTEI DBERN DERL DIFF DIV DO DOUBLE DPOI ELSE EQ EQUALS FUNC FX FY GRE GREATEQ GREATERTHAN ID IF INT INTEGER INVERSE KMEANS LCOR LESSEQ LESSTHAN LOGICAL LUGSTAT MEAN MEDIAN MINUS MODE MONT MULT NUMBER NUMERIC OBRACKET OPAREN OR PER PLOT PLUS PRINT QUOTE RCOR REF RELOP ROTATE RREF SCOLON STDV STRING TIPO TRANSPOSE VAR WHILE\n    lugstat : LUGSTAT ID SCOLON addmain lugstat2 lugstat3 block\n    addmain : empty\n    lugstat2 : vars\n    | empty\n    \n    lugstat3 : modules\n    | modules lugstat3\n    | empty\n    vars : VAR vars1 \n     \n    vars1 : ID COMMA vars1\n    | ID COLON tipo SCOLON lugstat2\n    | ID asign2 COLON tipo SCOLON\n    | ID asign2 COMMA vars1\n    savename : empty\n    modules : FUNC ID COLON tipo addfunction OPAREN modules2 CPAREN modules2 blockaddfunction : empty\n    modules2 : vars\n    | empty\n    block : OBRACKET block2 CBRACKET\n    \n    block2 : estatuto\n    | estatuto block2\n    | empty\n    tipo : INT\n    | BOOL \n    | DOUBLE\n    | STRING\n    | CHAR\n    \n    estatuto : asign\n    | cond \n    | escrt\n    | plot\n    | count\n    | countif\n    | metodos\n    | dwhile\n    \n    asign : ID EQUALS expresion SCOLON\n    | ID EQUALS ID SCOLON\n    | ID EQUALS ID asign2 SCOLON\n    | ID asign2 EQUALS ID SCOLON\n    | ID asign2 EQUALS expresion SCOLON\n    | ID asign2 EQUALS ID asign2 SCOLON\n    \n    asign2 : LCOR expresion RCOR asign3\n    | LCOR varcte RCOR asign3 \n    \n    asign3 : LCOR expresion RCOR\n    | LCOR varcte RCOR \n    | emptyescrt : PRINT OPAREN expresion CPAREN SCOLON\n\t| PRINT OPAREN CPAREN SCOLON\n    | PRINT OPAREN ID escrt2 CPAREN SCOLON\n    | PRINT OPAREN STRING CPAREN SCOLON\n    escrt2 : COMMA escrt3\n    | empty\n    escrt3 : ID escrt2\n    | ID\n    | STRING escrt2 escrt2\n    cond : IF OPAREN expresion CPAREN block SCOLON\n    | IF OPAREN expresion CPAREN block ELSE block SCOLON\n    count : COUNT OPAREN ID COMMA varcte COMMA varcte CPAREN SCOLONcountif : COUNTIF OPAREN ID COMMA varcte COMMA varcte COMMA cond CPAREN SCOLONplot : PLOT OPAREN xyfunc CPAREN SCOLON\n    | PLOT OPAREN plot2 CPAREN SCOLON\n    \n    plot2 : LCOR varcte COMMA varcte RCOR\n    | LCOR varcte COMMA varcte RCOR COMMA plot2\n    | empty\n    xyfunc : FX EQUALS exp SCOLON xyfunc\n    | FY EQUALS exp SCOLON xyfunc\n    | empty\n    expresion : exp \n    | expresion RELOP exp \n    \n    exp : termino\n    | termino PLUS exp\n    | termino MINUS exp\n    \n    termino : factor\n    | factor MULT termino\n    | factor DIV termino\n    \n    factor : OPAREN expresion CPAREN \n    | varcte\n    \n    varcte : ID\n    | ID asign2\n    | NUMERIC\n    | NUMBER\n    \n    dwhile : DO wblock WHILE OPAREN dwhileconds CPAREN SCOLON\n    \n    wblock : OBRACKET block2 CBRACKET   \n    \n    dwhileconds : expresion dwhileconds\n    | expresion AND dwhileconds\n    | expresion OR dwhileconds\n    | empty\n    \n    metodos : MEAN OPAREN mmmfunc CPAREN SCOLON\n    | MEDIAN OPAREN mmmfunc CPAREN SCOLON\n    | MODE OPAREN mmmfunc CPAREN SCOLON\n    | STDV OPAREN mmmfunc CPAREN SCOLON\n    | KMEANS OPAREN varcte COMMA mmmfunc CPAREN SCOLON\n    | DERL OPAREN expfunc CPAREN SCOLON\n    | DBERN OPAREN expfunc CPAREN SCOLON\n    | DPOI OPAREN expfunc2 CPAREN SCOLON\n    | TRANSPOSE OPAREN mmmfunc CPAREN SCOLON\n    | INVERSE OPAREN mmmfunc CPAREN SCOLON\n    | ROTATE OPAREN mmmfunc CPAREN SCOLON\n    | REF OPAREN mmmfunc CPAREN SCOLON\n    | RREF OPAREN mmmfunc CPAREN SCOLON\n    | MONT OPAREN mmmfunc CPAREN SCOLON\n    \n    expfunc : ID COMMA ID COMMA ID\n    | varcte COMMA varcte COMMA varcte\n    \n    expfunc2 : ID COMMA ID\n    | varcte COMMA varcte\n    \n    mmmfunc : ID \n    | OBRACKET  mmmarray CBRACKET\n\t| OBRACKET mmmarray CBRACKET COMMA mmmfunc\n\t| empty \n    \n    mmmarray : varcte\n    | varcte COMMA mmmarray\n    | empty\n    empty :'
    
_lr_action_items = {'LUGSTAT':([0,],[2,]),'$end':([1,17,76,],[0,-1,-18,]),'ID':([2,10,14,18,21,24,26,28,29,30,31,32,33,34,35,66,69,70,71,72,73,74,75,78,80,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,105,106,107,108,109,110,111,112,114,117,128,133,158,159,160,161,162,163,164,165,166,167,168,170,175,177,182,183,185,186,194,196,197,200,201,208,213,215,216,218,223,224,225,228,231,233,234,235,236,238,241,242,245,246,247,248,249,250,252,257,258,259,260,262,268,269,270,273,274,277,278,289,292,296,303,306,],[3,16,20,36,16,70,36,-27,-28,-29,-30,-31,-32,-33,-34,16,-67,-77,-79,-80,-69,-72,70,115,70,121,129,130,132,132,132,132,70,140,140,144,132,132,132,132,132,132,36,-112,70,-112,-78,70,70,70,70,-76,171,70,70,70,-41,-45,-68,-42,-70,-71,-73,-74,-75,-36,-35,-47,221,70,70,70,70,132,239,70,243,70,70,-37,-38,-39,-46,-49,-59,-60,70,-87,70,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,70,-43,-44,-40,-55,-48,70,70,132,290,70,70,70,-91,-81,-56,-57,-58,]),'SCOLON':([3,59,60,61,62,63,64,69,70,71,72,73,74,76,103,105,107,108,114,115,116,120,159,160,161,162,163,164,165,166,167,169,171,172,174,179,180,181,187,191,192,193,195,198,199,202,203,204,205,206,207,214,217,219,226,227,257,258,272,275,280,298,305,],[4,102,-22,-23,-24,-25,-26,-67,-77,-79,-80,-69,-72,-18,157,-112,-112,-78,-76,168,170,175,-41,-45,-68,-42,-70,-71,-73,-74,-75,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,265,266,-43,-44,289,292,296,303,306,]),'VAR':([4,5,6,102,210,279,],[-112,10,-2,10,10,10,]),'FUNC':([4,5,6,7,8,9,12,15,58,76,102,104,156,157,300,],[-112,-112,-2,14,-3,-4,14,-8,-9,-18,-112,-12,-10,-11,-14,]),'OBRACKET':([4,5,6,7,8,9,11,12,13,15,19,56,58,76,85,86,87,88,93,94,95,96,97,98,102,104,156,157,173,194,255,256,261,270,279,295,300,],[-112,-112,-2,-112,-3,-4,18,-5,-7,-8,-6,100,-9,-18,133,133,133,133,133,133,133,133,133,133,-112,-12,-10,-11,18,133,-16,-17,18,133,-112,18,-14,]),'CPAREN':([8,9,15,58,69,70,71,72,73,74,81,82,85,86,87,88,93,94,95,96,97,98,102,104,105,107,108,113,114,118,119,121,122,123,124,127,131,132,134,135,136,137,139,142,143,146,147,148,149,150,151,156,157,159,160,161,162,163,164,165,166,167,176,178,194,208,210,220,221,222,232,237,243,244,251,252,253,254,255,256,257,258,260,263,264,265,266,270,276,277,278,281,282,283,284,285,286,288,290,291,293,294,296,297,301,302,304,],[-3,-4,-8,-9,-67,-77,-79,-80,-69,-72,120,-112,-112,-112,-112,-112,-112,-112,-112,-112,-112,-112,-112,-12,-112,-112,-78,167,-76,173,174,-77,179,180,181,-63,187,-105,-108,191,192,193,195,198,199,202,203,204,205,206,207,-10,-11,-41,-45,-68,-42,-70,-71,-73,-74,-75,219,-51,-112,-112,-112,-50,-53,-112,-106,272,-103,-104,275,-112,-86,279,-16,-17,-43,-44,-55,-52,-112,-112,-112,-112,-83,-112,-112,-54,-64,-66,-65,-61,298,-107,-101,-102,-84,-85,-56,-112,-62,-63,305,]),'COMMA':([16,23,70,71,72,105,107,108,121,129,130,138,140,141,144,145,159,160,162,178,184,189,220,221,222,229,230,232,239,240,257,258,263,264,281,285,287,],[21,66,-77,-79,-80,-112,-112,-78,177,185,186,194,196,197,200,201,-41,-45,-42,-51,228,233,-50,177,177,268,269,270,273,274,-43,-44,-52,177,-54,297,299,]),'COLON':([16,20,23,105,107,159,160,162,257,258,],[22,57,65,-112,-112,-41,-45,-42,-43,-44,]),'LCOR':([16,36,70,82,105,107,115,121,140,144,171,297,],[24,24,24,128,158,158,24,24,24,24,24,128,]),'CBRACKET':([18,25,26,27,28,29,30,31,32,33,34,35,70,71,72,77,100,105,107,108,133,153,159,160,162,168,170,175,188,189,190,213,215,216,218,223,224,225,231,233,234,235,236,238,241,242,245,246,247,248,249,250,257,258,259,260,262,271,289,292,296,303,306,],[-112,76,-19,-21,-27,-28,-29,-30,-31,-32,-33,-34,-77,-79,-80,-20,-112,-112,-112,-78,-112,209,-41,-45,-42,-36,-35,-47,232,-109,-111,-37,-38,-39,-46,-49,-59,-60,-87,-112,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-43,-44,-40,-55,-48,-110,-91,-81,-56,-57,-58,]),'IF':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,299,303,306,],[37,37,-27,-28,-29,-30,-31,-32,-33,-34,37,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,37,-57,-58,]),'PRINT':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[38,38,-27,-28,-29,-30,-31,-32,-33,-34,38,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'PLOT':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[39,39,-27,-28,-29,-30,-31,-32,-33,-34,39,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'COUNT':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[40,40,-27,-28,-29,-30,-31,-32,-33,-34,40,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'COUNTIF':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[41,41,-27,-28,-29,-30,-31,-32,-33,-34,41,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'MEAN':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[42,42,-27,-28,-29,-30,-31,-32,-33,-34,42,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'MEDIAN':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[43,43,-27,-28,-29,-30,-31,-32,-33,-34,43,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'MODE':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[44,44,-27,-28,-29,-30,-31,-32,-33,-34,44,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'STDV':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[45,45,-27,-28,-29,-30,-31,-32,-33,-34,45,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'KMEANS':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[46,46,-27,-28,-29,-30,-31,-32,-33,-34,46,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'DERL':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[47,47,-27,-28,-29,-30,-31,-32,-33,-34,47,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'DBERN':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[48,48,-27,-28,-29,-30,-31,-32,-33,-34,48,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'DPOI':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[49,49,-27,-28,-29,-30,-31,-32,-33,-34,49,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'TRANSPOSE':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[50,50,-27,-28,-29,-30,-31,-32,-33,-34,50,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'INVERSE':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[51,51,-27,-28,-29,-30,-31,-32,-33,-34,51,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'ROTATE':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[52,52,-27,-28,-29,-30,-31,-32,-33,-34,52,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'REF':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[53,53,-27,-28,-29,-30,-31,-32,-33,-34,53,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'RREF':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[54,54,-27,-28,-29,-30,-31,-32,-33,-34,54,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'MONT':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[55,55,-27,-28,-29,-30,-31,-32,-33,-34,55,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'DO':([18,26,28,29,30,31,32,33,34,35,100,168,170,175,213,215,216,218,223,224,225,231,234,235,236,238,241,242,245,246,247,248,249,250,259,260,262,289,292,296,303,306,],[56,56,-27,-28,-29,-30,-31,-32,-33,-34,56,-36,-35,-47,-37,-38,-39,-46,-49,-59,-60,-87,-88,-89,-90,-92,-93,-94,-95,-96,-97,-98,-99,-100,-40,-55,-48,-91,-81,-56,-57,-58,]),'INT':([22,57,65,],[60,60,60,]),'BOOL':([22,57,65,],[61,61,61,]),'DOUBLE':([22,57,65,],[62,62,62,]),'STRING':([22,57,65,81,177,],[63,63,63,122,222,]),'CHAR':([22,57,65,],[64,64,64,]),'NUMERIC':([24,69,70,71,72,73,74,75,78,80,81,89,90,91,92,105,106,107,108,109,110,111,112,114,117,128,133,158,159,160,161,162,163,164,165,166,167,182,183,185,186,197,201,208,228,233,252,257,258,268,269,274,277,278,],[71,-67,-77,-79,-80,-69,-72,71,71,71,71,71,71,71,71,-112,71,-112,-78,71,71,71,71,-76,71,71,71,71,-41,-45,-68,-42,-70,-71,-73,-74,-75,71,71,71,71,71,71,71,71,71,71,-43,-44,71,71,71,71,71,]),'NUMBER':([24,69,70,71,72,73,74,75,78,80,81,89,90,91,92,105,106,107,108,109,110,111,112,114,117,128,133,158,159,160,161,162,163,164,165,166,167,182,183,185,186,197,201,208,228,233,252,257,258,268,269,274,277,278,],[72,-67,-77,-79,-80,-69,-72,72,72,72,72,72,72,72,72,-112,72,-112,-78,72,72,72,72,-76,72,72,72,72,-41,-45,-68,-42,-70,-71,-73,-74,-75,72,72,72,72,72,72,72,72,72,72,-43,-44,72,72,72,72,72,]),'OPAREN':([24,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,62,63,64,69,70,71,72,73,74,75,78,80,81,101,105,106,107,108,109,110,111,112,114,117,152,154,155,158,159,160,161,162,163,164,165,166,167,182,183,208,252,257,258,277,278,],[75,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,-22,-23,-24,-25,-26,-67,-77,-79,-80,-69,-72,75,75,75,75,-112,-112,75,-112,-78,75,75,75,75,-76,75,208,210,-15,75,-41,-45,-68,-42,-70,-71,-73,-74,-75,75,75,75,75,-43,-44,75,75,]),'EQUALS':([36,79,105,107,125,126,159,160,162,257,258,],[78,117,-112,-112,182,183,-41,-45,-42,-43,-44,]),'RCOR':([67,68,69,70,71,72,73,74,105,107,108,114,159,160,161,162,163,164,165,166,167,211,212,257,258,267,],[105,107,-67,-77,-79,-80,-69,-72,-112,-112,-78,-76,-41,-45,-68,-42,-70,-71,-73,-74,-75,257,258,-43,-44,285,]),'RELOP':([67,68,69,70,71,72,73,74,105,107,108,113,114,115,116,118,119,121,159,160,161,162,163,164,165,166,167,169,171,172,211,212,214,252,257,258,],[106,-76,-67,-77,-79,-80,-69,-72,-112,-112,-78,106,-76,-77,106,106,106,-77,-41,-45,-68,-42,-70,-71,-73,-74,-75,-78,-77,106,106,-76,-78,106,-43,-44,]),'MULT':([68,70,71,72,74,105,107,108,114,115,121,159,160,162,167,169,171,212,214,257,258,],[-76,-77,-79,-80,111,-112,-112,-78,-76,-77,-77,-41,-45,-42,-75,-78,-77,-76,-78,-43,-44,]),'DIV':([68,70,71,72,74,105,107,108,114,115,121,159,160,162,167,169,171,212,214,257,258,],[-76,-77,-79,-80,112,-112,-112,-78,-76,-77,-77,-41,-45,-42,-75,-78,-77,-76,-78,-43,-44,]),'PLUS':([68,70,71,72,73,74,105,107,108,114,115,121,159,160,162,165,166,167,169,171,212,214,257,258,],[-76,-77,-79,-80,109,-72,-112,-112,-78,-76,-77,-77,-41,-45,-42,-73,-74,-75,-78,-77,-76,-78,-43,-44,]),'MINUS':([68,70,71,72,73,74,105,107,108,114,115,121,159,160,162,165,166,167,169,171,212,214,257,258,],[-76,-77,-79,-80,110,-72,-112,-112,-78,-76,-77,-77,-41,-45,-42,-73,-74,-75,-78,-77,-76,-78,-43,-44,]),'AND':([69,70,71,72,73,74,105,107,108,114,159,160,161,162,163,164,165,166,167,252,257,258,],[-67,-77,-79,-80,-69,-72,-112,-112,-78,-76,-41,-45,-68,-42,-70,-71,-73,-74,-75,277,-43,-44,]),'OR':([69,70,71,72,73,74,105,107,108,114,159,160,161,162,163,164,165,166,167,252,257,258,],[-67,-77,-79,-80,-69,-72,-112,-112,-78,-76,-41,-45,-68,-42,-70,-71,-73,-74,-75,278,-43,-44,]),'ELSE':([76,217,],[-18,261,]),'FX':([82,265,266,],[125,125,125,]),'FY':([82,265,266,],[126,126,126,]),'WHILE':([99,209,],[152,-82,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lugstat':([0,],[1,]),'addmain':([4,],[5,]),'empty':([4,5,7,12,18,26,82,85,86,87,88,93,94,95,96,97,98,100,101,102,105,107,121,133,194,208,210,221,222,233,252,264,265,266,270,277,278,279,297,],[6,9,13,13,27,27,127,134,134,134,134,134,134,134,134,134,134,27,155,9,160,160,178,190,134,253,256,178,178,190,253,178,283,283,134,253,253,256,302,]),'lugstat2':([5,102,],[7,156,]),'vars':([5,102,210,279,],[8,8,255,255,]),'lugstat3':([7,12,],[11,19,]),'modules':([7,12,],[12,12,]),'vars1':([10,21,66,],[15,58,104,]),'block':([11,173,261,295,],[17,217,280,300,]),'asign2':([16,36,70,115,121,140,144,171,],[23,79,108,169,108,108,108,214,]),'block2':([18,26,100,],[25,77,153,]),'estatuto':([18,26,100,],[26,26,26,]),'asign':([18,26,100,],[28,28,28,]),'cond':([18,26,100,299,],[29,29,29,304,]),'escrt':([18,26,100,],[30,30,30,]),'plot':([18,26,100,],[31,31,31,]),'count':([18,26,100,],[32,32,32,]),'countif':([18,26,100,],[33,33,33,]),'metodos':([18,26,100,],[34,34,34,]),'dwhile':([18,26,100,],[35,35,35,]),'tipo':([22,57,65,],[59,101,103,]),'expresion':([24,75,78,80,81,117,158,208,252,277,278,],[67,113,116,118,119,172,211,252,252,252,252,]),'varcte':([24,75,78,80,81,89,90,91,92,106,109,110,111,112,117,128,133,158,182,183,185,186,197,201,208,228,233,252,268,269,274,277,278,],[68,114,114,114,114,138,141,141,145,114,114,114,114,114,114,184,189,212,114,114,229,230,240,244,114,267,189,114,286,287,291,114,114,]),'exp':([24,75,78,80,81,106,109,110,117,158,182,183,208,252,277,278,],[69,69,69,69,69,161,163,164,69,69,226,227,69,69,69,69,]),'termino':([24,75,78,80,81,106,109,110,111,112,117,158,182,183,208,252,277,278,],[73,73,73,73,73,73,73,73,165,166,73,73,73,73,73,73,73,73,]),'factor':([24,75,78,80,81,106,109,110,111,112,117,158,182,183,208,252,277,278,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'wblock':([56,],[99,]),'xyfunc':([82,265,266,],[123,282,284,]),'plot2':([82,297,],[124,301,]),'mmmfunc':([85,86,87,88,93,94,95,96,97,98,194,270,],[131,135,136,137,146,147,148,149,150,151,237,288,]),'expfunc':([90,91,],[139,142,]),'expfunc2':([92,],[143,]),'addfunction':([101,],[154,]),'asign3':([105,107,],[159,162,]),'escrt2':([121,221,222,264,],[176,263,264,281,]),'mmmarray':([133,233,],[188,271,]),'escrt3':([177,],[220,]),'dwhileconds':([208,252,277,278,],[251,276,293,294,]),'modules2':([210,279,],[254,295,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lugstat","S'",1,None,None,None),
  ('lugstat -> LUGSTAT ID SCOLON addmain lugstat2 lugstat3 block','lugstat',7,'p_lugstat','LUGSTAT.py',192),
  ('addmain -> empty','addmain',1,'p_addmain','LUGSTAT.py',196),
  ('lugstat2 -> vars','lugstat2',1,'p_lugstat2','LUGSTAT.py',207),
  ('lugstat2 -> empty','lugstat2',1,'p_lugstat2','LUGSTAT.py',208),
  ('lugstat3 -> modules','lugstat3',1,'p_lugstat3','LUGSTAT.py',213),
  ('lugstat3 -> modules lugstat3','lugstat3',2,'p_lugstat3','LUGSTAT.py',214),
  ('lugstat3 -> empty','lugstat3',1,'p_lugstat3','LUGSTAT.py',215),
  ('vars -> VAR vars1','vars',2,'p_vars','LUGSTAT.py',219),
  ('vars1 -> ID COMMA vars1','vars1',3,'p_vars1','LUGSTAT.py',254),
  ('vars1 -> ID COLON tipo SCOLON lugstat2','vars1',5,'p_vars1','LUGSTAT.py',255),
  ('vars1 -> ID asign2 COLON tipo SCOLON','vars1',5,'p_vars1','LUGSTAT.py',256),
  ('vars1 -> ID asign2 COMMA vars1','vars1',4,'p_vars1','LUGSTAT.py',257),
  ('savename -> empty','savename',1,'p_savename','LUGSTAT.py',283),
  ('modules -> FUNC ID COLON tipo addfunction OPAREN modules2 CPAREN modules2 block','modules',10,'p_modules','LUGSTAT.py',287),
  ('addfunction -> empty','addfunction',1,'p_addfunction','LUGSTAT.py',291),
  ('modules2 -> vars','modules2',1,'p_modules2','LUGSTAT.py',299),
  ('modules2 -> empty','modules2',1,'p_modules2','LUGSTAT.py',300),
  ('block -> OBRACKET block2 CBRACKET','block',3,'p_block','LUGSTAT.py',306),
  ('block2 -> estatuto','block2',1,'p_block2','LUGSTAT.py',321),
  ('block2 -> estatuto block2','block2',2,'p_block2','LUGSTAT.py',322),
  ('block2 -> empty','block2',1,'p_block2','LUGSTAT.py',323),
  ('tipo -> INT','tipo',1,'p_tipo','LUGSTAT.py',327),
  ('tipo -> BOOL','tipo',1,'p_tipo','LUGSTAT.py',328),
  ('tipo -> DOUBLE','tipo',1,'p_tipo','LUGSTAT.py',329),
  ('tipo -> STRING','tipo',1,'p_tipo','LUGSTAT.py',330),
  ('tipo -> CHAR','tipo',1,'p_tipo','LUGSTAT.py',331),
  ('estatuto -> asign','estatuto',1,'p_estatuto','LUGSTAT.py',337),
  ('estatuto -> cond','estatuto',1,'p_estatuto','LUGSTAT.py',338),
  ('estatuto -> escrt','estatuto',1,'p_estatuto','LUGSTAT.py',339),
  ('estatuto -> plot','estatuto',1,'p_estatuto','LUGSTAT.py',340),
  ('estatuto -> count','estatuto',1,'p_estatuto','LUGSTAT.py',341),
  ('estatuto -> countif','estatuto',1,'p_estatuto','LUGSTAT.py',342),
  ('estatuto -> metodos','estatuto',1,'p_estatuto','LUGSTAT.py',343),
  ('estatuto -> dwhile','estatuto',1,'p_estatuto','LUGSTAT.py',344),
  ('asign -> ID EQUALS expresion SCOLON','asign',4,'p_asign','LUGSTAT.py',349),
  ('asign -> ID EQUALS ID SCOLON','asign',4,'p_asign','LUGSTAT.py',350),
  ('asign -> ID EQUALS ID asign2 SCOLON','asign',5,'p_asign','LUGSTAT.py',351),
  ('asign -> ID asign2 EQUALS ID SCOLON','asign',5,'p_asign','LUGSTAT.py',352),
  ('asign -> ID asign2 EQUALS expresion SCOLON','asign',5,'p_asign','LUGSTAT.py',353),
  ('asign -> ID asign2 EQUALS ID asign2 SCOLON','asign',6,'p_asign','LUGSTAT.py',354),
  ('asign2 -> LCOR expresion RCOR asign3','asign2',4,'p_asign2','LUGSTAT.py',406),
  ('asign2 -> LCOR varcte RCOR asign3','asign2',4,'p_asign2','LUGSTAT.py',407),
  ('asign3 -> LCOR expresion RCOR','asign3',3,'p_asign3','LUGSTAT.py',412),
  ('asign3 -> LCOR varcte RCOR','asign3',3,'p_asign3','LUGSTAT.py',413),
  ('asign3 -> empty','asign3',1,'p_asign3','LUGSTAT.py',414),
  ('escrt -> PRINT OPAREN expresion CPAREN SCOLON','escrt',5,'p_escrt','LUGSTAT.py',418),
  ('escrt -> PRINT OPAREN CPAREN SCOLON','escrt',4,'p_escrt','LUGSTAT.py',419),
  ('escrt -> PRINT OPAREN ID escrt2 CPAREN SCOLON','escrt',6,'p_escrt','LUGSTAT.py',420),
  ('escrt -> PRINT OPAREN STRING CPAREN SCOLON','escrt',5,'p_escrt','LUGSTAT.py',421),
  ('escrt2 -> COMMA escrt3','escrt2',2,'p_escrt2','LUGSTAT.py',425),
  ('escrt2 -> empty','escrt2',1,'p_escrt2','LUGSTAT.py',426),
  ('escrt3 -> ID escrt2','escrt3',2,'p_escrt3','LUGSTAT.py',430),
  ('escrt3 -> ID','escrt3',1,'p_escrt3','LUGSTAT.py',431),
  ('escrt3 -> STRING escrt2 escrt2','escrt3',3,'p_escrt3','LUGSTAT.py',432),
  ('cond -> IF OPAREN expresion CPAREN block SCOLON','cond',6,'p_cond','LUGSTAT.py',436),
  ('cond -> IF OPAREN expresion CPAREN block ELSE block SCOLON','cond',8,'p_cond','LUGSTAT.py',437),
  ('count -> COUNT OPAREN ID COMMA varcte COMMA varcte CPAREN SCOLON','count',9,'p_count','LUGSTAT.py',441),
  ('countif -> COUNTIF OPAREN ID COMMA varcte COMMA varcte COMMA cond CPAREN SCOLON','countif',11,'p_countif','LUGSTAT.py',444),
  ('plot -> PLOT OPAREN xyfunc CPAREN SCOLON','plot',5,'p_plot','LUGSTAT.py',447),
  ('plot -> PLOT OPAREN plot2 CPAREN SCOLON','plot',5,'p_plot','LUGSTAT.py',448),
  ('plot2 -> LCOR varcte COMMA varcte RCOR','plot2',5,'p_plot2','LUGSTAT.py',452),
  ('plot2 -> LCOR varcte COMMA varcte RCOR COMMA plot2','plot2',7,'p_plot2','LUGSTAT.py',453),
  ('plot2 -> empty','plot2',1,'p_plot2','LUGSTAT.py',454),
  ('xyfunc -> FX EQUALS exp SCOLON xyfunc','xyfunc',5,'p_xyfunc','LUGSTAT.py',458),
  ('xyfunc -> FY EQUALS exp SCOLON xyfunc','xyfunc',5,'p_xyfunc','LUGSTAT.py',459),
  ('xyfunc -> empty','xyfunc',1,'p_xyfunc','LUGSTAT.py',460),
  ('expresion -> exp','expresion',1,'p_expresion','LUGSTAT.py',465),
  ('expresion -> expresion RELOP exp','expresion',3,'p_expresion','LUGSTAT.py',466),
  ('exp -> termino','exp',1,'p_exp','LUGSTAT.py',503),
  ('exp -> termino PLUS exp','exp',3,'p_exp','LUGSTAT.py',504),
  ('exp -> termino MINUS exp','exp',3,'p_exp','LUGSTAT.py',505),
  ('termino -> factor','termino',1,'p_termino','LUGSTAT.py',550),
  ('termino -> factor MULT termino','termino',3,'p_termino','LUGSTAT.py',551),
  ('termino -> factor DIV termino','termino',3,'p_termino','LUGSTAT.py',552),
  ('factor -> OPAREN expresion CPAREN','factor',3,'p_factor','LUGSTAT.py',591),
  ('factor -> varcte','factor',1,'p_factor','LUGSTAT.py',592),
  ('varcte -> ID','varcte',1,'p_varcte','LUGSTAT.py',607),
  ('varcte -> ID asign2','varcte',2,'p_varcte','LUGSTAT.py',608),
  ('varcte -> NUMERIC','varcte',1,'p_varcte','LUGSTAT.py',609),
  ('varcte -> NUMBER','varcte',1,'p_varcte','LUGSTAT.py',610),
  ('dwhile -> DO wblock WHILE OPAREN dwhileconds CPAREN SCOLON','dwhile',7,'p_dwhile','LUGSTAT.py',648),
  ('wblock -> OBRACKET block2 CBRACKET','wblock',3,'p_wblock','LUGSTAT.py',653),
  ('dwhileconds -> expresion dwhileconds','dwhileconds',2,'p_dwhileconds','LUGSTAT.py',658),
  ('dwhileconds -> expresion AND dwhileconds','dwhileconds',3,'p_dwhileconds','LUGSTAT.py',659),
  ('dwhileconds -> expresion OR dwhileconds','dwhileconds',3,'p_dwhileconds','LUGSTAT.py',660),
  ('dwhileconds -> empty','dwhileconds',1,'p_dwhileconds','LUGSTAT.py',661),
  ('metodos -> MEAN OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',667),
  ('metodos -> MEDIAN OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',668),
  ('metodos -> MODE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',669),
  ('metodos -> STDV OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',670),
  ('metodos -> KMEANS OPAREN varcte COMMA mmmfunc CPAREN SCOLON','metodos',7,'p_metodos','LUGSTAT.py',671),
  ('metodos -> DERL OPAREN expfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',672),
  ('metodos -> DBERN OPAREN expfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',673),
  ('metodos -> DPOI OPAREN expfunc2 CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',674),
  ('metodos -> TRANSPOSE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',675),
  ('metodos -> INVERSE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',676),
  ('metodos -> ROTATE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',677),
  ('metodos -> REF OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',678),
  ('metodos -> RREF OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',679),
  ('metodos -> MONT OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',680),
  ('expfunc -> ID COMMA ID COMMA ID','expfunc',5,'p_expfunc','LUGSTAT.py',685),
  ('expfunc -> varcte COMMA varcte COMMA varcte','expfunc',5,'p_expfunc','LUGSTAT.py',686),
  ('expfunc2 -> ID COMMA ID','expfunc2',3,'p_expfunc2','LUGSTAT.py',691),
  ('expfunc2 -> varcte COMMA varcte','expfunc2',3,'p_expfunc2','LUGSTAT.py',692),
  ('mmmfunc -> ID','mmmfunc',1,'p_mmmfunc','LUGSTAT.py',697),
  ('mmmfunc -> OBRACKET mmmarray CBRACKET','mmmfunc',3,'p_mmmfunc','LUGSTAT.py',698),
  ('mmmfunc -> OBRACKET mmmarray CBRACKET COMMA mmmfunc','mmmfunc',5,'p_mmmfunc','LUGSTAT.py',699),
  ('mmmfunc -> empty','mmmfunc',1,'p_mmmfunc','LUGSTAT.py',700),
  ('mmmarray -> varcte','mmmarray',1,'p_mmmarray','LUGSTAT.py',705),
  ('mmmarray -> varcte COMMA mmmarray','mmmarray',3,'p_mmmarray','LUGSTAT.py',706),
  ('mmmarray -> empty','mmmarray',1,'p_mmmarray','LUGSTAT.py',707),
  ('empty -> <empty>','empty',0,'p_empty','LUGSTAT.py',711),
]
