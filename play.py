import random

class Blackjack:
    """
    This project is a simulated black jack application where you play against the dealer
    while making bets, decide on hands, and get advice from a black jack strategy card
    """
    def __init__(self):
        # global variable declarations
        self.bet = 0

        self.cardDeck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        self.dealerCard1 = self.cardDeck
        self.dealerCard2 = self.cardDeck
        self.dealerHitCard = self.cardDeck

        self.playerCard1 = self.cardDeck
        self.playerCard2 = self.cardDeck
        self.doubleDownCard = self.cardDeck

        self.playerTotalCardAmount = 0
        self.dealerTotalCardAmount = 0

    # Make a function to give you strategic blackjack advice , i.e. whether to hit, stay, etc.
    def blackJackStrategyFunction(self):
        print("continue")

    # Make a blackjack simulator to simulate one hand of blackjack
    def blackJackDealerFunction(self):
        # allow player to pick bet amount
        self.bet = input("Please place your bet - $5, $25, $50, $100: ")

        # randomly deal dealer two cards and show first one
        dealerFirstCard = random.choice(self.dealerCard1)
        dealerSecondCard = random.choice(self.dealerCard2)
        print("\nDealer: {}".format(dealerFirstCard))

        # if the dealer cards is a face card, convert it to a value of 10
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
        self.dealerTotalCardAmount += dealerFirstCard
        self.dealerTotalCardAmount += dealerSecondCard

        # randomly deal player two cards and show them
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
        self.playerTotalCardAmount += playerFirstCard
        self.playerTotalCardAmount += playerSecondCard
        print(self.playerTotalCardAmount)

        # while loop to allow the player to keep making decisions while his/her total amount is below 21
        while self.playerTotalCardAmount <= 21:

            # decision input from the user from the following options
            decision = input("\nDouble, Hit, Split, Stand: ")

            # if user decides to double down on bet he/she gets one more card only and their turn is over
            if decision == "Double":
                doubleDownCard = random.choice(self.doubleDownCard)
                if doubleDownCard == "J" or doubleDownCard == "Q" or doubleDownCard == "K" or doubleDownCard == "A":
                    doubleDownCard = 10
                    self.playerTotalCardAmount += int(doubleDownCard)
                else:
                    self.playerTotalCardAmount += int(doubleDownCard)
                if self.playerTotalCardAmount == 21:
                    print("\nPlayer: {}, {}, {} -- {} BLACKJACK!".format(playerFirstCard, playerSecondCard, doubleDownCard, self.playerTotalCardAmount))
                    self.bet = self.bet * 1.5
                    break
                elif self.playerTotalCardAmount > 21:
                    print("\nPlayer: {}, {}, {} -- {} BUST".format(playerFirstCard, playerSecondCard, doubleDownCard, self.playerTotalCardAmount))
                    break
                else:
                    print("Player: {}, {}, {} -- {}".format(playerFirstCard, playerSecondCard, doubleDownCard, self.playerTotalCardAmount))
                    break
            elif decision == "Hit":

                print("Player: {}, {}".format(playerFirstCard, playerSecondCard))
            elif decision == "Split":
                print("Sp")
            elif decision == "Stand":
                print("\nPlayer: {}, {} -- {}".format(playerFirstCard, playerSecondCard, self.playerTotalCardAmount))
                break

        dealerList = []
        while self.dealerTotalCardAmount < 17:
            if self.bet == 21:
                print("Player has Blackjack! You win ${}!".format(self.bet))
            elif self.dealerTotalCardAmount >= 17:
                print("Dealer: {}, {} -- {}".format(dealerFirstCard, dealerSecondCard, self.dealerTotalCardAmount))
            elif self.dealerTotalCardAmount < 17:
                self.dealerHitCard = random.choice(self.dealerHitCard)
                if self.dealerHitCard == "J" or self.dealerHitCard == "Q" or self.dealerHitCard == "K" or  self.dealerHitCard == "A":
                    self.dealerHitCard = 10
                    self.dealerTotalCardAmount += int(self.dealerHitCard)
                else:
                    self.dealerTotalCardAmount += int(self.dealerHitCard)

            dealerList.append(int(self.dealerHitCard))
        print("Dealer: {}, {}, {} -- {}".format(dealerFirstCard, dealerSecondCard, str(dealerList).strip('[]'), self.dealerTotalCardAmount))

        if self.dealerTotalCardAmount < self.playerTotalCardAmount or self.dealerTotalCardAmount > 21:
            print("\nPlayer wins ${}!".format(self.bet))
        elif self.dealerTotalCardAmount > self.playerTotalCardAmount and self.dealerTotalCardAmount < 21:
            print("\nDealer wins, you lose ${}.".format(self.bet))
        else:
            print("\nPush, you get your ${} back.".format(self.bet))
if __name__ == "__main__":
    main = Blackjack()
    result = main.blackJackDealerFunction()