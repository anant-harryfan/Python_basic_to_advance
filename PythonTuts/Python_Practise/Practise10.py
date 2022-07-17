import pyttsx3
from prettytable import PrettyTable
import pyfiglet
table = PrettyTable(["Item number", "Price"])

welcome = pyfiglet.figlet_format("WELCOME TO KIRANA STORE", font="digital")
print(welcome)

total = 0
tu = 1
while True:
    name = input("Enter the item\n")
    # 'q' to exit and print the table
    if (name != 'q'):
        price = int(input('Enter the Price:'))

        # store all the prices in 'total'
        total += price
        table.add_row([name, price])
        continue

    elif (name == 'q'):
        break
table.add_row(["______", "______"])
table.add_row(["TOTAL", total])
print(table)