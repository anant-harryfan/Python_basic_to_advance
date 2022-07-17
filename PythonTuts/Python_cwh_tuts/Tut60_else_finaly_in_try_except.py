
f1 = open("tut54_lended_book")

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:  # ye run hoga koi isse rok nahi sakta chahe pura code hi kyo na hil jae
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")
