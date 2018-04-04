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
global cont

token = diccToken[0]

def PROGRAMA():
    global token
    if token == 'funcion' or token== 'id' or token == 'log' or token == 'for' or token == 'while' or token == 'if' or token == 'leer' or token == 'import' or token == 'desde':
        FUNCTIONSECT()
        MODULE()
    else:
        print("Error PROGRAMA()")


def FUNCTIONSECT():
    global token
    if token == 'funcion':
        FUNCTION()
        FUNCTIONSECT()
    elif token == 'id' or token == 'log' or token == 'for' or token == 'while' or token == 'if' or token == 'leer' or token == 'import' or token == 'desde':
        pass
    else:
        print("Error FUNCTIONSECT")


def FUNCTION():
    global token
    if token == 'funcion':
        match('funcion')
        match('id')
        match('token_par_izq')
        SENTENCE()
        match('token_par_der')
        match('eol')
        BLOCK()
        RETURN()
        match("end")
        match("funcion")
        match('eol')
    else:
        print("Error FUNCTION")

def ARGDEC():
    global token
    if token == 'id':
        match('id')
        ARGDECP()
    else:
        print("Error ARGDEC")

def ARGDECP():
    global token
    if token == 'token_coma':
        match('token_coma')
        ARGDEC()
    elif token == 'token_par_der':
        pass
    else:
        print("Error ARGDECP")

def RETURN():
    global token
    if token == 'retorno':
        match('retorno')
        match('token_par_izq')
        SENTENCE()
        match('token_par_der')
        match('eol')
    elif token == 'end':
        pass
    else:
        print("Error RETURN")

def MODULE():
    global token
    if token == 'import' or token == 'desde':
        IMPORT()
    elif token == 'id' or token == 'log' or token == 'for' or token == 'while' or token == 'token_par_izq' or token == 'if' or token == 'leer':
        BLOCK()
    else:
        print("Error MODULE")

def IMPORT():
    global token
    if token=="import":
        match('import')
        ID()
    elif token == 'desde':
        match('desde')
        match('id')
        match('import')
        match('id')
    else:
        print("Error IMPORT")

def ID():
    global token
    print('ID')
    if token == 'token_point':
        match('token_point')
        ID()
        MODULE()
    elif token == 'id':
        match('id')
        MODULE()
    else:
        print("Error ID")


def BLOCK():
    global token
    if token == 'id':
        match('id')
        ASSICALL()
        MODULE()
    if token == ('log'):
        PRINT()
        MODULE()
    elif token == ('leer'):
        READ()
        MODULE()
    elif token == 'for':
        BUCLE()
        MODULE()
    elif token == 'if':
        IF()
        MODULE()
    elif token == 'while':
        WHILE()
        MODULE()
    else:
        print("Error BLOCK")

def ASSICALL():
    global token
    if token == 'token_assign':
        ASSIGN()
    elif token == 'token_par_izq':
        CALLFUNC()
    else:
        print("Error ASSICALL")

def SENTENCE():
    global token
    if token == 'token_not' or token == 'token_par_der' or token == 'token_integer' or token == 'token_float' or token == 'true' or token == 'false':
        BB()
    elif token == 'id':
        match('id')
        SENTENCEP()
    elif token == 'token_string':
        match('token_string')
    elif token == 'token_cor_izq':
        ARRAY()
    elif token == 'token_llave_izq':
        STRUC()
    else:
        print("Error SENTENCE")

def SENTENCEP():
    if token == 'token_par_izq':
        CALLFUNC()
    elif token == 'token_not' or token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id' or token == 'true' or token == 'false':
        BB()
    else:
        print("Error SENTENCEP")

def CALLFUNC():
    global token
    if token == 'token_par_izq':
        match('token_par_izq')
        SENTENCE()
        match('token_par_der')
    else:
        print("Error CALLFUNC")

def ASSIGN():
    global token
    if token == 'token_assign':
        match('token_assign')
        SENTENCE()
        match('eol')
    else:
        print("Error ASSIGN")

def PRINT():
    global token
    if token == 'log':
        match('log')
        match('token_par_izq')
        OUTPUT()
        match('token_par_der')
    else:
        print("Error PRINT")

def OUTPUT():
    global token
    if token == 'id' or token == 'token_string' or token == 'token_not' or token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'true' or token == 'false' or token == 'token_llave_izq':
        SENTENCE()
        OUTPUTP()
    else:
        print("Error OUTPUT")

def OUTPUTP():
    global  token
    if token == 'token_mas':
        match('token_mas')
        OUTPUT()
    elif token == 'token_par_der':
        pass
    else:
        print("Error OUTPUTP")

