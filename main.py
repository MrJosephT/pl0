from scanner import Lexical
from block import block
f = open('test2.txt')
text = f.read()
token  = Lexical(text)
for i in token:
    print(i)
stack = ['程序']
block(token ,stack)
