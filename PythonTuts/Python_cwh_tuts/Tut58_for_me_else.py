classs = ["Alexis Hogan", "Brandy Nichols", "Geraldine Joseph", "Ruby Peters", "Bryan Simon", "anant"]
nama = input("Enter the name of the student\n")
for names in classs:
    if nama in names:
        print(f"The role number of this student is {classs.index(nama) + 1}")
        break

else:
    print(f"There is no student named {nama} in this class")
# ye mane ese banaya hai ese hi varna samajta nahi
# agar for loop me break nahi hai ya vo achhe se end nahi hota tabh else ka use hota
# bina break ke vo for loop to print karega hi karega par uske sath else bhi print ho jaega