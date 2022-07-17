# hamme karna ye hai ki jaise hi mane run kiya to vo mujhe time batae or jaise hi me likhu stop to vo kahe mummy ne itne time tak serial dekha aaj or vo fhir ek file me likha jae esa f"mummy ne aaj {time} dekha"
# map reduce filter sabh lagana hai try except jo bhi abhi tak sikha vo sabh use kar

import time
import datetime

def gettime():
    return datetime.datetime.now()


from datetime import datetime
timi = time.asctime(time.localtime(time.time()))
timii = datetime.now()

print(f"mummy ne is time pe chalu kiya serial\n{timi}")
stop = input()
if stop == "stop":
    timmmi = time.asctime(time.localtime(time.time()))
    timmi = datetime.now()
    print(f"mummy ne is bajhe khatam kiya {timmmi}")

    hour = timmi - timii
    h2 = int(hour.total_seconds()/60**2)
    f = open("6_mummy_serial.txt", 'a')
    f.write(f"in hour {h2}\n")
    f.close()
    print(f"in hour {h2}")

else:
    print("tere bap ka raj nahi hai shanti se stop likh pata karne ke liye")


