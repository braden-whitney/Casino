def draw_card(unused):
    x = 0
    while (x == 0):
        card = random.randrange(0, 52)
        if card in unused:
            x = 1
            unused.remove(card)
    return card

def scoring(cardNum):
    suits = [0,0,0,0,0]
    cards = [0,0,0,0,0]
    x = 0
    
    while (x < 5):
        suits[x] = 4 * (float(cardNum[x] / 4) - int(cardNum[x] / 4))
        if (cardNum[x] < 4):
            cards[x] = 1
        elif (cardNum[x] < 8):
            cards[x] = 2
        elif (cardNum[x] < 12):
            cards[x] = 3
        elif (cardNum[x] < 16):
            cards[x] = 4
        elif (cardNum[x] < 20):
            cards[x] = 5
        elif (cardNum[x] < 24):
            cards[x] = 6
        elif (cardNum[x] < 28):
            cards[x] = 7
        elif (cardNum[x] < 32):
            cards[x] = 8
        elif (cardNum[x] < 36):
            cards[x] = 9
        elif (cardNum[x] < 40):
            cards[x] = 10
        elif (cardNum[x] < 44):
            cards[x] = 11
        elif (cardNum[x] < 48):
            cards[x] = 12
        elif (cardNum[x] < 52):
            cards[x] = 13
        x += 1
    
    if (suits[0] == suits[1] and suits [1] == suits[2] and suits[2] == suits[3] and suits[3] == suits[4]):
        if(cards[0] == 1 and cards[1] == 10 and cards[2] == 11 and cards[3] == 12 and cards[4] == 13):
            score = 10
        elif(((cards[4] - cards[3]) == 1 and (cards[3] - cards[2]) == 1 and (cards[2] - cards[1]) == 1 and (cards[1] - cards[0]) == 1) or (cards[0] == 1 and cards[4] == 13 and cards[3] == 12 and cards[2] == 11 and cards[1] == 10)):
            score = 9
        else:
            score = 6
    else:
        if ((cards[0] == cards[1] and cards[1] == cards[2] and cards[2] == cards[3]) or (cards[1] == cards[2] and cards[2] == cards[3] and cards[3] == cards[4])):
            score = 8
        elif ((cards[0] == cards[1] and cards[2] == cards[4]) or (cards[0] == cards[2] and cards[3] == cards[4])):
            score = 7
        elif((cards[4] - cards[3]) == 1 and (cards[3] - cards[2]) == 1 and (cards[2] - cards[1]) == 1 and (cards[1] - cards[0]) == 1 or (cards[0] == 1 and cards[4] == 13 and cards[3] == 12 and cards[2] == 11 and cards[1] == 10)):
            score = 5
        elif (cards[0] == cards[2] or cards[1] == cards[3] or cards[2] == cards[4]):
            score = 4
        elif ((cards[0] == cards[1] and cards[2] == cards[3]) or (cards[0] == cards[1] and cards[3] == cards[4]) or (cards[1] == cards[2] and cards[3] == cards[4])):
            score = 3
        elif (cards[0] == cards[1] or cards[1] == cards[2] or cards[2] == cards[3] or cards[3] == cards[4]):
            score = 2
        else:
            score = 1
            
    return score
            

def card_name(hand, card, you):
    if (card < 4):
        cardName = "Ace of"
        cardScore = 14
    elif (card < 8):
        cardName = "Two of"
        cardScore = 2
    elif (card < 12):
        cardName = "Three of"
        cardScore = 3
    elif (card < 16):
        cardName = "Four of"
        cardScore = 4
    elif (card < 20):
        cardName = "Five of"
        cardScore = 5
    elif (card < 24):
        cardName = "Six of"
        cardScore = 6
    elif (card < 28):
        cardName = "Seven of"
        cardScore = 7
    elif (card < 32):
        cardName = "Eight of"
        cardScore = 8
    elif (card < 36):
        cardName = "Nine of"
        cardScore = 9
    elif (card < 40):
        cardName = "Ten of"
        cardScore = 10
    elif (card < 44):
        cardName = "Jack of"
        cardScore = 11
    elif (card < 48):
        cardName = "Queen of"
        cardScore = 12
    elif (card < 52):
        cardName = "King of"
        cardScore = 13
        
    suit = 4 * (float(card / 4) - int(card / 4))
    if (suit == 0):
        cardName = cardName + " Spades"
    elif (suit == 1):
        cardName = cardName + " Hearts"
    elif (suit == 2):
        cardName = cardName + " Diamonds"
    elif (suit == 3):
        cardName = cardName + " Clubs"
    
    hand.append(cardName)
    if (you == 1):
        print('You drew: ', cardName)
    elif (you == 2):
        print('Card flipped: ', cardName)
        
    return cardScore

