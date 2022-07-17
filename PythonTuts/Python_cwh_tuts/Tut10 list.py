market = ["Chocleet", "bug killer", "bhindi", "idk", 12]   # array jaisa hai oyhton me list bana diya
number = [1, 26, 2, 4543, 4, 4545, 100]
# number[1] = 122   # we can do like this
# print(number)
# # print(market)
# # print(market[3])  # slicing jaisa hai
# print(market[0:4])   # pichle wale me ja samjha ya hai
# print(market[:])   # pichle wale me ja samjha ya hai
# print(market[::])
# sabh vaisa ka vaisa hai
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
# market.append("I am anaNT")
# # print(market.clear())
# # print(market.copy())
# # print(market.count("bug killer"))
# market.extend("1")
# # print(market.index("Chocleet"))
# market.insert(1, "anant")
# market.pop(1)
# # market.remove(12)
# market.reverse()
# number.sort()
# print(number)
# print(market)


# 1. Mutable - can change
# 2. Immutable - cannot change

# TUPPLE IS A IMUTABLE OBJECT
# tp = (1,2,3)
# tp = (1,)  # to make a single thing tupple you have to put a comma after that number otherwise tupple will not be created
# print(tp)

a = 34
b = 45
a, b = b, a

print("A =", a, "\nB =", b)