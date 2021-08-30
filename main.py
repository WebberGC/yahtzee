import dice
import random


# function to catch invalid input for y and n
def inputCatcher(input1):
    while input1 != "y" and input1 != "n":
        print("Please enter either 'y' or 'n'\n")
        input1 = input("Would you like to play Yahtzee [y|n]? ").lower()
    return input1


# function to display the dice roll
def diceDisplay():
    print("\nYou rolled:")
    dice.display_hand(rolledDice)


# function to ask what dice to remove and then reset the dice values
def diceReset():
    rerollDiceNum = int(input("\nHow many dice do you want to get rid of? "))
    rerollDiceCount = 0
    if rerollDiceNum < 5:
        while rerollDiceCount < rerollDiceNum:
            rerollDiceIndex = int(input("What is the die number of the die you want to get rid of? "))
            rolledDice[rerollDiceIndex - 1] = 0
            rerollDiceCount += 1
        return rolledDice
    else:
        while rerollDiceCount < 5:
            rerollDiceIndex = rerollDiceCount
            rolledDice[rerollDiceIndex - 1] = 0
            rerollDiceCount += 1
        return rolledDice


# function to set new random dice numbers
def newDiceNums():
    index = 0
    for num in rolledDice:
        if num == 0:
            rolledDice[index] = random.randint(1, 6)
        index += 1
    return rolledDice


# function to roll 2 times
def nextTurn():
    diceDisplay()
    diceReset()
    newDiceNums()
    diceDisplay()
    diceReset()
    newDiceNums()


# function to display scores
def displayScores():
    print()
    print("                      SCORING")
    print()
    print("                UPPER SECTION")
    print("                     Ones(1): ", oneCount)
    print("                     Twos(2): ", twoCount)
    print("                   Threes(3): ", threeCount)
    print("                    Fours(4): ", fourCount)
    print("                    Fives(5): ", fiveCount)
    print("                    Sixes(6): ", sixCount)
    print("                       Bonus: ", bonus)
    print()
    print("                LOWER SECTION")
    print("              3 of a kind(7): ", threeKind)
    print("              4 of a kind(8): ", fourKind)
    print("               Full house(9): ", fullHouse)
    print("          Small straight(10): ", smallStraight)
    print("          Large straight(11): ", largeStraight)
    print("                 Yahtzee(12): ", yahtzee)
    print("                  Chance(13): ", chance)
    print()
    print("      Total of lower section: ", totalLower)
    print("      Total of upper section: ", totalUpper)
    print("                 Grand total: ", grandTotal)
    print()


# play input
playInput = input("\nWould you like to play Yahtzee [y|n]? ").lower()

# input catcher if they don't type y or n
inputCatcher(playInput)

# score variables
oneCount = None
twoCount = None
threeCount = None
fourCount = None
fiveCount = None
sixCount = None
threeKind = None
fourKind = None
fullHouse = None
smallStraight = None
largeStraight = None
yahtzee = None
chance = None
totalLowerList = []
totalLower = sum(totalLowerList)
totalUpperList = []
totalUpper = sum(totalUpperList)
grandTotalList = []
grandTotal = sum(grandTotalList)
bonusList = []
bonus = sum(bonusList)

turnCounter = 0  # variable to show how many turns have been had
selectedScores = []  # list of scores to prevent scoring in same score
highScore = []  # list of previous scores

