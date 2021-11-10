"""
Bracket Matcher
Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly
matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))", then the output
should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match
up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.
Examples
Input: "(coder)(byte))"
Output: 0
Input: "(c(oder)) b(yte)"
Output: 1
"""


def bracket_matcher(exp):

    # code goes here
    stack = []
    for car in exp:
        if "(" in car or ")" in car:
            stack.append(car)  # "(coder)(byte))" => ['(', ')', '(', ')', ')']
    if stack[0] == ")":
        return "invalid syntax!"
    return int(len(stack) % 2 == 0)  # verifying the pairs


# keep this function call here
if __name__ == '__main__':
    print(bracket_matcher("(coder)(byte))"))    # 0
    print(bracket_matcher("(c(oder)) b(yte)"))  # 1

"""
It was done quickly, so...
in development yet.. the code requires some improvements...
the idea will be joining the couple of corresponding brackets "( )" and removing trough the .pop() method from
the stack[], then, resting only no-couple bracket(s), that in turn will be outputted when asking for the stack length.
And, it must cover the syntax with no brackets as well, which should return a casted int of True => 1.
"""
