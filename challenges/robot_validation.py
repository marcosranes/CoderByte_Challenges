import sys
import re


def username_validation() -> bool:

    # code goes here
    trigger1 = trigger2 = 0
    while True:
        try:
            if trigger1 == 3:
                print("""
    1. Are you a robot?
    2. If it's a mistake, please type:
         "  I'm not a robot  "
                """)
                robot = ""
                while not robot == "I'm not a robot":
                    robot = input("Type: ")
                    if robot == "I'm not a robot":
                        print("""
         "  You've passed!  "
                        """)
                        trigger1 = 0
                    else:
                        trigger2 += 1
                        if trigger2 < 4:
                            print("""
         "  Consider typing:  I'm not a robot  " 
                            """)
                        else:
                            print("""
         "    Shutting down application...     " 
                            """)
                            sys.exit()
            user = input("Username: ")
        except ValueError:
            """
            In handling on strings, there's no way to fall down here, once any inputted data can be read as
            a character, no matter what is inserted. So, exceptions will be treated in the "else" block.
            """
            pass
        else:
            if 4 <= len(user) <= 25 \
                    and user[0].isalpha() \
                    and re.match("^[a-zA-Z0-9_]*$", user) \
                    and not user.endswith("_"):
                break
            else:
                print(not bool(user))
                print(
                    """
    1. The username is between 4 and 25 characters.
    2. It must start with a letter.
    3. It can only contain letters, numbers, and the underscore character.
    4. It cannot end with an underscore character.
                    """)
                trigger1 += 1
    return bool(user)


# keep this function call here
if __name__ == "__main__":
    print(username_validation())
