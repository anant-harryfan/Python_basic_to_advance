# dic banana hai usme kya karna hai ki user se bhhot sare input lene hai or jabh vo puche ki iska matlab kya hai tabh vo usse print kar vade
# or iske alava ye kar

# ek quiz jaisa bana user se q puch (unse hi input karva lena) or uske hisabh se ans de dic ki madat se or matlab user ko batana sahi galat

# quiz -> 1. question 2. ans
# question -> samne wale ne input diya to usse print karvao or ek dictionary me store kardo or jabh user puchhe tell the question to usme se randomly koisa bhi quetion puchle (or sabh mcq form me)
# mcq me kya karna hai -> q jabh likhe pura to enter marne ke bad comp print kare what should be a,b,c,d or phir if else me dalke kar le ki sahi hai to sahi print kare galat hai to galat ke sath sath ans bhi print kare
# max question 5 hone chahiye
# ans me kya karna -> dic me q:ans esa save karna hai to jabh user ans ka puche to dic ki property use karke hi print karva

# 1st step hai apna user se input karke dic me store karvaan hai or ans bhi store karvana hai
print("Enter the question")
q1 = input()
print("Enter the mcq")
print("a -")
a = input()
print("b -")
b = input()
print("c(this should be the ans) -")
c = input()
print("d -")
d = input()
correct_ans = input("What should be ans\n")
print("Enter 2nd question")
q2 = input()
print("Enter the mcq")
print("a(this should be the ans) -")
a2 = input()
print("b -")
b2 = input()
print("c -")
c2 = input()
print("d -")
d2 = input()
correct_ans2 = input("What should be ans\n")
print("Quiz Question")
quiz = {q1: {a, b, c, d}, q2: {a2, b2, c2, d2}}
print(quiz)

ans = input("What should be the ans a, b, c, d\n in first question\n")
if ans == correct_ans:
    print("Your Ans is correct")
else:
    print("You failed")
ans1 = input("What should be the ans a, b, c, d\n")
if ans1 == correct_ans2:
    print("Your Ans is correct")
else:
    print("You failed")