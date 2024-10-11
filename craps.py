def roll(): 
    dieOne = random.randrange(1, 7)
    dieTwo = random.randrange(1, 7)
    
    roll = dieOne + dieTwo
    
    return roll

import random

total = 0
go = 10
print('Welcome to Craps!')
while (total < 1000):
    total = int(input("Starting value: $"))
    if (total < 1000):
        print()
        print('Starting amount must be above $1000.')
        print()
print()
while (go != 0):
    print('There are several ways to bet, type the number of a bet you would like to know more about or type 0 to place your bet.')
    print('0.) BET')
    print('1.) Pass')
    print("2.) Don't Pass")
    print("3.) Come")
    print("4.) Don't Come")
    print('5.) Odds')
    print('6.) Place')
    print('7.) Field')
    print('8.) Low Dice')
    print('9.) High Dice')
    print()
    go = 100
    
    while (go > 9 or go < 0):
        go = int(input('Type a number to continue: '))
        print()
        if (go > 9 or go < 0):
            print("Please select a number between 0 and 9.")
            print()
    
    if (go == 1):
        print('A pass bet is an even money bet made on the first roll of the dice. On the first roll, if a 7 or 11 is rolled, you win the bet. However, if a 2, 3, or 12 is rolled, you lose the bet. If another number is rolled, this number becomes the point. If the point is rolled again before a 7 is rolled, you win. However, if the 7 is rolled first, you will lose the bet.')
    if (go == 2):
        print("A don't pass bet is an even money bet made on the first roll of the dice. On the first roll, if a 7 or 11 is rolled, you lose the bet. However, if a 2, 3, or 12 is rolled, you win the bet. If another number is rolled, this number becomes the point. If the point is rolled again before a 7 is rolled, you lose. However, if the 7 is rolled first, you will win the bet.")
    if (go == 3):
        print("A come bet is made after a point is etablished. On the next roll, you win on a 7 or 11 and lose on a 2, 3, or 12. Any other number becomes the come point. If this come point is rolled again before a 7 is rolled, you win the bet.")
    if (go == 4):
        print("A don't come bet is made after a point is etablished. On the next roll, you lose on a 7 or 11 and win on a 2, 3, or 12. Any other number becomes the don't come point. If this don't come point is rolled again before a 7 is rolled, you lose the bet.")
    if (go == 5):
        print("After a point is made, you may take the odds and win if the point is made before a 7. The payout depends on the number of the point.")
    if (go == 6):
        print("You may take a place bet on numbers 4, 5, 6, 8, 9, and 10. If this number is rolled again before a 7 is rolled, you win. The payout depends on the value chosen.")
    if (go == 7):
        print("A field bet is a one roll bet. If a 3, 4, 9, 10, or 11 are rolled you win even money. If a 2 or 12 is rolled, you win 2 to 1.")
    if (go == 8):
        print("A low dice bet is a one roll bet in which you win if a 2, 3, 4, 5, or 6 are rolled. The payout depends on the number rolled.")
    if (go == 9):
        print("A low dice bet is a one roll bet in which you win if a 2, 3, 4, 5, or 6 are rolled. The payout depends on the number rolled.")
    if (go != 0):
        print()
        continuation = input('Press ENTER to continue.')
    
    print()
    
