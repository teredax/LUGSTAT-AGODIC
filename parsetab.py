
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CBRACKET CHAR CHARACTER COLON COMMA COMMENT COUNT COUNTIF CPAREN CTED CTEI DBERN DERL DIFF DIV DO DOUBLE DPOI ELSE EQ EQUALS FUNC FX FY GRE GREATEQ GREATERTHAN ID IF INT INTEGER INVERSE KMEANS LCOR LESSEQ LESSTHAN LOGICAL LUGSTAT MEAN MEDIAN MINUS MODE MONT MULT NUMBER NUMERIC OBRACKET OPAREN OR PER PLOT PLUS PRINT QUOTE RCOR REF RELOP ROTATE RREF SCOLON STDV STRING TIPO TRANSPOSE VAR WHILE\n    lugstat : LUGSTAT ID SCOLON addmain lugstat2 lugstat3 block\n    addmain : empty\n    lugstat2 : vars\n    | empty\n    \n    lugstat3 : modules\n    | modules lugstat3\n    | empty\n    vars : VAR vars1 \n     \n    vars1 : ID COMMA vars1\n    | ID COLON tipo SCOLON lugstat2\n    | ID asign2 COLON tipo SCOLON\n    | ID asign2 COMMA vars1\n    savename : empty\n    modules : FUNC ID COLON tipo addfunction OPAREN modules2 CPAREN modules2 blockaddfunction : empty\n    modules2 : vars\n    | empty\n    block : OBRACKET block2 CBRACKET\n    \n    block2 : estatuto\n    | estatuto block2\n    | empty\n    tipo : INT\n    | BOOL \n    | DOUBLE\n    | STRING\n    | CHAR\n    \n    estatuto : asign\n    | cond \n    | escrt\n    | plot\n    | count\n    | countif\n    | metodos\n    | dwhile\n    \n    asign : ID EQUALS expresion SCOLON\n    | ID EQUALS ID SCOLON\n    | ID EQUALS ID asign2 SCOLON\n    | ID asign2 EQUALS ID SCOLON\n    | ID asign2 EQUALS expresion SCOLON\n    | ID asign2 EQUALS ID asign2 SCOLON\n    \n    asign2 : LCOR expresion RCOR asign3\n    | LCOR varcte RCOR asign3 \n    \n    asign3 : LCOR expresion RCOR\n    | LCOR varcte RCOR \n    | emptyescrt : PRINT OPAREN expresion CPAREN SCOLON\n\t| PRINT OPAREN CPAREN SCOLON\n    | PRINT OPAREN ID escrt2 CPAREN SCOLON\n    | PRINT OPAREN STRING CPAREN SCOLON\n    escrt2 : COMMA escrt3\n    | empty\n    escrt3 : ID escrt2\n    | ID\n    | STRING escrt2 escrt2\n    cond : IF OPAREN expresion cn1 CPAREN ifblock SCOLON cn2\n    | IF OPAREN expresion cn1 CPAREN ifblock ELSE cn3 ifblock SCOLON cn2\n    cn1 : emptycn2 : emptycn3 : empty\n    ifblock : OBRACKET ifblock2 CBRACKET\n    \n    ifblock2 : estatuto\n    | estatuto ifblock2\n    | emptycount : COUNT OPAREN ID COMMA varcte COMMA varcte CPAREN SCOLONcountif : COUNTIF OPAREN ID COMMA varcte COMMA varcte COMMA cond CPAREN SCOLONplot : PLOT OPAREN xyfunc CPAREN SCOLON\n    | PLOT OPAREN plot2 CPAREN SCOLON\n    \n    plot2 : LCOR varcte COMMA varcte RCOR\n    | LCOR varcte COMMA varcte RCOR COMMA plot2\n    | empty\n    xyfunc : FX EQUALS exp SCOLON xyfunc\n    | FY EQUALS exp SCOLON xyfunc\n    | empty\n    expresion : exp \n    | expresion RELOP exp \n    \n    exp : termino\n    | termino PLUS exp\n    | termino MINUS exp\n    \n    termino : factor\n    | factor MULT termino\n    | factor DIV termino\n    \n    factor : OPAREN expresion CPAREN \n    | varcte\n    \n    varcte : ID\n    | ID asign2\n    | NUMERIC\n    | NUMBER\n    \n    dwhile : DO wn1 wblock WHILE OPAREN dwhileconds CPAREN wn2 SCOLON \n    wn1 : emptywn2 : empty\n    wblock : OBRACKET block2 CBRACKET   \n    \n    dwhileconds : expresion dwhileconds\n    | expresion AND dwhileconds\n    | expresion OR dwhileconds\n    | empty\n    \n    metodos : MEAN OPAREN mmmfunc CPAREN SCOLON\n    | MEDIAN OPAREN mmmfunc CPAREN SCOLON\n    | MODE OPAREN mmmfunc CPAREN SCOLON\n    | STDV OPAREN mmmfunc CPAREN SCOLON\n    | KMEANS OPAREN varcte COMMA mmmfunc CPAREN SCOLON\n    | DERL OPAREN expfunc CPAREN SCOLON\n    | DBERN OPAREN expfunc CPAREN SCOLON\n    | DPOI OPAREN expfunc2 CPAREN SCOLON\n    | TRANSPOSE OPAREN mmmfunc CPAREN SCOLON\n    | INVERSE OPAREN mmmfunc CPAREN SCOLON\n    | ROTATE OPAREN mmmfunc CPAREN SCOLON\n    | REF OPAREN mmmfunc CPAREN SCOLON\n    | RREF OPAREN mmmfunc CPAREN SCOLON\n    | MONT OPAREN mmmfunc CPAREN SCOLON\n    \n    expfunc : ID COMMA ID COMMA ID\n    | varcte COMMA varcte COMMA varcte\n    \n    expfunc2 : ID COMMA ID\n    | varcte COMMA varcte\n    \n    mmmfunc : ID \n    | OBRACKET  mmmarray CBRACKET\n\t| OBRACKET mmmarray CBRACKET COMMA mmmfunc\n\t| empty \n    \n    mmmarray : varcte\n    | varcte COMMA mmmarray\n    | empty\n    empty :'
    
