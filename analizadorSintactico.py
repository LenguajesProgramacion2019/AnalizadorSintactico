#Oscar Fabian Nanez Nunez
#Gabriela Suarez Carvajal

import re
import sys

global lexeme
global line
global diccLexema
global diccToken
diccLexema = []
diccToken = []
row = 1
back = [0, 0]

reserved_words = [
    'log',
    'true',
    'false',
    'importar',
    'for',
    'funcion',
    'retorno',
    'end',
    'if',
    'while',
    'nil',
    'else',
    'desde',
    'todo',
    'leer'
]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '{', '}', '#', '[', ']', '(', ')', '<', '>', '=', '.',
            '!', '&', '|', '+', '-', '*', '/', '%', '^', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '"', ',', ':', '\n']

def delta(column, char, state):
    global lexeme
    global line
    if state == 0:
        #cadenas no especificas => string
        if char not in alphabet:
            print(">>> Error lexico(linea:" + str(row) + ",posicion:" + str(column) + ")")
            exit(0)
        if char == '"':
            lexeme = ""
            return [8, 0]
        # operadores especiales
        elif char == '{':
            diccLexema.append('{')
            diccToken.append('token_llave_izq')
            return [0, 0]
        elif char == '}':
            diccLexema.append('}')
            diccToken.append('token_llave_der')
            return [0, 0]
        elif char == '#':
            line = ""
            return [0, 0]
        elif char == '[':
            diccLexema.append('[')
            diccToken.append('token_cor_izq')
            return [0, 0]
        elif char == ']':
            diccLexema.append(']')
            diccToken.append('token_cor_der')
            return [0, 0]
        elif char == '(':
            diccLexema.append('(')
            diccToken.append('token_par_izq')
            return [0, 0]
        elif char == ')':
            diccLexema.append(')')
            diccToken.append('token_par_der')
            return [0, 0]
        elif char == '.':
            diccLexema.append('.')
            diccToken.append('token_point')
            return [0, 0]
        elif char == '+':
            diccLexema.append('+')
            diccToken.append('token_mas')
            return [0, 0]
        elif char == '-':
            diccLexema.append('-')
            diccToken.append('token_menos')
            return [0, 0]
        elif char == '*':
            diccLexema.append('*')
            diccToken.append('token_mul')
            return [0, 0]
        elif char == '/':
            diccLexema.append('/')
            diccToken.append('token_div')
            return [0, 0]
        elif char == '%':
            diccLexema.append('%')
            diccToken.append('token_mod')
            return [0, 0]
        elif char == '^':
            diccLexema.append('^')
            diccToken.append('token_pot')
            return [0, 0]
        elif char == ',':
            diccLexema.append(',')
            diccToken.append('token_coma')
            return [0, 0]
        elif char == ':':
            diccLexema.append(':')
            diccToken.append('token_dosp')
            return [0, 0]
        elif char == '>':
            return [1, 0]
        elif char == '<':
            return [2, 0]
        elif char == '=':
            return [3, 0]
        elif char == '!':
            return [4, 0]
        elif char == '&':
            return [5, 0]
        elif char == '|':
            return [6, 0]
        elif char == 'i':
            return [7, 0]
        #cadenas no especificas => id
        #palabras reservadas
        elif re.match(r'[a-z]', char) or re.match(r'[A-Z]', char):
            lexeme=char
            return [9, 0]
        #cadenas no especificas => int, float
        elif re.match(r'[0-9]', char):
            lexeme = char
            return [10, 0]
        else:
            return [0, 0]

    if state == 1:
        if char == '=':
            diccLexema.append('>=')
            diccToken.append('token_mayor_igual')
            return [0, 0]
        else:
            diccLexema.append('>')
            diccToken.append('token_mayor')
            state = 0
            return [0, 1]

    if state == 2:
        if char == '=':
            diccLexema.append('<=')
            diccToken.append('token_menor_igual')
            return [0,0]
        else:
            diccLexema.append('<')
            diccToken.append('token_menor')
            return [0,1]

    if state == 3:
        if char == '=':
            diccLexema.append('==')
            diccToken.append('token_igual_num')
            return [0, 0]
        else:
            diccLexema.append('=')
            diccToken.append('token_assign')
            return [0, 1]

    if state == 4:
        if char == '=':
            diccLexema.append('!=')
            diccToken.append('token_diff_num')
            return [0, 0]
        else:
            diccLexema.append('!')
            diccToken.append('token_not')
            return [0, 1]

    if state == 5:
        if char == '&':
            diccLexema.append('&&')
            diccToken.append('token_and')
            return [0, 0]
        else:
            print(">>> Error lexico(linea:" + str(row) + ",posicion:" + str(column - 1) + ")")
            exit(0)

    if state == 6:
        if char == '|':
            diccLexema.append('||')
            diccToken.append('token_or')
            return [0, 0]
        else:
            print(">>> Error lexico(linea:" + str(row) + ",posicion:" + str(column - 1) + ")")
            exit(0)

    if state == 7:
        if char == 'n':
            diccLexema.append('in')
            diccToken.append('in')
            return [0, 0]
        else:
            lexeme = 'i'
            return [9, 1]

    if state == 8:
        if char == '"':
            diccLexema.append(lexeme)
            diccToken.append('token_string')
            return[0, 0]
        else:
            lexeme = lexeme + char
            return [8, 0]

    if state == 9:
        if re.match(r'[a-z]', char) or re.match(r'[A-Z]', char) or re.match(r'[0-9]', char):
            lexeme = lexeme + str(char)
            return[9, 0]
        else:
            if lexeme in reserved_words:
                diccLexema.append(lexeme)
                diccToken.append(lexeme)
            else:
                diccLexema.append(lexeme)
                diccToken.append('id')
            return [0, 1]

    if state == 10:
        if re.match(r'[0-9]', char):
            lexeme = lexeme + char
            return [10, 0]
        elif char == '.':
            lexeme = lexeme + char
            return [11, 0]
        else:
            diccLexema.append(lexeme)
            diccToken.append('token_integer')
            return [0, 1]

    if state == 11:
        if re.match(r'[0-9]', char):
            lexeme = lexeme + char
            return[12, 0]
        else:
            diccLexema.append(lexeme[0:len(lexeme)-1])
            diccToken.append('token_integer')
            return[0, 2]

    if state == 12:
        if re.match(r'[0-9]', char):
            lexeme = lexeme + char
            return[12, 0]
        else:
            diccLexema.append(lexeme)
            diccToken.append('token_float')
            return [0, 1]




