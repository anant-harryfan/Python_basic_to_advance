# “A set is a data structure, having unordered, unique, and unindexed elements.”
s = set()
# print(type(s))
s.add(1)  # by this we can add item to set
s.add(1)  # agar tu sochta hai ki 2 bar print ho jaega isse to tu galat hai, set me bas unique value store hote hai
s.add(2)  # ye ho jaega
# print(s)
# sl = s.union({1, 2, 3})
sl = s.intersection({1, 2, 3})  # common lelega 2no me se
print(s, sl)
# min max esse esse wale bhi ho sakte hai slicing me hamne dekha tha or ye iske purane wale file me jo hai na usme bhi ho sakta 1-2 ko chhod ke, remove wala bhi chalega
sf = {1}
print(s.isdisjoint(sf)) # batata hai ki sf or s me kuch same hai ki nahi


la = [1, 2, 3, 4]
abc = set(la)
# print(abc)
