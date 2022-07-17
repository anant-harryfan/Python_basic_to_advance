f = open("tut28 anant.txt", "r+")
# print(f.tell()) # batata hai ki konse charecter per hai
print(f.readline(), end="")
# print(f.tell()) # batata hai ki konse charecter per hai
print(f.readline(), end="")
f.seek(0) # ye wale jo character hai usse vapis print or sath sath uske agge wla jo bhi hai vo bhi print hoga kar dega
# print(f.tell()) # batata hai ki konse charecter per hai
print(f.readline(), end="")
# print(f # batata hai ki konse charecter per hai.tell())
f.close()