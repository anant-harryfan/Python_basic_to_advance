# visit this  https://www.geeksforgeeks.org/json-load-in-python/


import json
# ye python ko javascript ke form me convert kar deta hai

data = '{"var1":"harry", "var2":56}'
print(data)

parsed = json.loads(data)
print(type(parsed))

#Task 1 - json.load?
# ye json file handling ke kam aata

data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)

# Task 2 = what is sort_keys parameter in dumps
# agar sort key true ho to ye us line ko js ke hisabh se convert kar deta jo ham usme challa sakte