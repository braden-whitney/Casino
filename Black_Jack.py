def draw_card(unused, hand):
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
    
import random  

print('Welcome to Blackjack!')
print("Buy in is $100.")
total = 0
instructions = 0

while (instructions != 'yes' and instructions != 'no'):
    instructions = input("Would you like to know how to play?")
    print()
    if (instructions != 'yes' and instructions != 'no'):
        print('Please type either "yes" or "no" to continue.')
        print()

if (instructions == 'yes'):
    print("The goal of blackjack is to get as close to 21 without going over. Each card is worth its face value (ex: 3 is worth 3). Face cards are each worth 10. An ace can be chosen to be equal to either 1 or 11.")
    print()
    print('The game starts with 2 cards being dealt to each player, one face up and the other face down. To draw another card, you may request a "hit" and to stop drawing you can request to "stay." If the player gets over 21, they will instantly lose. Once both players are done drawing, they will show their hands. Whoever is closest to 21 without going over will win.')
    
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
    unused = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
    hand = []
    score = 0
    bust = 0
    dealerBust = 0
    opponentScore = 0
    opponent_hand = []
    bet += 100.0
    score += draw_card(unused, hand)
    opponentScore += opponent_draw(unused, opponent_hand)
    score += draw_card(unused, hand)
    opponentScore += opponent_draw(unused, opponent_hand)
    opponentCards = 2
    print()
    print('Your current score is: ', score)
    print('Dealer drew: ', opponent_hand[0])
    print()
    
    newBet = total
    while (total - (bet + newBet) < 0):
        newBet = int(input("Additional bet: $"))
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
                    score += draw_card(unused, hand)
                    if (score <= 21):
                        print('Your current score is: ', score)
                        print()
                        newBet = total
                        while (total - (bet + newBet) < 0):
                            newBet = int(input("Additional bet: $"))
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
            print("Tiebreaker Round")
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