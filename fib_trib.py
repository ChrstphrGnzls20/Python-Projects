import timeit
# Fibonacci sequence implementation using sum() function, a much easier approach
def fib(signature, n):
    for _ in range(n):
        # the sum() add the previous 2 numbers starting from 2nd to the last(-2)
        signature.append(sum(signature[-2:]))
    return signature[:n]

# Tribonacci sequence implementation using sum() function, a much easier approach
def trib(signature, n):
    for _ in range(n):
        # the sum() add the previous 3 numbers starting from 3nd to the last(-3)
        signature.append(sum(signature[-3:]))
    return signature[:n]


if __name__ == '__main__':
    x = 10
    # signature is the first terms in a sequence that differs in someway
    print(f'Fib({x}) = {fib([0, 1], x)}')
    print(f'Execution time: {timeit.default_timer()}')
    print(f'Trib({x}) = {trib([1, 1, 1], x)}')
    print(f'Execution time: {timeit.default_timer()}')
