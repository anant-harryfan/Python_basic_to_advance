import re

amu = '''Code With Harry is my attempt to teach basics and those coding techniques to people in short time which took me ages to learn. 
At Code_With_Harry@gmail.com, I provide a quick and to the point demo along with resources of anything and everything I teach. Source code and other resources are hosted on my website CodeWithHarry.com. I provide source code(if any) in the description of every video.
Quality programming videos in Hindi :)
anant@gmail.com
asfsd@ggas.fd
ffassad@f.dsfd
'''

nu = 1
emu = re.findall(r'[a-zA-Z0-9]+@[a-zA-z0-9]+[.][a-zA-Z0-9]+', amu)
f = open('Tut72_exe11_logs.txt', 'a')
for email in emu:
    print(f"{nu}. {email}")

    f.write(f"{nu}. {email}\n")
    nu = nu + 1

print("All email are store in Tut72_exe11_logs.txt file")
print(f"There are {nu-1} email in this extract")
f.write("\n")
f.close()