def READ():
    global token
    if token == 'leer':
        match('leer')
        match('token_par_izq')
        INPUT()
        match('token_par_der')
    else:
        print("Error READ")

def INPUT():
    global token
    if token == 'token_integer':
        match('token_integer')
    elif token == 'token_float':
        match('token_float')
    elif token == 'token_string':
        match('token_string')
    else:
        print("Error INPUT")

def ARRAY():
    global token
    if token == 'token_cor_izq':
        match('token_cor_izq')
        ARRELE()
        match('token_cor_der')
    else:
        print("Error ARRAY")

def ARRELE():
    global token
    if token == 'id' or token == 'token_string' or token == 'token_not' or token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'true' or token == 'false' or token == 'token_llave_izq':
        SENTENCE()
        ARRELEP()
    else:
        print("Error ARRELE")

def ARRELEP():
    global token
    if token == 'token_comma':
        match('token_coma')
        ARRELE()
    elif token == 'token_cor_der':
        pass
    else:
        print("Error ARRELEP")

def STRUC():
    global token
    if token == 'token_llave_izq':
        match('token_llave_izq')
        STRUCELE()
        match('token_llave_der')
    else:
        print("Error STRUC")

def STRUCELE():
    global token
    if token == 'id':
        match('id')
        match('token_dosp')
        SENTENCE()
        STRUCELEP()
    else:
        print("Error STRUCELE")

def STRUCELEP():
    global token
    if token == 'token_comma':
        match('token_coma')
        STRUCELE()
    elif token == 'token_llave_der':
        pass
    else:
        print("Error STRUCELEP")

def BB():
    global token
    if token == 'token_not' or token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id' or token == 'true' or token == 'false':
        EBAND()
        BBP()
    else:
        print("Error BB")

def BBP():
    global token
    if token == 'or':
        token = match('or')
        BBP2()
    elif token == 'token_par_der' or token == 'token_coma' or 'token_mas' or 'token_par_izq' or token == 'retorno':
        pass
    else:
        print("error BBP")

def BBP2():
    global token
    print("BBP2")

    if token == 'token_par_izq':
        match('token_par_izq')
        BB()
        match('token_par_der')
    elif token == 'token_not' or token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id' or token == 'true' or token == 'false':
        BB()
    else:
        print("error BB")

def EBAND():
    global token
    if token == 'token_not' or token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id' or token == 'true' or token == 'false':
        EB()
        EBANDP()
    else:
        print("error EBAND")

def EBANDP():
    global token
    if token == 'and':
        match('and')
        EBANDP2(token)
    elif token == 'token_par_der' or token == 'token_or' or token == 'token_coma' or 'token_mas' or 'token_par_izq' or token == 'retorno':
        pass
    else:
        print("Error EBANDP")

def EBANDP2():
    global token
    print('EBANDP2')
    if token == 'token_par_izq':
        match('token_par_izq')
        EBAND()
        match('token_par_der')
    elif token == 'token_not' or token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id' or token == 'true' or token == 'false':
        pass
    else:
        print("error token EBANDP2")

def EB():
    global token
    if token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id' or token == 'true' or token == 'false':
        EBCOM()
        EBP()
    elif token == 'token_not':
        match('token_not')
        EBP2()
    else:
        print("Error EB")

def EBP():
    if token == 'token_igual_num' or token == 'token_diff_num':
        OBIGU()
        EBP3()
    elif token == 'token_par_der' or token == 'token_and' or token == 'token_or' or token == 'token_coma' or token == 'token_mas' or token == 'token_par_der' or token == 'retorno' or token == 'eol':
        pass
    else:
        print("Error EBP")

def EBP3():
    global token
    if token == 'token_par_izq':
        match('token_par_izq')
        EB()
        match('token_par_der')
    elif token == 'token_not' or token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id' or token == 'true' or token == 'false':
        pass
    else:
        print("EBP3")

def EBP2():
    global token
    if token == 'token_not' or token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id' or token == 'true' or token == 'false':
        EB()
    elif token == 'token_par_der':
        match('token_par_izq')
        EB()
        match('token_par_der')
    else:
        print("error EBP2")

def OBIGU():
    global token
    if token == 'token_igual_num':
        match('token_igual_num')
    elif token == 'token_diff_num':
        match('token_diff_num')
    else:
        print("Error OBIGU")

def EBCOM():
    global token
    if token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id':
        EARI()
        OBCOMP()
    elif token == 'true' or token == 'false':
        BOOL()
    else:
        print("Error EBCOM")

