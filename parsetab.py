
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CBRACKET CHAR CHARACTER COLON COMMA COMMENT COUNT COUNTIF CPAREN CTED CTEI DBERN DERL DIFF DIV DO DOUBLE DPOI ELSE EQ EQUALS EULER FUNC FX FY GRE GREATEQ GREATERTHAN ID IF INT INTEGER INVERSE KMEANS LCOR LESSEQ LESSTHAN LOGICAL LUGSTAT MEAN MEDIAN MINUS MODE MONT MULT NUMBER NUMERIC OBRACKET OPAREN OR PER PLOT PLUS PRINT QUOTE RCOR READ REF RELOP ROTATE RREF SCOLON STDV STRING STRING TIPO TRANSPOSE VAR WHILE\n    lugstat : LUGSTAT ID SCOLON addmain lugstat2 lugstat3 mnv block\n    addmain : empty mnv : empty \n    lugstat2 : vars\n    | empty\n    \n    lugstat3 : modules\n    | modules lugstat3\n    | empty\n    vars : VAR vars1 \n     \n    vars1 : ID COMMA vars1\n    | ID COLON tipo SCOLON lugstat2\n    | ID LCOR NUMBER RCOR COLON tipo SCOLON lugstat2\n    | ID LCOR NUMBER RCOR COLON tipo SCOLON \n    | ID LCOR NUMBER RCOR LCOR NUMBER RCOR COLON tipo SCOLON lugstat2\n    | ID LCOR NUMBER RCOR LCOR NUMBER RCOR COLON tipo SCOLON \n    | ID asign2 COLON tipo SCOLON\n    | ID asign2 COMMA vars1\n    savename : empty\n    modules : FUNC ID COLON tipo mn1 OPAREN  modules2 mn2 CPAREN modules2 mn3 funblock mn7mn1 : emptymn7 : emptymn2 : mn3 : empty funccall : ID OPAREN fcn1 expresion fcn2 funccall2 CPAREN fcn3  fcn1 : empty fcn2 : emptyfcn3 : empty  funccall2 : COMMA expresion fcn2 funccall2\n    | empty \n    modules2 : vars\n    | empty\n    funblock : OBRACKET block2 CBRACKET\n    \n    block : OBRACKET block2 CBRACKET\n    \n    block2 : estatuto\n    | estatuto block2\n    | empty\n    tipo : INT\n    | BOOL \n    | DOUBLE\n    | STRING\n    | CHAR\n    \n    estatuto : asign\n    | cond \n    | escrt\n    | plot\n    | count\n    | countif\n    | metodos\n    | dwhile\n    | readln\n    | funccall\n    \n    asign : ID EQUALS expresion SCOLON\n    | ID EQUALS ID SCOLON\n    | ID EQUALS ID asign2 SCOLON\n    | ID asign2 EQUALS ID SCOLON\n    | ID asign2 EQUALS expresion SCOLON\n    | ID asign2 EQUALS ID asign2 SCOLON\n    \n    asign2 : LCOR expresion RCOR LCOR varcte RCOR\n    | LCOR expresion RCOR LCOR expresion RCOR\n    | LCOR varcte RCOR LCOR expresion RCOR\n    | LCOR varcte RCOR LCOR varcte RCOR\n    | LCOR expresion RCOR\n    | LCOR varcte RCOR \n    \n    asign3 : LCOR expresion RCOR\n    | LCOR varcte RCOR \n    escrt : PRINT OPAREN ID en3 escrt2 CPAREN SCOLON\n    | PRINT OPAREN expresion en1 CPAREN SCOLON\n    | PRINT OPAREN STRING CPAREN en2 SCOLON\n    | PRINT OPAREN STRING  escrt2 CPAREN en2 SCOLON\n    escrt2 : COMMA escrt3\n    | empty\n    escrt3 : ID escrt2\n    | ID\n    | STRING escrt2 escrt2\n    en1 : emptyen2 : emptyen3 : emptycond : IF OPAREN expresion cn1 CPAREN ifblock SCOLON cn2\n    | IF OPAREN expresion cn1 CPAREN ifblock ELSE cn3 ifblock SCOLON cn2\n    cn1 : emptycn2 : emptycn3 : empty\n    ifblock : OBRACKET ifblock2 CBRACKET\n    \n    ifblock2 : estatuto\n    | estatuto ifblock2\n    | emptycount : COUNT OPAREN ID COMMA varcte COMMA varcte CPAREN SCOLONcountif : COUNTIF OPAREN ID COMMA varcte COMMA varcte COMMA cond CPAREN SCOLONplot : PLOT OPAREN xyfunc CPAREN SCOLON\n    | PLOT OPAREN plot2 CPAREN SCOLON\n    \n    plot2 : LCOR varcte COMMA varcte RCOR\n    | LCOR varcte COMMA varcte RCOR COMMA plot2\n    | empty\n    xyfunc : FX EQUALS exp SCOLON xyfunc\n    | FY EQUALS exp SCOLON xyfunc\n    | empty\n    expresion : exp \n    | expresion RELOP exp \n    \n    exp : termino\n    | termino PLUS exp\n    | termino MINUS exp\n    \n    termino : factor\n    | factor MULT termino\n    | factor DIV termino\n    \n    factor : OPAREN expresion CPAREN \n    | varcte\n    \n    varcte : ID\n    | ID asign2\n    | NUMERIC\n    | NUMBER\n    | LOGICAL\n    \n    dwhile : DO wn1 wblock WHILE OPAREN dwhileconds CPAREN wn2 SCOLON \n    wn1 : emptywn2 : empty\n    wblock : OBRACKET block2 CBRACKET   \n    \n    dwhileconds : expresion dwhileconds\n    | expresion AND dwhileconds\n    | expresion OR dwhileconds\n    | empty\n     readln : READ OPAREN ID rn1 CPAREN SCOLON rn1 : empty \n    metodos : MEAN OPAREN mmmfunc CPAREN SCOLON\n    | MEDIAN OPAREN mmmfunc CPAREN SCOLON\n    | MODE OPAREN mmmfunc CPAREN SCOLON\n    | STDV OPAREN mmmfunc CPAREN SCOLON\n    | KMEANS OPAREN varcte COMMA mmmfunc CPAREN SCOLON\n    | DERL OPAREN expfunc CPAREN SCOLON\n    | DBERN OPAREN expfunc CPAREN SCOLON\n    | DPOI OPAREN expfunc2 CPAREN SCOLON\n    | TRANSPOSE OPAREN mmmfunc CPAREN SCOLON\n    | INVERSE OPAREN mmmfunc CPAREN SCOLON\n    | ROTATE OPAREN mmmfunc CPAREN SCOLON\n    | REF OPAREN mmmfunc CPAREN SCOLON\n    | RREF OPAREN mmmfunc CPAREN SCOLON\n    | MONT OPAREN mmmfunc CPAREN SCOLON\n    | EULER OPAREN CPAREN SCOLON\n    \n    expfunc : ID COMMA ID COMMA ID\n    | varcte COMMA varcte COMMA varcte\n    \n    expfunc2 : ID COMMA ID\n    | varcte COMMA varcte\n    \n    mmmfunc : LCOR RCOR\n\t| LCOR mmmarray RCOR COMMA mmmfunc\n    | LCOR mmmarray RCOR\n    | ID\n\t| empty \n    \n    mmmarray : varcte\n    | varcte COMMA mmmarray\n    | empty\n    empty :'
    
