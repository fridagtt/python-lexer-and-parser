
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN COLON COMMA CTEF CTEI CTESTRING DIVIDE ELSE FLOAT GREATER ID IF INT LBRACKET LESS LPAREN MINUS NOTEQUAL PLUS PRINT PROGRAM RBRACKET RPAREN SEMICOLON TIMES VAR\n    program : PROGRAM ID SEMICOLON programT bloque\n    programT : vars\n             | empty\n    \n    vars : VAR ID varsT COLON tipo SEMICOLON varsF\n    varsT : COMMA ID varsT\n          | empty\n    varsF : ID varsT COLON tipo SEMICOLON varsF\n          | empty\n    \n    tipo : INT\n         | FLOAT\n    \n    bloque : LBRACKET bloqueT RBRACKET\n    bloqueT : estatuto bloqueT\n            | empty\n    \n    estatuto : asignacion\n             | condicion\n             | escritura\n    \n    asignacion : ID ASSIGN expresion SEMICOLON\n    \n    escritura : PRINT LBRACKET escrituraT RBRACKET SEMICOLON\n    escrituraT : expresion escrituraF\n               | CTESTRING escrituraF\n    escrituraF : COMMA escrituraT\n               | empty\n    \n    expresion : exp expresionT\n    expresionT : GREATER exp\n               | LESS exp\n               | NOTEQUAL exp\n               | empty\n    \n    condicion : IF LPAREN expresion RPAREN bloque condicionT\n    condicionT : ELSE bloque\n               | SEMICOLON\n    \n    exp : termino expT\n    expT : PLUS exp\n         | MINUS exp\n         | empty\n    \n    termino : factor terminoT\n    terminoT : TIMES termino\n             | DIVIDE termino\n             | empty\n    \n    factor : LPAREN expresion RPAREN\n           | factorT\n    factorT : factorF varcte\n    factorF : PLUS\n            | MINUS\n            | empty\n    \n    varcte : ID\n            | CTEI\n            | CTEF\n    \n    empty : \n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,9,24,],[0,-1,-11,]),'ID':([2,8,10,13,15,16,17,22,24,26,27,28,35,37,38,39,40,49,51,52,53,56,57,60,61,71,74,84,89,91,93,96,],[3,11,18,18,-14,-15,-16,30,-11,-48,-48,-48,-48,65,-42,-43,-44,-17,-48,-48,-48,-48,-48,-48,-48,-48,86,-18,-28,-30,-29,86,]),'SEMICOLON':([3,24,31,32,33,34,36,45,46,47,50,54,55,58,59,62,64,65,66,67,69,75,76,77,78,79,80,81,82,83,95,],[4,-11,49,-48,-48,-48,-40,74,-9,-10,-23,-27,-31,-34,-35,-38,-41,-45,-46,-47,84,-24,-25,-26,-32,-33,-36,-37,-39,91,96,]),'VAR':([4,],[8,]),'LBRACKET':([4,5,6,7,20,68,74,87,88,90,96,97,],[-48,10,-2,-3,28,10,-48,-4,-8,10,-48,-7,]),'RBRACKET':([10,12,13,14,15,16,17,24,25,32,33,34,36,42,43,44,49,50,54,55,58,59,62,64,65,66,67,70,72,73,75,76,77,78,79,80,81,82,84,85,89,91,93,],[-48,24,-48,-13,-14,-15,-16,-11,-12,-48,-48,-48,-40,69,-48,-48,-17,-23,-27,-31,-34,-35,-38,-41,-45,-46,-47,-19,-22,-20,-24,-25,-26,-32,-33,-36,-37,-39,-18,-21,-28,-30,-29,]),'IF':([10,13,15,16,17,24,49,84,89,91,93,],[19,19,-14,-15,-16,-11,-17,-18,-28,-30,-29,]),'PRINT':([10,13,15,16,17,24,49,84,89,91,93,],[20,20,-14,-15,-16,-11,-17,-18,-28,-30,-29,]),'COMMA':([11,30,32,33,34,36,43,44,50,54,55,58,59,62,64,65,66,67,75,76,77,78,79,80,81,82,86,],[22,22,-48,-48,-48,-40,71,71,-23,-27,-31,-34,-35,-38,-41,-45,-46,-47,-24,-25,-26,-32,-33,-36,-37,-39,22,]),'COLON':([11,21,23,30,48,86,92,],[-48,29,-6,-48,-5,-48,94,]),'ASSIGN':([18,],[26,]),'LPAREN':([19,26,27,28,35,51,52,53,56,57,60,61,71,],[27,35,35,35,35,35,35,35,35,35,35,35,35,]),'ELSE':([24,83,],[-11,90,]),'PLUS':([26,27,28,33,34,35,36,51,52,53,56,57,59,60,61,62,64,65,66,67,71,80,81,82,],[38,38,38,56,-48,38,-40,38,38,38,38,38,-35,38,38,-38,-41,-45,-46,-47,38,-36,-37,-39,]),'MINUS':([26,27,28,33,34,35,36,51,52,53,56,57,59,60,61,62,64,65,66,67,71,80,81,82,],[39,39,39,57,-48,39,-40,39,39,39,39,39,-35,39,39,-38,-41,-45,-46,-47,39,-36,-37,-39,]),'CTEI':([26,27,28,35,37,38,39,40,51,52,53,56,57,60,61,71,],[-48,-48,-48,-48,66,-42,-43,-44,-48,-48,-48,-48,-48,-48,-48,-48,]),'CTEF':([26,27,28,35,37,38,39,40,51,52,53,56,57,60,61,71,],[-48,-48,-48,-48,67,-42,-43,-44,-48,-48,-48,-48,-48,-48,-48,-48,]),'CTESTRING':([28,71,],[44,44,]),'INT':([29,94,],[46,46,]),'FLOAT':([29,94,],[47,47,]),'GREATER':([32,33,34,36,55,58,59,62,64,65,66,67,78,79,80,81,82,],[51,-48,-48,-40,-31,-34,-35,-38,-41,-45,-46,-47,-32,-33,-36,-37,-39,]),'LESS':([32,33,34,36,55,58,59,62,64,65,66,67,78,79,80,81,82,],[52,-48,-48,-40,-31,-34,-35,-38,-41,-45,-46,-47,-32,-33,-36,-37,-39,]),'NOTEQUAL':([32,33,34,36,55,58,59,62,64,65,66,67,78,79,80,81,82,],[53,-48,-48,-40,-31,-34,-35,-38,-41,-45,-46,-47,-32,-33,-36,-37,-39,]),'RPAREN':([32,33,34,36,41,50,54,55,58,59,62,63,64,65,66,67,75,76,77,78,79,80,81,82,],[-48,-48,-48,-40,68,-23,-27,-31,-34,-35,-38,82,-41,-45,-46,-47,-24,-25,-26,-32,-33,-36,-37,-39,]),'TIMES':([34,36,64,65,66,67,82,],[60,-40,-41,-45,-46,-47,-39,]),'DIVIDE':([34,36,64,65,66,67,82,],[61,-40,-41,-45,-46,-47,-39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'programT':([4,],[5,]),'vars':([4,],[6,]),'empty':([4,10,11,13,26,27,28,30,32,33,34,35,43,44,51,52,53,56,57,60,61,71,74,86,96,],[7,14,23,14,40,40,40,23,54,58,62,40,72,72,40,40,40,40,40,40,40,40,88,23,88,]),'bloque':([5,68,90,],[9,83,93,]),'bloqueT':([10,13,],[12,25,]),'estatuto':([10,13,],[13,13,]),'asignacion':([10,13,],[15,15,]),'condicion':([10,13,],[16,16,]),'escritura':([10,13,],[17,17,]),'varsT':([11,30,86,],[21,48,92,]),'expresion':([26,27,28,35,71,],[31,41,43,63,43,]),'exp':([26,27,28,35,51,52,53,56,57,71,],[32,32,32,32,75,76,77,78,79,32,]),'termino':([26,27,28,35,51,52,53,56,57,60,61,71,],[33,33,33,33,33,33,33,33,33,80,81,33,]),'factor':([26,27,28,35,51,52,53,56,57,60,61,71,],[34,34,34,34,34,34,34,34,34,34,34,34,]),'factorT':([26,27,28,35,51,52,53,56,57,60,61,71,],[36,36,36,36,36,36,36,36,36,36,36,36,]),'factorF':([26,27,28,35,51,52,53,56,57,60,61,71,],[37,37,37,37,37,37,37,37,37,37,37,37,]),'escrituraT':([28,71,],[42,85,]),'tipo':([29,94,],[45,95,]),'expresionT':([32,],[50,]),'expT':([33,],[55,]),'terminoT':([34,],[59,]),'varcte':([37,],[64,]),'escrituraF':([43,44,],[70,73,]),'varsF':([74,96,],[87,97,]),'condicionT':([83,],[89,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON programT bloque','program',5,'p_program','tarea3_ply.py',100),
  ('programT -> vars','programT',1,'p_program','tarea3_ply.py',101),
  ('programT -> empty','programT',1,'p_program','tarea3_ply.py',102),
  ('vars -> VAR ID varsT COLON tipo SEMICOLON varsF','vars',7,'p_vars','tarea3_ply.py',108),
  ('varsT -> COMMA ID varsT','varsT',3,'p_vars','tarea3_ply.py',109),
  ('varsT -> empty','varsT',1,'p_vars','tarea3_ply.py',110),
  ('varsF -> ID varsT COLON tipo SEMICOLON varsF','varsF',6,'p_vars','tarea3_ply.py',111),
  ('varsF -> empty','varsF',1,'p_vars','tarea3_ply.py',112),
  ('tipo -> INT','tipo',1,'p_tipo','tarea3_ply.py',118),
  ('tipo -> FLOAT','tipo',1,'p_tipo','tarea3_ply.py',119),
  ('bloque -> LBRACKET bloqueT RBRACKET','bloque',3,'p_bloque','tarea3_ply.py',125),
  ('bloqueT -> estatuto bloqueT','bloqueT',2,'p_bloque','tarea3_ply.py',126),
  ('bloqueT -> empty','bloqueT',1,'p_bloque','tarea3_ply.py',127),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','tarea3_ply.py',133),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','tarea3_ply.py',134),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','tarea3_ply.py',135),
  ('asignacion -> ID ASSIGN expresion SEMICOLON','asignacion',4,'p_asignacion','tarea3_ply.py',141),
  ('escritura -> PRINT LBRACKET escrituraT RBRACKET SEMICOLON','escritura',5,'p_escritura','tarea3_ply.py',147),
  ('escrituraT -> expresion escrituraF','escrituraT',2,'p_escritura','tarea3_ply.py',148),
  ('escrituraT -> CTESTRING escrituraF','escrituraT',2,'p_escritura','tarea3_ply.py',149),
  ('escrituraF -> COMMA escrituraT','escrituraF',2,'p_escritura','tarea3_ply.py',150),
  ('escrituraF -> empty','escrituraF',1,'p_escritura','tarea3_ply.py',151),
  ('expresion -> exp expresionT','expresion',2,'p_expresion','tarea3_ply.py',157),
  ('expresionT -> GREATER exp','expresionT',2,'p_expresion','tarea3_ply.py',158),
  ('expresionT -> LESS exp','expresionT',2,'p_expresion','tarea3_ply.py',159),
  ('expresionT -> NOTEQUAL exp','expresionT',2,'p_expresion','tarea3_ply.py',160),
  ('expresionT -> empty','expresionT',1,'p_expresion','tarea3_ply.py',161),
  ('condicion -> IF LPAREN expresion RPAREN bloque condicionT','condicion',6,'p_condicion','tarea3_ply.py',167),
  ('condicionT -> ELSE bloque','condicionT',2,'p_condicion','tarea3_ply.py',168),
  ('condicionT -> SEMICOLON','condicionT',1,'p_condicion','tarea3_ply.py',169),
  ('exp -> termino expT','exp',2,'p_exp','tarea3_ply.py',175),
  ('expT -> PLUS exp','expT',2,'p_exp','tarea3_ply.py',176),
  ('expT -> MINUS exp','expT',2,'p_exp','tarea3_ply.py',177),
  ('expT -> empty','expT',1,'p_exp','tarea3_ply.py',178),
  ('termino -> factor terminoT','termino',2,'p_termino','tarea3_ply.py',184),
  ('terminoT -> TIMES termino','terminoT',2,'p_termino','tarea3_ply.py',185),
  ('terminoT -> DIVIDE termino','terminoT',2,'p_termino','tarea3_ply.py',186),
  ('terminoT -> empty','terminoT',1,'p_termino','tarea3_ply.py',187),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor','tarea3_ply.py',193),
  ('factor -> factorT','factor',1,'p_factor','tarea3_ply.py',194),
  ('factorT -> factorF varcte','factorT',2,'p_factor','tarea3_ply.py',195),
  ('factorF -> PLUS','factorF',1,'p_factor','tarea3_ply.py',196),
  ('factorF -> MINUS','factorF',1,'p_factor','tarea3_ply.py',197),
  ('factorF -> empty','factorF',1,'p_factor','tarea3_ply.py',198),
  ('varcte -> ID','varcte',1,'p_varcte','tarea3_ply.py',204),
  ('varcte -> CTEI','varcte',1,'p_varcte','tarea3_ply.py',205),
  ('varcte -> CTEF','varcte',1,'p_varcte','tarea3_ply.py',206),
  ('empty -> <empty>','empty',0,'p_empty','tarea3_ply.py',212),
]
