# Operators In Pythons
# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators

#Arithmetic Operators:
#Basic mathematical operations such as addition, multiplication, subtraction, division, etc. are performed with the help of arithmetic Operations. It contains nearly all operations that we can perform with the help of a calculator. Symbols for such operators include *, /, %, -, //, etc.
# Arithmetic Operators
# print("5 + 6 is ", 5+6)
# print("5 - 6 is ", 5-6)
# print("5 * 6 is ", 5*6)
# print("5 / 6 is ", 5/6) # bas int batata (. ke bad ka nahi batata)
# print("5 ** 3 is ", 5**3) # power batata hai
# print("5 % 5 is ", 5%5) # remainder batata
# print("15 // 6 is ", 15//6) # ye ekdam sahi value batata (point me batata)

# Assignment Operators:
# The assignment operator is used to assign values to a variable.
# In some cases, we have to assign a variable’s value to another variable, in such cases the value of the right operand is assigned to the left operand.
# One of the basic signs from which we can recognize an assignment operator is that it must have an equal-to(=) sign.
# Some commonly used assignment operators include +=, -=, /=, etc.
# Assignment Operators
# print("Assignment Operators")
# x = 5
# print(x)
# x += 7 # 7 + kardega x me
# x /= 7 # 7 / kardega x me
# x -= 7 # 7 - kardega x me
# x %=7 # x = x%7
# print(x)

# Comparison Operators:
# They are also known as relational operators.
# They compare the values on either side of the operator and decide the relation among them.
# Commonly used comparison operators include ==, >, < , >=,etc.
# Comparison Operators
# i = 5
# j = 2
# if j == i:
    # print("compared")
#
# Logical Operators:
# Logical operators perform logical AND, OR and NOT, operations. They are usually used in conditional statements to join multiple conditions. AND, OR and NOT keywords are used to perform logical operations.
# Logical Operators
a = True
b = False
# print(a and b)
# print(a is not b)

# Identity Operations:
# Identity operator checks if two operands share the same identity or not, which means that they share the same location in memory or different. “is” and “is not” are the keywords used for identity operands.
# Identity Operations
# print(5 is not 5)

# Membership Operands:
#  Membership operand checks if the value or variable is a part of a sequence or not. The sequence could be string, list, tuple, etc. “in” and “not in” are keywords used for membership operands.
# Membership Operators
anant = [3, 3, 2, 2, 39, 33, 35, 32]
# print(324 not in anant)

# Bitwise Operand:
# Bitwise operands are used to perform bit by bit operation on binary numbers. First, we have to change the format of the number from decimal to binary and then compare them using AND, OR, XOR, NOT, etc.
# Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

print(0 & 2)
print(0 | 3)