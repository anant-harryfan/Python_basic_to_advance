# f = open("tut28 anant.txt", "w")
# f.write("Anant bhai sabka bhai, bhai bhai\n")
# f = open("tut28 anant.txt", "a")
# a = f.write("Bhai bhai ohho bhai bhai\n")
# print("The number of character are", a)
# f.close()

# handle read and write both
f = open("tut28 anant.txt", "r+")
print(f.read())
f.write("Anant bhai ka bhai ka bhai ka bhai hai ")
print(f.read())
print(f.read())

"""

MODES:

PURPOSE

“w” mode:

Here “w” stands for write. After opening or creating a file, a function, f.write() is used to insert text into the file. The text is written inside closed parenthesis surrounded by double quotations. There is a certain limitation to the write mode of the opening file that it overrides the existing data into the file. For a newly created file, it does no harm, but in case of already existing files, the previous data is lost as f.write() overrides it.   

“a” mode: 

“a” symbolizes append mode here. In English, appends mean adding something at the end of an already written document, and the same is the function the mode performs here. Unlike write mode, when we use "a" keyword, it adds more content at the end of the existing content. The same function i.e., f.write() is used to add text to the file in append mode. It is worth noting that append mode will also create a new file if the file with the same name does not exist and can also be used to write in an empty file. 

“r+” mode: 

At the beginning of the description, I told you that we would learn reading and writing a file simultaneously. Well, r+ mode is more of a combination of reading and append than read and write. By opening a file in this mode, we can print the existing content on to the screen by printing f.read() function and adding or appending text to it using f.write() function.
"""