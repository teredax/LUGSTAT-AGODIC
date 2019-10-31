
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CBRACKET CHAR CHARACTER COLON COMMA COMMENT COUNT COUNTIF CPAREN CTED CTEI DBERN DERL DIFF DIV DOUBLE DPOI ELSE EQ EQUALS FUNC FX FY GRE GREATEQ GREATERTHAN ID IF INT INTEGER INVERSE KMEANS LCOR LESSEQ LESSTHAN LOGICAL LUGSTAT MEAN MEDIAN MINUS MODE MONT MULT NUMBER NUMERIC OBRACKET OPAREN OR PER PLOT PLUS PRINT QUOTE RCOR REF RELOP ROTATE RREF SCOLON STDV STRING TIPO TRANSPOSE VAR\n    lugstat : LUGSTAT ID SCOLON lugstat2 lugstat3 block\n    \n    lugstat2 : vars\n    | empty\n    \n    lugstat3 : modules\n    | modules lugstat3\n    | empty\n    vars : VAR vars1 \n    \n    vars1 : ID COLON tipo SCOLON\n    | ID COMMA vars1\n    | ID asign2 COLON tipo SCOLON\n    | ID asign2 COMMA vars1\n    \n    modules : FUNC ID COLON tipo addfunction OPAREN modules2 CPAREN modules2 blockaddfunction : empty\n    modules2 : vars\n    | empty\n    block : OBRACKET block2 CBRACKET\n    \n    block2 : estatuto\n    | estatuto block2\n    | empty\n    tipo : INT\n    | BOOL \n    | DOUBLE\n    | STRING\n    | CHAR\n    \n    estatuto : asign\n    | cond \n    | escrt\n    | plot\n    | count\n    | countif\n    | metodos\n    \n    asign : ID EQUALS expresion SCOLON\n    | ID EQUALS ID SCOLON\n    | ID EQUALS ID asign2 SCOLON\n    | ID asign2 EQUALS ID SCOLON\n    | ID asign2 EQUALS expresion SCOLON\n    | ID asign2 EQUALS ID asign2 SCOLON\n    \n    asign2 : LCOR expresion RCOR asign3\n    | LCOR varcte RCOR asign3 \n    \n    asign3 : LCOR expresion RCOR\n    | LCOR varcte RCOR \n    | emptyescrt : PRINT OPAREN expresion CPAREN SCOLON\n\t| PRINT OPAREN CPAREN SCOLON\n    | PRINT OPAREN ID escrt2 CPAREN SCOLON\n    | PRINT OPAREN STRING CPAREN SCOLON\n    escrt2 : COMMA escrt3\n    | empty\n    escrt3 : ID escrt2\n    | ID\n    | STRING escrt2 escrt2\n    cond : IF OPAREN expresion CPAREN block SCOLON\n    | IF OPAREN expresion CPAREN block ELSE block SCOLON\n    count : COUNT OPAREN ID COMMA varcte COMMA varcte CPAREN SCOLONcountif : COUNTIF OPAREN ID COMMA varcte COMMA varcte COMMA cond CPAREN SCOLONplot : PLOT OPAREN xyfunc CPAREN SCOLON\n    | PLOT OPAREN plot2 CPAREN SCOLON\n    \n    plot2 : LCOR varcte COMMA varcte RCOR\n    | LCOR varcte COMMA varcte RCOR COMMA plot2\n    | empty\n    xyfunc : FX EQUALS exp SCOLON xyfunc\n    | FY EQUALS exp SCOLON xyfunc\n    | empty\n    expresion : exp \n    | expresion RELOP exp \n    \n    exp : termino\n    | termino PLUS exp\n    | termino MINUS exp\n    \n    termino : factor\n    | factor MULT termino\n    | factor DIV termino\n    \n    factor : OPAREN expresion CPAREN \n    | PLUS varcte\n    | MINUS varcte\n    | varcte\n    \n    varcte : ID\n    | ID asign2\n    | NUMERIC\n    | NUMBER\n    \n    metodos : MEAN OPAREN mmmfunc CPAREN SCOLON\n    | MEDIAN OPAREN mmmfunc CPAREN SCOLON\n    | MODE OPAREN mmmfunc CPAREN SCOLON\n    | STDV OPAREN mmmfunc CPAREN SCOLON\n    | KMEANS OPAREN varcte COMMA mmmfunc CPAREN SCOLON\n    | DERL OPAREN expfunc CPAREN SCOLON\n    | DBERN OPAREN expfunc CPAREN SCOLON\n    | DPOI OPAREN expfunc2 CPAREN SCOLON\n    | TRANSPOSE OPAREN mmmfunc CPAREN SCOLON\n    | INVERSE OPAREN mmmfunc CPAREN SCOLON\n    | ROTATE OPAREN mmmfunc CPAREN SCOLON\n    | REF OPAREN mmmfunc CPAREN SCOLON\n    | RREF OPAREN mmmfunc CPAREN SCOLON\n    | MONT OPAREN mmmfunc CPAREN SCOLON\n    \n    expfunc : ID COMMA ID COMMA ID\n    | varcte COMMA varcte COMMA varcte\n    \n    expfunc2 : ID COMMA ID\n    | varcte COMMA varcte\n    \n    mmmfunc : ID \n    | OBRACKET  mmmarray CBRACKET\n\t| OBRACKET mmmarray CBRACKET COMMA mmmfunc\n\t| empty \n    \n    mmmarray : varcte\n    | varcte COMMA mmmarray\n    | empty\n    empty :'
    
