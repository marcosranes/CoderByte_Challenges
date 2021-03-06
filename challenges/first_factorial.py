"""
    expected:
    >>> for f in range(1, 19):
    ...     f"{f}!  =>  {first_factorial(f)}"
    '1!  =>  1'
    '2!  =>  2'
    '3!  =>  6'
    '4!  =>  24'
    '5!  =>  120'
    '6!  =>  720'
    '7!  =>  5040'
    '8!  =>  40320'
    '9!  =>  362880'
    '10!  =>  3628800'
    '11!  =>  39916800'
    '12!  =>  479001600'
    '13!  =>  6227020800'
    '14!  =>  87178291200'
    '15!  =>  1307674368000'
    '16!  =>  20922789888000'
    '17!  =>  355687428096000'
    '18!  =>  6402373705728000'
"""

"""
First Factorial
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: 
if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 
18 and the input will always be an integer.
Examples
Input: 4
Output: 24
Input: 8
Output: 40320
"""


def first_factorial(num: int) -> int:

    # code goes here
    for ff in range(num-1, 1, -1):  # ff =  7  6  5  4  3  2
        num *= ff
    return num


# keep this function call here
if __name__ == '__main__':
    print(first_factorial(4))  # 24
    print(first_factorial(8))  # 40320
