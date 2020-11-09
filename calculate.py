in_num = input("식을 입력하시오:(띄어쓰기 필수)").split()
operator = ["+", "-", "*", "/", "(", ")"]
postfix = []
stack = []

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def post_fix(*args):
    for arg in args:
        if arg not in operator:
            arg=int(arg)
            postfix.append(arg)
        else:
            if len(stack)==0:
                stack.append(arg)
            else:
                operator_value=operator_num(arg)
                stack_value=operator_num(stack[-1])
                if oerpator_value > stack_value:
                    if operator_value == 4:
                        while True:
                            postfix.append(stack.pop())
                            if stack[-1]=="(":
                                stack.pop()
                                break
                    else:
                        stack.append(arg)
        elif operator_value < stack_value:
            if stack[-1] == '(':
                stack.append(arg)
            else:
                while len(stack)>0:
                    if stack[-1] == 3:
                        break
                    postfix.append(stack.pop())
                stack.append(arg)
        elif operator_value == stack_value:
            if stack_value ==3 :
                stack.append(arg)
            else:
                postfix.append((stack.pop()))
                stack.append(arg)
    while len (stack)>0:
        postfix.append(stack.pop())
    return postfix

def calculator_function(*args):
    while len(postfix) >1 :
        for operate in args:
            if operate in operator:
                arg_index= postfix.index(operate)
                print("후위식:",end='')
                print(postfix)
            if operate == "+":
                    postfix.pop(arg_index)
                    result = add(postfix.pop(arg_index - 1), postfix.pop(arg_index - 2))
                    postfix.insert(arg_index - 2, result)

                elif operate == "-":
                    postfix.pop(arg_index)
                    result = minus(postfix.pop(arg_index - 1), postfix.pop(arg_index - 2))
                    postfix.insert(arg_index - 2, result)

                elif operate == "*":
                    postfix.pop(arg_index)
                    result = multi(postfix.pop(arg_index - 1), postfix.pop(arg_index - 2))
                    postfix.insert(arg_index - 2, result)

                elif operate == "/":
                    postfix.pop(arg_index)
                    result = divide(postfix.pop(arg_index - 1), postfix.pop(arg_index - 2))
                    postfix.insert(arg_index - 2, result)
            else:
                continue

    return postfix

print(post_fix(*in_num))
print(calculator_function(*postfix))