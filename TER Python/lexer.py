import re

token_list = (
        'INT',
        'FLOAT',
        'PLUS',
        'ESPECE',
        'DIAMETRE',
        'TAILLE',
        'VITESSE',
        'INIT',
        'EQ',
        'LPAREN',
        'RPAREN',
        'LBRACKET',
        'RBRACKET',
        'COLON',
        'SEMICOLON',
        'ARROW',
        'IDENT',
    )
    
class LexicalAnalyzer:
    lin_num=1
    
    def tokenize(self, data):
        rules = [
            ('ESPECE', r'espece'),
            ('DIAMETRE', r'diametre'),
            ('TAILLE', r'taille'),
            ('VITESSE', r'vitesse'),
            ('INIT', r'init'),  
            ('EQ', r'::='),
            ('PLUS', r'\+'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('LBRACKET', r'\['),
            ('RBRACKET', r'\]'),
            ('COLON', r','),
            ('SEMICOLON', r';'),
            ('ARROW', r'->'),
            ('FLOAT', r'\d(\d)*\.\d(\d)*'),
            ('INTEGER', r'\d(\d)*'),
            ('IDENT', r'[a-zA-Z]\w*'),
            ('SKIP', r'[ \t]+'),
            ('NEWLINE', r'\n'),
            ('MISMATCH', r'.'),
        ]

        token_regex = '|'.join('(?P<%s>%s)' % x for x in rules)
        lin_start=0
        
        token=[]
        lexeme=[]
        row=[]
        column=[]

        for m in re.finditer(token_regex, data):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == 'INTEGER':
                token_lexeme = int(token_lexeme)
            if token_type == 'FLOAT':
                token_lexeme = float(token_lexeme)
            if token_type == 'NEWLINE':
                lin_start = m.end()
                self.lin_num +=1
            elif token_type == 'SKIP':
                continue
            elif token_type == 'MISMATCH':
                raise RuntimeError('%r unexpected on line %d' % (token_lexeme, self.lin_num))
            else:
                    col = m.start() - lin_start
                    column.append(col)
                    token.append(token_type)
                    lexeme.append(token_lexeme)
                    row.append(self.lin_num)
                    # To print information about a Token
                    print('({0}, \'{1}\'), Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))

        return token, lexeme, row, column

