# dictionary hoti hai na vaise hi dictinory py me bhi hota hai bas cheeze tum define karte ho
dic1 = {}  # dictionary banana hai to {} yer wala bracket banana padega    or abhi ye ek empty dic hai
# print(type(dic1))  # ye dict karega print matlab dictinory
dic2 = {
    "anant": "The best coder",
    # "anant": "infinity", # ese karke override kar sakte
    "Programming": "A way to talk to a computer",
    "ek or dic": {1: "a", 2: "b", 3: "c"}
}
# dic2["ankit"] = "mera dost"  # ese ham bad me bhi cheeze add kar sakte
# print(dic2)  # pura dic print karega
# print("The meaning of anant is","\"", dic2["anant"],"\"")  # ab jo mane : iske bad likha hai na anant me vo print ho jaega
# print(dic2["ek or dic"])  # esse karke ek or dic print ho jaega
# print(dic2["ek or dic"][1])  # esse karke dusre dic ka bhi info le sakte

# ab dekh ankit kamine ne tujhe bola oe mc bc bhosadiwale tu ek programmer nahi hai mujhe hatta apni dic se to tu ye use karega
# del dic2["ankit"]

# ab ham ye bhi kar sakte
dic3 = dic2 # note ye ek nayya dic3 nahi banata ye ussi ko ref karta, isme change karge to dic2 me bhi ho jaega
# del dic3["ek or dic"] # dic 2 me bhi dlt or dic3 me bhi
# isse bachane ke liye esa likhna chahiye
dic3 = dic2.copy()
del dic3["ek or dic"]  # ab esa karega to d2 me kuch farak nahi padega
# print(dic3)
# dic2.update({"Harry": "The best teacher"})  # ese ham bad me bhi cheeze add kar sakte
# print(dic2.keys())  # jo keys hai na : iske phele type hai vo print ho jaega
print(dic2.items())  # jo item hai na : iske phele bad type hai vo sabh print ho jaega
print(dic2)