line = input()
#for line in lines:
while line != 'wea':
    i = 0
    line = line + " "
    while i < len(line):
        back = delta(i+1, line[i], back[0])
        i = i + 1 - back[1]
    if back[0] == 8:
        print("Error lexico(linea:" + str(row) + ",posicion:" + str(i - len(lexeme)) + ")")
        exit(0)

    line = input()
    row += 1

#print(diccLexema)
#print(diccToken)

global no_terminal
global derivation_chain
no_terminal = 'BB' #token inicial de la gramática
derivation_chain = ['BB'] #token inicial de la gramática


def derivation (token):
    global  no_terminal
    global derivation_chain

    derivation_chain.pop(0)

    if no_terminal == 'MULASIG':
        derivation_chain.insert(0, 'ASIG')
        derivation_chain.insert(1, 'MULASIGP')
    elif no_terminal == 'MULASIGP':
        if(token == 'token_coma'):
            derivation_chain.insert(0, 'token_coma')
            derivation_chain.insert(1, 'MULASIG')
    elif no_terminal == 'ASIG':
        derivation_chain.insert(0, 'id')
        derivation_chain.insert(1, 'token_assign')
        derivation_chain.insert(2, 'ASIGP')
    elif no_terminal == 'ASIGP':
        if(token == 'token_integer'):
            derivation_chain.insert(0, 'token_integer')
        if (token == 'token_float'):
            derivation_chain.insert(0, 'token_float')
        if(token == 'token_string'):
            derivation_chain.insert(0, 'token_string')
    #Bloque boleano
    elif no_terminal == 'BB':
        if token == 'token_par_izq':
            derivation_chain.insert(0, 'token_par_izq')
            derivation_chain.insert(1, 'EBAND')
            derivation_chain.insert(2, 'token_or')
            derivation_chain.insert(3, 'BB')
            derivation_chain.insert(4, 'token_par_der')
        else:
            derivation_chain.insert(0, 'EBAND')
            derivation_chain.insert(1, 'BBP')
    elif no_terminal == 'BBP':
        if token == 'token_or':
            derivation_chain.insert(0, 'token_or')
            derivation_chain.insert(0, 'BB')
    elif no_terminal == 'EBAND':
        if token == 'token_par_izq':
            derivation_chain.insert(0, 'token_par_izq')
            derivation_chain.insert(1, 'EB')
            derivation_chain.insert(2, 'token_and')
            derivation_chain.insert(3, 'EBAND')
            derivation_chain.insert(4, 'token_par_der')
        else:
            derivation_chain.insert(0, 'EB')
            derivation_chain.insert(1, 'EBANDP')
    elif no_terminal == 'EBANDP':
        if token == 'token_and':
            derivation_chain.insert(0, 'token_and')
            derivation_chain.insert(1, 'EBAND')
    elif no_terminal == 'EB':
        if token == 'token_par_izq':
            derivation_chain.insert(0, 'token_par_izq')
            derivation_chain.insert(1, 'EBCOM')
            derivation_chain.insert(2, 'OBIGU')
            derivation_chain.insert(3, 'EB')
            derivation_chain.insert(4, 'token_par_der')
        elif token == 'token_not':
            derivation_chain.insert(0, 'token_not')
            derivation_chain.insert(1, 'EB')
        else:
            derivation_chain.insert(0, 'EBCOM')
            derivation_chain.insert(1, 'EBP')
    elif no_terminal == 'OBIGU':
        if token == 'token_igual_num':
            derivation_chain.insert(0, 'token_igual_num')
        if token == 'token_diff_num':
            derivation_chain.insert(0, 'token_diff_num')
    elif no_terminal == 'EBCOM':
        if token == 'token_par_izq':
            derivation_chain.insert(0, 'token_par_izq')
            derivation_chain.insert(1, 'EARI')
            derivation_chain.insert(2, 'OBCOM')
            derivation_chain.insert(3, 'EARI')
            derivation_chain.insert(4, 'token_par_der')
        elif token == 'true':
            derivation_chain.insert(0, 'true')
        elif token == 'false':
            derivation_chain.insert(0, 'false')
        else:
            derivation_chain.insert(0, 'EARI')
            derivation_chain.insert(1, 'OBCOM')
            derivation_chain.insert(2, 'EARI')
    elif no_terminal == 'OBCOM':
        if token == 'token_menor_igual':
            derivation_chain.insert(0, 'token_menor_igual')
        if token == 'token_menor':
            derivation_chain.insert(0, 'token_menor')
        if token == 'token_mayor_igual':
            derivation_chain.insert(0, 'token_mayor_igual')
        if token == 'token_mayor':
            derivation_chain.insert(0, 'token_mayor')
    elif no_terminal == 'EARI':
        if token == 'token_par_izq':
            derivation_chain.insert(0, 'token_par_izq')
            derivation_chain.insert(1, 'EMUL')
            derivation_chain.insert(2, 'OPSUM')
            derivation_chain.insert(3, 'EARI')
            derivation_chain.insert(4, 'token_par_der')
        elif token == 'token_mas' or token == 'token_menos':
            derivation_chain.insert(0, 'OPSUM')
            derivation_chain.insert(1, 'EARI')
        else:
            derivation_chain.insert(0, 'EMUL')
            derivation_chain.insert(1, 'EARIP')
    elif no_terminal == 'EARIP':
        if token == 'token_mas' or token == 'token_menos':
            derivation_chain.insert(0, 'OPSUM')
            derivation_chain.insert(1, 'EARI')
    elif no_terminal == 'OPSUM':
        if token == 'token_mas':
            derivation_chain.insert(0, 'token_mas')
        elif token == 'token_menos':
            derivation_chain.insert(0, 'token_menos')
    elif no_terminal == 'EMUL':
        if token == 'token_par_izq':
            derivation_chain.insert(0, 'token_par_izq')
            derivation_chain.insert(1, 'E')
            derivation_chain.insert(2, 'OPMUL')
            derivation_chain.insert(3, 'EMUL')
            derivation_chain.insert(4, 'token_par_der')
        else:
            derivation_chain.insert(0, 'E')
            derivation_chain.insert(1, 'EMULP')
    elif no_terminal == 'EMULP':
        if token == 'token_mul' or token == 'token_div':
            derivation_chain.insert(0, 'OPMUL')
            derivation_chain.insert(1, 'EMUL')
    elif no_terminal == 'OPMUL':
        if token == 'token_mul':
            derivation_chain.insert(0, 'token_mul')
        elif token == 'token_div':
            derivation_chain.insert(0, 'token_div')
    elif no_terminal == 'E':
        if token == 'token_integer':
            derivation_chain.insert(0, 'token_integer')
        elif token == 'token_float':
            derivation_chain.insert(0, 'token_float')
        elif token == 'id':
            derivation_chain.insert(0, 'id')

