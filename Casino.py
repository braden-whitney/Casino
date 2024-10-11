def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

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

def draw_card_blackjack(unused, hand):
    x = 0
    cardScore = 0
    while (x == 0):
        card = random.randrange(0, 52)
        if card in unused:
            x = 1
            unused.remove(card)
    
    if (card < 4):
        cardName = "Ace of"
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
        cardScore = 10
    elif (card < 48):
        cardName = "Queen of"
        cardScore = 10
    elif (card < 52):
        cardName = "King of"
        cardScore = 10
        
    suit = 4 * (float(card / 4) - int(card / 4))
    if (suit == 0):
        cardName = cardName + " Spades"
    elif (suit == 1):
        cardName = cardName + " Hearts"
    elif (suit == 2):
        cardName = cardName + " Clubs"
    elif (suit == 3):
        cardName = cardName + " Diamonds"
    
    hand.append(cardName)
    print('You drew: ', cardName)
    if (card < 4):
        cardScore = int(input('Count as 1 or 11? '))
        
    return cardScore
    
def opponent_draw(unused, opponent_hand):
    x = 0
    cardScore = 0
    while (x == 0):
        card = random.randrange(0, 52)
        if card in unused:
            x = 1
            unused.remove(card)
    if (card < 4):
        cardName = "Ace of"
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
        cardScore = 10
    elif (card < 48):
        cardName = "Queen of"
        cardScore = 10
    elif (card < 52):
        cardName = "King of"
        cardScore = 10
        
    suit = 4 * (float(card / 4) - int(card / 4))
    if (suit == 0):
        cardName = cardName + " Spades"
    elif (suit == 1):
        cardName = cardName + " Hearts"
    elif (suit == 2):
        cardName = cardName + " Clubs"
    elif (suit == 3):
        cardName = cardName + " Diamonds"
    
    opponent_hand.append(cardName)
    return cardScore

def spin():
    spin = random.randrange(0,37)
    
    return spin

def roll(): 
    dieOne = random.randrange(1, 7)
    dieTwo = random.randrange(1, 7)
    
    roll = dieOne + dieTwo
    
    return roll

print("WELCOME TO BRADEN'S CASINO!")

import random
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

total = 0

while (total < 1000):
    total = input("Starting value: $")
    num = is_number(total)
    while (num == False):
        print("Starting value must be a number.")
        print()
        total = input("Starting value: $")
        num = is_number(total)
    total = int(total)
    if (total < 1000):
        print()
        print('Starting amount must be above $1000.')
        print()
