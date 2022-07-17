# x = 20  # global variable jo sabh jagaha chalega
# def rit():
#     x = 10  # ye bas function ke ander iski value define rahega
#     print("lol")
#     print(x)

# rit()
# print(x)  # yaha error(jabh x as a global variable define nahi kiya) dega kyoki rit ka x local variable tha
# isse ese samaj
# india me rs chalta hai or america me $ to ab bata rs kya america me chalega or $ kya india me chalega nahi na to ye dono ek local variable hai

# print(x)
# ab ye error nahi dega kyoki hamne define kar liya
# samaj india ne goshna ki sabh jagaha rs chalega to america me bhi rs chalega na tasbh vo ek global ho gaya
# america $ bhi use kar sakta koi manae nahi hai par agar $ mana kar diya (value nahi diya) to rs hi chalega

# p = 56
# print(p)
#
#
# def rty():
    # p = 45  # agar tu soch raha tune ye globally change kiya hai to tu galat hai
    # print(p)
    # global p
    # p = 45  # ab change ho jaega kyoki python ke keyword(global) ne is function ko anumati dedi
    # print(p)

# rty()
# print(p)

def harry():
    x = 20

    def rohan():
        global x
        x = 88  # ye change nahi karega kyoki- x abhi harry function ka local variable hai global nahi hai
    print("before calling rohan()", x)  # same output rahega
    rohan()
    print("after calling rohan()", x)  # same output rahega

harry()
print(x)  # kyoki usse koisa global variable nahi mila to function ke ander ka hi x global bana diya
