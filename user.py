# -*-coding:Utf-8 -*
__author__ = 'shuiei'

def user_number():
    user = input("Veuillez saisir un numero compris entre 0 et 49: ")
    if isinstance(user, int):
        return user
    else:
        print("Numero saisie incorrect.")
        user_number()

def user_bet():
    user = input("Veuillez saisir votre mise:  ")

    if isinstance(user, int):
        return user
    else:
        print("Veuillez saisir un nombre.")
        user_bet()