game = 'yes'
bet = 0
while (game == 'yes'):
    
    rollCount = 0
    rollVal = 0
    point = 0
    betRoll = 0
    betType = 100
    comeCount = 0
    
    while (rollVal != 7):
        if (betType != 100):
            betRoll = 'no'
        
        if (betType != 1 and betType != 2 and betType != 3 and betType != 4 and betType != 5 and betType != 6):
            betType = 100
            while (betRoll != 'yes' and betRoll != 'no'):
                betRoll = input('Would you like to bet on the next roll? ')
                print()
                if (betRoll != 'yes' and betRoll != 'no'):
                    print('Please type either "yes" or "no" to continue.')
                    print()
        
        if (betRoll == 'yes'):
            print('Select the number of the type of bet you would like to place.')
            print('0.) SKIP BETTING ON THIS ROLL')
            print('1.) Pass')
            print("2.) Don't Pass")
            print("3.) Come")
            print("4.) Don't Come")
            print('5.) Odds')
            print('6.) Place')
            print('7.) Field')
            print('8.) Low Dice')
            print('9.) High Dice')
            print()
            
            if (betType == 100):
                if (rollCount == 0):
                    while (betType > 9 or betType < 0 or betType == 3 or betType == 4 or betType == 5):
                        betType = int(input('Type a number to continue: '))
                        print()
                        if (go > 9 or go < 0 or betType == 3 or betType == 4 or betType == 5):
                            print("Please select a number between 0 and 9.")
                            print("Note: Come, Don't Come, and Odds bets cannot be placed before the first roll.")
                            print()
                else:
                    while (betType > 9 or betType < 0 or betType == 1 or betType == 2):
                        betType = int(input('Type a number to continue: '))
                        print()
                        if (betType > 9 or betType < 0 or betType == 1 or betType == 2):
                            print("Please select a number between 0 and 9.")
                            print("Note: Pass and Don't Pass bets can only be placed before the first roll.")
                            print()
                            
                if (betType != 0): 
                    bet = total + 1
                    while (bet > total):
                        bet = int(input("How much would you like to bet? $"))
                        print()
                        if (bet > total):
                            print('Insufficient funds to make this bet.')
                            print('Current total funds: $', total)
                            print()
                            
            
        rollVal = roll()
        print("A", rollVal, "was rolled.")
        print()
        
        rollCount += 1
        if (betType == 3 or betType == 4):
            comeCount += 1

        if (betType == 1):
            if (rollCount == 1 and (rollVal == 2 or rollVal == 3 or rollVal == 12)):
                print("You lose.")
                total -= bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
            elif (rollCount == 1 and (rollVal == 11 or rollVal == 7)):
                print("YOU WIN!")
                total += bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                
                betType = 100
            elif (rollCount == 1):
                point = rollVal
            elif (rollVal == point):
                print("YOU WIN!")
                total += bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
            
        if (betType == 2):
            if (rollCount == 1 and (rollVal == 2 or rollVal == 3 or rollVal == 12)):
                print("YOU WIN!")
                total += bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
            elif (rollCount == 1 and (rollVal == 11 or rollVal == 7)):
                print("You lose.")
                total -= bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
            elif (rollCount == 1):
                point = rollVal
            elif (rollVal == point):
                print("You lose.")
                total -= bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
        
        if (betType == 3):
            if (comeCount == 1 and (rollVal == 2 or rollVal == 3 or rollVal == 12)): 
                print("You lose.")
                total -= bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
            elif (comeCount == 1 and (rollVal == 11 or rollVal == 7)):
                print("YOU WIN!")
                total += bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
            elif (comeCount == 1):
                comePoint = rollVal
            elif (rollVal == comePoint):
                print("YOU WIN!")
                total += bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
                
        if (betType == 4):
            if (comeCount == 1 and (rollVal == 2 or rollVal == 3 or rollVal == 12)): 
                print("YOU WIN!")
                total += bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
            elif (comeCount == 1 and (rollVal == 11 or rollVal == 7)):
                print("You lose.")
                total -= bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
            elif (comeCount == 1):
                comePoint = rollVal
            elif (rollVal == comePoint):
                print("You lose.")
                total -= bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
                
        if (betType == 5):
            if (rollVal == point):
                if (point == 4 or point == 10):
                    print("YOU WIN!")
                    total += bet * 2
                    print()
                    round(total, 2)
                    print("Money left: $", total)
                    print()
                elif (point == 5 or point == 9):
                    print("YOU WIN!")
                    total += bet * 2 / 3.0
                    print()
                    round(total, 2)
                    print("Money left: $", total)
                    print()
                elif (point == 6 or point == 8):
                    print("YOU WIN!")
                    total += bet * 6 / 5
                    print()
                    round(total, 2)
                    print("Money left: $", total)
                    print()
                betType = 100
                
        if (betType == 6):
            if (rollVal == 4 or rollVal == 10):
                print("YOU WIN!")
                total += bet * 9 / 5
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
            elif (rollVal == 5 or rollVal == 9):
                print("YOU WIN!")
                total += bet * 7 / 5
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
            elif (rollVal == 6 or rollVal == 8):
                print("YOU WIN!")
                total += bet * 6 / 5
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                betType = 100
                
        if (betType == 7):
            if (rollVal == 3 or rollVal == 4 or rollVal == 9 or rollVal == 10 or rollVal == 11):
                print("YOU WIN!")
                total += bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
            elif (rollVal == 2 or rollVal == 12):
                print("YOU WIN!")
                total += bet * 2
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
            else:
                print("You lose.")
                total -= bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
        
        if (betType == 8):
            if (rollVal < 7):
                if (rollVal == 2):
                    print("YOU WIN!")
                    total += bet * 5
                    print()
                    round(total, 2)
                    print("Money left: $", total)
                    print()
                else:
                    print("YOU WIN!")
                    total += bet
                    print()
                    round(total, 2)
                    print("Money left: $", total)
                    print()
            else:
                print("You lose.")
                total -= bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
                
        if (betType == 9):
            if (rollVal > 7):
                if (rollVal == 12):
                    print("YOU WIN!")
                    total += bet * 5
                    print()
                    round(total, 2)
                    print("Money left: $", total)
                    print()
                else:
                    print("YOU WIN!")
                    total += bet
                    print()
                    round(total, 2)
                    print("Money left: $", total)
                    print()
            else:
                print("You lose.")
                total -= bet
                print()
                round(total, 2)
                print("Money left: $", total)
                print()
        
        if (betType != 1 and betType != 2 and betType != 3 and betType != 4 and betType != 5 and betType != 6):
            betRoll = 0
            betType = 100
            
        if (rollVal == 7):
            if (betType != 100):
                print("You lose.")
                total -= bet
                print()
                print("Money left: $", total)
                print()
                betType = 100
        
        if (betType == 100):
            game = 0
            if (total > 500):
                while (game != 'yes' and game != 'no'):
                    game = input("Continue betting? ")
                    if (game != 'yes' and game != 'no'):
                        print()
                        print('Type either "yes" or "no"')
                        print()
                if (game == 'yes'):        
                    if (rollVal != 7):
                        print()
                        print()
                        print()
                        print('Continue Round')
                        print()
                    else:
                        print()
                        print()
                        print('NEW ROUND')
                        print()
                    bet = 0
                else:
                    rollVal = 7
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
                    if (rollVal != 7):
                        print()
                        print()
                        print()
                        print('Continue Round')
                        print()
                    else:
                        print()
                        print()
                        print('NEW ROUND')
                        print()
                    game = 'yes'
                else:
                    game = 'no'
                    rollVal = 7
    