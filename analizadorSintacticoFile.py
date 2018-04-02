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
#lines = sys.stdin.readlines()
#for line in lines:
while line != 'wea':
    i = 0
    line = line + " "
    while i < len(line):
        back = delta(i+1, line[i], back[0])
        i = i + 1 - back[1]
    diccLexema.append("\n")
    diccToken.append('eol')
    if back[0] == 8:
        print("Error lexico(linea:" + str(row) + ",posicion:" + str(i - len(lexeme)) + ")")
        exit(0)

    line = input()
    row += 1

#print(diccLexema)
print(diccToken)

global no_terminal
global derivation_chain
global token
token = diccToken[0]

def PROGRAMA():
    print("PROGRAMA")
    global token
    if token == 'funcion' or token== 'id':
        SENTENCE()
    elif token == 'eol':
        match('eol')
        PROGRAMA()
def FUNC():
    print("FUNC")
    global token
    if token == 'funcion':
        a = 1

def SENTENCE():
    print("SENTENCE")
    global token
    if token == 'id':
        ASSIGN()
def ASSIGN():
    print("ASSIGN")
    global token
    if token == 'id':
        match('id')
        match('token_assign')
        ASSIGNP()
def ASSIGNP():
    global token
    print("ASSIGNP", token)
    if token == 'token_integer':
        match('token_integer')
    elif token == 'token_float':
        match('token_float')
    elif token == 'token_string':
        match('token_string')
    PROGRAMA()
def BB(token):
    if token == 'token_not' or token == 'true' or token == 'false' or token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id':
        EBAND(token)
        BBP(token)
    else:
        print("error BB")

def BBP(token):
    if token == 'or':
        token = match()
        BB(token)
    elif token == 'eol':
        pass
    else:
        print("error BBP")

def EBAND(token):
    if token == 'token_not' or token == 'true' or token == 'false' or token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id':
        EB(token)
        EBANDP(token)
    else:
        print("error EBAND")

def EBANDP(token):
    if token == 'and':
        token = match()
        EBAND(token)
    elif token == 'or' or token == 'eol':
        pass
    else:
        print("Error EBANDP")

def EB(token):
    if token == 'true' or token == 'false' or token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id':    
        EBCOM(token)
        EBP(token)
    elif token == 'token_not':
        token = match()
        EB(token)
    else:
        print("Error EB")

def EBP(token):
    if token == 'token_igual_num' or token == 'token_diff_num':
        OBIGU(token)
        EB(token)
    elif token == 'token_and' or token == 'token_or' or token == 'eol':
        pass
    else:
        print("Error EBP")

def OBIGU(token):
    if token == 'token_igual_num':
        token = match()
    elif token == 'token_diff_num':
        token = match()
    else:
        print("Error OBIGU")

def EBCOM(token):
    if token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id':
        EARI(token)
        OBCOM(token)
        EARI(token)
    elif token == 'true':
        token = match()
    elif token == 'false':
        token = match()
    else:
        print("Error EBCOM")

def OBCOM(token):
    if token == 'token_menor':
        token = match()
    elif token == 'token_mayor':
        token = match()
    if token == 'token_menor_igual':
        token = match()
    if token == 'token_mayor_igual':
        token = match()
    else:
        print("Error OBCOM")

def EARI(token):
    if token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id':
        EMUL(token)
        EARIP(token)
    else:
        print("Error EARI")

def EARIP(token):
    if token == 'token_mas' or token == 'token_menos':
        OPSUM(token)
        EARI(token)
    elif token == 'token_menor' or token == 'token_mayor' or token == 'token_mayor_igual' or token == 'token_menor_igual' or token == 'token_igual_num' or token == 'token_diff_num' or token == 'token_and' or token == 'token_or' or token == 'eol' :
        pass
    else:
        print('Error EARIP')

def OPSUM(token):
    if token == 'token_mas':
        token = match()
    elif token == 'token_menos':
        token == match()
    else:
        print('Error OPSUM')

def EMUL(token):
    if token == 'token_par_izq':
        token = match()
        E(token)
        OPMUL(token)
        EMUL(token)
        token = match()
    elif token == 'token_integer' or token == 'token_float' or token == 'id':
        E(token)
        EMULP(token)
    else:
        print("Error EMUL")

def EMULP(token):
    if token == 'token_div' or token == 'token_mul':
        OPMUL(token)
        EMUL(token)
    elif token == 'token_par_der' or token == 'token_mas':
        #or token == 'token_menos' or token == 'token_menor' or token == 'token_mayor' token == 'token_mayor_igual' or token == 'token_menor_igual' or token == 'token_igual_num' or token == 'token_diff_num' or token == 'token_and' or token == 'token_or' or token == 'eol' :
        pass
    else:
        print("Error EMULP")

def OPMUL(token):
    if token == 'token_div':
        token = match()
    elif token == 'token_mul':
        token = match()
    else:
        print('Error OPMUL')

def E(token):
    if token == 'token_integer':
        token = match()
    elif token == 'token_float':
        token = match()
    elif token == 'id':
        token = match()
    else:
        print('Error E')

global cont
cont=0
def match(espectedToken):
    global token
    global cont
    print("match", espectedToken, token)
    if(token == espectedToken):
        cont+=1
    else:
        errorSintaxis(espectedToken)

    if cont == len(diccToken):
        print("El analisis sintactico ha finalizado correctamente.")
        exit(0)
    else:
        token = diccToken[cont]

def errorSintaxis(espectedToken):
    a = 1

PROGRAMA()