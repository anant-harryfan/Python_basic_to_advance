import requests
import pickle

try:
    data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
    # print(data)

    l1 = [item.split(",") for item in data.split("\n") if len(item) != 0]
    # print(l1)

    with open("Tut67_myiris", "wb") as f:
        pickle.dump(l1, f)

    a = input("If you want to see all the data type yes or type no\n")
    if a == "yes":
        with open("Tut67_myiris", "rb") as j:
            print(pickle.load(j))
except:
    print("Error!!!!!!!!!")