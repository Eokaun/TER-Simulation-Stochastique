from lexer import LexicalAnalyzer
from molecule import Molecule

token = []
lexeme = []
row = []
column = []
analyzer = LexicalAnalyzer()
# Tokenize and reload of the buffer
data = """espece ::= E, S, P, Es;
        diametre ::= 1000;
        taille(E) ::= 7;
        vitesse(E) ::= 0.5;
        init(E)::=50;
        taille(P) ::= 3;
        vitesse(P) ::= 1;
        init(P)::=40;
        taille(S) ::= 8;
        vitesse(S) ::= 0.7;
        init(S)::=70;
        taille(Es) ::= 6;
        vitesse(Es) ::= 0.6;
        init(Es)::=60;
        E+S->Es[0.3];
        Es->E+S[0.0002];
        Es -> E + P [0.005];"""
t, lex, lin, col = analyzer.tokenize(data)
token += t
lexeme += lex
row += lin
column += col

print('\nRecognize Tokens: ', token)
tabPars = [['E', 'S', 'P', 'Es'],
           [7, 3, 8, 6],
           [0.5, 1, 0.7, 0.6],
           [50, 40, 70, 60],
           [('E','S'), ('Es'), ('Es')],
           ['Es', ('E', 'S'), ('E', 'P')],
           [0.3, 0.0002, 0.005]]

m = []
for index in range(len(tabPars[0])):
        name = tabPars[0][index]
        taille = tabPars[1][index]
        vitesse = tabPars[2][index]
        init = tabPars[3][index]
        m.append(Molecule(name, taille, vitesse, init))

