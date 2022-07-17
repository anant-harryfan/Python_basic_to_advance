# for ka USE Karke banana hai user list user se le or usse print karva

a = input("User Name\n")
b = input("User Name\n")
c = input("User Name\n")
d = input("User Name\n")

users = [a, b, c, d]
num = 1
for user in users:
    print(num, "User-", user)
    num = num+1