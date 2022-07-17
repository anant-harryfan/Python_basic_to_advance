import time
# def searcher():
#     book = "This is anant who knows python and web developer"
#     time.sleep(4)
#
#     while True:
#         text = (yield)
#         if text in book:
#             print("Your text is in the book")
#         else:
#             print("Text is not in the book")
#
# search = searcher()
# next(search)
# search.send("anant")
# search.close()
# # input("kuch bhi\n")
# search.send("anantfdsfssfd")
# input("kuch bhi\n")
# search.send("anantsfdsdf")
# input("kuch bhi\n")
# search.send("python")

# exercise
def name_searcher():
    names = "anant harry carry trigger ashish abhuday rohan haris"
    time.sleep(4)

    while True:
        text = (yield)
        if text in names:
            print("Your name is in this list")
        elif text not in names:
            print("Your name is not in this list")


print("Collecting name list")
my_name = name_searcher()
next(my_name)
n = int(input("How many name you want to search\n"))
for _ in range(n):
    nama = input("Enter your name here\n")
    my_name.send(nama)