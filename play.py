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

        self.playerCard1 = self.cardDeck
        self.playerCard2 = self.cardDeck
        self.doubleCard = self.cardDeck

        self.playerTotalCardAmount = 0
        self.dealerTotalCardAmount = 0

    # Make a function to give you strategic blackjack advice , i.e. whether to hit, stay, etc.
    def blackJackStrategyFunction(self):
        print("continue")

    # Make a blackjack simulator to simulate one hand of blackjack
    def blackJackDealerFunction(self):
        self.bet = input("Please place your bet - $5, $25, $50, $100: ")

        dealerFirstCard = random.choice(self.dealerCard1)
        dealerSecondCard = random.choice(self.dealerCard2)

        print("\nDealer: {}".format(dealerFirstCard))

        playerFirstCard = random.choice(self.playerCard1)
        playerSecondCard = random.choice(self.playerCard2)

        print("Player: {}, {}".format(playerFirstCard, playerSecondCard))

        if playerFirstCard == "J" or playerFirstCard == "Q" or playerFirstCard == "K" or playerFirstCard == "A":
            playerFirstCard = 10
        else:
            playerFirstCard = int(playerFirstCard)

        if playerSecondCard == "J" or playerSecondCard == "Q" or playerSecondCard == "K" or  playerSecondCard == "A":
            playerSecondCard = 10
        else:
            playerSecondCard = int(playerSecondCard)

        self.playerTotalCardAmount += playerFirstCard
        self.playerTotalCardAmount += playerSecondCard
        print(self.playerTotalCardAmount)

        while self.playerTotalCardAmount <= 21:

            decision = input("\nDouble, Hit, Split, Stand: ")

            # if user decides to double down on bet
            if decision == "Double":
                doubleCard = random.choice(self.doubleCard)
                if playerFirstCard == 'J' or 'Q' or 'K' or 'A':
                    self.playerTotalCardAmount += 10
                else:
                    self.playerTotalCardAmount += int(doubleCard)
                if self.playerTotalCardAmount == 21:
                    print("Player: {}, {}, {} -- BLACKJACK!".format(playerFirstCard, playerSecondCard, doubleCard))
                    self.bet = self.bet * 1.5
                    print("You win ${}!".format(self.bet))
                    break
                elif self.playerTotalCardAmount > 21:
                    print("Player: {}, {}, {} -- BUST :'(".format(playerFirstCard, playerSecondCard, doubleCard))
                    break
                else:
                    print("Player: {}, {}, {} -- {}".format(playerFirstCard, playerSecondCard, doubleCard, self.playerTotalCardAmount))
                    break
            elif decision == "Hit":

                print("Player: {}, {}".format(playerFirstCard, playerSecondCard))
            elif decision == "Split":
                print("Sp")
            elif decision == "Stand":
                print("St")


if __name__ == "__main__":
    main = Blackjack()
    result = main.blackJackDealerFunction()