def OBCOMP():
    global token
    if token == 'token_menor' or token == 'token_mayor' or token == 'token_menor_igual' or token == 'token_mayor_igual':
        OBCOM()
        EARI()
    elif token == 'token_igual_num' or token == 'token_diff_num' or token == 'token_par_der' or token == 'token_and' or token == 'token_or ' or token == 'token_coma' or token == 'token_mas' or token == 'token_menos' or token == 'token_llave_der' or token == 'else' or token == 'token_llave_izq' or token == 'retorno' or token == 'eol':
        pass
    else:
        print("Error OBCOMP")

def BOOL():
    global token
    if token == 'true':
        match('true')
    elif token == 'false':
        match('false')
    else:
        print("Error BOOL")

def OBCOM():
    if token == 'token_menor':
        match('token_menor')
    elif token == 'token_mayor':
        match('token_mayor')
    if token == 'token_menor_igual':
        match('token_menor_igual')
    if token == 'token_mayor_igual':
        match('token_mayor_igual')
    else:
        print("Error OBCOM")

def EARI():
    global token
    if token == 'token_par_izq':
        match('token_par_izq')
        EMUL()
        OPSUM()
        EARI()
        match('token_par_der')
    if token == 'token_par_izq' or token == 'token_integer' or token == 'token_float' or token == 'id':
        EMUL()
        EARIP()
    else:
        print("Error EARI")

def EARIP():
    global token
    if token == 'token_mas' or token == 'token_menos':
        OPSUM()
        EARI()
    elif token == 'token_par_der' or token == 'token_menor' or token == 'token_mayor' or token == 'token_mayor_igual' or token == 'token_menor_igual' or token == 'token_igual_num' or token == 'token_diff_num' or token == 'token_and' or token == 'token_or' or token == 'eol' or token == 'token_mas ' or token == 'token_par_izq' or token == 'retorno':
        pass
    else:
        print('Error EARIP')

def OPSUM():
    global token
    if token == 'token_mas':
        match('token_mas')
    elif token == 'token_menos':
        match('token_menos')
    else:
        print('Error OPSUM')

def EMUL():
    global token
    if token == 'token_par_izq':
        match('token_par_izq')
        E()
        OPMUL()
        EMUL()
        match('token_par_der')
    elif token == 'token_integer' or token == 'token_float' or token == 'id':
        E()
        EMULP()
    else:
        print("Error EMUL")

def EMULP():
    global token
    if token == 'token_div' or token == 'token_mul' or token == 'token_mod':
        OPMUL()
        EMUL()
    elif token == 'token_integer' or token == 'token_float' or token == 'id' or token == 'eol':
        pass
    else:
        print("Error EMULP")

def OPMUL():
    global token
    if token == 'token_div':
        match('token_div')
    elif token == 'token_mul':
        match('token_mul')
    elif token == 'token_mod':
        match('token_mod')
    else:
        print('Error OPMUL')

def E():
    global token
    if token == 'token_integer':
        match('token_integer')
    elif token == 'token_float':
        match('token_float')
    elif token == 'id':
        match('id')
        EP()
    else:
        print('Error E')

def EP():
    global token
    if token == 'token_mul' or token == 'token_div' or token == 'token_mod' or token == 'token_par_der' or token == 'token_menos' or token == 'token_mas' or token == 'token_menor' or token == 'token_mayor' or token == 'token_mayor_igual' or token == 'token_menor_igual' or token == 'token_igual_num' or token == 'token_diff_num' or token == 'token_and' or token == 'token_or' or token == 'eol' or token == 'token_mas ' or token == 'token_par_izq' or token == 'retorno':
        pass
    elif token == 'token_cor_izq':
        match('token_cor_izq')
        EARI()
        match('token_cor_der')
    elif token == 'token_point':
        match('token_point')
        match('id')
        E()

def BUCLE():
    global token
    if token == 'for':
        match('for')
        match('id')
        match('in')
        ARRAY()
        match('token_llave_izq')
        BLOCK()
        match('token_llave_der')
    else:
        print("Error BUCLE")

def IF():
    global token
    if token == 'if':
        match('if')
        match('token_par_izq')
        BB()
        match('token_par_der')
        ELSE()
    else:
        print("Error IF")

def ELSE():
    global token
    if token == 'else':
        match('else')
        ELSEP()
    elif token == 'token_llave_der' or token == 'token_par_izq' or token == 'retorno':
        pass
    else:
       print("Error ELSE")

def ELSEP():
    global token
    if token =='if':
        IF()
    elif token == 'token_llave_der' or token == 'token_par_izq' or token == 'retorno':
        pass
    else:
        print("Error ELSEP")

def WHILE():
    global token
    if token == 'while':
        match('while')
        match('token_par_izq')
        BB()
        match('token_par_der')
        match('eol')
        BLOCK()



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
        print('\n token:'+token)

def errorSintaxis(espectedToken):
    a = 1

PROGRAMA()