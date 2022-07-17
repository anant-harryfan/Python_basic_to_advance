i = 1

while True:
    if i < 5:
        i = i + 1
        continue
    # print(i, end=" ")
    if i >= 45:
        break
    i = i + 1

# quiz
while True:
    a = float(input("Enter the number \n"))
    if a > 100:
        print("Congo tu 100 cross kar diya")
        break
    else:
        print("Try Again")
        # continue