global predictions
predictions = { 'MULASIG': ['id'],
                'MULASIGP': diccToken,
                'ASIG': ['id'],
                'ASIGP': diccToken,
                'BBINIT': ['token_integer', 'token_float', 'id', 'true', 'false', 'token_par_izq'],
                'BB': ['token_integer', 'token_float', 'id', 'true', 'false', 'token_par_izq'],
                'BBP': diccToken,
                'EBAND': ['token_integer', 'token_float', 'id', 'true', 'false', 'token_par_izq'],
                'EBANDP': diccToken,
                'EB': ['token_integer', 'token_float', 'id', 'true', 'false', 'token_not', 'token_par_izq'],
                'EBP': diccToken,
                'OBIGU': ['token_igual_num', 'token_diff_num'],
                'EBCOM': ['token_integer', 'token_float', 'id', 'true', 'false', 'token_par_izq'],
                'OBCOM': ['token_menor_igual', 'token_menor', 'token_mayor_igual', 'token_mayor'],
                'EARI': ['token_integer', 'token_float', 'id', 'token_mas', 'token_menos', 'token_par_izq'],
                'EARIP': diccToken,
                'OPSUM': ['token_mas', 'token_menos'],
                'EMUL': ['token_integer', 'token_float', 'id', 'token_par_izq'],
                'EMULP': diccToken,
                'OPMUL': ['token_mul', 'token_div'],
                'E': ['token_integer', 'token_float', 'id'],
                #Expresion booleana
                'FIN': []
              }


for token in diccToken:

    print("token:" + token)
    #print(no_terminal)
    while token != no_terminal:
        if token in predictions[no_terminal]:
            print(no_terminal)
            print(derivation_chain)
            derivation(token)
            if len(derivation_chain)>0:
                no_terminal = derivation_chain[0]
            else:
                no_terminal= 'FIN'
                print("error")
        else:
            no_terminal = 'FIN'
            print("error 1")
            break

    print(derivation_chain)
    if no_terminal == 'FIN':
        break
    elif len(derivation_chain) > 0:
        derivation_chain.pop(0)
        no_terminal = derivation_chain[0]



token = '0'
while len(derivation_chain)>0:
    no_terminal = derivation_chain[0]
    derivation(token)

print(derivation_chain)
