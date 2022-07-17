import time
from functools import lru_cache
import random

# @lru_cache(maxsize=32)
# def some_work(n):
#     #Some task taking n seconds
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("Now running some work")
#     some_work(3)
#     some_work(1)
#     some_work(6)
#     some_work(2)
#     print("Done... Calling again")
#     input()
#     some_work(3)
#     print("Called again")

cache = int(input("How many files you want to cache\n"))
rand = random.randint(0, 5)
@lru_cache(maxsize=cache)
def cahe():
    time.sleep(rand)
if __name__ == '__main__':
    for i in range(cache):
        lis = [i for i in range(cache)]
        cahe()
        print(lis[i])
        cahe()
        print("Phataphat hoga")
        


