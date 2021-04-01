# a simple evaluation of prefix and postfix notation

def evaluate(a, b, op):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '*':
        return int(a) * int(b)
    elif op == '/':
        return int(a) / int(b)

def post_fix(expre):
    lst = expre.strip().split(' ')
    stack = []
    # if the expression is not valid (at min: 2 operands, 1 operator)
    if len(lst) < 3:
        return

    # if the given expression and the method is not applicable, simply reverse the list
    elif not lst[0].isdigit():
        lst.reverse()

    # if the given expression is valid
    for num in lst:
        # if it is an operand, append to stack
        if num.isdigit():
            stack.append(num)
        else:
            # returns None if it detects an error, usually if the expression is not valid
            try:
                num2 = stack.pop()
                num1 = stack.pop()
                operator = num
                stack.append(evaluate(num1, num2, operator))
            except IndexError:
                return None
    return stack.pop()


def pre_fix(expre):
    # reverse the string and apply post-fix calculation
    my_str = expre[::-1]
    return post_fix(my_str)

def solve():
    ans = 0
    # user prompt
    expression = input('Enter the expression to be evaluated: ')
    choice = input('Choose from below the method:\n\t1. Pre-fix\n\t2. Post-fix\n\tWhat is your choice?: ')

    # choose what method to apply
    if choice == '1':
        ans = pre_fix(expression)
    elif choice == '2':
        ans = post_fix(expression)

    # results prompt
    print(f'Done evaluating.\n{expression.strip()} = {ans}') if ans is not None else print('Invalid expression.')


if __name__ == '__main__':
    solve()