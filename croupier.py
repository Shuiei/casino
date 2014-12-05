# -*-coding:Utf-8 -*
__author__ = 'shuiei'
import user
import random


def courpier():
    number = user.user_number()
    if number == False:
        return False
    bet = user.user_bet()
    if bet == False:
        return False
    else:
        print("Les jeux sont faits")
        rand = coup_nb()
        result = win_or_not(bet, rand)
        price = gain(result, bet)
        print("Vous gagner donc", price)


def coup_nb():
    rand = random.randrange(50)
    if rand % 2 == 0:
        print("Le tirage est ", rand, " Rouge Pair")
    else:
        print("Le tirage est: ", rand, " Noir Impair")
    return rand


def win_or_not(user_input, rand):
        if user_input == rand:
            print("Bon Numero, gain 3x la mise")
            return 2
        if user_input % 2 == 0 and rand % 2 == 0:
            print("Mauvais numéro Bonne Couleur")
            return 1
        else:
            print("Mauvaise couleur, mauvais numéro")
            return 0

def gain(gain, bet):
    if gain == 2:
        return (bet * 3) + bet
    if gain == 1:
        return (bet / 2 ) + bet
    if gain == 0:
        return 0