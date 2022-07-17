ls = [i for i in range(100) if i % 3 == 0]
# print(ls)
ds = {i: f"item {i}" for i in range(1, 10)}
# print(ds)
ds2 = {value: key for key, value in ds.items()}
# print(ds2)

dres = {dress for dress in ["dress 1", "dress 2", "dress 1", "dress 2"]}  # iske ander agar ek jaise cheez hai to vo bas eek bar hi print karega us cheezz ko
# ye dictionary nahi set hai
# print(dres)
# typ = int(input("Enter the number you want to table \n"))
# gen = (i for i in range(1, typ*10+typ) if i % typ == 0)
# ye tuple nahi generator ban gaya yaha pe
# for item in gen:
    # print(item)

no_of_item = int(input("How many item you want to add\n"))
string_added = input("Write the item you want to add with ','\n")
items = string_added.split(", ")

if len(items) > no_of_item:
    print(f"You want to add {no_of_item} items but you added more than that")
elif len(items) < no_of_item:
    print(f"You want to add {no_of_item} items but you added less than that")
elif len(items) == no_of_item:
    compre = int(input("Which type of comprehension you use 1. List Comprehension 2.Dictionary Comprehension 3. Set Comprehension "))
    if compre == 1:
        lis = [i for i in items]
        print(lis, "\n", type(lis))
    elif compre == 2:
        sic = {f"item{i}": i for i in items}
        print(f"{sic} \n{type(sic)}")
    elif compre == 3:
        off = {of for of in items}
        print(f"{off}\n{type(off)}")
