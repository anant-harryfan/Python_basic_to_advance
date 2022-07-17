def gen(n):
  for num in range(n):
    yield num

g = gen(51)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__()) # it will show error because we gen only 5 numbers and in this we try to gen more than five (0,1,2,3,4) these are 5 number

# for i in g:
#   print(i)

# h = "anant"
# ier = iter(h)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# we can itrate a string but we cannot do this with numbers

# quiz - make a Fibonacci series with generator
# 0 1 1 2 3 5 8 13

inn = int(input('Give amount: '))
def fib(n):
  inn, c = 0, 1
  for _ in range(n):
    yield inn
    inn, c = c, inn + c

if inn == 0 or inn == 1:
  print(0)
elif inn > 1:
  print(list(fib(inn)))