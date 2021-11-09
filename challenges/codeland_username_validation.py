"""
    Tests:

    1. The username is between 4 and 25 characters.
    >>> codeland_username_validation("jon")   # 3 characters
    False
    >>> codeland_username_validation("john")  # 4 characters
    True
    >>> codeland_username_validation("johnjohnjohnjohnjohnjohn2")   # 25 characters
    True
    >>> codeland_username_validation("johnjohnjohnjohnjohnjohn26")  # 26 characters
    False

    2. It must start with a letter.
    >>> codeland_username_validation("20John")
    False
    >>> codeland_username_validation("John_Doe")
    True

    3. It can only contain letters, numbers, and the underscore character.
    >>> codeland_username_validation("John__1_2")
    True
    >>> codeland_username_validation("John@john")
    False
    >>> codeland_username_validation("John.12")
    False

    4. It cannot end with an underscore character.
    >>> codeland_username_validation("John12__")
    False
"""

"""
Codeland Username Validation
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a
valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.
Examples
Input: "aa_"
Output: false
Input: "u__hello_world123"
Output: true
"""


def codeland_username_validation(username: str) -> bool:

    # code goes here
    if 4 <= len(username) <= 25 \
            and username[0].isalpha() \
            and (username.isalnum() or "_" in username) \
            and not username.endswith("_"):
        return bool(username)
    return not bool(username)


# keep this function call here
if __name__ == '__main__':
    print(codeland_username_validation("aa_"))
    print(codeland_username_validation("u__hello_world123"))

    print(codeland_username_validation("__bbbbbbb"))                           # false
    print(codeland_username_validation("oooooooooooooooooo________a"))         # false
    print(codeland_username_validation("a______b_________555555555555aaaa"))   # false
