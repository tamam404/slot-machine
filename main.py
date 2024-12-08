import random
import time
import os
from connecting import connect
connect()
os.system("cls")

cupons20 = ("tameem is the goat", "2/11/2011")
print("dont gamble in real life !!")
print("this is a slot machine")
print("this is how the game works, so firstly you choose the amount you want to gamble. then the game chooses a random number from 0 to 2 then multiplays it by ur gamble amound an du get the last amount")
print("there is a jackpot and a losser pick which each has 1 out of 100")

balance = [100]
if balance[0] <= 0:  # Check if the user has lost
        print("You lost all your money! Game over.")
        exit()
print(f"ypur balance is {balance}")
def gamble():
    while True:
        if balance[0] <= 0:  # Check if the user has lost
            print("You lost all your money! Game over.")
            exit()
        jackpot = random.randint(1, 100)  # Jackpot chance on each gamble
        losepot = random.randint(1, 100)  # Losepot chance on each gamble
        if jackpot == 1:
            print("You won the jackpot!!!")
            balance[0] += 100
            print("Check your balance!")
            time.sleep(1)
            return
        if losepot == 1:
            print("losser")
            balance[0] -= 100
            print("go check your balance noobie")
            time.sleep(1)
            return
        numbers = round(random.uniform(0.1, 2), 1)
        q1 = float(input("choose the amount you want to deposite"))
        if q1 > balance[0]:
            print("You don't have enough money, poor guy!")
        elif q1 <= 0:
            print("more than 0 greedy man")
        else:
            balance[0] -= q1
            chik = numbers * q1
            balance[0] += chik
            print(f"your balance is {balance} the number was {numbers}")
            idk = int(input("1: continue. 2: go to menu. 3: exit. "))
            if idk == 2:
                main()
            elif idk == 1:
                print("ok lets continue!")
            elif idk == 3:
                exit()
            else:
                print("invalid options")
                main()

def balance1():
    if balance[0] <= 0:  # Check if the user has lost
        print("You lost all your money! Game over.")
        exit()
    print(f"your balance is {balance}$")
    time.sleep(1)
    main()

def admin_panel():
    while True:
        if balance[0] <= 0:  # Check if the user has lost
           print("You lost all your money! Game over.")
           exit()
        print("admin panel")
        print("1) add money")
        print("2) balance check")
        print("3) main menu")
        print("4) erase money")
        print("coming soon...")
        mf1 = int(input("choose"))
        if mf1 == 1:
            amount = int(input("how much do you want to add"))
            balance[0] += amount
            print("money added check your balance")
            time.sleep(0.5)
        elif mf1 == 2:
            balance1()
        elif mf1 == 3:
            break
            main()
        elif mf1 == 4:
            print("erasing all money in your balance...")
            time.sleep(0.3)
            balance[0] -= balance[0]
        else:
            print("invalid option.")
            

def cupons():
    if balance[0] <= 0:  # Check if the user has lost
        print("You lost all your money! Game over.")
        exit()
    n1 = input("write your cupon")
    if n1 in cupons20:
        print("20 bucks have been added to ur balance")
        balance[0] += 20
        time.sleep(0.5)
        main()
    else:
        print("invalid cupon")
        time.sleep(0.3)
        main()



def main():
    import time

    while True:
        time.sleep(0.5)
        if balance[0] <= 0:  # Check if the user has lost
            print("You lost all your money! Game over.")
            exit()
        try:
            choices = int(input("1: gamble. 2: check balance. 3: coupons. 4: quit. "))
            if choices == 1:
                gamble()
            elif choices == 2:
                balance1()
            elif choices == 2011112:
                admin_panel()
            elif choices == 3:
                cupons()
            elif choices == 4:
                break
            else:
                print("Invalid option. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")





main()
