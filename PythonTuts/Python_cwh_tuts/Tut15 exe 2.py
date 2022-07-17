"""
Suppose that you are an invigilator in an exam. Calculator is not allowed for the exam. You discover somehow that students are planning to cheat in exam, using a calculator program in Python language. Somehow you get your hands on the calculator program and now you want to alter few results in calculator with your own provided results, so you can catch the students who are trying to cheat using the calculator program.

The user will provide the following inputs:

Operator
The two numbers, between which the operator is applied
All the results will be correct, except for these few:

45 * 3 = 555
56+9 = 77
56/6 = 4
"""

print("Enter Your 1st number")
num1 = int(input())
print("Enter Your 2nd number")
num2 = int(input())
print("What you have to do *,+,-,/")
op = input()

if num1 == 45 and num2 == 3 and op == '*':
    print("The ans of 45 * 3 = 145")
elif num1 == 56 and num2 == 9 and op == '+':
    print("The ans of 56 + 9 = 67")
elif num1 == 56 and num2 == 6 and op == '/':
    print("The ans of 56 / 6 = 9.7")
elif op == '*':
    ans = num1*num2
    print("The ans of", num1, op, num2, "=", ans)
elif op == '+':
    ans = num1+num2
    print("The ans of", num1, op, num2, "=", ans)
elif op == '-':
    ans = num1-num2
    print("The ans of", num1, op, num2, "=", ans)
elif op == '/':
    ans = num1/num2
    print("The ans of", num1, op, num2, "=", ans)
else:
    print("Salle tere bap ka mal nahi hai ki kuch bhi dalega or me usse solve kar dunga")