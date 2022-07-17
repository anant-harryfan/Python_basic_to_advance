# def minus(a, b):
#     return a - b
#
# print("Done by function", minus(19, 10))
#
#
# # this same thing can be done by lambda
#
# # lambda is a function which work without function(do same thing which is done by function)
#
# minuss = lambda x, b: x - b
#
# print("Done by lambda function", minuss(19, 10))


# a = [[6, 24], [5, 6], [8, 23]]
# a.sort(key=lambda x: x[0])        # 0 se sabse(comma) phele wala se sort hoga or 1 se comma ke bad wala se sort hoga
# print(a)

# n = [["🥚"], ["🐔"]]       # aaj prove ho gaya ki murgi phele aaye phir anda
#
# n.sort()
# print(n)


"""
Python List sort():
Sorting means arranging data systematically. If the data we want to work with is not sorted, we will face problems finding the desired element.

The Python language, like other programming languages, can sort data.

Python has an in-built method i.e. sort(), which is used to sort the elements of the given list in a specified ascending or descending order. There is also a built-in function i.e. sorted(), that builds a new sorted list from an iterable like list, dictionary, etc.

The syntax of the sort() method is:

list.sort(key=myFunc ,reverse=True|False)
"""
"""
Parameter Values:-
Parameters

Values

key

In the key parameter, we specify a function that is called on each list element before making comparisons. 

reverse

This is optional. False will sort the list in ascending order, and true will sort the list in descending order.

Default is reverse=False.

 

Sort() does not return any value, but it changes from the original list.

"""

