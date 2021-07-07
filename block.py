from lltable import table
def block(token ,stack):
    for i in token :
        blankword = "  "
        while stack[-1] != i[1]:
            while stack[-1] == 'ϵ':
                print(stack)
                stack.pop()
            if stack[-1] == '.':
                print('成功！！！')
                break
            if stack[-1] == i[1]:
                break
            str = table[stack[-1]][i[1]].split('->')
            str = str[1].split(' ')
            str.reverse()
            print(stack,'使用推导式 ： '+table[stack[-1]][i[1]])
            stack.pop()
            stack = stack + str
        print(stack)
        if stack[-1] == 'period':
            print('成功！！！')
            break
        stack.pop()




