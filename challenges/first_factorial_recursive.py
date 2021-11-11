def factorial_recursive(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    return num * factorial_recursive(num - 1)


if __name__ == '__main__':
    print(factorial_recursive(5))  # 120

"""
That seems simple. Isn't it? A recursive function needs a break condition, it ever ought to run inside a conditional
if/else block, in which IF will be the base case, i.e. the root of the problem, the recursion stop condition. If not..
run ELSE. So, the function in turn will call itself, regressing (num -1) or progressing (num +1) to the stop condition.
For example, given the function in which the stop condition (case base) is 100, the input ought to be below it, and 
once my input it's not equal to 100, ELSE, myfunction(num + 1) will be called and recalled and recalled until its case 
base alignment, i.e. if your input is 60 you'll have to go ahead and verify the first condition block (IF) in more 39 
times because 100 is your break point.

Note: The recursive solution isn't ever the most efficient solution when it requires a lot of system memory to be
resolved. For example...
Between the given three power functions below. For me, the most effective function begins with the last one.
"""


def calc_power1(num1, num2):
    if num2 == 0:
        return 1
    return num1 * calc_power1(num1, num2 - 1)


def calc_power2(num1, num2):
    return pow(num1, num2)


def calc_power3(num1, num2):
    return num1 ** num2


if __name__ == '__main__':
    print(calc_power1(4, 3))   # 64 'using a recursive solution to resolve'
    print(calc_power2(4, 3))   # 64 'calling for an internal Python method'
    print(calc_power3(4, 3))   # 64 'using system operators directly'
