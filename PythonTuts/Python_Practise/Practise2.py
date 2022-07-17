# Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. These “n” number of apples is provided to harry by his friends, and he can request for few more or a few less apples.
#
# You need to print whether a number is in range mn to mx, is a divisor of “n” or not.

# Input:
#
# Take input n, mn, and mx from the user.
#
# Output:
# Print whether the numbers between mn and mx are divisors of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.
#
# Example:
# If n is 20 and mn=2 and mx=5
#
# 2 is a divisor of20
#
# 3 is not a divisor of 20
#
# …
#
# 5 is a divisor of 20
try:
    n = int(input("Enter the number of apples\n"))
    mn = int(input("Enter the minimum number of student\n"))
    mx = int(input("Enter the maximum number of student\n"))
except ValueError:
    print("No string pls")
    exit()

if mn >= mx:
    print("minimum can't be more or bigger than maximum")
for _ in range(mn, mx+1):
    if n % _ == 0:
        print(f"{_} is divisor of {n}")
    else:
        print(f"{_} is not divisor of {n}")