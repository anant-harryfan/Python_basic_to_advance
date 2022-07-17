# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~map~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# lis = ["23", "24", "25", "26"]
# tujhe agar sabhi num ko int me dalna to for loop chalana padhta jo bekar hai
# for item in range(len(lis)):
#     lis[item] = int(lis[item])
#     print(item, end=", ")

# iski jagaha ye kam aata
# lis = list(map(int, lis))
# lis = list(map(float, lis))
# print(lis)

# isse bhhot cheese ho sakta eg -
# num = [6, 5, 5, 4, 5, 5, 6545]
# square = list(map(lambda x: x*x, num))
# print(f"\n{square}")

# def squaree(x):
#     return x*x
# def cube(x):
#     return x*x*x
#
# math = [squaree, cube]
# for i in range(5):
#     val = list(map(lambda x: x(i), math))
#     print(val)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~filter function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def is_gr_than(num):
    return num > 5
li = [6, 5, 7, 4, 8, 2, 65]

gr_than_5 = list(filter(is_gr_than, li))
# print(gr_than_5)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Reduce~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
from functools import reduce
list = [4, 5, 6, 7, 8, 9, 2, 1, 3]
num = reduce(lambda c, d: c+d, list)
# print(num)