_lr_action_items = {'LUGSTAT':([0,],[2,]),'$end':([1,17,76,],[0,-1,-18,]),'ID':([2,10,14,18,21,24,26,28,29,30,31,32,33,34,35,66,69,70,71,72,73,74,75,78,80,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,105,106,107,108,109,110,111,112,114,117,128,133,153,158,159,160,161,162,163,164,165,166,167,168,170,176,178,183,184,186,187,195,197,198,201,202,214,216,217,219,224,225,226,229,232,234,235,236,237,239,242,243,246,247,248,249,250,251,252,257,258,259,261,262,268,269,270,273,274,276,279,282,292,297,298,300,301,317,319,320,322,323,],[3,16,20,36,16,70,36,-27,-28,-29,-30,-31,-32,-33,-34,16,-74,-84,-86,-87,-76,-79,70,115,70,121,129,130,132,132,132,132,70,140,140,144,132,132,132,132,132,132,-121,70,-121,-85,70,70,70,70,-83,171,70,70,36,70,-41,-45,-75,-42,-77,-78,-80,-81,-82,-36,-35,-47,222,70,70,70,70,132,240,70,244,70,-37,-38,-39,-46,-49,-66,-67,70,-96,70,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,70,-43,-44,-40,36,-48,70,70,132,293,70,70,-121,36,-100,70,70,-55,-58,-64,-88,-121,-56,-65,]),'SCOLON':([3,59,60,61,62,63,64,69,70,71,72,73,74,103,105,107,108,114,115,116,120,159,160,161,162,163,164,165,166,167,169,171,172,175,180,181,182,188,192,193,194,196,199,200,203,204,205,206,207,208,215,220,227,228,257,258,260,272,295,304,307,309,310,314,321,],[4,102,-22,-23,-24,-25,-26,-74,-84,-86,-87,-76,-79,157,-121,-121,-85,-83,168,170,176,-41,-45,-75,-42,-77,-78,-80,-81,-82,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,262,265,266,-43,-44,279,292,-121,-60,317,319,-90,320,323,]),'VAR':([4,5,6,102,211,278,],[-121,10,-2,10,10,10,]),'FUNC':([4,5,6,7,8,9,12,15,58,76,102,104,156,157,313,],[-121,-121,-2,14,-3,-4,14,-8,-9,-18,-121,-12,-10,-11,-14,]),'OBRACKET':([4,5,6,7,8,9,11,12,13,15,19,56,58,76,85,86,87,88,93,94,95,96,97,98,99,100,102,104,156,157,195,218,255,256,270,278,280,299,302,303,313,],[-121,-121,-2,-121,-3,-4,18,-5,-7,-8,-6,-121,-9,-18,133,133,133,133,133,133,133,133,133,133,153,-89,-121,-12,-10,-11,133,261,-16,-17,133,-121,-121,18,261,-59,-14,]),'CPAREN':([8,9,15,58,69,70,71,72,73,74,81,82,85,86,87,88,93,94,95,96,97,98,102,104,105,107,108,113,114,118,119,121,122,123,124,127,131,132,134,135,136,137,139,142,143,146,147,148,149,150,151,156,157,159,160,161,162,163,164,165,166,167,173,174,177,179,195,211,221,222,223,233,238,244,245,252,254,255,256,257,258,263,264,265,266,270,275,276,277,279,284,285,286,287,288,289,291,293,294,296,297,298,300,301,306,311,312,315,316,318,320,322,],[-3,-4,-8,-9,-74,-84,-86,-87,-76,-79,120,-121,-121,-121,-121,-121,-121,-121,-121,-121,-121,-121,-121,-12,-121,-121,-85,167,-83,-121,175,-84,180,181,182,-70,188,-114,-117,192,193,194,196,199,200,203,204,205,206,207,208,-10,-11,-41,-45,-75,-42,-77,-78,-80,-81,-82,218,-57,220,-51,-121,-121,-50,-53,-121,-115,272,-112,-113,-121,278,-16,-17,-43,-44,-52,-121,-121,-121,-121,295,-121,-95,-121,-54,-71,-73,-72,-68,307,-116,-110,-111,-92,-121,-121,-55,-58,-121,-93,-94,-69,-70,321,-121,-56,]),'COMMA':([16,23,70,71,72,105,107,108,121,129,130,138,140,141,144,145,159,160,162,179,185,190,221,222,223,230,231,233,240,241,257,258,263,264,284,288,290,],[21,66,-84,-86,-87,-121,-121,-85,178,186,187,195,197,198,201,202,-41,-45,-42,-51,229,234,-50,178,178,268,269,270,273,274,-43,-44,-52,178,-54,306,308,]),'COLON':([16,20,23,105,107,159,160,162,257,258,],[22,57,65,-121,-121,-41,-45,-42,-43,-44,]),'LCOR':([16,36,70,82,105,107,115,121,140,144,171,306,],[24,24,24,128,158,158,24,24,24,24,24,128,]),'CBRACKET':([18,25,26,27,28,29,30,31,32,33,34,35,70,71,72,77,105,107,108,133,153,159,160,162,168,170,176,189,190,191,210,214,216,217,219,224,225,226,232,234,235,236,237,239,242,243,246,247,248,249,250,251,257,258,259,261,262,271,279,281,282,283,292,300,301,305,317,319,320,322,323,],[-121,76,-19,-21,-27,-28,-29,-30,-31,-32,-33,-34,-84,-86,-87,-20,-121,-121,-85,-121,-121,-41,-45,-42,-36,-35,-47,233,-118,-120,253,-37,-38,-39,-46,-49,-66,-67,-96,-121,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-43,-44,-40,-121,-48,-119,-121,304,-61,-63,-100,-55,-58,-62,-64,-88,-121,-56,-65,]),'IF':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,308,317,319,320,322,323,],[37,37,-27,-28,-29,-30,-31,-32,-33,-34,37,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,37,-48,-121,37,-100,-55,-58,37,-64,-88,-121,-56,-65,]),'PRINT':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[38,38,-27,-28,-29,-30,-31,-32,-33,-34,38,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,38,-48,-121,38,-100,-55,-58,-64,-88,-121,-56,-65,]),'PLOT':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[39,39,-27,-28,-29,-30,-31,-32,-33,-34,39,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,39,-48,-121,39,-100,-55,-58,-64,-88,-121,-56,-65,]),'COUNT':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[40,40,-27,-28,-29,-30,-31,-32,-33,-34,40,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,40,-48,-121,40,-100,-55,-58,-64,-88,-121,-56,-65,]),'COUNTIF':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[41,41,-27,-28,-29,-30,-31,-32,-33,-34,41,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,41,-48,-121,41,-100,-55,-58,-64,-88,-121,-56,-65,]),'MEAN':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[42,42,-27,-28,-29,-30,-31,-32,-33,-34,42,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,42,-48,-121,42,-100,-55,-58,-64,-88,-121,-56,-65,]),'MEDIAN':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[43,43,-27,-28,-29,-30,-31,-32,-33,-34,43,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,43,-48,-121,43,-100,-55,-58,-64,-88,-121,-56,-65,]),'MODE':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[44,44,-27,-28,-29,-30,-31,-32,-33,-34,44,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,44,-48,-121,44,-100,-55,-58,-64,-88,-121,-56,-65,]),'STDV':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[45,45,-27,-28,-29,-30,-31,-32,-33,-34,45,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,45,-48,-121,45,-100,-55,-58,-64,-88,-121,-56,-65,]),'KMEANS':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[46,46,-27,-28,-29,-30,-31,-32,-33,-34,46,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,46,-48,-121,46,-100,-55,-58,-64,-88,-121,-56,-65,]),'DERL':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[47,47,-27,-28,-29,-30,-31,-32,-33,-34,47,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,47,-48,-121,47,-100,-55,-58,-64,-88,-121,-56,-65,]),'DBERN':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[48,48,-27,-28,-29,-30,-31,-32,-33,-34,48,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,48,-48,-121,48,-100,-55,-58,-64,-88,-121,-56,-65,]),'DPOI':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[49,49,-27,-28,-29,-30,-31,-32,-33,-34,49,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,49,-48,-121,49,-100,-55,-58,-64,-88,-121,-56,-65,]),'TRANSPOSE':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[50,50,-27,-28,-29,-30,-31,-32,-33,-34,50,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,50,-48,-121,50,-100,-55,-58,-64,-88,-121,-56,-65,]),'INVERSE':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[51,51,-27,-28,-29,-30,-31,-32,-33,-34,51,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,51,-48,-121,51,-100,-55,-58,-64,-88,-121,-56,-65,]),'ROTATE':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[52,52,-27,-28,-29,-30,-31,-32,-33,-34,52,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,52,-48,-121,52,-100,-55,-58,-64,-88,-121,-56,-65,]),'REF':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[53,53,-27,-28,-29,-30,-31,-32,-33,-34,53,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,53,-48,-121,53,-100,-55,-58,-64,-88,-121,-56,-65,]),'RREF':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[54,54,-27,-28,-29,-30,-31,-32,-33,-34,54,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,54,-48,-121,54,-100,-55,-58,-64,-88,-121,-56,-65,]),'MONT':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[55,55,-27,-28,-29,-30,-31,-32,-33,-34,55,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,55,-48,-121,55,-100,-55,-58,-64,-88,-121,-56,-65,]),'DO':([18,26,28,29,30,31,32,33,34,35,153,168,170,176,214,216,217,219,224,225,226,232,235,236,237,239,242,243,246,247,248,249,250,251,259,261,262,279,282,292,300,301,317,319,320,322,323,],[56,56,-27,-28,-29,-30,-31,-32,-33,-34,56,-36,-35,-47,-37,-38,-39,-46,-49,-66,-67,-96,-97,-98,-99,-101,-102,-103,-104,-105,-106,-107,-108,-109,-40,56,-48,-121,56,-100,-55,-58,-64,-88,-121,-56,-65,]),'INT':([22,57,65,],[60,60,60,]),'BOOL':([22,57,65,],[61,61,61,]),'DOUBLE':([22,57,65,],[62,62,62,]),'STRING':([22,57,65,81,178,],[63,63,63,122,223,]),'CHAR':([22,57,65,],[64,64,64,]),'NUMERIC':([24,69,70,71,72,73,74,75,78,80,81,89,90,91,92,105,106,107,108,109,110,111,112,114,117,128,133,158,159,160,161,162,163,164,165,166,167,183,184,186,187,198,202,229,234,252,257,258,268,269,274,276,297,298,],[71,-74,-84,-86,-87,-76,-79,71,71,71,71,71,71,71,71,-121,71,-121,-85,71,71,71,71,-83,71,71,71,71,-41,-45,-75,-42,-77,-78,-80,-81,-82,71,71,71,71,71,71,71,71,71,-43,-44,71,71,71,71,71,71,]),'NUMBER':([24,69,70,71,72,73,74,75,78,80,81,89,90,91,92,105,106,107,108,109,110,111,112,114,117,128,133,158,159,160,161,162,163,164,165,166,167,183,184,186,187,198,202,229,234,252,257,258,268,269,274,276,297,298,],[72,-74,-84,-86,-87,-76,-79,72,72,72,72,72,72,72,72,-121,72,-121,-85,72,72,72,72,-83,72,72,72,72,-41,-45,-75,-42,-77,-78,-80,-81,-82,72,72,72,72,72,72,72,72,72,-43,-44,72,72,72,72,72,72,]),'OPAREN':([24,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,62,63,64,69,70,71,72,73,74,75,78,80,81,101,105,106,107,108,109,110,111,112,114,117,154,155,158,159,160,161,162,163,164,165,166,167,183,184,209,252,257,258,276,297,298,],[75,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,-22,-23,-24,-25,-26,-74,-84,-86,-87,-76,-79,75,75,75,75,-121,-121,75,-121,-85,75,75,75,75,-83,75,211,-15,75,-41,-45,-75,-42,-77,-78,-80,-81,-82,75,75,252,75,-43,-44,75,75,75,]),'EQUALS':([36,79,105,107,125,126,159,160,162,257,258,],[78,117,-121,-121,183,184,-41,-45,-42,-43,-44,]),'RCOR':([67,68,69,70,71,72,73,74,105,107,108,114,159,160,161,162,163,164,165,166,167,212,213,257,258,267,],[105,107,-74,-84,-86,-87,-76,-79,-121,-121,-85,-83,-41,-45,-75,-42,-77,-78,-80,-81,-82,257,258,-43,-44,288,]),'RELOP':([67,68,69,70,71,72,73,74,105,107,108,113,114,115,116,118,119,121,159,160,161,162,163,164,165,166,167,169,171,172,212,213,215,257,258,276,],[106,-83,-74,-84,-86,-87,-76,-79,-121,-121,-85,106,-83,-84,106,106,106,-84,-41,-45,-75,-42,-77,-78,-80,-81,-82,-85,-84,106,106,-83,-85,-43,-44,106,]),'MULT':([68,70,71,72,74,105,107,108,114,115,121,159,160,162,167,169,171,213,215,257,258,],[-83,-84,-86,-87,111,-121,-121,-85,-83,-84,-84,-41,-45,-42,-82,-85,-84,-83,-85,-43,-44,]),'DIV':([68,70,71,72,74,105,107,108,114,115,121,159,160,162,167,169,171,213,215,257,258,],[-83,-84,-86,-87,112,-121,-121,-85,-83,-84,-84,-41,-45,-42,-82,-85,-84,-83,-85,-43,-44,]),'PLUS':([68,70,71,72,73,74,105,107,108,114,115,121,159,160,162,165,166,167,169,171,213,215,257,258,],[-83,-84,-86,-87,109,-79,-121,-121,-85,-83,-84,-84,-41,-45,-42,-80,-81,-82,-85,-84,-83,-85,-43,-44,]),'MINUS':([68,70,71,72,73,74,105,107,108,114,115,121,159,160,162,165,166,167,169,171,213,215,257,258,],[-83,-84,-86,-87,110,-79,-121,-121,-85,-83,-84,-84,-41,-45,-42,-80,-81,-82,-85,-84,-83,-85,-43,-44,]),'AND':([69,70,71,72,73,74,105,107,108,114,159,160,161,162,163,164,165,166,167,257,258,276,],[-74,-84,-86,-87,-76,-79,-121,-121,-85,-83,-41,-45,-75,-42,-77,-78,-80,-81,-82,-43,-44,297,]),'OR':([69,70,71,72,73,74,105,107,108,114,159,160,161,162,163,164,165,166,167,257,258,276,],[-74,-84,-86,-87,-76,-79,-121,-121,-85,-83,-41,-45,-75,-42,-77,-78,-80,-81,-82,-43,-44,298,]),'FX':([82,265,266,],[125,125,125,]),'FY':([82,265,266,],[126,126,126,]),'WHILE':([152,253,],[209,-91,]),'ELSE':([260,304,],[280,-60,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lugstat':([0,],[1,]),'addmain':([4,],[5,]),'empty':([4,5,7,12,18,26,56,82,85,86,87,88,93,94,95,96,97,98,101,102,105,107,118,121,133,153,195,211,222,223,234,252,261,264,265,266,270,276,278,279,280,282,295,297,298,306,320,],[6,9,13,13,27,27,100,127,134,134,134,134,134,134,134,134,134,134,155,9,160,160,174,179,191,27,134,256,179,179,191,277,283,179,286,286,134,277,256,301,303,283,310,277,277,316,301,]),'lugstat2':([5,102,],[7,156,]),'vars':([5,102,211,278,],[8,8,255,255,]),'lugstat3':([7,12,],[11,19,]),'modules':([7,12,],[12,12,]),'vars1':([10,21,66,],[15,58,104,]),'block':([11,299,],[17,313,]),'asign2':([16,36,70,115,121,140,144,171,],[23,79,108,169,108,108,108,215,]),'block2':([18,26,153,],[25,77,210,]),'estatuto':([18,26,153,261,282,],[26,26,26,282,282,]),'asign':([18,26,153,261,282,],[28,28,28,28,28,]),'cond':([18,26,153,261,282,308,],[29,29,29,29,29,318,]),'escrt':([18,26,153,261,282,],[30,30,30,30,30,]),'plot':([18,26,153,261,282,],[31,31,31,31,31,]),'count':([18,26,153,261,282,],[32,32,32,32,32,]),'countif':([18,26,153,261,282,],[33,33,33,33,33,]),'metodos':([18,26,153,261,282,],[34,34,34,34,34,]),'dwhile':([18,26,153,261,282,],[35,35,35,35,35,]),'tipo':([22,57,65,],[59,101,103,]),'expresion':([24,75,78,80,81,117,158,252,276,297,298,],[67,113,116,118,119,172,212,276,276,276,276,]),'varcte':([24,75,78,80,81,89,90,91,92,106,109,110,111,112,117,128,133,158,183,184,186,187,198,202,229,234,252,268,269,274,276,297,298,],[68,114,114,114,114,138,141,141,145,114,114,114,114,114,114,185,190,213,114,114,230,231,241,245,267,190,114,289,290,294,114,114,114,]),'exp':([24,75,78,80,81,106,109,110,117,158,183,184,252,276,297,298,],[69,69,69,69,69,161,163,164,69,69,227,228,69,69,69,69,]),'termino':([24,75,78,80,81,106,109,110,111,112,117,158,183,184,252,276,297,298,],[73,73,73,73,73,73,73,73,165,166,73,73,73,73,73,73,73,73,]),'factor':([24,75,78,80,81,106,109,110,111,112,117,158,183,184,252,276,297,298,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'wn1':([56,],[99,]),'xyfunc':([82,265,266,],[123,285,287,]),'plot2':([82,306,],[124,315,]),'mmmfunc':([85,86,87,88,93,94,95,96,97,98,195,270,],[131,135,136,137,146,147,148,149,150,151,238,291,]),'expfunc':([90,91,],[139,142,]),'expfunc2':([92,],[143,]),'wblock':([99,],[152,]),'addfunction':([101,],[154,]),'asign3':([105,107,],[159,162,]),'cn1':([118,],[173,]),'escrt2':([121,222,223,264,],[177,263,264,284,]),'mmmarray':([133,234,],[189,271,]),'escrt3':([178,],[221,]),'modules2':([211,278,],[254,299,]),'ifblock':([218,302,],[260,314,]),'dwhileconds':([252,276,297,298,],[275,296,311,312,]),'ifblock2':([261,282,],[281,305,]),'cn2':([279,320,],[300,322,]),'cn3':([280,],[302,]),'wn2':([295,],[309,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lugstat","S'",1,None,None,None),
  ('lugstat -> LUGSTAT ID SCOLON addmain lugstat2 lugstat3 block','lugstat',7,'p_lugstat','LUGSTAT.py',211),
  ('addmain -> empty','addmain',1,'p_addmain','LUGSTAT.py',215),
  ('lugstat2 -> vars','lugstat2',1,'p_lugstat2','LUGSTAT.py',226),
  ('lugstat2 -> empty','lugstat2',1,'p_lugstat2','LUGSTAT.py',227),
  ('lugstat3 -> modules','lugstat3',1,'p_lugstat3','LUGSTAT.py',232),
  ('lugstat3 -> modules lugstat3','lugstat3',2,'p_lugstat3','LUGSTAT.py',233),
  ('lugstat3 -> empty','lugstat3',1,'p_lugstat3','LUGSTAT.py',234),
  ('vars -> VAR vars1','vars',2,'p_vars','LUGSTAT.py',238),
  ('vars1 -> ID COMMA vars1','vars1',3,'p_vars1','LUGSTAT.py',274),
  ('vars1 -> ID COLON tipo SCOLON lugstat2','vars1',5,'p_vars1','LUGSTAT.py',275),
  ('vars1 -> ID asign2 COLON tipo SCOLON','vars1',5,'p_vars1','LUGSTAT.py',276),
  ('vars1 -> ID asign2 COMMA vars1','vars1',4,'p_vars1','LUGSTAT.py',277),
  ('savename -> empty','savename',1,'p_savename','LUGSTAT.py',303),
  ('modules -> FUNC ID COLON tipo addfunction OPAREN modules2 CPAREN modules2 block','modules',10,'p_modules','LUGSTAT.py',307),
  ('addfunction -> empty','addfunction',1,'p_addfunction','LUGSTAT.py',311),
  ('modules2 -> vars','modules2',1,'p_modules2','LUGSTAT.py',319),
  ('modules2 -> empty','modules2',1,'p_modules2','LUGSTAT.py',320),
  ('block -> OBRACKET block2 CBRACKET','block',3,'p_block','LUGSTAT.py',326),
  ('block2 -> estatuto','block2',1,'p_block2','LUGSTAT.py',337),
  ('block2 -> estatuto block2','block2',2,'p_block2','LUGSTAT.py',338),
  ('block2 -> empty','block2',1,'p_block2','LUGSTAT.py',339),
  ('tipo -> INT','tipo',1,'p_tipo','LUGSTAT.py',343),
  ('tipo -> BOOL','tipo',1,'p_tipo','LUGSTAT.py',344),
  ('tipo -> DOUBLE','tipo',1,'p_tipo','LUGSTAT.py',345),
  ('tipo -> STRING','tipo',1,'p_tipo','LUGSTAT.py',346),
  ('tipo -> CHAR','tipo',1,'p_tipo','LUGSTAT.py',347),
  ('estatuto -> asign','estatuto',1,'p_estatuto','LUGSTAT.py',353),
  ('estatuto -> cond','estatuto',1,'p_estatuto','LUGSTAT.py',354),
  ('estatuto -> escrt','estatuto',1,'p_estatuto','LUGSTAT.py',355),
  ('estatuto -> plot','estatuto',1,'p_estatuto','LUGSTAT.py',356),
  ('estatuto -> count','estatuto',1,'p_estatuto','LUGSTAT.py',357),
  ('estatuto -> countif','estatuto',1,'p_estatuto','LUGSTAT.py',358),
  ('estatuto -> metodos','estatuto',1,'p_estatuto','LUGSTAT.py',359),
  ('estatuto -> dwhile','estatuto',1,'p_estatuto','LUGSTAT.py',360),
  ('asign -> ID EQUALS expresion SCOLON','asign',4,'p_asign','LUGSTAT.py',365),
  ('asign -> ID EQUALS ID SCOLON','asign',4,'p_asign','LUGSTAT.py',366),
  ('asign -> ID EQUALS ID asign2 SCOLON','asign',5,'p_asign','LUGSTAT.py',367),
  ('asign -> ID asign2 EQUALS ID SCOLON','asign',5,'p_asign','LUGSTAT.py',368),
  ('asign -> ID asign2 EQUALS expresion SCOLON','asign',5,'p_asign','LUGSTAT.py',369),
  ('asign -> ID asign2 EQUALS ID asign2 SCOLON','asign',6,'p_asign','LUGSTAT.py',370),
  ('asign2 -> LCOR expresion RCOR asign3','asign2',4,'p_asign2','LUGSTAT.py',431),
  ('asign2 -> LCOR varcte RCOR asign3','asign2',4,'p_asign2','LUGSTAT.py',432),
  ('asign3 -> LCOR expresion RCOR','asign3',3,'p_asign3','LUGSTAT.py',437),
  ('asign3 -> LCOR varcte RCOR','asign3',3,'p_asign3','LUGSTAT.py',438),
  ('asign3 -> empty','asign3',1,'p_asign3','LUGSTAT.py',439),
  ('escrt -> PRINT OPAREN expresion CPAREN SCOLON','escrt',5,'p_escrt','LUGSTAT.py',443),
  ('escrt -> PRINT OPAREN CPAREN SCOLON','escrt',4,'p_escrt','LUGSTAT.py',444),
  ('escrt -> PRINT OPAREN ID escrt2 CPAREN SCOLON','escrt',6,'p_escrt','LUGSTAT.py',445),
  ('escrt -> PRINT OPAREN STRING CPAREN SCOLON','escrt',5,'p_escrt','LUGSTAT.py',446),
  ('escrt2 -> COMMA escrt3','escrt2',2,'p_escrt2','LUGSTAT.py',450),
  ('escrt2 -> empty','escrt2',1,'p_escrt2','LUGSTAT.py',451),
  ('escrt3 -> ID escrt2','escrt3',2,'p_escrt3','LUGSTAT.py',455),
  ('escrt3 -> ID','escrt3',1,'p_escrt3','LUGSTAT.py',456),
  ('escrt3 -> STRING escrt2 escrt2','escrt3',3,'p_escrt3','LUGSTAT.py',457),
  ('cond -> IF OPAREN expresion cn1 CPAREN ifblock SCOLON cn2','cond',8,'p_cond','LUGSTAT.py',461),
  ('cond -> IF OPAREN expresion cn1 CPAREN ifblock ELSE cn3 ifblock SCOLON cn2','cond',11,'p_cond','LUGSTAT.py',462),
  ('cn1 -> empty','cn1',1,'p_cn1','LUGSTAT.py',466),
  ('cn2 -> empty','cn2',1,'p_cn2','LUGSTAT.py',480),
  ('cn3 -> empty','cn3',1,'p_cn3','LUGSTAT.py',487),
  ('ifblock -> OBRACKET ifblock2 CBRACKET','ifblock',3,'p_ifblock','LUGSTAT.py',495),
  ('ifblock2 -> estatuto','ifblock2',1,'p_ifblock2','LUGSTAT.py',499),
  ('ifblock2 -> estatuto ifblock2','ifblock2',2,'p_ifblock2','LUGSTAT.py',500),
  ('ifblock2 -> empty','ifblock2',1,'p_ifblock2','LUGSTAT.py',501),
  ('count -> COUNT OPAREN ID COMMA varcte COMMA varcte CPAREN SCOLON','count',9,'p_count','LUGSTAT.py',504),
  ('countif -> COUNTIF OPAREN ID COMMA varcte COMMA varcte COMMA cond CPAREN SCOLON','countif',11,'p_countif','LUGSTAT.py',507),
  ('plot -> PLOT OPAREN xyfunc CPAREN SCOLON','plot',5,'p_plot','LUGSTAT.py',510),
  ('plot -> PLOT OPAREN plot2 CPAREN SCOLON','plot',5,'p_plot','LUGSTAT.py',511),
  ('plot2 -> LCOR varcte COMMA varcte RCOR','plot2',5,'p_plot2','LUGSTAT.py',515),
  ('plot2 -> LCOR varcte COMMA varcte RCOR COMMA plot2','plot2',7,'p_plot2','LUGSTAT.py',516),
  ('plot2 -> empty','plot2',1,'p_plot2','LUGSTAT.py',517),
  ('xyfunc -> FX EQUALS exp SCOLON xyfunc','xyfunc',5,'p_xyfunc','LUGSTAT.py',521),
  ('xyfunc -> FY EQUALS exp SCOLON xyfunc','xyfunc',5,'p_xyfunc','LUGSTAT.py',522),
  ('xyfunc -> empty','xyfunc',1,'p_xyfunc','LUGSTAT.py',523),
  ('expresion -> exp','expresion',1,'p_expresion','LUGSTAT.py',528),
  ('expresion -> expresion RELOP exp','expresion',3,'p_expresion','LUGSTAT.py',529),
  ('exp -> termino','exp',1,'p_exp','LUGSTAT.py',559),
  ('exp -> termino PLUS exp','exp',3,'p_exp','LUGSTAT.py',560),
  ('exp -> termino MINUS exp','exp',3,'p_exp','LUGSTAT.py',561),
  ('termino -> factor','termino',1,'p_termino','LUGSTAT.py',603),
  ('termino -> factor MULT termino','termino',3,'p_termino','LUGSTAT.py',604),
  ('termino -> factor DIV termino','termino',3,'p_termino','LUGSTAT.py',605),
  ('factor -> OPAREN expresion CPAREN','factor',3,'p_factor','LUGSTAT.py',643),
  ('factor -> varcte','factor',1,'p_factor','LUGSTAT.py',644),
  ('varcte -> ID','varcte',1,'p_varcte','LUGSTAT.py',659),
  ('varcte -> ID asign2','varcte',2,'p_varcte','LUGSTAT.py',660),
  ('varcte -> NUMERIC','varcte',1,'p_varcte','LUGSTAT.py',661),
  ('varcte -> NUMBER','varcte',1,'p_varcte','LUGSTAT.py',662),
  ('dwhile -> DO wn1 wblock WHILE OPAREN dwhileconds CPAREN wn2 SCOLON','dwhile',9,'p_dwhile','LUGSTAT.py',706),
  ('wn1 -> empty','wn1',1,'p_wn1','LUGSTAT.py',709),
  ('wn2 -> empty','wn2',1,'p_wn2','LUGSTAT.py',712),
  ('wblock -> OBRACKET block2 CBRACKET','wblock',3,'p_wblock','LUGSTAT.py',726),
  ('dwhileconds -> expresion dwhileconds','dwhileconds',2,'p_dwhileconds','LUGSTAT.py',731),
  ('dwhileconds -> expresion AND dwhileconds','dwhileconds',3,'p_dwhileconds','LUGSTAT.py',732),
  ('dwhileconds -> expresion OR dwhileconds','dwhileconds',3,'p_dwhileconds','LUGSTAT.py',733),
  ('dwhileconds -> empty','dwhileconds',1,'p_dwhileconds','LUGSTAT.py',734),
  ('metodos -> MEAN OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',740),
  ('metodos -> MEDIAN OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',741),
  ('metodos -> MODE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',742),
  ('metodos -> STDV OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',743),
  ('metodos -> KMEANS OPAREN varcte COMMA mmmfunc CPAREN SCOLON','metodos',7,'p_metodos','LUGSTAT.py',744),
  ('metodos -> DERL OPAREN expfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',745),
  ('metodos -> DBERN OPAREN expfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',746),
  ('metodos -> DPOI OPAREN expfunc2 CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',747),
  ('metodos -> TRANSPOSE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',748),
  ('metodos -> INVERSE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',749),
  ('metodos -> ROTATE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',750),
  ('metodos -> REF OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',751),
  ('metodos -> RREF OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',752),
  ('metodos -> MONT OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',753),
  ('expfunc -> ID COMMA ID COMMA ID','expfunc',5,'p_expfunc','LUGSTAT.py',758),
  ('expfunc -> varcte COMMA varcte COMMA varcte','expfunc',5,'p_expfunc','LUGSTAT.py',759),
  ('expfunc2 -> ID COMMA ID','expfunc2',3,'p_expfunc2','LUGSTAT.py',764),
  ('expfunc2 -> varcte COMMA varcte','expfunc2',3,'p_expfunc2','LUGSTAT.py',765),
  ('mmmfunc -> ID','mmmfunc',1,'p_mmmfunc','LUGSTAT.py',770),
  ('mmmfunc -> OBRACKET mmmarray CBRACKET','mmmfunc',3,'p_mmmfunc','LUGSTAT.py',771),
  ('mmmfunc -> OBRACKET mmmarray CBRACKET COMMA mmmfunc','mmmfunc',5,'p_mmmfunc','LUGSTAT.py',772),
  ('mmmfunc -> empty','mmmfunc',1,'p_mmmfunc','LUGSTAT.py',773),
  ('mmmarray -> varcte','mmmarray',1,'p_mmmarray','LUGSTAT.py',778),
  ('mmmarray -> varcte COMMA mmmarray','mmmarray',3,'p_mmmarray','LUGSTAT.py',779),
  ('mmmarray -> empty','mmmarray',1,'p_mmmarray','LUGSTAT.py',780),
  ('empty -> <empty>','empty',0,'p_empty','LUGSTAT.py',784),
]