_lr_action_items = {'LUGSTAT':([0,],[2,]),'$end':([1,25,100,],[0,-1,-33,]),'ID':([2,10,14,21,23,26,35,39,40,41,42,43,44,46,48,50,51,52,53,54,55,56,57,58,59,85,86,88,89,90,91,92,93,94,96,97,102,104,105,106,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,133,134,135,136,137,138,139,140,144,145,146,156,160,182,191,193,205,209,210,212,213,222,224,225,228,229,236,246,247,248,249,250,252,253,265,266,269,272,274,275,276,277,279,282,283,286,287,288,289,290,291,292,298,300,303,305,306,313,314,315,318,319,321,323,326,328,331,333,334,343,348,349,352,353,355,356,375,377,379,380,385,386,],[3,16,20,16,35,60,-107,-97,-109,-111,-99,-102,35,16,60,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-108,35,-62,35,-63,35,35,35,35,-106,-110,142,-149,35,148,157,158,161,161,161,161,35,168,168,172,161,161,161,161,161,161,183,35,-98,35,-100,-101,-103,-104,-105,194,35,-25,35,35,60,-53,-52,263,35,35,35,35,161,280,35,284,35,-136,-59,-58,-61,-60,-54,-55,-56,-89,-90,35,-122,35,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,35,-57,35,60,-67,-68,35,35,161,344,35,35,-120,-149,-149,60,-66,-69,-126,35,35,-24,-27,-78,-81,-87,-112,60,-149,-79,-88,]),'SCOLON':([3,29,30,31,32,33,34,35,39,40,41,42,43,85,88,90,96,97,98,134,136,137,138,139,140,142,143,180,186,192,194,195,203,207,208,214,219,220,221,223,226,227,230,231,232,233,234,235,246,247,248,249,251,258,259,260,261,267,268,294,302,304,307,317,325,346,359,362,364,365,372,381,],[4,84,-37,-38,-39,-40,-41,-107,-97,-109,-111,-99,-102,-108,-62,-63,-106,-110,141,-98,-100,-101,-103,-104,-105,191,193,236,245,250,252,253,-149,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,-59,-58,-61,-60,298,305,306,-76,-149,310,311,323,328,333,334,343,351,-149,-83,375,377,-114,380,386,]),'VAR':([4,5,6,84,184,245,324,351,],[-149,10,-2,10,10,10,10,10,]),'FUNC':([4,5,6,7,8,9,12,15,28,84,99,130,141,245,297,351,370,378,382,383,387,],[-149,-149,-2,14,-4,-5,14,-9,-10,-149,-17,-11,-16,-13,-12,-15,-14,-149,-19,-21,-32,]),'OBRACKET':([4,5,6,7,8,9,11,12,13,15,17,18,19,28,81,84,99,125,126,130,141,242,243,245,256,297,324,329,350,351,357,358,368,369,370,378,382,383,387,],[-149,-149,-2,-149,-4,-5,-149,-6,-8,-9,26,-3,-7,-10,-149,-149,-17,182,-113,-11,-16,-30,-31,-13,303,-12,-149,-149,-149,-15,303,-82,379,-23,-14,-149,-19,-21,-32,]),'CPAREN':([8,9,15,28,35,39,40,41,42,43,84,85,88,90,95,96,97,99,107,110,111,112,113,118,119,120,121,122,123,124,130,134,136,137,138,139,140,141,147,148,149,150,151,152,155,159,161,162,163,164,165,167,170,171,174,175,176,177,178,179,183,184,196,197,198,199,200,201,202,204,206,215,222,239,240,241,242,243,245,246,247,248,249,254,255,257,262,263,264,273,278,284,285,292,295,297,299,301,308,309,310,311,315,320,321,322,327,328,335,336,337,338,339,340,342,344,345,347,348,349,351,354,355,356,361,366,367,370,371,373,374,376,380,385,],[-4,-5,-9,-10,-107,-97,-109,-111,-99,-102,-149,-108,-62,-63,140,-106,-110,-17,-149,-149,-149,-149,-149,-149,-149,-149,-149,-149,-149,180,-11,-98,-100,-101,-103,-104,-105,-16,-149,-107,-149,203,207,208,-93,214,-144,-145,219,220,221,223,226,227,230,231,232,233,234,235,-149,-149,-149,256,-80,-149,-77,258,-75,261,-71,-141,-149,294,-121,-22,-30,-31,-13,-59,-58,-61,-60,-149,-26,304,-70,-73,-149,-143,317,-139,-140,-149,324,-12,326,-29,-72,-149,-149,-149,-149,346,-149,-119,-149,-149,-74,-94,-96,-95,-91,362,-142,-137,-138,-116,-149,-149,-15,-149,-78,-81,-149,-117,-118,-14,-28,-92,-93,381,-149,-79,]),'COMMA':([16,24,35,39,40,41,42,43,85,88,90,96,97,134,136,137,138,139,140,148,150,157,158,166,168,169,172,173,196,199,200,206,211,217,246,247,248,249,254,255,262,263,264,270,271,273,280,281,308,309,327,335,339,341,354,],[21,46,-107,-97,-109,-111,-99,-102,-108,-62,-63,-106,-110,-98,-100,-101,-103,-104,-105,-149,205,212,213,222,224,225,228,229,-149,205,-77,-71,269,274,-59,-58,-61,-60,300,-26,-70,205,205,313,314,315,318,319,-72,205,-149,-74,361,363,300,]),'COLON':([16,20,24,87,88,90,244,246,247,248,249,],[22,27,45,132,-62,-63,296,-59,-58,-61,-60,]),'LCOR':([16,35,60,87,88,90,107,110,111,112,113,118,119,120,121,122,123,142,148,168,172,194,222,315,361,],[23,86,86,131,133,135,156,160,160,160,160,160,160,160,160,160,160,86,86,86,86,86,160,160,156,]),'INT':([22,27,45,132,296,],[30,30,30,30,30,]),'BOOL':([22,27,45,132,296,],[31,31,31,31,31,]),'DOUBLE':([22,27,45,132,296,],[32,32,32,32,32,]),'STRING':([22,27,45,106,132,205,296,],[33,33,33,150,33,264,33,]),'CHAR':([22,27,45,132,296,],[34,34,34,34,34,]),'NUMBER':([23,35,39,40,41,42,43,44,85,86,88,89,90,91,92,93,94,96,97,102,104,105,106,114,115,116,117,131,133,134,135,136,137,138,139,140,144,145,146,156,160,209,210,212,213,225,229,246,247,248,249,269,274,292,300,313,314,319,321,348,349,],[36,-107,-97,-109,-111,-99,-102,97,-108,97,-62,97,-63,97,97,97,97,-106,-110,97,-149,97,97,97,97,97,97,185,97,-98,97,-100,-101,-103,-104,-105,97,97,-25,97,97,97,97,97,97,97,97,-59,-58,-61,-60,97,97,97,97,97,97,97,97,97,97,]),'NUMERIC':([23,35,39,40,41,42,43,44,85,86,88,89,90,91,92,93,94,96,97,102,104,105,106,114,115,116,117,133,134,135,136,137,138,139,140,144,145,146,156,160,209,210,212,213,225,229,246,247,248,249,269,274,292,300,313,314,319,321,348,349,],[40,-107,-97,-109,-111,-99,-102,40,-108,40,-62,40,-63,40,40,40,40,-106,-110,40,-149,40,40,40,40,40,40,40,-98,40,-100,-101,-103,-104,-105,40,40,-25,40,40,40,40,40,40,40,40,-59,-58,-61,-60,40,40,40,40,40,40,40,40,40,40,]),'LOGICAL':([23,35,39,40,41,42,43,44,85,86,88,89,90,91,92,93,94,96,97,102,104,105,106,114,115,116,117,133,134,135,136,137,138,139,140,144,145,146,156,160,209,210,212,213,225,229,246,247,248,249,269,274,292,300,313,314,319,321,348,349,],[41,-107,-97,-109,-111,-99,-102,41,-108,41,-62,41,-63,41,41,41,41,-106,-110,41,-149,41,41,41,41,41,41,41,-98,41,-100,-101,-103,-104,-105,41,41,-25,41,41,41,41,41,41,41,41,-59,-58,-61,-60,41,41,41,41,41,41,41,41,41,41,]),'OPAREN':([23,30,31,32,33,34,35,39,40,41,42,43,44,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,85,86,88,89,90,91,92,93,94,96,97,102,104,105,106,128,129,133,134,135,136,137,138,139,140,144,145,146,209,210,237,246,247,248,249,292,300,321,348,349,],[44,-37,-38,-39,-40,-41,-107,-97,-109,-111,-99,-102,44,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,127,-149,-108,44,-62,44,-63,44,44,44,44,-106,-110,44,-149,44,44,184,-20,44,-98,44,-100,-101,-103,-104,-105,44,44,-25,44,44,292,-59,-58,-61,-60,44,44,44,44,44,]),'CBRACKET':([26,47,48,49,50,51,52,53,54,55,56,57,58,59,101,182,191,193,236,238,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,330,331,332,333,334,343,352,353,355,356,360,375,377,379,380,384,385,386,],[-149,100,-34,-36,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-35,-149,-53,-52,-136,293,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,-149,-67,-68,-120,-149,-149,359,-84,-86,-66,-69,-126,-24,-27,-78,-81,-85,-87,-112,-149,-149,387,-79,-88,]),'IF':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,363,375,377,379,380,385,386,],[61,61,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,61,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,61,-67,-68,-120,-149,-149,61,-66,-69,-126,-24,-27,-78,-81,61,-87,-112,61,-149,-79,-88,]),'PRINT':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[62,62,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,62,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,62,-67,-68,-120,-149,-149,62,-66,-69,-126,-24,-27,-78,-81,-87,-112,62,-149,-79,-88,]),'PLOT':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[63,63,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,63,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,63,-67,-68,-120,-149,-149,63,-66,-69,-126,-24,-27,-78,-81,-87,-112,63,-149,-79,-88,]),'COUNT':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[64,64,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,64,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,64,-67,-68,-120,-149,-149,64,-66,-69,-126,-24,-27,-78,-81,-87,-112,64,-149,-79,-88,]),'COUNTIF':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[65,65,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,65,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,65,-67,-68,-120,-149,-149,65,-66,-69,-126,-24,-27,-78,-81,-87,-112,65,-149,-79,-88,]),'MEAN':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[66,66,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,66,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,66,-67,-68,-120,-149,-149,66,-66,-69,-126,-24,-27,-78,-81,-87,-112,66,-149,-79,-88,]),'MEDIAN':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[67,67,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,67,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,67,-67,-68,-120,-149,-149,67,-66,-69,-126,-24,-27,-78,-81,-87,-112,67,-149,-79,-88,]),'MODE':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[68,68,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,68,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,68,-67,-68,-120,-149,-149,68,-66,-69,-126,-24,-27,-78,-81,-87,-112,68,-149,-79,-88,]),'STDV':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[69,69,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,69,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,69,-67,-68,-120,-149,-149,69,-66,-69,-126,-24,-27,-78,-81,-87,-112,69,-149,-79,-88,]),'KMEANS':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[70,70,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,70,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,70,-67,-68,-120,-149,-149,70,-66,-69,-126,-24,-27,-78,-81,-87,-112,70,-149,-79,-88,]),'DERL':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[71,71,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,71,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,71,-67,-68,-120,-149,-149,71,-66,-69,-126,-24,-27,-78,-81,-87,-112,71,-149,-79,-88,]),'DBERN':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[72,72,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,72,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,72,-67,-68,-120,-149,-149,72,-66,-69,-126,-24,-27,-78,-81,-87,-112,72,-149,-79,-88,]),'DPOI':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[73,73,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,73,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,73,-67,-68,-120,-149,-149,73,-66,-69,-126,-24,-27,-78,-81,-87,-112,73,-149,-79,-88,]),'TRANSPOSE':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[74,74,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,74,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,74,-67,-68,-120,-149,-149,74,-66,-69,-126,-24,-27,-78,-81,-87,-112,74,-149,-79,-88,]),'INVERSE':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[75,75,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,75,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,75,-67,-68,-120,-149,-149,75,-66,-69,-126,-24,-27,-78,-81,-87,-112,75,-149,-79,-88,]),'ROTATE':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[76,76,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,76,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,76,-67,-68,-120,-149,-149,76,-66,-69,-126,-24,-27,-78,-81,-87,-112,76,-149,-79,-88,]),'REF':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[77,77,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,77,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,77,-67,-68,-120,-149,-149,77,-66,-69,-126,-24,-27,-78,-81,-87,-112,77,-149,-79,-88,]),'RREF':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[78,78,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,78,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,78,-67,-68,-120,-149,-149,78,-66,-69,-126,-24,-27,-78,-81,-87,-112,78,-149,-79,-88,]),'MONT':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[79,79,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,79,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,79,-67,-68,-120,-149,-149,79,-66,-69,-126,-24,-27,-78,-81,-87,-112,79,-149,-79,-88,]),'EULER':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[80,80,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,80,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,80,-67,-68,-120,-149,-149,80,-66,-69,-126,-24,-27,-78,-81,-87,-112,80,-149,-79,-88,]),'DO':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[81,81,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,81,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,81,-67,-68,-120,-149,-149,81,-66,-69,-126,-24,-27,-78,-81,-87,-112,81,-149,-79,-88,]),'READ':([26,48,50,51,52,53,54,55,56,57,58,59,182,191,193,236,250,252,253,265,266,272,275,276,277,279,282,283,286,287,288,289,290,291,298,303,305,306,323,326,328,331,333,334,343,352,353,355,356,375,377,379,380,385,386,],[82,82,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,82,-53,-52,-136,-54,-55,-56,-89,-90,-122,-123,-124,-125,-127,-128,-129,-130,-131,-132,-133,-134,-135,-57,82,-67,-68,-120,-149,-149,82,-66,-69,-126,-24,-27,-78,-81,-87,-112,82,-149,-79,-88,]),'RCOR':([35,36,37,38,39,40,41,42,43,85,88,90,96,97,134,136,137,138,139,140,160,185,187,188,189,190,216,217,218,246,247,248,249,274,312,316,],[-107,87,88,90,-97,-109,-111,-99,-102,-108,-62,-63,-106,-110,-98,-100,-101,-103,-104,-105,215,244,246,247,248,249,273,-146,-148,-59,-58,-61,-60,-149,339,-147,]),'MULT':([35,36,38,40,41,43,85,88,90,96,97,140,142,148,188,189,192,194,246,247,248,249,251,],[-107,-110,-106,-109,-111,93,-108,-62,-63,-106,-110,-105,-107,-107,-106,-106,-108,-107,-59,-58,-61,-60,-108,]),'DIV':([35,36,38,40,41,43,85,88,90,96,97,140,142,148,188,189,192,194,246,247,248,249,251,],[-107,-110,-106,-109,-111,94,-108,-62,-63,-106,-110,-105,-107,-107,-106,-106,-108,-107,-59,-58,-61,-60,-108,]),'PLUS':([35,36,38,40,41,42,43,85,88,90,96,97,138,139,140,142,148,188,189,192,194,246,247,248,249,251,],[-107,-110,-106,-109,-111,91,-102,-108,-62,-63,-106,-110,-103,-104,-105,-107,-107,-106,-106,-108,-107,-59,-58,-61,-60,-108,]),'MINUS':([35,36,38,40,41,42,43,85,88,90,96,97,138,139,140,142,148,188,189,192,194,246,247,248,249,251,],[-107,-110,-106,-109,-111,92,-102,-108,-62,-63,-106,-110,-103,-104,-105,-107,-107,-106,-106,-108,-107,-59,-58,-61,-60,-108,]),'RELOP':([35,36,37,38,39,40,41,42,43,85,88,90,95,96,97,134,136,137,138,139,140,142,143,147,148,149,187,188,189,190,192,194,195,196,246,247,248,249,251,321,327,],[-107,-110,89,-106,-97,-109,-111,-99,-102,-108,-62,-63,89,-106,-110,-98,-100,-101,-103,-104,-105,-107,89,89,-107,89,89,-106,-106,89,-108,-107,89,89,-59,-58,-61,-60,-108,89,89,]),'AND':([35,39,40,41,42,43,85,88,90,96,97,134,136,137,138,139,140,246,247,248,249,321,],[-107,-97,-109,-111,-99,-102,-108,-62,-63,-106,-110,-98,-100,-101,-103,-104,-105,-59,-58,-61,-60,348,]),'OR':([35,39,40,41,42,43,85,88,90,96,97,134,136,137,138,139,140,246,247,248,249,321,],[-107,-97,-109,-111,-99,-102,-108,-62,-63,-106,-110,-98,-100,-101,-103,-104,-105,-59,-58,-61,-60,349,]),'EQUALS':([60,88,90,103,153,154,246,247,248,249,],[102,-62,-63,144,209,210,-59,-58,-61,-60,]),'FX':([107,310,311,],[153,153,153,]),'FY':([107,310,311,],[154,154,154,]),'WHILE':([181,293,],[237,-115,]),'ELSE':([302,359,],[329,-83,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lugstat':([0,],[1,]),'addmain':([4,],[5,]),'empty':([4,5,7,11,12,26,48,81,83,84,104,107,110,111,112,113,118,119,120,121,122,123,147,148,149,150,160,182,183,184,196,199,203,222,245,254,261,263,264,274,292,303,309,310,311,315,321,324,326,327,328,329,331,346,348,349,350,351,354,361,378,379,380,],[6,9,13,18,13,49,49,126,129,9,146,155,162,162,162,162,162,162,162,162,162,162,198,200,202,206,218,49,240,243,255,206,260,162,9,301,260,206,206,218,322,332,206,337,337,162,322,243,353,255,356,358,332,365,322,322,369,9,301,374,383,49,356,]),'lugstat2':([5,84,245,351,],[7,130,297,370,]),'vars':([5,84,184,245,324,351,],[8,8,242,8,242,8,]),'lugstat3':([7,12,],[11,19,]),'modules':([7,12,],[12,12,]),'vars1':([10,21,46,],[15,28,99,]),'mnv':([11,],[17,]),'asign2':([16,35,60,142,148,168,172,194,],[24,85,103,192,85,85,85,251,]),'block':([17,],[25,]),'tipo':([22,27,45,132,296,],[29,83,98,186,325,]),'expresion':([23,44,86,102,105,106,133,135,144,145,292,300,321,348,349,],[37,95,37,143,147,149,187,190,195,196,321,327,321,321,321,]),'varcte':([23,44,86,89,91,92,93,94,102,105,106,114,115,116,117,133,135,144,145,156,160,209,210,212,213,225,229,269,274,292,300,313,314,319,321,348,349,],[38,96,38,96,96,96,96,96,96,96,96,166,169,169,173,188,189,96,96,211,217,96,96,270,271,281,285,312,217,96,96,340,341,345,96,96,96,]),'exp':([23,44,86,89,91,92,102,105,106,133,135,144,145,209,210,292,300,321,348,349,],[39,39,39,134,136,137,39,39,39,39,39,39,39,267,268,39,39,39,39,39,]),'termino':([23,44,86,89,91,92,93,94,102,105,106,133,135,144,145,209,210,292,300,321,348,349,],[42,42,42,42,42,42,138,139,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'factor':([23,44,86,89,91,92,93,94,102,105,106,133,135,144,145,209,210,292,300,321,348,349,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'block2':([26,48,182,379,],[47,101,238,384,]),'estatuto':([26,48,182,303,331,379,],[48,48,48,331,331,48,]),'asign':([26,48,182,303,331,379,],[50,50,50,50,50,50,]),'cond':([26,48,182,303,331,363,379,],[51,51,51,51,51,376,51,]),'escrt':([26,48,182,303,331,379,],[52,52,52,52,52,52,]),'plot':([26,48,182,303,331,379,],[53,53,53,53,53,53,]),'count':([26,48,182,303,331,379,],[54,54,54,54,54,54,]),'countif':([26,48,182,303,331,379,],[55,55,55,55,55,55,]),'metodos':([26,48,182,303,331,379,],[56,56,56,56,56,56,]),'dwhile':([26,48,182,303,331,379,],[57,57,57,57,57,57,]),'readln':([26,48,182,303,331,379,],[58,58,58,58,58,58,]),'funccall':([26,48,182,303,331,379,],[59,59,59,59,59,59,]),'wn1':([81,],[125,]),'mn1':([83,],[128,]),'fcn1':([104,],[145,]),'xyfunc':([107,310,311,],[151,336,338,]),'plot2':([107,361,],[152,373,]),'mmmfunc':([110,111,112,113,118,119,120,121,122,123,222,315,],[159,163,164,165,174,175,176,177,178,179,278,342,]),'expfunc':([115,116,],[167,170,]),'expfunc2':([117,],[171,]),'wblock':([125,],[181,]),'cn1':([147,],[197,]),'en3':([148,],[199,]),'en1':([149,],[201,]),'escrt2':([150,199,263,264,309,],[204,257,308,309,335,]),'mmmarray':([160,274,],[216,316,]),'rn1':([183,],[239,]),'modules2':([184,324,],[241,350,]),'fcn2':([196,327,],[254,354,]),'en2':([203,261,],[259,307,]),'escrt3':([205,],[262,]),'mn2':([241,],[295,]),'funccall2':([254,354,],[299,371,]),'ifblock':([256,357,],[302,372,]),'dwhileconds':([292,321,348,349,],[320,347,366,367,]),'ifblock2':([303,331,],[330,360,]),'fcn3':([326,],[352,]),'cn2':([328,380,],[355,385,]),'cn3':([329,],[357,]),'wn2':([346,],[364,]),'mn3':([350,],[368,]),'funblock':([368,],[378,]),'mn7':([378,],[382,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lugstat","S'",1,None,None,None),
  ('lugstat -> LUGSTAT ID SCOLON addmain lugstat2 lugstat3 mnv block','lugstat',8,'p_lugstat','LUGSTAT.py',257),
  ('addmain -> empty','addmain',1,'p_addmain','LUGSTAT.py',261),
  ('mnv -> empty','mnv',1,'p_mnv','LUGSTAT.py',271),
  ('lugstat2 -> vars','lugstat2',1,'p_lugstat2','LUGSTAT.py',276),
  ('lugstat2 -> empty','lugstat2',1,'p_lugstat2','LUGSTAT.py',277),
  ('lugstat3 -> modules','lugstat3',1,'p_lugstat3','LUGSTAT.py',282),
  ('lugstat3 -> modules lugstat3','lugstat3',2,'p_lugstat3','LUGSTAT.py',283),
  ('lugstat3 -> empty','lugstat3',1,'p_lugstat3','LUGSTAT.py',284),
  ('vars -> VAR vars1','vars',2,'p_vars','LUGSTAT.py',288),
  ('vars1 -> ID COMMA vars1','vars1',3,'p_vars1','LUGSTAT.py',617),
  ('vars1 -> ID COLON tipo SCOLON lugstat2','vars1',5,'p_vars1','LUGSTAT.py',618),
  ('vars1 -> ID LCOR NUMBER RCOR COLON tipo SCOLON lugstat2','vars1',8,'p_vars1','LUGSTAT.py',619),
  ('vars1 -> ID LCOR NUMBER RCOR COLON tipo SCOLON','vars1',7,'p_vars1','LUGSTAT.py',620),
  ('vars1 -> ID LCOR NUMBER RCOR LCOR NUMBER RCOR COLON tipo SCOLON lugstat2','vars1',11,'p_vars1','LUGSTAT.py',621),
  ('vars1 -> ID LCOR NUMBER RCOR LCOR NUMBER RCOR COLON tipo SCOLON','vars1',10,'p_vars1','LUGSTAT.py',622),
  ('vars1 -> ID asign2 COLON tipo SCOLON','vars1',5,'p_vars1','LUGSTAT.py',623),
  ('vars1 -> ID asign2 COMMA vars1','vars1',4,'p_vars1','LUGSTAT.py',624),
  ('savename -> empty','savename',1,'p_savename','LUGSTAT.py',656),
  ('modules -> FUNC ID COLON tipo mn1 OPAREN modules2 mn2 CPAREN modules2 mn3 funblock mn7','modules',13,'p_modules','LUGSTAT.py',660),
  ('mn1 -> empty','mn1',1,'p_mn1','LUGSTAT.py',665),
  ('mn7 -> empty','mn7',1,'p_mn7','LUGSTAT.py',678),
  ('mn2 -> <empty>','mn2',0,'p_mn2','LUGSTAT.py',697),
  ('mn3 -> empty','mn3',1,'p_mn3','LUGSTAT.py',711),
  ('funccall -> ID OPAREN fcn1 expresion fcn2 funccall2 CPAREN fcn3','funccall',8,'p_funccall','LUGSTAT.py',718),
  ('fcn1 -> empty','fcn1',1,'p_fcn1','LUGSTAT.py',722),
  ('fcn2 -> empty','fcn2',1,'p_fcn2','LUGSTAT.py',744),
  ('fcn3 -> empty','fcn3',1,'p_fcn3','LUGSTAT.py',768),
  ('funccall2 -> COMMA expresion fcn2 funccall2','funccall2',4,'p_funccall2','LUGSTAT.py',785),
  ('funccall2 -> empty','funccall2',1,'p_funccall2','LUGSTAT.py',786),
  ('modules2 -> vars','modules2',1,'p_modules2','LUGSTAT.py',791),
  ('modules2 -> empty','modules2',1,'p_modules2','LUGSTAT.py',792),
  ('funblock -> OBRACKET block2 CBRACKET','funblock',3,'p_funblock','LUGSTAT.py',797),
  ('block -> OBRACKET block2 CBRACKET','block',3,'p_block','LUGSTAT.py',801),
  ('block2 -> estatuto','block2',1,'p_block2','LUGSTAT.py',812),
  ('block2 -> estatuto block2','block2',2,'p_block2','LUGSTAT.py',813),
  ('block2 -> empty','block2',1,'p_block2','LUGSTAT.py',814),
  ('tipo -> INT','tipo',1,'p_tipo','LUGSTAT.py',818),
  ('tipo -> BOOL','tipo',1,'p_tipo','LUGSTAT.py',819),
  ('tipo -> DOUBLE','tipo',1,'p_tipo','LUGSTAT.py',820),
  ('tipo -> STRING','tipo',1,'p_tipo','LUGSTAT.py',821),
  ('tipo -> CHAR','tipo',1,'p_tipo','LUGSTAT.py',822),
  ('estatuto -> asign','estatuto',1,'p_estatuto','LUGSTAT.py',828),
  ('estatuto -> cond','estatuto',1,'p_estatuto','LUGSTAT.py',829),
  ('estatuto -> escrt','estatuto',1,'p_estatuto','LUGSTAT.py',830),
  ('estatuto -> plot','estatuto',1,'p_estatuto','LUGSTAT.py',831),
  ('estatuto -> count','estatuto',1,'p_estatuto','LUGSTAT.py',832),
  ('estatuto -> countif','estatuto',1,'p_estatuto','LUGSTAT.py',833),
  ('estatuto -> metodos','estatuto',1,'p_estatuto','LUGSTAT.py',834),
  ('estatuto -> dwhile','estatuto',1,'p_estatuto','LUGSTAT.py',835),
  ('estatuto -> readln','estatuto',1,'p_estatuto','LUGSTAT.py',836),
  ('estatuto -> funccall','estatuto',1,'p_estatuto','LUGSTAT.py',837),
  ('asign -> ID EQUALS expresion SCOLON','asign',4,'p_asign','LUGSTAT.py',842),
  ('asign -> ID EQUALS ID SCOLON','asign',4,'p_asign','LUGSTAT.py',843),
  ('asign -> ID EQUALS ID asign2 SCOLON','asign',5,'p_asign','LUGSTAT.py',844),
  ('asign -> ID asign2 EQUALS ID SCOLON','asign',5,'p_asign','LUGSTAT.py',845),
  ('asign -> ID asign2 EQUALS expresion SCOLON','asign',5,'p_asign','LUGSTAT.py',846),
  ('asign -> ID asign2 EQUALS ID asign2 SCOLON','asign',6,'p_asign','LUGSTAT.py',847),
  ('asign2 -> LCOR expresion RCOR LCOR varcte RCOR','asign2',6,'p_asign2','LUGSTAT.py',916),
  ('asign2 -> LCOR expresion RCOR LCOR expresion RCOR','asign2',6,'p_asign2','LUGSTAT.py',917),
  ('asign2 -> LCOR varcte RCOR LCOR expresion RCOR','asign2',6,'p_asign2','LUGSTAT.py',918),
  ('asign2 -> LCOR varcte RCOR LCOR varcte RCOR','asign2',6,'p_asign2','LUGSTAT.py',919),
  ('asign2 -> LCOR expresion RCOR','asign2',3,'p_asign2','LUGSTAT.py',920),
  ('asign2 -> LCOR varcte RCOR','asign2',3,'p_asign2','LUGSTAT.py',921),
  ('asign3 -> LCOR expresion RCOR','asign3',3,'p_asign3','LUGSTAT.py',929),
  ('asign3 -> LCOR varcte RCOR','asign3',3,'p_asign3','LUGSTAT.py',930),
  ('escrt -> PRINT OPAREN ID en3 escrt2 CPAREN SCOLON','escrt',7,'p_escrt','LUGSTAT.py',936),
  ('escrt -> PRINT OPAREN expresion en1 CPAREN SCOLON','escrt',6,'p_escrt','LUGSTAT.py',937),
  ('escrt -> PRINT OPAREN STRING CPAREN en2 SCOLON','escrt',6,'p_escrt','LUGSTAT.py',938),
  ('escrt -> PRINT OPAREN STRING escrt2 CPAREN en2 SCOLON','escrt',7,'p_escrt','LUGSTAT.py',939),
  ('escrt2 -> COMMA escrt3','escrt2',2,'p_escrt2','LUGSTAT.py',943),
  ('escrt2 -> empty','escrt2',1,'p_escrt2','LUGSTAT.py',944),
  ('escrt3 -> ID escrt2','escrt3',2,'p_escrt3','LUGSTAT.py',948),
  ('escrt3 -> ID','escrt3',1,'p_escrt3','LUGSTAT.py',949),
  ('escrt3 -> STRING escrt2 escrt2','escrt3',3,'p_escrt3','LUGSTAT.py',950),
  ('en1 -> empty','en1',1,'p_en1','LUGSTAT.py',954),
  ('en2 -> empty','en2',1,'p_en2','LUGSTAT.py',963),
  ('en3 -> empty','en3',1,'p_en3','LUGSTAT.py',971),
  ('cond -> IF OPAREN expresion cn1 CPAREN ifblock SCOLON cn2','cond',8,'p_cond','LUGSTAT.py',996),
  ('cond -> IF OPAREN expresion cn1 CPAREN ifblock ELSE cn3 ifblock SCOLON cn2','cond',11,'p_cond','LUGSTAT.py',997),
  ('cn1 -> empty','cn1',1,'p_cn1','LUGSTAT.py',1001),
  ('cn2 -> empty','cn2',1,'p_cn2','LUGSTAT.py',1019),
  ('cn3 -> empty','cn3',1,'p_cn3','LUGSTAT.py',1026),
  ('ifblock -> OBRACKET ifblock2 CBRACKET','ifblock',3,'p_ifblock','LUGSTAT.py',1039),
  ('ifblock2 -> estatuto','ifblock2',1,'p_ifblock2','LUGSTAT.py',1043),
  ('ifblock2 -> estatuto ifblock2','ifblock2',2,'p_ifblock2','LUGSTAT.py',1044),
  ('ifblock2 -> empty','ifblock2',1,'p_ifblock2','LUGSTAT.py',1045),
  ('count -> COUNT OPAREN ID COMMA varcte COMMA varcte CPAREN SCOLON','count',9,'p_count','LUGSTAT.py',1048),
  ('countif -> COUNTIF OPAREN ID COMMA varcte COMMA varcte COMMA cond CPAREN SCOLON','countif',11,'p_countif','LUGSTAT.py',1051),
  ('plot -> PLOT OPAREN xyfunc CPAREN SCOLON','plot',5,'p_plot','LUGSTAT.py',1054),
  ('plot -> PLOT OPAREN plot2 CPAREN SCOLON','plot',5,'p_plot','LUGSTAT.py',1055),
  ('plot2 -> LCOR varcte COMMA varcte RCOR','plot2',5,'p_plot2','LUGSTAT.py',1059),
  ('plot2 -> LCOR varcte COMMA varcte RCOR COMMA plot2','plot2',7,'p_plot2','LUGSTAT.py',1060),
  ('plot2 -> empty','plot2',1,'p_plot2','LUGSTAT.py',1061),
  ('xyfunc -> FX EQUALS exp SCOLON xyfunc','xyfunc',5,'p_xyfunc','LUGSTAT.py',1065),
  ('xyfunc -> FY EQUALS exp SCOLON xyfunc','xyfunc',5,'p_xyfunc','LUGSTAT.py',1066),
  ('xyfunc -> empty','xyfunc',1,'p_xyfunc','LUGSTAT.py',1067),
  ('expresion -> exp','expresion',1,'p_expresion','LUGSTAT.py',1072),
  ('expresion -> expresion RELOP exp','expresion',3,'p_expresion','LUGSTAT.py',1073),
  ('exp -> termino','exp',1,'p_exp','LUGSTAT.py',1140),
  ('exp -> termino PLUS exp','exp',3,'p_exp','LUGSTAT.py',1141),
  ('exp -> termino MINUS exp','exp',3,'p_exp','LUGSTAT.py',1142),
  ('termino -> factor','termino',1,'p_termino','LUGSTAT.py',1219),
  ('termino -> factor MULT termino','termino',3,'p_termino','LUGSTAT.py',1220),
  ('termino -> factor DIV termino','termino',3,'p_termino','LUGSTAT.py',1221),
  ('factor -> OPAREN expresion CPAREN','factor',3,'p_factor','LUGSTAT.py',1277),
  ('factor -> varcte','factor',1,'p_factor','LUGSTAT.py',1278),
  ('varcte -> ID','varcte',1,'p_varcte','LUGSTAT.py',1293),
  ('varcte -> ID asign2','varcte',2,'p_varcte','LUGSTAT.py',1294),
  ('varcte -> NUMERIC','varcte',1,'p_varcte','LUGSTAT.py',1295),
  ('varcte -> NUMBER','varcte',1,'p_varcte','LUGSTAT.py',1296),
  ('varcte -> LOGICAL','varcte',1,'p_varcte','LUGSTAT.py',1297),
  ('dwhile -> DO wn1 wblock WHILE OPAREN dwhileconds CPAREN wn2 SCOLON','dwhile',9,'p_dwhile','LUGSTAT.py',1358),
  ('wn1 -> empty','wn1',1,'p_wn1','LUGSTAT.py',1361),
  ('wn2 -> empty','wn2',1,'p_wn2','LUGSTAT.py',1368),
  ('wblock -> OBRACKET block2 CBRACKET','wblock',3,'p_wblock','LUGSTAT.py',1383),
  ('dwhileconds -> expresion dwhileconds','dwhileconds',2,'p_dwhileconds','LUGSTAT.py',1388),
  ('dwhileconds -> expresion AND dwhileconds','dwhileconds',3,'p_dwhileconds','LUGSTAT.py',1389),
  ('dwhileconds -> expresion OR dwhileconds','dwhileconds',3,'p_dwhileconds','LUGSTAT.py',1390),
  ('dwhileconds -> empty','dwhileconds',1,'p_dwhileconds','LUGSTAT.py',1391),
  ('readln -> READ OPAREN ID rn1 CPAREN SCOLON','readln',6,'p_readln','LUGSTAT.py',1395),
  ('rn1 -> empty','rn1',1,'p_rn1','LUGSTAT.py',1398),
  ('metodos -> MEAN OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1421),
  ('metodos -> MEDIAN OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1422),
  ('metodos -> MODE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1423),
  ('metodos -> STDV OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1424),
  ('metodos -> KMEANS OPAREN varcte COMMA mmmfunc CPAREN SCOLON','metodos',7,'p_metodos','LUGSTAT.py',1425),
  ('metodos -> DERL OPAREN expfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1426),
  ('metodos -> DBERN OPAREN expfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1427),
  ('metodos -> DPOI OPAREN expfunc2 CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1428),
  ('metodos -> TRANSPOSE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1429),
  ('metodos -> INVERSE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1430),
  ('metodos -> ROTATE OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1431),
  ('metodos -> REF OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1432),
  ('metodos -> RREF OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1433),
  ('metodos -> MONT OPAREN mmmfunc CPAREN SCOLON','metodos',5,'p_metodos','LUGSTAT.py',1434),
  ('metodos -> EULER OPAREN CPAREN SCOLON','metodos',4,'p_metodos','LUGSTAT.py',1435),
  ('expfunc -> ID COMMA ID COMMA ID','expfunc',5,'p_expfunc','LUGSTAT.py',1446),
  ('expfunc -> varcte COMMA varcte COMMA varcte','expfunc',5,'p_expfunc','LUGSTAT.py',1447),
  ('expfunc2 -> ID COMMA ID','expfunc2',3,'p_expfunc2','LUGSTAT.py',1452),
  ('expfunc2 -> varcte COMMA varcte','expfunc2',3,'p_expfunc2','LUGSTAT.py',1453),
  ('mmmfunc -> LCOR RCOR','mmmfunc',2,'p_mmmfunc','LUGSTAT.py',1458),
  ('mmmfunc -> LCOR mmmarray RCOR COMMA mmmfunc','mmmfunc',5,'p_mmmfunc','LUGSTAT.py',1459),
  ('mmmfunc -> LCOR mmmarray RCOR','mmmfunc',3,'p_mmmfunc','LUGSTAT.py',1460),
  ('mmmfunc -> ID','mmmfunc',1,'p_mmmfunc','LUGSTAT.py',1461),
  ('mmmfunc -> empty','mmmfunc',1,'p_mmmfunc','LUGSTAT.py',1462),
  ('mmmarray -> varcte','mmmarray',1,'p_mmmarray','LUGSTAT.py',1467),
  ('mmmarray -> varcte COMMA mmmarray','mmmarray',3,'p_mmmarray','LUGSTAT.py',1468),
  ('mmmarray -> empty','mmmarray',1,'p_mmmarray','LUGSTAT.py',1469),
  ('empty -> <empty>','empty',0,'p_empty','LUGSTAT.py',1473),
]
