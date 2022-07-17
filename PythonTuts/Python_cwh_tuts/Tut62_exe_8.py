## Oh soldier prettify my folder
import os
import time
# def soldier():
#
#     print("\t----Welcome----\nThis program will arrange all of your files")
#     time.sleep(2)
#     print("Requirements:- \n Make a text file and mention files"
#           "\n which we don't have to touch (for e.g:- folder_name.txt ) ")
#     time.sleep(3)
#     path=input("Enter the path to folder:-")
#     important_file=input("Enter file name in which you have \nmentioned files which we don't have to touch:- ")
#     format_file=input("Enter format in which you want to gave changes:- ")
#     try:
#         os.chdir(path)
#         number_of_files=1
#         with open(important_file) as f:
#             l = set(f.readlines())
#             directories = set(os.listdir())
#             #removing \n and making a set of file to arrange
#             g = [l.replace('\n', '') for l in l]
#             directories.difference_update(g)
#             directories.remove(important_file)
#             for old_name in directories:
#                 extentions=path + old_name
#                 extention = os.path.splitext(extentions)[1]
#                 formated="."+format_file
#
#                 if extention == formated:
#                     new_name = str(number_of_files) + formated
#                     os.rename(old_name, new_name)
#                     number_of_files += 1
#                 if extention not in formated:
#                     os.rename(old_name, old_name.lower())
#     except Exception as e:
#         print(f"Error!!!\n{e}")
#         print("Rerunning the program....")
#         time.sleep(3)
#         soldier()
# soldier()

# abhi khud ka bhi bana samjha na
def soldier():
    print("Welcome to ohh soldier, prettify my folder")
    print("Make a file which has file name which we don't have to shoot")
    time.sleep(3)
    path = input("Enter the path of folder we have to prettify\n")
    imp_file = input("Enter the file in which all file name given we don't have to shoot\n")
    for_file = input("Which file format we have to name in 1,2,3... .format\n")

    try:
        i = 1
        os.chdir(path)
        gg = os.listdir(path)
        with open(imp_file) as f:
            file_list = f.read().split("\n")
            # print(file_list)

        for file in gg:
            if file not in file_list:
                os.rename(file, file.capitalize())
            if os.path.splitext(file)[1] == for_file:
                os.rename(file, f"{i}{file}")
                i = i+1

    except:
        print("Error!!!")
        print("Restarting program...")
        soldier()

soldier()