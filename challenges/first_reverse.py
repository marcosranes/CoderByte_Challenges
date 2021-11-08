"""
    expected:
    >>> first_reverse("python language")
    'egaugnal nohtyp'
"""

"""
First Reverse
Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For
example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW 
olleH.

Examples
Input: "coderbyte"
Output: etybredoc
Input: "I Love Code"
Output: edoC evoL I
"""


def first_reverse(string: str) -> str:
    # code goes here
    return string[::-1]


# keep this function call here
if __name__ == '__main__':
    print(first_reverse("I Love Code"))
    print(first_reverse("coderbyte"))
