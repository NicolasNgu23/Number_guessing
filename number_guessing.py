import random

user_top_number = input("Saisissez un numéro: ")

if user_top_number.isdigit():
    user_top_number = int(user_top_number)

    if user_top_number <= 0:
        print ("Saisissez un nombre plus grand la prochaine fois. ")
        quit()
else:
    print("Saisissez un nombre la prochaine fois.")
    quit()

number = random.randint(0,user_top_number)
score = 0

while True:
    score +=1
    user_number = input ("Devinez le numéro ")
    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print ("Saisissez un nombre la prochaine fois. ")
        continue

    if user_number == number:
        print("Bravo tu l'as eu ! ")
        break
    elif user_number > number:
            print("Vous êtes au dessus du nombre.")
    else:
             print("Vous êtes en dessous du nombre")

print("Ton score est", score)
