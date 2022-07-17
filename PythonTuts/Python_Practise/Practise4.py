# Problem Statement:-
# A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
# 676, 616, mom, 100001.
#
# You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.
#
# Input:
# 3
# 45
# 10
# 2133
# Output:
# Next palindrome for 451 is 454
# Next palindrome for 10 is 11
# Next palindrome for 2311 is 2222

# user se mangna ki kitne number ke palindrome chahiye
k = int(input("Enter how many number you want to check\n"))
for j in range(k):
    try:
        num = int(input("Enter the number \n"))
        for _ in range(num, num*10):   # mane * 10 isliye kiya kyoki itne me to mil hi jaega palindrome
            str_num = str(_)
            # reverse list or sidhi list same hai ki nahi ye dekhta
            pali = str_num[::-1] == str_num
            if not pali:
                _ = _ + 1
                # print(_)
            if pali:
                if num == _:
                    print("This number is itself a palindrome")
                else:
                    print(f"The next palindrome near {num} is {_}")
                break
    except:
        print("This can't be iterate")