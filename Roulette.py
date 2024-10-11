def spin():
    spin = random.randrange(0,37)
    
    return spin

import random
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
print("Welcome to Roulette!")
total = 0
instructions = 0

while (instructions != 'yes' and instructions != 'no'):
    instructions = input("Would you like to know how to play?")
    print()
    if (instructions != 'yes' and instructions != 'no'):
        print('Please type either "yes" or "no" to continue.')
        print()

if (instructions == 'yes'):
    print('The player will begin by making a bet. After the bet is made, a ball will be dropped on the spinning wheel. The player can bet that the ball will land on even numbers, odd numbers, red numbers, or black numbers. Each of these bets will result in an even money payout. The player can also bet on a specific number. This bet will have a payout of 35 to 1.')
    print()
    
while (total < 1000):
    total = int(input("Starting value: $"))
    if (total < 1000):
        print()
        print('Starting amount must be above $1000.')
        print()
print()
game = 'yes'
bet = 0
while (game == 'yes'):
    plt.title("Wheel")
    plt.xlabel("X pixel scaling")
    plt.ylabel("Y pixel scaling")
    
    redList = [3, 12, 7, 18, 9, 14, 1, 16, 5, 23, 30, 36, 27, 34, 25, 21, 19, 32]
    blackList = [26, 35, 28, 29, 22, 31, 20, 33, 24, 10, 8, 11, 13, 6, 17, 2, 4, 15]
    evenList = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    oddList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    image = mpimg.imread("Wheel.jpg")
    betType = 0
    bet = total + 1
    plt.imshow(image)
    plt.show()
    print("What would you like to bet on?")
    while (betType != 'red' and betType != 'black' and betType != 'even' and betType != 'odd' and betType != 'number'):
        betType = input( )
        print()
        if (betType != 'red' and betType != 'black' and betType != 'even' and betType != 'odd' and betType != 'number'):
            print('Select to bet on red, black, evens, odds, or type "number" to bet on a specific number.')
            print()
    if (betType == 'number'):
        betValue = -100
        while (betValue > 36 or betValue < 0):
            print()
            betValue = int(input('What number would you like to bet on? '))
            print()
            if (betValue > 36 or betValue < 0):
                print('Number must be between 0 and 36.')
                print()
    
    while (bet > total):
        bet = int(input("How much would you like to bet? $"))
        print()
        if (bet > total):
            print('Insufficient funds to make this bet.')
            print('Current total funds: $', total)
            print()
    
    value = spin()
    print('The ball has landed on ', value)
    print()
    
    if (betType == 'red'):
        if value in redList:
            total += bet
            print ('YOU WIN!')
        else:
            total -= bet
            print('You lose.')
            
    if (betType == 'black'):
        if value in blackList:
            total += bet
            print ('YOU WIN!')
        else:
            total -= bet
            print('You lose.')
            
    if (betType == 'even'):
        if value in evenList:
            total += bet
            print ('YOU WIN!')
        else:
            total -= bet
            print('You lose.')
            
    if (betType == 'odd'):
        if value in oddList:
            total += bet
            print ('YOU WIN!')
        else:
            total -= bet
            print('You lose.')
            
    if (betType == 'number'):
        if (value == betValue):
            total += bet * 35
            print ('YOU WIN!')
        else:
            total -= bet
            print('You lose.')
            
    print()
    print('Money left: $',total)
    print()
    
    game = 0
    if (total > 500):
        while (game != 'yes' and game != 'no'):
            game = input("Play again? ")
            if (game != 'yes' and game != 'no'):
                print()
                print('Type either "yes" or "no"')
                print()
        if (game == 'yes'):        
            print()
            print()
            print()
            print('NEW ROUND')
            print()
            bet = 0
    else:
        print("Must have at least $500 to continue.")
        print("Current balance: $", total)
        addMoney = input("Add money? ")
        if (addMoney == 'yes'):
            amountAdded = 0
            while (amountAdded < 1000):
                amountAdded = int(input('How much would you like to add? '))
                if (amountAdded < 1000):
                    print()
                    print('Must add more than $1000.')
                    print()
            print()
            print()
            print()
            print('NEW ROUND')
            print()
            game = 'yes'
        else:
            game = 'no'
    plt.clf()
    plt.title(' ')
    plt.show()