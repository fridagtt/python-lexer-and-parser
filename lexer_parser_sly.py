from sly import Lexer, Parser

#__________LEXER____________

class CalcLexer(Lexer):
    # Set of token names
    tokens = { 'IF', 'ELSE', 'PROGRAM', 'VAR', 'PRINT', 'INT', 'FLOAT', 'COLON',
              'SEMICOLON', 'COMMA', 'LBRACKET', 'RBRACKET', 'RPAREN', 'LPAREN',
              'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'GREATER', 'LESS', 'NOTEQUAL',
              'ASSIGN', 'ID', 'CTEF', 'CTEI', 'CTESTRING' }

    # String containing ignored characters between tokens
    ignore = ' \t'

    COLON = r':'
    SEMICOLON = r';'
    COMMA = r','
    LBRACKET = r'\{'
    RBRACKET = r'\}'
    LPAREN = r'\('
    RPAREN = r'\)'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    GREATER = r'>'
    LESS = r'<'
    NOTEQUAL = r'<>'
    ASSIGN = r'='
    CTESTRING = r'"[a-zA-Z0-9!@#$%^&*()]*"'

    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = 'IF'
    ID['else'] = 'ELSE'
    ID['program'] = 'PROGRAM'
    ID['var'] = 'VAR'
    ID['print'] = 'PRINT'
    ID['int'] = 'INT'
    ID['float'] = 'FLOAT'

    @_(r'\d+\.\d+')
    def CTEF(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def CTEI(self, t):
        t.value = int(t.value)
        return t
    
    # Define a rule so we can track line numbers
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    # Error handling rule
    def t_error(self, t):
        print('Line: %d: Not valid character: %r' % (self.lineno, t.value[0]))

#Testear el léxico
"""
if __name__ == '__main__':
    data = 'if else print program var print int float 14.5 14 + - * / > = frida_98 "Frida"'
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print(tok)
"""

#__________PARSER____________

class CalcParser(Parser):
    # Get the token list from the lexer
    tokens = CalcLexer.tokens

    # Grammar rules and actions
    @_('PROGRAM ID SEMICOLON programT bloque')
    def program(self, p):
        return p
    
    @_('vars',
       'empty')
    def programT(self, p):
        return p
    
    @_('VAR ID varsT COLON tipo SEMICOLON varsF')
    def vars(self, p):
        return p
    
    @_('COMMA ID varsT',
       'empty')
    def varsT(self, p):
        return p
    
    @_('ID varsT COLON tipo SEMICOLON varsF',
       'empty')
    def varsF(self, p):
        return p
    
    @_('INT',
       'FLOAT')
    def tipo(self, p):
        return p
    
    @_('LBRACKET bloqueT RBRACKET')
    def bloque(self, p):
        return p
    
    @_('estatuto bloqueT',
       'empty')
    def bloqueT(self, p):
        return p
    
    @_('asignacion',
       'condicion',
       'escritura')
    def estatuto(self, p):
        return p
    
    @_('ID ASSIGN expresion SEMICOLON')
    def asignacion(self, p):
        return p
    
    @_('PRINT LBRACKET escrituraT RBRACKET SEMICOLON')
    def escritura(self, p):
        return p
    
    @_('expresion escrituraF',
       'CTESTRING escrituraF')
    def escrituraT(self, p):
        return p
    
    @_('COMMA escrituraT',
       'empty')
    def escrituraF(self, p):
        return p
    
    @_('exp expresionT')
    def expresion(self, p):
        return p
    
    @_('GREATER exp',
       'LESS exp',
       'NOTEQUAL exp',
       'empty')
    def expresionT(self, p):
        return p
    
    @_('IF LPAREN expresion RPAREN bloque condicionT')
    def condicion(self, p):
        return p
    
    @_('ELSE bloque',
       'SEMICOLON')
    def condicionT(self, p):
        return p
    
    @_('termino expT')
    def exp(self, p):
        return p
    
    @_('PLUS exp',
       'MINUS exp',
       'empty')
    def expT(self, p):
        return p
    
    @_('factor terminoT')
    def termino(self, p):
        return p
    
    @_('TIMES termino',
       'DIVIDE termino',
       'empty')
    def terminoT(self, p):
        return p
    
    @_('LPAREN expresion RPAREN',
       'factorT')
    def factor(self, p):
        return p
    
    @_('factorF varcte')
    def factorT(self, p):
        return p
    
    @_('PLUS',
       'MINUS',
       'empty')
    def factorF(self, p):
        return p
    
    @_('ID',
       'CTEI',
       'CTEF')
    def varcte(self, p):
        return p
    
    @_(' ')
    def empty(self, p):
        return p
    
    def error(self, p):
        if p:
            print("Syntax error at token", p.type)
            self.tokens
        else:
            print("Syntax error at EOF")
    
if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()

    try:
        file = open("ejemplos.txt", "r")
        print(f"SLY LEXER AND PARSER")
        for line in file:
            parser.parse(lexer.tokenize(line))
            print(f"approved line: {line}")
    except EOFError:
        print('ERROR')