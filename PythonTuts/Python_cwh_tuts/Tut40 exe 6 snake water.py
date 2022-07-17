import random
import pyttsx3
com_chance = ["snake", "water", "gun"]
i = 1
com_win = 0
user_win = 0
draw = 0
friend = pyttsx3.init()
while i <= 10:
    user_chance = input("Enter snake or water or gun\n")
    a = random.choice(com_chance)
    draw_say = f"computer move is {a} and your move is {user_chance} \nits a draw"
    win_say = f"computer move is {a} and your move is {user_chance} \nyou win"
    lose_say = f"computer move is {a} and your move is {user_chance} \nYou lose"
    # print(a)
    if a == "snake" and user_chance == "snake" or a == "water" and user_chance == "water" or a == "gun" and user_chance == "gun":
        print(f"computer move is {a} and your move is {user_chance} \nits a draw")
        friend.say(draw_say)
        friend.runAndWait()
        friend.stop()
        draw = draw + 1
        i = i + 1
        # print(a)
    elif a == "snake" and user_chance == "water" or a == "water" and user_chance == "gun" or a == "gun" and user_chance == "snake":
        print(f"computer move is {a} and your move is {user_chance} \nYou lose")
        com_win = com_win + 1
        i = i + 1
        friend.say(lose_say)
        friend.runAndWait()
        friend.stop()
        # print(a)
    elif user_chance == "snake" and a == "water" or user_chance == "water" and a == "gun" or user_chance == "gun" and a == "snake":
        print(f"computer move is {a} and your move is {user_chance} \nYou win")
        user_win = user_win + 1
        friend.say(win_say)
        friend.runAndWait()
        friend.stop()
        i = i + 1
        # print(a)
    else:
        print("Tere bap ka raj nahi chal raha kuch bhi dale ja raha")
    if i == 10:
        print(f"Computer points = {com_win}\nYour points = {user_win}\n Draw = {draw}")
        if com_win > user_win:
            print(f"Tere se ye hi ummed thi haar ke aayega\ncomputer win by {com_win - user_win} point")
        elif com_win < user_win:
            print(f"tujhse umeed nahi thi kaise jeet gaya \nYou win by- {user_win - com_win} point")
        break
