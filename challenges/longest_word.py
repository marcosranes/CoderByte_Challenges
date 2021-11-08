"""
    expected:
    >>> longest_word('Hello world123 567')
    ['Hello', 'world123', '567']
    ['Hello', 'world', '']
    ('Hello', 5)

    >>> longest_word("fun&!! time")
    ['fun&!!', 'time']
    ['fun', 'time']
    ('time', 4)
"""
"""
Longest Word
Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If
there are two or more words that are the same length, return the first word from the string with that length. Ignore
punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
"""


def longest_word(sen):
    # code goes here
    if not len(sen.strip()):
        raise TypeError("Field mustn't be empty")

    list1 = sen.split()  # ['fun&!!', 'time']
    print(list1)
    alpha_only = []
    for word in list1:
        string = "".join(string for string in word if string.isalpha())
        alpha_only.append(string)
    print(alpha_only)

    long_word_length = len(alpha_only[0])
    current_word = alpha_only[0]
    for word in alpha_only:
        word_length = len(word)
        if word_length > long_word_length:
            long_word_length = word_length
            current_word = word

    return current_word, long_word_length


# keep this function call here
if __name__ == '__main__':
    print(longest_word("Hello world123 567"))  # ('Hello', 5)
    print(longest_word("fun&!! time"))         # ('time', 4)
    print(longest_word("I love dogs"))         # ('love', 4)
#    print(longest_word("       "))             # TypeError: Field mustn't be empty
    print(longest_word(""))                    # TypeError: Field mustn't be empty
