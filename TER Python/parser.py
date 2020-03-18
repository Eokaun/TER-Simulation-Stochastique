import ply.yacc as yacc
import molecule
from lexer import token_list

def p_expression_espece(p):
    'ESPECE ::= especes'
    p_list_species(p[1])

def p_list_species(p):
    "IDENT; | IDENT, especes"
     