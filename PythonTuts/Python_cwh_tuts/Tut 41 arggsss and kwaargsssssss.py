def fungi(*anant, **hij):
    for item in anant:
        print(item)
    for key, value in hij.items():
        print(f" {key}: {value} ")

gadarinsaan = ["idk", "sussy baka", "bhindi ki sabji", "allu ka paratha", "haram khor bande"]
pig = {"Anant": "The best coder insaan",
       "GG": "chomu insaan"}
fungi(*gadarinsaan, **pig)



