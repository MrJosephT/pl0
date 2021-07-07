import re
from vocabulary import *
def Lexical(text):
    token = []
    i = 0
    while(i < len(text)):
        ch = text[i]
        if re.match('\s',ch):
            i += 1
            continue
        elif re.match('[a-z]|[A-Z]',ch):
            A = ch
            i += 1
            while(re.match('[a-z]|[A-Z]|[0-9]',text[i])):
                A = A + text[i]
                i += 1
            if A in basic:
                token.append(('basic',basic[A]))
            else:
                token.append((A,'ident'))
        elif re.match('[0-9]',ch):
            A = ch
            i += 1
            while (re.match('[0-9]', text[i])):
                A = A + text[i]
                i += 1
            token.append((A,'number'))
        else:
            if ch in bounder:
                token.append(('bounder',bounder[ch]))
                i += 1
            elif ch in operator or ch == ":":
                A = ch
                i += 1
                while (text[i] in operator or text[i] == ':'):
                    A = A + text[i]
                    i += 1
                token.append(('operator', operator[A]))
    return token