print()
another = 'yes'
while (another == 'yes'):
    gameType = 0
    print("We have several games you can play. Please choose one to continue.")
    print()
    print("1.) POKER")
    print("2.) BLACKJACK")
    print("3.) ROULETTE")
    print("4.) CRAPS")
    
    while (gameType != 1 and gameType != 2 and gameType != 3 and gameType != 4):
        gameType = input("Type a number corresponding to a game above: ")
        num = is_number(gameType)
        while (num == False):
            print("Game selection must be a number.")
            print()
            gameType = input("Type a number corresponding to a game above: ")
            num = is_number(gameType)
        gameType = int(gameType)
        print()
        if (gameType != 1 and gameType != 2 and gameType != 3 and gameType != 4):
            print("Please select a number above.")
            print()
    
    if (gameType == 1):
        print('Welcome to Poker!')
        print("Buy in is $100.")
        
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
                go = input("Type a number corresponding to a hand above or 0 to continue: ")
                num = is_number(go)
                while (num == False):
                    print("Game selection must be a number.")
                    print()
                    go = input("Type a number corresponding to a hand above or 0 to continue: ")
                    num = is_number(go)
                go = int(go)
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
                    newBet = input("Additional bet: $")
                    num = is_number(newBet)
                    while (num == False):
                        print("Bet must be a number.")
                        print()
                        newBet = input("Additional bet: $")
                        num = is_number(newBet)
                    newBet = int(newBet)
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
                        newBet = input("Additional bet: $")
                        num = is_number(newBet)
                        while (num == False):
                            print("Bet must be a number.")
                            print()
                            newBet = input("Additional bet: $")
                            num = is_number(newBet)
                        newBet = int(newBet)
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
                            newBet = input("Additional bet: $")
                            num = is_number(newBet)
                            while (num == False):
                                print("Bet must be a number.")
                                print()
                                newBet = input("Additional bet: $")
                                num = is_number(newBet)
                            newBet = int(newBet)
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
                                newBet = input("Additional bet: $")
                                num = is_number(newBet)
                                while (num == False):
                                    print("Bet must be a number.")
                                    print()
                                    newBet = input("Additional bet: $")
                                    num = is_number(newBet)
                                newBet = int(newBet)
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
    
    elif (gameType == 2):
        print('Welcome to Blackjack!')
        print("Buy in is $100.")
        
        instructions = 0
    
        while (instructions != 'yes' and instructions != 'no'):
            instructions = input("Would you like to know how to play? ")
            print()
            if (instructions != 'yes' and instructions != 'no'):
                print('Please type either "yes" or "no" to continue.')
                print()
    
        if (instructions == 'yes'):
            print("The goal of blackjack is to get as close to 21 without going over. Each card is worth its face value (ex: 3 is worth 3). Face cards are each worth 10. An ace can be chosen to be equal to either 1 or 11.")
            print()
            print('The game starts with 2 cards being dealt to each player, one face up and the other face down. To draw another card, you may request a "hit" and to stop drawing you can request to "stay." If the player gets over 21, they will instantly lose. Once both players are done drawing, they will show their hands. Whoever is closest to 21 without going over will win.')
            print()
            
        game = 'yes'
        bet = 0
        while (game == 'yes'):
            unused = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
            hand = []
            score = 0
            bust = 0
            dealerBust = 0
            opponentScore = 0
            opponent_hand = []
            bet += 100.0
            score += draw_card_blackjack(unused, hand)
            opponentScore += opponent_draw(unused, opponent_hand)
            score += draw_card_blackjack(unused, hand)
            opponentScore += opponent_draw(unused, opponent_hand)
            opponentCards = 2
            print()
            print('Your current score is: ', score)
            print('Dealer drew: ', opponent_hand[0])
            print()
            
            newBet = total
            while (total - (bet + newBet) < 0):
                newBet = input("Additional bet: $")
                num = is_number(newBet)
                while (num == False):
                    print("Bet must be a number.")
                    print()
                    newBet = input("Additional bet: $")
                    num = is_number(newBet)
                newBet = int(newBet)
                if (total - (bet + newBet) < 0):
                    print()
                    print("Bet cannot exceed total")
                    print('Current total: ', total - 100)
                    print()
            print()
            bet += newBet
            
            if (score < 21):
                hitStay = 0
                while (hitStay != 'stay'):
                    hitStay = 0
                    if (score >= 21):
                        hitStay = 'stay'
                    else:
                        while (hitStay != 'hit' and hitStay != 'stay'):
                            hitStay = input("Would you like to hit or stay? ")
                            if (hitStay != 'hit' and hitStay != 'stay'):
                                print()
                                print('Type "hit" for another card and "stay" to end your turn.')
                                print()
                        if (hitStay == 'hit'):
                            score += draw_card_blackjack(unused, hand)
                            if (score <= 21):
                                print('Your current score is: ', score)
                                print()
                                newBet = total
                                while (total - (bet + newBet) < 0):
                                    newBet = input("Additional bet: $")
                                    num = is_number(newBet)
                                    while (num == False):
                                        print("Bet must be a number.")
                                        print()
                                        newBet = input("Additional bet: $")
                                        num = is_number(newBet)
                                    newBet = int(newBet)
                                    if (total - (bet + newBet) < 0):
                                        print()
                                        print("Bet cannot exceed total")
                                        print('Current total: ', total - 100)
                                        print()
                                print()
                                bet += newBet
                        elif (hitStay == 'stay'):
                            print()
            
            if (score > 21):
                print("You Bust!")
                score = 0
                bust = 1
                total -= bet
               
            if (bust == 0):         
                while (opponentScore < 17):
                    opponentScore += opponent_draw(unused, opponent_hand)
                    opponentCards += 1
                    
                if (opponentScore > 21):
                    print("DEALER BUST!!!")
                    print()
                    dealerBust = 1
                    opponentScore = 0
                print("Dealer hand:")
                x = 0
                
                while (x < opponentCards):
                    print(opponent_hand[x])
                    x += 1
                    
                if (dealerBust == 0):
                    print()
                    print("Dealer score: ", opponentScore)
                    print("Your Score: ", score)
                
                if (score > opponentScore):
                    print()
                    if (score == 21):
                        print("BLACKJACK!!!")
                        total += bet * 3 / 2
                    else:
                        print("YOU WIN!")
                        total += bet
                elif(score == opponentScore):
                    print()
                    print("Tie!")
                    print()
                else:
                    print()
                    print("You Lose.")
                    total -= bet
            
            if (score != opponentScore):
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
                print("Must have at least $500 to continue.")
                print("Current balance: $", total)
                addMoney = input("Add money? ")
                if (addMoney == 'yes'):
                    amountAdded = 0
                    while (amountAdded < 1000):
                        amountAdded = input("How much would you like to add? $")
                        num = is_number(amountAdded)
                        while (num == False):
                            print("Additional funds must be a number.")
                            print()
                            amountAdded = input("Additional funds: $")
                            num = is_number(amountAdded)
                        amountAdded = int(amountAdded)
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
    
    if (gameType == 3):
        print("Welcome to Roulette!")
        
        instructions = 0
    
        while (instructions != 'yes' and instructions != 'no'):
            instructions = input("Would you like to know how to play? ")
            print()
            if (instructions != 'yes' and instructions != 'no'):
                print('Please type either "yes" or "no" to continue.')
                print()
    
        if (instructions == 'yes'):
            print('The player will begin by making a bet. After the bet is made, a ball will be dropped on the spinning wheel. The player can bet that the ball will land on even numbers, odd numbers, red numbers, or black numbers. Each of these bets will result in an even money payout. The player can also bet on a specific number. This bet will have a payout of 35 to 1.')
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
                    betValue = input("What number would you like to bet on? ")
                    num = is_number(betValue)
                    while (num == False):
                        print("Type a number.")
                        print()
                        newBet = input("What number would you like to bet on? ")
                        num = is_number(betValue)
                    betValue = int(betValue)
                    print()
                    if (betValue > 36 or betValue < 0):
                        print('Number must be between 0 and 36.')
                        print()
            
            while (bet > total):
                    bet = input("How much would you like to bet? $")
                    num = is_number(bet)
                    while (num == False):
                        print("Bet must be a number.")
                        print()
                        bet = input("How much would you like to bet? $")
                        num = is_number(bet)
                    bet = int(bet)
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
            
    if (gameType == 4):
        go = 10
        print('Welcome to Craps!')
        
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

                    if (betType > 0): 
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
    
    another = 0
    while (another != 'yes' and another != 'no'):
        another = input('Would you like to play a different game? ')
        print()
        if (another != 'yes' and another != 'no' and total >= 500):
            print('Please type either "yes" or "no" to continue.')
            print()
        elif (total <= 500):
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
                another = 'yes'
            else:
                another = 'no'
                           
print('Congratulations! You have $', total, '!')