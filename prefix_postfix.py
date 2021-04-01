def evaluate(a, b, op):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '*':
        return int(a) * int(b)
    elif op == '/':
        return int(a) / int(b)

def pre_fix(expre):
    lst = expre.split(' ')
    stack = []
    for num in lst[::-1]:
        if num.isdigit():
            stack.append(num)
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            operator = num
            stack.append(evaluate(num1, num2, operator))
    else:
        print('Done evaluating.\n{} = {}'.format(expre,stack.pop()))

def post_fix(expre):
    lst = expre.split(' ')
    stack = []
    for num in lst:
        if num.isdigit():
            stack.append(num)
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            operator = num
            stack.append(evaluate(num1, num2, operator))
    else:
        print('Done evaluating.\n{} = {}'.format(expre,stack.pop()))

def solve():
    expression: str = input('Enter the expression to be evaluated: ')
    choice = input('Choose from below the method:\n\t1. Pre-fix\n\t2. Post-fix\n\tWhat is your choice?: ')
    if choice == '1':
        pre_fix(expression)
    elif choice == '2':
        post_fix(expression)

if __name__ == '__main__':
    solve()