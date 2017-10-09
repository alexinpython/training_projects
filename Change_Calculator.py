# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:29:04 2017

@author: alexinpython
"""

## A program to calculate how much change is needed after a purchase and what
## coins will make up that change.
## from: https://www.reddit.com/r/beginnerprojects/comments/19jkn8/project_change_calculator/


# Variables
again = 'yes' #whether the user wants to use the program again
coin_v = [0.25, 0.10, 0.05, 0.01] #values of quarter, dime, nickle, penny


# Function
def coin(amount):
    """
    amount = float, change from user entered purchase
    
    breaks down amount into coins by subtracting them from amount
    """
    for i in range(len(coin_v)):
        while round(amount, 2) >= coin_v[i]:
            coin_n[i] += 1
            amount -= coin_v[i]
    return coin_n


# Start of program
print('This program calculates the change from a purchase and what coins '
      'you\'ll need to equal that change.')

while again == 'yes':
    coin_n = [0, 0, 0, 0] #holds number of coins needed to make amount
    price = float(input('Please enter the price of the item: '))
    money = float(input('Please enter the amount of money received: '))
    amount = round(money - price, 2) #change from purchase
    coin(amount)
    print('You need {} quarters, {} dimes, {} nickles, and {} pennies '
                 'to make ${}.' .format(coin_n[0], coin_n[1], coin_n[2], 
                           coin_n[3], amount))
    again = input('Would you like to enter another amount? yes, no: ')
            
print('Thanks for using my program!')