# while input is y
while playInput == "y":
    rolledDice = []  # rolled dice
    dieCount = [0, 0, 0, 0, 0, 0]  # counts how many of each dice number
    diceCount = 0  # counting the number of dice added

    # adds 5 dice to rolled dice list
    while diceCount < 5:
        diceNum = random.randint(1, 6)
        rolledDice.append(diceNum)
        diceCount += 1

    # displays hand, rolls dice and updates dice for 2 turns
    nextTurn()

    # displays hand
    diceDisplay()

    # displays scores
    displayScores()
    index = 1
    while index <= 6:
        dieCount[index - 1] = rolledDice.count(index)
        index += 1

    # asking user where they would like to place their score
    scoreInput = int(input("Where would you like to place your score? "))

    # if input is in selectedscores list, it will ask them to place their score again
    while scoreInput in selectedScores:
        scoreInput = int(input("You have already placed a score there. Where would you like to place your score?  "))

    # player selection gets added to the scoreboard and added to appropriate lists
    if scoreInput == 1:
        oneCount = rolledDice.count(1)
        bonusList.append(oneCount)
        totalLowerList.append(oneCount)
        grandTotalList.append(oneCount)
        selectedScores.append(scoreInput)

    # player selection gets added to the scoreboard and added to appropriate lists
    elif scoreInput == 2:
        twoCount = rolledDice.count(2)
        twoCount *= 2
        bonusList.append(twoCount)
        totalLowerList.append(twoCount)
        grandTotalList.append(twoCount)
        selectedScores.append(scoreInput)

    # player selection gets added to the scoreboard and added to appropriate lists
    elif scoreInput == 3:
        threeCount = rolledDice.count(3)
        threeCount *= 3
        bonusList.append(threeCount)
        totalLowerList.append(threeCount)
        grandTotalList.append(threeCount)
        selectedScores.append(scoreInput)

    # player selection gets added to the scoreboard and added to appropriate lists
    elif scoreInput == 4:
        fourCount = rolledDice.count(4)
        fourCount *= 4
        bonusList.append(fourCount)
        totalLowerList.append(fourCount)
        grandTotalList.append(fourCount)
        selectedScores.append(scoreInput)

    # player selection gets added to the scoreboard and added to appropriate lists
    elif scoreInput == 5:
        fiveCount = rolledDice.count(5)
        fiveCount *= 5
        bonusList.append(fiveCount)
        totalLowerList.append(fiveCount)
        grandTotalList.append(fiveCount)
        selectedScores.append(scoreInput)

    # player selection gets added to the scoreboard and added to appropriate lists
    elif scoreInput == 6:
        sixCount = rolledDice.count(6)
        sixCount *= 6
        bonusList.append(sixCount)
        totalLowerList.append(sixCount)
        grandTotalList.append(sixCount)
        selectedScores.append(scoreInput)

    # player selection gets added to the scoreboard and added to appropriate lists
    elif scoreInput == 7:
        if 3 in dieCount or 4 in dieCount or 5 in dieCount:
            threeKind = sum(rolledDice)
        else:
            threeKind = 0
        totalUpperList.append(threeKind)
        grandTotalList.append(threeKind)
        selectedScores.append(scoreInput)

    # player selection gets added to the scoreboard and added to appropriate lists
    elif scoreInput == 8:
        if 4 in dieCount or 5 in dieCount:
            fourKind = sum(rolledDice)
        else:
            fourKind = 0
        totalUpperList.append(fourKind)
        grandTotalList.append(fourKind)
        selectedScores.append(scoreInput)

    # player selection gets added to the scoreboard and added to appropriate lists
    elif scoreInput == 9:
        if 3 in dieCount and 2 in dieCount:
            fullHouse = 25
        else:
            fullHouse = 0
        totalUpperList.append(fullHouse)
        grandTotalList.append(fullHouse)
        selectedScores.append(scoreInput)

    # player selection gets added to the scoreboard and added to appropriate lists
    elif scoreInput == 10:
        if 1 in rolledDice and 2 in rolledDice and 3 in rolledDice and 4 in rolledDice:
            smallStraight = 30
        elif 2 in rolledDice and 3 in rolledDice and 4 in rolledDice and 5 in rolledDice:
            smallStraight = 30
        elif 3 in rolledDice and 4 in rolledDice and 5 in rolledDice and 6 in rolledDice:
            smallStraight = 30
        else:
            smallStraight = 0
        totalUpperList.append(smallStraight)
        grandTotalList.append(smallStraight)
        selectedScores.append(scoreInput)

    # player selection gets added to the scoreboard and added to appropriate lists
    elif scoreInput == 11:
        if 1 in rolledDice and 2 in rolledDice and 3 in rolledDice and 4 in rolledDice and 5 in rolledDice:
            largeStraight = 40
        elif 2 in rolledDice and 3 in rolledDice and 4 in rolledDice and 5 in rolledDice and 6 in rolledDice:
            largeStraight = 40
        else:
            largeStraight = 0
        totalUpperList.append(largeStraight)
        grandTotalList.append(largeStraight)
        selectedScores.append(scoreInput)

    # player selection gets added to the scoreboard and added to appropriate lists
    elif scoreInput == 12:
        if 5 in dieCount:
            yahtzee = 50
        else:
            yahtzee = 0
        totalUpperList.append(yahtzee)
        grandTotalList.append(yahtzee)
        selectedScores.append(scoreInput)

    # player selection gets added to the scoreboard and added to appropriate lists
    elif scoreInput == 13:
        chance = sum(rolledDice)
        totalUpperList.append(chance)
        grandTotalList.append(chance)
        selectedScores.append(scoreInput)

    # adds all the items to make up totallower, totalupper, grand total and bonus sum
    totalLower = sum(totalLowerList)
    totalUpper = sum(totalUpperList)
    grandTotal = sum(grandTotalList)
    bonusSum = sum(bonusList)

    # if bonussum is more than 63, user gets 25 points
    if bonusSum >= 63:
        bonus = 25
        grandTotalList.append(bonus)

    # display scores to user
    displayScores()

    # turn adds 1, once it reaches 13 it ends the game
    turnCounter += 1
    while turnCounter == 13:

        # score variables
        oneCount = None
        twoCount = None
        threeCount = None
        fourCount = None
        fiveCount = None
        sixCount = None
        threeKind = None
        fourKind = None
        fullHouse = None
        smallStraight = None
        largeStraight = None
        yahtzee = None
        chance = None
        totalLowerList = [0]
        totalLower = sum(totalLowerList)
        totalUpperList = [0]
        totalUpper = sum(totalUpperList)
        grandTotalList = [0]
        grandTotal = sum(grandTotalList)
        bonusList = [0]
        bonus = sum(bonusList)

        turnCounter = 0  # variable to show how many turns have been had
        selectedScores = []  # list of scores to prevent scoring in same score

        # play input
        playInput = input("\nThanks for playing! Do you want to play again [y|n]? ").lower()

        # input catcher if they don't type y or n
        inputCatcher(playInput)
