#    Title: Blackjack Trainer
#    Author: Tucker McCoy
#    Date: September 10, 2019
#    Code version: 1.0
#    Availability: https://github.com/tmccoy14/Blackjack

import random

class Blackjack:
    """
    This file is a simulated black jack application where you play
    against the dealer while making bets and deciding on hands
    """
    def __init__(self):
        # simulated deck of cards
        self.cardDeck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        # two cards dealt to dealer
        self.dealerCard1 = self.cardDeck
        self.dealerCard2 = self.cardDeck

        # dealer hit card if below 17
        self.dealerHitCard = self.cardDeck

        # two cards dealt to player
        self.playerCard1 = self.cardDeck
        self.playerCard2 = self.cardDeck

        # player double down card
        self.doubleDownCard = self.cardDeck

        # player hit card
        self.playerHitCard = self.cardDeck

    # blackJackDealerFunction is a blackjack simulator to simulate hands of blackjack
    def blackJackDealerFunction(self):
        # get the players money
        totalMoney = input("Welcome to Blackjack Trainer, how much money would you like to deposit? ")

        # while the player still has money to play with continue to let them play
        while int(totalMoney) > 0:

            # set the player and dealer amount to 0 so it can be reset each time the player plays a hand
            playerTotalCardAmount = 0
            dealerTotalCardAmount = 0

            # allow player to pick bet amount
            bet = input("Please place your bet - $5, $25, $50, $100: ")

            # randomly deal dealer two cards and show first one to the player
            dealerFirstCard = random.choice(self.dealerCard1)
            dealerSecondCard = random.choice(self.dealerCard2)
            print("\nDealer: {}".format(dealerFirstCard))

            # if the dealer card is a face card, convert it to a value of 10
            # otherwise convert the value to int and assign it to the card
            if dealerFirstCard == "J" or dealerFirstCard == "Q" or dealerFirstCard == "K" or dealerFirstCard == "A":
                dealerFirstCard = 10
            else:
                dealerFirstCard = int(dealerFirstCard)

            if dealerSecondCard == "J" or dealerSecondCard == "Q" or dealerSecondCard == "K" or  dealerSecondCard == "A":
                dealerSecondCard = 10
            else:
                dealerSecondCard = int(dealerSecondCard)

            # get the value of the two cards to keep track of the total number
            dealerTotalCardAmount += dealerFirstCard
            dealerTotalCardAmount += dealerSecondCard

            # randomly deal player two cards and show them both
            playerFirstCard = random.choice(self.playerCard1)
            playerSecondCard = random.choice(self.playerCard2)
            print("Player: {}, {}".format(playerFirstCard, playerSecondCard))

            # if either of the players cards is a face card, convert it to a value of 10
            # otherwise convert the value to int and assign it to the card
            if playerFirstCard == "J" or playerFirstCard == "Q" or playerFirstCard == "K" or playerFirstCard == "A":
                playerFirstCard = 10
            else:
                playerFirstCard = int(playerFirstCard)

            if playerSecondCard == "J" or playerSecondCard == "Q" or playerSecondCard == "K" or  playerSecondCard == "A":
                playerSecondCard = 10
            else:
                playerSecondCard = int(playerSecondCard)

            # get the value of the two cards to keep track of the total number
            playerTotalCardAmount += playerFirstCard
            playerTotalCardAmount += playerSecondCard
            print(playerTotalCardAmount)

            # while loop to allow the player to keep making decisions while the total amount is below 21
            while playerTotalCardAmount <= 21:

                # decision input from the user from the following options
                decision = input("\nDouble, Hit, Split, Stand: ")

                # if user decides to double down on bet they get one more card only and their turn is over
                if decision == "Double":
                    doubleDownCard = random.choice(self.doubleDownCard)
                    if doubleDownCard == "J" or doubleDownCard == "Q" or doubleDownCard == "K" or doubleDownCard == "A":
                        doubleDownCard = 10
                        playerTotalCardAmount += int(doubleDownCard)
                    else:
                        playerTotalCardAmount += int(doubleDownCard)
                    
                    if playerTotalCardAmount == 21:
                        print("\nPlayer: {}, {}, {} -- {} BLACKJACK!".format(playerFirstCard, playerSecondCard, doubleDownCard, playerTotalCardAmount))
                        bet = int(bet) * 1.5
                        break
                    elif playerTotalCardAmount > 21:
                        print("\nPlayer: {}, {}, {} -- {} BUST".format(playerFirstCard, playerSecondCard, doubleDownCard, playerTotalCardAmount))
                        bet = int(bet) * 2
                        break
                    else:
                        print("Player: {}, {}, {} -- {}".format(playerFirstCard, playerSecondCard, doubleDownCard, playerTotalCardAmount))
                        bet = int(bet) * 2
                        break
                # if user decides to hit they can do so until they want to stop or go above 21
                elif decision == "Hit":
                    playerList = []
                    while playerTotalCardAmount < 21:
                        if playerTotalCardAmount == 21:
                            print("Player has Blackjack! You win ${}!".format(bet))
                        elif playerTotalCardAmount < 21:
                            self.playerHitCard = random.choice(self.playerHitCard)
                            if self.playerHitCard == "J" or self.playerHitCard == "Q" or self.playerHitCard == "K" or  self.playerHitCard == "A":
                                self.playerHitCard = 10
                                playerTotalCardAmount += int(self.playerHitCard)
                            else:
                                playerTotalCardAmount += int(self.playerHitCard)

                        playerList.append(int(self.playerHitCard))
                    print("\nPlayer: {}, {}, {} -- {}".format(playerFirstCard, playerSecondCard, str(playerList).strip('[]'), playerTotalCardAmount))
                # if user decides to split they get dealt two new cards and get to play both hands for double the original bet
                elif decision == "Split":
                    print("Sp")
                # if user decides to stand their turn is over and they accept the two cards they have been given
                elif decision == "Stand":
                    print("\nPlayer: {}, {} -- {}".format(playerFirstCard, playerSecondCard, playerTotalCardAmount))
                    break

            # after the players turn is over it is the dealers turn to go
            # the dealer goes until they have busted or their card amount equals 17
            dealerList = []
            while dealerTotalCardAmount < 17:
                if dealerTotalCardAmount == 21:
                    bet = float(bet) * 1.5
                    print("Player has Blackjack! You win ${}!".format(bet))
                elif dealerTotalCardAmount >= 17:
                    print("Dealer: {}, {} -- {}".format(dealerFirstCard, dealerSecondCard, dealerTotalCardAmount))
                elif dealerTotalCardAmount < 17:
                    self.dealerHitCard = random.choice(self.dealerHitCard)
                    if self.dealerHitCard == "J" or self.dealerHitCard == "Q" or self.dealerHitCard == "K" or  self.dealerHitCard == "A":
                        self.dealerHitCard = 10
                        dealerTotalCardAmount += int(self.dealerHitCard)
                    else:
                        dealerTotalCardAmount += int(self.dealerHitCard)

                dealerList.append(int(self.dealerHitCard))
            print("Dealer: {}, {}, {} -- {}".format(dealerFirstCard, dealerSecondCard, str(dealerList).strip('[]'), dealerTotalCardAmount))

            # convert totalMoney to an int in order to be able to add or subtract the total
            totalMoney = int(totalMoney)

            # if players card total is more than the dealers and the players card total is less than or equal to 21
            if (dealerTotalCardAmount < playerTotalCardAmount) and (playerTotalCardAmount <= 21) or (dealerTotalCardAmount > 21):
                print("\nPlayer wins ${}!".format(bet))
                totalMoney += int(bet)
                print("Your total balance is now: ${}\n".format(totalMoney))
            # if deales card total is more than the players and the the dealer card total is less than or equal to 21 or if the player busts and the dealer doesn't
            elif (dealerTotalCardAmount > playerTotalCardAmount and dealerTotalCardAmount <= 21) or (playerTotalCardAmount > 21 and dealerTotalCardAmount <= 21):
                print("\nDealer wins, you lose ${}.".format(bet))
                totalMoney -= int(bet)
                print("Your total balance is now: ${}\n".format(totalMoney))
            # else the player and the dealer card amount is the same therefore the player pushes and gets their money back
            else:
                print("\nPush, you get your ${} back.".format(bet))
                print("Your total balance is now: ${}\n".format(totalMoney))
        
        print("GAME OVER")

if __name__ == "__main__":
    main = Blackjack()
    result = main.blackJackDealerFunction()