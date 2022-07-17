def lo(a, b):
    return print(f"hello {a} \nhello {b}")

# __name__ batata ki nam kya hai file ka (current file ho to __main__ batata)
print(__name__)  # ye run sabhi file me hoga (import karne me)
# agar ham chahete hai li ye wala function dusri file me import karne ke bad run na ho to isse if __name__ = '__main__' wali me dalte

if __name__ == '__main__':
    print(lo("pratush", "pagal"))  # to ye bas if file me run hoga or kisi me nahi