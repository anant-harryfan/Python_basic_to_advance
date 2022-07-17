# time table banana hai user se input leke
# ki dalna hai "When you done with any of time table thing just see how you have to type after that" -> "i have done with [work] now tell my rest of the time table"
# user bolega ki "i have done with cooking now tell my rest of the time table"
# to ab usse vo kam chhodh ke bachha hua time table batana hai or agar jo usne likha hai vo time table me nahi hai(input jo diya tha) to batana hai ki nahi hai time table me


def TableRemove(k):
    j = "i have done with work"
    h = input()
    if h == j:
        timeTable.remove(k)
        for workss in timeTable:
            print(workss, end=", ")
        print("This is your time table")
work1 = input("Work-1\n")
work2 = input("Work-2\n")
work3 = input("Work-3\n")
work4 = input("Work-4\n")
work5 = input("Work-5\n")
work6 = input("Work-6\n")
timeTable = [work1,  work2,  work3,   work4,  work5,  work6]
for workss in timeTable:
    print(workss, end=", ")
print("This is your time table")
print("\ni have done with work, to remove thing from timetable")

TableRemove(work1)
TableRemove(work2)
TableRemove(work3)
TableRemove(work4)
TableRemove(work5)
TableRemove(work6)