import random

print('Welcome to Poker!')
print("Buy in is $100.")
total = 0
while (total < 1000):
    total = int(input("Starting value: $"))
    if (total < 1000):
        print()
        print('Starting amount must be above $1000.')
        print()
game = 'yes'
go = 100

while (go != 0):
    print('There are several different hands to play, type the number of a hand you would like to know more about or type 0 to continue.')
    print('The following hands are ranked in order of strength:')
    print('0.) BET')
    print('1.) Royal Flush')
    print("2.) Straight Flush")
    print("3.) Four of a Kind")
    print("4.) Full House")
    print('5.) Flush')
    print('6.) Straight')
    print('7.) Three of Kind')
    print('8.) Two Pair')
    print('9.) Pair')
    print('10.) High Card')
    print()

    go = 100
    while (go > 10 or go < 0):
        go = int(input('Type a number to continue: '))
        print()
        if (go > 10 or go < 0):
            print("Please select a number between 0 and 10.")
            print()
    
    if (go == 1):
        print('A royal flush includes a 10, jack, queen, king, and ace all of the same suit.')
    if (go == 2):
        print("A straight flush is 5 cards in sequential order all of the same suit.")
    if (go == 3):
        print("A four of a kind is 4 cards of the same card value.")
    if (go == 4):
        print("A full house is a pair of cards of the same card value along with another set of three cards of the same value.")
    if (go == 5):
        print("A flush is five cards of the same suit not in any order.")
    if (go == 6):
        print("A straight is five cards in sequential order that are not of the same suit.")
    if (go == 7):
        print("A three of a kind is 3 cards of the same card value.")
    if (go == 8):
        print("A two pair is two sets of 2 cards of the same card value.")
    if (go == 9):
        print("A pair is one set of 2 cards of the same card value.")
    if (go == 10):
        print("A high card is only utilized if a player has no other hand or if a player and their opponent have the same hand. An ace is the highest value followed by the king and so forth, leaving the 2 as the lowest value.")
    if (go != 0):
        print()
        continuation = input('Press ENTER to continue.')
    
    print()
    
