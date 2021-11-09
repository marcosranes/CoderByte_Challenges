"""
    expected:
    >>> arr = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    >>> find_intersection(arr)
    '1,4,13'
    >>> arr = ["1, 3, 4, 7, 13", "2, 5, 6, 14, 15"]
    >>> find_intersection(arr)
    False
"""

"""
Find Intersection
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will
represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string 
containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string 
false.
Examples
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13
Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10
"""


def find_intersection(str_arr: []) -> str:

    # code goes here
    list0 = str_arr[0].split(", ")  # ['1', '3', '4', '7', '13']
    list1 = str_arr[1].split(", ")  # ['1', '2', '4', '13', '15']

    inter_set = set.intersection(set(list0), set(list1))   # {'13', '4', '1'}
    inter_list = sorted(int(x) for x in inter_set)         # [1, 4, 13]
    str_list = list(str(s) for s in inter_list)            # ['1', '4', '13']
    str_list_join = ",".join(str_list)                     # 1,4,13

    return str_list_join if str_list_join else bool(str_list_join)


if __name__ == '__main__':
    # keep this function call here
    input1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    input2 = ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
    input3 = ["1, 3, 4, 7, 13", "0, 2, 5, 14, 15"]
    print(find_intersection(input1))  # 1,4,13
    print(find_intersection(input2))  # 1,9,10
    print(find_intersection(input3))  # False