_lr_action_items = {'LUGSTAT':([0,],[2,]),'$end':([1,15,74,],[0,-1,-16,]),'ID':([2,8,12,16,20,22,24,26,27,28,29,30,31,32,62,70,71,73,76,78,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,102,105,106,109,110,115,126,131,153,163,165,170,172,177,178,180,181,189,191,192,195,196,206,208,209,211,216,217,218,221,224,226,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,258,259,260,263,264,275,279,286,289,],[3,14,18,33,14,66,33,-25,-26,-27,-28,-29,-30,-31,14,66,66,66,113,66,119,127,128,130,130,130,130,66,138,138,142,130,130,130,130,130,130,66,66,66,66,66,166,66,66,66,-33,-32,-44,214,66,66,66,66,130,232,66,236,66,-34,-35,-36,-43,-46,-56,-57,66,-80,66,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,66,66,130,276,66,-84,-53,-54,-55,]),'SCOLON':([3,54,55,56,57,58,59,65,66,67,68,69,72,74,99,101,103,104,107,108,112,113,114,118,154,155,156,157,158,159,160,161,162,164,166,167,169,174,175,176,182,186,187,188,190,193,194,197,198,199,200,201,202,207,210,212,219,220,247,248,262,266,281,288,],[4,98,-20,-21,-22,-23,-24,-64,-76,-78,-79,-66,-69,-16,152,-105,-105,-77,-73,-74,-75,163,165,170,-38,-42,-65,-39,-67,-68,-70,-71,-72,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,255,256,-40,-41,275,279,286,289,]),'VAR':([4,203,265,],[8,8,8,]),'FUNC':([4,5,6,7,10,13,60,74,98,100,152,283,],[-105,12,-2,-3,12,-7,-9,-16,-8,-11,-10,-12,]),'OBRACKET':([4,5,6,7,9,10,11,13,17,60,74,83,84,85,86,91,92,93,94,95,96,98,100,152,168,189,245,246,251,260,265,278,283,],[-105,-105,-2,-3,16,-4,-6,-7,-5,-9,-16,131,131,131,131,131,131,131,131,131,131,-8,-11,-10,16,131,-14,-15,16,131,-105,16,-12,]),'CPAREN':([13,60,65,66,67,68,69,72,79,80,83,84,85,86,91,92,93,94,95,96,98,100,101,103,104,107,108,111,112,116,117,119,120,121,122,125,129,130,132,133,134,135,137,140,141,144,145,146,147,148,149,152,154,155,156,157,158,159,160,161,162,171,173,189,203,213,214,215,225,230,236,237,244,245,246,247,248,250,253,254,255,256,260,267,268,269,270,271,272,274,276,277,279,280,284,285,287,],[-7,-9,-64,-76,-78,-79,-66,-69,118,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-8,-11,-105,-105,-77,-73,-74,162,-75,168,169,-76,174,175,176,-60,182,-98,-101,186,187,188,190,193,194,197,198,199,200,201,202,-10,-38,-42,-65,-39,-67,-68,-70,-71,-72,212,-48,-105,-105,-47,-50,-105,-99,262,-96,-97,265,-14,-15,-40,-41,-52,-49,-105,-105,-105,-105,-51,-61,-63,-62,-58,281,-100,-94,-95,-53,-105,-59,-60,288,]),'COLON':([14,18,21,101,103,154,155,157,247,248,],[19,53,61,-105,-105,-38,-42,-39,-40,-41,]),'COMMA':([14,21,66,67,68,101,103,104,119,127,128,136,138,139,142,143,154,155,157,173,179,184,213,214,215,222,223,225,232,233,247,248,253,254,267,271,273,],[20,62,-76,-78,-79,-105,-105,-77,172,180,181,189,191,192,195,196,-38,-42,-39,-48,221,226,-47,172,172,258,259,260,263,264,-40,-41,-49,172,-51,280,282,]),'LCOR':([14,33,66,80,101,103,113,119,138,142,166,280,],[22,22,22,126,153,153,22,22,22,22,22,126,]),'CBRACKET':([16,23,24,25,26,27,28,29,30,31,32,66,67,68,75,101,103,104,131,154,155,157,163,165,170,183,184,185,206,208,209,211,216,217,218,224,226,227,228,229,231,234,235,238,239,240,241,242,243,247,248,249,250,252,261,275,279,286,289,],[-105,74,-17,-19,-25,-26,-27,-28,-29,-30,-31,-76,-78,-79,-18,-105,-105,-77,-105,-38,-42,-39,-33,-32,-44,225,-102,-104,-34,-35,-36,-43,-46,-56,-57,-80,-105,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-40,-41,-37,-52,-45,-103,-84,-53,-54,-55,]),'IF':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,282,286,289,],[34,34,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,34,-54,-55,]),'PRINT':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[35,35,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'PLOT':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[36,36,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'COUNT':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[37,37,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'COUNTIF':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[38,38,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'MEAN':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[39,39,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'MEDIAN':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[40,40,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'MODE':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[41,41,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'STDV':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[42,42,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'KMEANS':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[43,43,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'DERL':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[44,44,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'DBERN':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[45,45,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'DPOI':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[46,46,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'TRANSPOSE':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[47,47,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'INVERSE':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[48,48,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'ROTATE':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[49,49,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'REF':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[50,50,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'RREF':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[51,51,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'MONT':([16,24,26,27,28,29,30,31,32,163,165,170,206,208,209,211,216,217,218,224,227,228,229,231,234,235,238,239,240,241,242,243,249,250,252,275,279,286,289,],[52,52,-25,-26,-27,-28,-29,-30,-31,-33,-32,-44,-34,-35,-36,-43,-46,-56,-57,-80,-81,-82,-83,-85,-86,-87,-88,-89,-90,-91,-92,-93,-37,-52,-45,-84,-53,-54,-55,]),'INT':([19,53,61,],[55,55,55,]),'BOOL':([19,53,61,],[56,56,56,]),'DOUBLE':([19,53,61,],[57,57,57,]),'STRING':([19,53,61,79,172,],[58,58,58,120,215,]),'CHAR':([19,53,61,],[59,59,59,]),'NUMERIC':([22,70,71,73,76,78,79,87,88,89,90,102,105,106,109,110,115,126,131,153,177,178,180,181,192,196,221,226,258,259,264,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'NUMBER':([22,70,71,73,76,78,79,87,88,89,90,102,105,106,109,110,115,126,131,153,177,178,180,181,192,196,221,226,258,259,264,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'OPAREN':([22,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,73,76,78,79,97,102,105,106,109,110,115,150,151,153,177,178,],[73,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,-20,-21,-22,-23,-24,73,73,73,73,-105,73,73,73,73,73,73,203,-13,73,73,73,]),'PLUS':([22,64,66,67,68,69,72,73,76,78,79,101,102,103,104,105,106,107,108,109,110,112,113,115,119,153,154,155,157,160,161,162,164,166,177,178,205,207,247,248,],[70,-75,-76,-78,-79,105,-69,70,70,70,70,-105,70,-105,-77,70,70,-73,-74,70,70,-75,-76,70,-76,70,-38,-42,-39,-70,-71,-72,-77,-76,70,70,-75,-77,-40,-41,]),'MINUS':([22,64,66,67,68,69,72,73,76,78,79,101,102,103,104,105,106,107,108,109,110,112,113,115,119,153,154,155,157,160,161,162,164,166,177,178,205,207,247,248,],[71,-75,-76,-78,-79,106,-69,71,71,71,71,-105,71,-105,-77,71,71,-73,-74,71,71,-75,-76,71,-76,71,-38,-42,-39,-70,-71,-72,-77,-76,71,71,-75,-77,-40,-41,]),'EQUALS':([33,77,101,103,123,124,154,155,157,247,248,],[76,115,-105,-105,177,178,-38,-42,-39,-40,-41,]),'RCOR':([63,64,65,66,67,68,69,72,101,103,104,107,108,112,154,155,156,157,158,159,160,161,162,204,205,247,248,257,],[101,103,-64,-76,-78,-79,-66,-69,-105,-105,-77,-73,-74,-75,-38,-42,-65,-39,-67,-68,-70,-71,-72,247,248,-40,-41,271,]),'RELOP':([63,64,65,66,67,68,69,72,101,103,104,107,108,111,112,113,114,116,117,119,154,155,156,157,158,159,160,161,162,164,166,167,204,205,207,247,248,],[102,-75,-64,-76,-78,-79,-66,-69,-105,-105,-77,-73,-74,102,-75,-76,102,102,102,-76,-38,-42,-65,-39,-67,-68,-70,-71,-72,-77,-76,102,102,-75,-77,-40,-41,]),'MULT':([64,66,67,68,72,101,103,104,107,108,112,113,119,154,155,157,162,164,166,205,207,247,248,],[-75,-76,-78,-79,109,-105,-105,-77,-73,-74,-75,-76,-76,-38,-42,-39,-72,-77,-76,-75,-77,-40,-41,]),'DIV':([64,66,67,68,72,101,103,104,107,108,112,113,119,154,155,157,162,164,166,205,207,247,248,],[-75,-76,-78,-79,110,-105,-105,-77,-73,-74,-75,-76,-76,-38,-42,-39,-72,-77,-76,-75,-77,-40,-41,]),'ELSE':([74,210,],[-16,251,]),'FX':([80,255,256,],[123,123,123,]),'FY':([80,255,256,],[124,124,124,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lugstat':([0,],[1,]),'lugstat2':([4,],[5,]),'vars':([4,203,265,],[6,245,245,]),'empty':([4,5,10,16,24,80,83,84,85,86,91,92,93,94,95,96,97,101,103,119,131,189,203,214,215,226,254,255,256,260,265,280,],[7,11,11,25,25,125,132,132,132,132,132,132,132,132,132,132,151,155,155,173,185,132,246,173,173,185,173,269,269,132,246,285,]),'lugstat3':([5,10,],[9,17,]),'modules':([5,10,],[10,10,]),'vars1':([8,20,62,],[13,60,100,]),'block':([9,168,251,278,],[15,210,266,283,]),'asign2':([14,33,66,113,119,138,142,166,],[21,77,104,164,104,104,104,207,]),'block2':([16,24,],[23,75,]),'estatuto':([16,24,],[24,24,]),'asign':([16,24,],[26,26,]),'cond':([16,24,282,],[27,27,287,]),'escrt':([16,24,],[28,28,]),'plot':([16,24,],[29,29,]),'count':([16,24,],[30,30,]),'countif':([16,24,],[31,31,]),'metodos':([16,24,],[32,32,]),'tipo':([19,53,61,],[54,97,99,]),'expresion':([22,73,76,78,79,115,153,],[63,111,114,116,117,167,204,]),'varcte':([22,70,71,73,76,78,79,87,88,89,90,102,105,106,109,110,115,126,131,153,177,178,180,181,192,196,221,226,258,259,264,],[64,107,108,112,112,112,112,136,139,139,143,112,112,112,112,112,112,179,184,205,112,112,222,223,233,237,257,184,272,273,277,]),'exp':([22,73,76,78,79,102,105,106,115,153,177,178,],[65,65,65,65,65,156,158,159,65,65,219,220,]),'termino':([22,73,76,78,79,102,105,106,109,110,115,153,177,178,],[69,69,69,69,69,69,69,69,160,161,69,69,69,69,]),'factor':([22,73,76,78,79,102,105,106,109,110,115,153,177,178,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'xyfunc':([80,255,256,],[121,268,270,]),'plot2':([80,280,],[122,284,]),'mmmfunc':([83,84,85,86,91,92,93,94,95,96,189,260,],[129,133,134,135,144,145,146,147,148,149,230,274,]),'expfunc':([88,89,],[137,140,]),'expfunc2':([90,],[141,]),'addfunction':([97,],[150,]),'asign3':([101,103,],[154,157,]),'escrt2':([119,214,215,254,],[171,253,254,267,]),'mmmarray':([131,226,],[183,261,]),'escrt3':([172,],[213,]),'modules2':([203,265,],[244,278,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lugstat","S'",1,None,None,None),
  ('lugstat -> LUGSTAT ID SCOLON lugstat2 lugstat3 block','lugstat',6,'p_lugstat','LUGSTAT.py',144),
  ('lugstat2 -> vars','lugstat2',1,'p_lugstat2','LUGSTAT.py',150),
  ('lugstat2 -> empty','lugstat2',1,'p_lugstat2','LUGSTAT.py',151),
  ('lugstat3 -> modules','lugstat3',1,'p_lugstat3','LUGSTAT.py',156),
  ('lugstat3 -> modules lugstat3','lugstat3',2,'p_lugstat3','LUGSTAT.py',157),
  ('lugstat3 -> empty','lugstat3',1,'p_lugstat3','LUGSTAT.py',158),
  ('vars -> VAR vars1','vars',2,'p_vars','LUGSTAT.py',162),
  ('vars1 -> ID COLON tipo SCOLON','vars1',4,'p_vars1','LUGSTAT.py',170),
  ('vars1 -> ID COMMA vars1','vars1',3,'p_vars1','LUGSTAT.py',171),
  ('vars1 -> ID asign2 COLON tipo SCOLON','vars1',5,'p_vars1','LUGSTAT.py',172),
  ('vars1 -> ID asign2 COMMA vars1','vars1',4,'p_vars1','LUGSTAT.py',173),
  ('modules -> FUNC ID COLON tipo addfunction OPAREN modules2 CPAREN modules2 block','modules',10,'p_modules','LUGSTAT.py',184),
  ('addfunction -> empty','addfunction',1,'p_addfunction','LUGSTAT.py',187),
  ('modules2 -> vars','modules2',1,'p_modules2','LUGSTAT.py',195),
  ('modules2 -> empty','modules2',1,'p_modules2','LUGSTAT.py',196),
  ('block -> OBRACKET block2 CBRACKET','block',3,'p_block','LUGSTAT.py',202),
  ('block2 -> estatuto','block2',1,'p_block2','LUGSTAT.py',207),
  ('block2 -> estatuto block2','block2',2,'p_block2','LUGSTAT.py',208),
  ('block2 -> empty','block2',1,'p_block2','LUGSTAT.py',209),
  ('tipo -> INT','tipo',1,'p_tipo','LUGSTAT.py',213),
  ('tipo -> BOOL','tipo',1,'p_tipo','LUGSTAT.py',214),
  ('tipo -> DOUBLE','tipo',1,'p_tipo','LUGSTAT.py',215),
  ('tipo -> STRING','tipo',1,'p_tipo','LUGSTAT.py',216),
  ('tipo -> CHAR','tipo',1,'p_tipo','LUGSTAT.py',217),
  ('estatuto -> asign','estatuto',1,'p_estatuto','LUGSTAT.py',223),
  ('estatuto -> cond','estatuto',1,'p_estatuto','LUGSTAT.py',224),
  ('estatuto -> escrt','estatuto',1,'p_estatuto','LUGSTAT.py',225),
  ('estatuto -> plot','estatuto',1,'p_estatuto','LUGSTAT.py',226),
  ('estatuto -> count','estatuto',1,'p_estatuto','LUGSTAT.py',227),
  ('estatuto -> countif','estatuto',1,'p_estatuto','LUGSTAT.py',228),
  ('estatuto -> metodos','estatuto',1,'p_estatuto','LUGSTAT.py',229),
  ('asign -> ID EQUALS expresion SCOLON','asign',4,'p_asign','LUGSTAT.py',234),
  ('asign -> ID EQUALS ID SCOLON','asign',4,'p_asign','LUGSTAT.py',235),
  ('asign -> ID EQUALS ID asign2 SCOLON','asign',5,'p_asign','LUGSTAT.py',236),
  ('asign -> ID asign2 EQUALS ID SCOLON','asign',5,'p_asign','LUGSTAT.py',237),
  ('asign -> ID asign2 EQUALS expresion SCOLON','asign',5,'p_asign','LUGSTAT.py',238),
  ('asign -> ID asign2 EQUALS ID asign2 SCOLON','asign',6,'p_asign','LUGSTAT.py',239),
  ('asign2 -> LCOR expresion RCOR asign3','asign2',4,'p_asign2','LUGSTAT.py',244),
  ('asign2 -> LCOR varcte RCOR asign3','asign2',4,'p_asign2','LUGSTAT.py',245),
  ('asign3 -> LCOR expresion RCOR','asign3',3,'p_asign3','LUGSTAT.py',250),
  ('asign3 -> LCOR varcte RCOR','asign3',3,'p_asign3','LUGSTAT.py',251),
  ('asign3 -> empty','asign3',1,'p_asign3','LUGSTAT.py',252),
  ('escrt -> PRINT OPAREN expresion CPAREN SCOLON','escrt',5,'p_escrt','LUGSTAT.py',256),
  ('escrt -> PRINT OPAREN CPAREN SCOLON','escrt',4,'p_escrt','LUGSTAT.py',257),
  ('escrt -> PRINT OPAREN ID escrt2 CPAREN SCOLON','escrt',6,'p_escrt','LUGSTAT.py',258),
  ('escrt -> PRINT OPAREN STRING CPAREN SCOLON','escrt',5,'p_escrt','LUGSTAT.py',259),
  ('escrt2 -> COMMA escrt3','escrt2',2,'p_escrt2','LUGSTAT.py',263),
  ('escrt2 -> empty','escrt2',1,'p_escrt2','LUGSTAT.py',264),
  ('escrt3 -> ID escrt2','escrt3',2,'p_escrt3','LUGSTAT.py',268),
  ('escrt3 -> ID','escrt3',1,'p_escrt3','LUGSTAT.py',269),
  ('escrt3 -> STRING escrt2 escrt2','escrt3',3,'p_escrt3','LUGSTAT.py',270),
  ('cond -> IF OPAREN expresion CPAREN block SCOLON','cond',6,'p_cond','LUGSTAT.py',274),
  ('cond -> IF OPAREN expresion CPAREN block ELSE block SCOLON','cond',8,'p_cond','LUGSTAT.py',275),
  ('count -> COUNT OPAREN ID COMMA varcte COMMA varcte CPAREN SCOLON','count',9,'p_count','LUGSTAT.py',279),
  ('countif -> COUNTIF OPAREN ID COMMA varcte COMMA varcte COMMA cond CPAREN SCOLON','countif',11,'p_countif','LUGSTAT.py',282),
  ('plot -> PLOT OPAREN xyfunc CPAREN SCOLON','plot',5,'p_plot','LUGSTAT.py',285),
  ('plot -> PLOT OPAREN plot2 CPAREN SCOLON','plot',5,'p_plot','LUGSTAT.py',286),
  ('plot2 -> LCOR varcte COMMA varcte RCOR','plot2',5,'p_plot2','LUGSTAT.py',290),
  ('plot2 -> LCOR varcte COMMA varcte RCOR COMMA plot2','plot2',7,'p_plot2','LUGSTAT.py',291),
  ('plot2 -> empty','plot2',1,'p_plot2','LUGSTAT.py',292),
  ('xyfunc -> FX EQUALS exp SCOLON xyfunc','xyfunc',5,'p_xyfunc','LUGSTAT.py',296),
  ('xyfunc -> FY EQUALS exp SCOLON xyfunc','xyfunc',5,'p_xyfunc','LUGSTAT.py',297),
  ('xyfunc -> empty','xyfunc',1,'p_xyfunc','LUGSTAT.py',298),
  ('expresion -> exp','expresion',1,'p_expresion','LUGSTAT.py',303),
  ('expresion -> expresion RELOP exp','expresion',3,'p_expresion','LUGSTAT.py',304),
  ('exp -> termino','exp',1,'p_exp','LUGSTAT.py',309),
  ('exp -> termino PLUS exp','exp',3,'p_exp','LUGSTAT.py',310),
  ('exp -> termino MINUS exp','exp',3,'p_exp','LUGSTAT.py',311),
  ('termino -> factor','termino',1,'p_termino','LUGSTAT.py',316),
  ('termino -> factor MULT termino','termino',3,'p_termino','LUGSTAT.py',317),
  ('termino -> factor DIV termino','termino',3,'p_termino','LUGSTAT.py',318),
  ('factor -> OPAREN expresion CPAREN','factor',3,'p_factor','LUGSTAT.py',325),
  ('factor -> PLUS varcte','factor',2,'p_factor','LUGSTAT.py',326),
  ('factor -> MINUS varcte','factor',2,'p_factor','LUGSTAT.py',327),
  ('factor -> varcte','factor',1,'p_factor','LUGSTAT.py',328),
  ('varcte -> ID','varcte',1,'p_varcte','LUGSTAT.py',333),
  ('varcte -> ID asign2','varcte',2,'p_varcte','LUGSTAT.py',334),
  ('varcte -> NUMERIC','varcte',1,'p_varcte','LUGSTAT.py',335),
  ('varcte -> NUMBER','varcte',1,'p_varcte','LUGSTAT.py',336),
  ('metodos -> MEAN OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',341),
  ('metodos -> MEDIAN OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',342),
  ('metodos -> MODE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',343),
  ('metodos -> STDV OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',344),
  ('metodos -> KMEANS OPAREN varcte COMMA mmmfunc CPAREN SCOLON','metodos',7,'p_metodos','LUGSTAT.py',345),
  ('metodos -> DERL OPAREN expfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',346),
  ('metodos -> DBERN OPAREN expfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',347),
  ('metodos -> DPOI OPAREN expfunc2 CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',348),
  ('metodos -> TRANSPOSE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',349),
  ('metodos -> INVERSE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',350),
  ('metodos -> ROTATE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',351),
  ('metodos -> REF OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',352),
  ('metodos -> RREF OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',353),
  ('metodos -> MONT OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',354),
  ('expfunc -> ID COMMA ID COMMA ID','expfunc',5,'p_expfunc','LUGSTAT.py',359),
  ('expfunc -> varcte COMMA varcte COMMA varcte','expfunc',5,'p_expfunc','LUGSTAT.py',360),
  ('expfunc2 -> ID COMMA ID','expfunc2',3,'p_expfunc2','LUGSTAT.py',365),
  ('expfunc2 -> varcte COMMA varcte','expfunc2',3,'p_expfunc2','LUGSTAT.py',366),
  ('mmmfunc -> ID','mmmfunc',1,'p_mmmfunc','LUGSTAT.py',371),
  ('mmmfunc -> OBRACKET mmmarray CBRACKET','mmmfunc',3,'p_mmmfunc','LUGSTAT.py',372),
  ('mmmfunc -> OBRACKET mmmarray CBRACKET COMMA mmmfunc','mmmfunc',5,'p_mmmfunc','LUGSTAT.py',373),
  ('mmmfunc -> empty','mmmfunc',1,'p_mmmfunc','LUGSTAT.py',374),
  ('mmmarray -> varcte','mmmarray',1,'p_mmmarray','LUGSTAT.py',379),
  ('mmmarray -> varcte COMMA mmmarray','mmmarray',3,'p_mmmarray','LUGSTAT.py',380),
  ('mmmarray -> empty','mmmarray',1,'p_mmmarray','LUGSTAT.py',381),
  ('empty -> <empty>','empty',0,'p_empty','LUGSTAT.py',385),
]