while(game == 'yes'):
    high_card = [0,0,0,0,0]
    unused = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
    hand = []
    opp_high = [0,0,0,0,0]
    opp_hand = []
    table_high = [0,0,0,0,0]
    handNum = [0,0,0,0,0]
    tableNum = [0,0,0,0,0]
    oppNum = [0,0,0,0,0]
    table = []
    card = 0
    you = 1
    notYou = 0
    tableFlip = 2
    bet = 100
    fold = 0
    
    card = draw_card(unused)
    handNum[0] = card
    high_card[0] = card_name(hand, card, you)
    
    card = draw_card(unused)
    oppNum[0] = card
    opp_high[0] = card_name(opp_hand, card, notYou)
    
    card = draw_card(unused)
    handNum[1] = card
    high_card[1] = card_name(hand, card, you)
    
    card = draw_card(unused)
    oppNum[1] = card
    opp_high[1] = card_name(opp_hand, card, notYou)
    print()
    
    print("$100 to Continue")
    fold = 0
    while (fold != 'no' and fold != 'yes'):
        fold = input("Fold? ")
        if (fold != 'no' and fold != 'yes'):
            print()
            print('Type "yes" or "no"')
            print()
    if (fold == 'no'):
        bet += 100
        newBet = total
        while (total - (bet + newBet) < 400):
            newBet = int(input("Additional bet: $"))
            if (total - (bet + newBet) < 400):
                print()
                print("Must have $400 left to continue")
                print('Current total: ', total)
                print()
        bet += newBet
        card = draw_card(unused)
        tableNum[0] = card
        table_high[0] = card_name(table, card, tableFlip)
        
        card = draw_card(unused)
        tableNum[1] = card
        table_high[1] = card_name(table, card, tableFlip)
        
        card = draw_card(unused)
        tableNum[2] = card
        table_high[2] = card_name(table, card, tableFlip)
        print() 
        
        print("$100 to Continue")
        fold = 0
        while (fold != 'no' and fold != 'yes'):
            fold = input("Fold? ")
            if (fold != 'no' and fold != 'yes'):
                print()
                print('Type "yes" or "no"')
                print()
        if (fold == 'no'):
            bet += 100
            newBet = total
            while (total - (bet + newBet) < 300):
                newBet = int(input("Additional bet: $"))
                if (total - (bet + newBet) < 300):
                    print()
                    print("Must have at least $300 left to continue")
                    print('Current total: ', total)
                    print()
            bet += newBet
            card = draw_card(unused)
            tableNum[3] = card
            table_high[3] = card_name(table, card, tableFlip)
            print()
            
            print("$100 to Continue")
            fold = 0
            while (fold != 'no' and fold != 'yes'):
                fold = input("Fold? ")
                if (fold != 'no' and fold != 'yes'):
                    print()
                    print('Type "yes" or "no"')
                    print()
            if (fold == 'no'):
                bet += 100
                newBet = total
                while (total - (bet + newBet) < 200):
                    newBet = int(input("Additional bet: $"))
                    if (total - (bet + newBet) < 200):
                        print()
                        print("Must have $200 left to continue")
                        print('Current total: ', total)
                        print()
                bet += newBet
                card = draw_card(unused)
                tableNum[4] = card
                table_high[4] = card_name(table, card, tableFlip)
                print()
                print("$100 to Continue")
                fold = 0
                while (fold != 'no' and fold != 'yes'):
                    fold = input("Fold? ")
                    if (fold != 'no' and fold != 'yes'):
                        print()
                        print('Type "yes" or "no"')
                        print()
                if (fold == 'no'):
                    bet += 100
                    newBet = total
                    while (total - (bet + newBet) < 100):
                        newBet = int(input("Additional bet: $"))
                        if (total - (bet + newBet) < 100):
                            print()
                            print("Must have $100 left to continue")
                            print('Current total: ', total)
                            print()
                    bet += newBet
                    
                    print()
                    print("Your cards: ", hand[0], " and ", hand[1])
                    print("Choose 3 cards from table to use in hand (type corresponding numbers separated by a spaces):")
                    print("(1) ", table[0])
                    print("(2) ", table[1])
                    print("(3) ", table[2])
                    print("(4) ", table[3])
                    print("(5) ", table[4])
                    x = 0
                    y = 0
                    z = 0
                    while (int(x) > 5 or int(y) > 5 or int(z) > 5 or int(x) < 1 or int(y) < 1 or int(z) < 1 or x == y or x == z or z == y):
                        x, y, z = input().split()
                        if (int(x) > 5 or int(y) > 5 or int(z) > 5 or int(x) < 1 or int(y) < 1 or int(z) < 1 or x == y or x == z or z == y):
                            print()
                            print('Choose three cards from the list by typing the corresponding number.')
                            print('Seperate each choice with a space.')
                            print('You may not select the same card more than once.')
                            print()
                    hand.append(table[int(x) - 1])
                    hand.append(table[int(y) - 1])
                    hand.append(table[int(z) - 1])
                    high_card[2] = table_high[int(x) - 1]
                    high_card[3] = table_high[int(y) - 1]
                    high_card[4] = table_high[int(z) - 1]
                    handNum[2] = tableNum[int(x) - 1]
                    handNum[3] = tableNum[int(y) - 1]
                    handNum[4] = tableNum[int(z) - 1]
                    
                    handNum.sort()
                    print()
                    
                    score = scoring(handNum)
                    
                    opp_hand.append('empty')
                    opp_hand.append('empty')
                    opp_hand.append('empty')
                    oppMax = 0
                    x = 0
                    y = 0
                    z = 0
                    oppMaxScore = 0
                    
                    while(x < 5):
                        y = 0
                        while(y < 5):
                            z = 0
                            while(z < 5):
                                if (x != y and x != z and y != z):
                                    oppBest = [oppNum[0], oppNum[1], tableNum[x], tableNum[y], tableNum[z]]
                                    oppBestHigh = [opp_high[0], opp_high[1], table_high[x], table_high[y], table_high[z]]
                                    
                                    oppBest.sort()
                                    oppBestHigh.sort()
                                    
                                    oppScore = scoring(oppBest)
                                    
                                    if (oppScore > oppMaxScore):
                                        oppMaxScore = oppScore
                                        oppMaxHand = oppBest
                                        oppMaxHigh = oppBestHigh
                                        opp_hand[2] = (table[int(x)])
                                        opp_hand[3] = (table[int(y)])
                                        opp_hand[4] = (table[int(z)])
                                    elif (oppScore == oppMaxScore):
                                        if (oppBestHigh[4] > oppMaxHigh[4]):
                                            oppMaxScore = oppScore
                                            oppMaxHand = oppBest
                                            oppMaxHigh = oppBestHigh
                                            opp_hand[2] = (table[int(x)])
                                            opp_hand[3] = (table[int(y)])
                                            opp_hand[4] = (table[int(z)])
                                        elif (oppBestHigh[4] == oppMaxHigh[4]):
                                            if (oppBestHigh[3] > oppMaxHigh[3]):
                                                oppMaxScore = oppScore
                                                oppMaxHand = oppBest
                                                oppMaxHigh = oppBestHigh
                                                opp_hand[2] = (table[int(x)])
                                                opp_hand[3] = (table[int(y)])
                                                opp_hand[4] = (table[int(z)])
                                            elif (oppBestHigh[3] == oppMaxHigh[3]):
                                                if (oppBestHigh[2] > oppMaxHigh[2]):
                                                    oppMaxScore = oppScore
                                                    oppMaxHand = oppBest
                                                    oppMaxHigh = oppBestHigh
                                                    opp_hand[2] = (table[int(x)])
                                                    opp_hand[3] = (table[int(y)])
                                                    opp_hand[4] = (table[int(z)])
                                                elif (oppBestHigh[2] == oppMaxHigh[2]):
                                                    if (oppBestHigh[1] > oppMaxHigh[1]):
                                                        oppMaxScore = oppScore
                                                        oppMaxHand = oppBest
                                                        oppMaxHigh = oppBestHigh
                                                        opp_hand[2] = (table[int(x)])
                                                        opp_hand[3] = (table[int(y)])
                                                        opp_hand[4] = (table[int(z)])
                                                    elif (oppBestHigh[1] == oppMaxHigh[1]):
                                                        if (oppBestHigh[0] > oppMaxHigh[0]):
                                                            oppMaxScore = oppScore
                                                            oppMaxHand = oppBest
                                                            oppMaxHigh = oppBestHigh
                                                            opp_hand[2] = (table[int(x)])
                                                            opp_hand[3] = (table[int(y)])
                                                            opp_hand[4] = (table[int(z)])
                                z += 1
                            y += 1
                        x += 1
                    
                    print("Opponent's hand: ")
                    lcv = 0
                    high_card.sort()
                    while (lcv < 5):
                        print(opp_hand[lcv])
                        lcv += 1
                    print()
                    lcv = 0
                    print("Your hand: ")
                    while (lcv < 5):
                        print(hand[lcv])
                        lcv += 1
                    print()
                    win = 0
                    if (0 == 0):    
                        if (score > oppMaxScore):
                            print("YOU WIN!!!")
                            total += bet
                            win = 1
                        elif (score == oppMaxScore):
                            if (high_card[4] > oppMaxHigh[4]):
                                print("YOU WIN!!!")
                                total += bet
                                win = 1
                            elif (high_card[4] == oppMaxHigh[4]):
                                if (high_card[3] > oppMaxHigh[3]):
                                    print("YOU WIN!!!")
                                    total += bet
                                    win = 1
                                elif (high_card[3] == oppMaxHigh[3]):
                                    if (high_card[2] > oppMaxHigh[2]):
                                        print("YOU WIN!!!")
                                        total += bet
                                        win = 1
                                    elif (high_card[2] == oppMaxHigh[2]):
                                        if (high_card[1] > oppMaxHigh[1]):
                                            print("YOU WIN!!!")
                                            total += bet
                                            win = 1
                                        elif (high_card[1] == oppMaxHigh[1]):
                                            if (high_card[0] > oppMaxHigh[0]):
                                                print("YOU WIN!!!")
                                                total += bet
                                                win = 1
                                            elif (high_card[4] == oppMaxHigh[4]):
                                                print("TIE!")
                                                win = 1
                    if (win == 0):
                        print("You Lose.")
                        total -= bet
                            
    if (fold == 'yes'):
        total = total - bet
    print()
    print("Money left: $", total)
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
        print("Not enough money to continue.")
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