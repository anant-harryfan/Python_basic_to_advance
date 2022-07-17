import time
initial = time.time()  # print in second
# print(initial)


localtime = time.asctime(time.localtime(time.time()))
while True:
    timi = time.asctime(time.localtime(time.time()))  # apni bhasha me time ko banata
    time.sleep(1)  # make program to run after 2 sec(samaj 2 sec ke liye suladeta pure while loop ko / ya code ko jo given hai iske sath)
    print(timi)