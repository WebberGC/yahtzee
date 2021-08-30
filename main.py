import dice
import random


def inputCatcher(input1):
    while input1 != "y" and input1 != "n":
        print("Please enter either 'y' or 'n'\n")
        input1 = input("Would you like to play Yahtzee [y|n]? ").lower()
    return input1


def diceDisplay():
    print("\nYou rolled:")
    dice.display_hand(lockedDice)


def diceReset():
    keptDiceNum = int(input("\nHow many dice do you want to get rid of? "))
    keptDiceCount = 0
    if keptDiceNum >= 5:
        return lockedDice
    while keptDiceCount < keptDiceNum:
        keptDiceIndex = int(input("What is the die number of the die you want to get rid of? "))
        lockedDice[keptDiceIndex - 1] = 0
        keptDiceCount += 1
    return lockedDice


def newDiceNums():
    index = 0
    for num in lockedDice:
        if num == 0:
            lockedDice[index] = random.randint(1, 6)
        index += 1
    return lockedDice


def nextTurn():
    diceDisplay()
    diceReset()
    newDiceNums()


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
    print("      Total of lower section: ", totalLower)
    print("      Total of upper section: ", totalUpper)
    print("                 Grand total: ", grandTotal)
    print()


# play input
playInput = input("\nWould you like to play Yahtzee [y|n]? ").lower()

# input catcher if they don't type y or n
inputCatcher(playInput)

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
turnCounter = 0

# while input is y
while playInput == "y" and turnCounter < 13:
    lockedDice = []  # locked dice
    dieCount = [0, 0, 0, 0, 0, 0]
    diceCount = 0  # counting the number of dice added

    # adds 5 dice to rolled dice list
    while diceCount < 5:
        diceNum = random.randint(1, 6)
        lockedDice.append(diceNum)
        diceCount += 1

    # displays hand, rolls dice and updates dice for 2 turns
    nextTurn()
    nextTurn()

    # displays hand
    diceDisplay()

    # displays scores
    displayScores()
    index = 1
    while index <= 6:
        dieCount[index - 1] = lockedDice.count(index)
        index += 1

    scoreInput = int(input("Where would you like to place your score? "))

    if scoreInput == 1:
        oneCount = lockedDice.count(1)
        bonusList.append(oneCount)
        totalLowerList.append(oneCount)
        grandTotalList.append(oneCount)

    elif scoreInput == 2:
        twoCount = lockedDice.count(2)
        twoCount *= 2
        bonusList.append(twoCount)
        totalLowerList.append(twoCount)
        grandTotalList.append(twoCount)

    elif scoreInput == 3:
        threeCount = lockedDice.count(3)
        threeCount *= 3
        bonusList.append(threeCount)
        totalLowerList.append(threeCount)
        grandTotalList.append(threeCount)

    elif scoreInput == 4:
        fourCount = lockedDice.count(4)
        fourCount *= 4
        bonusList.append(fourCount)
        totalLowerList.append(fourCount)
        grandTotalList.append(fourCount)

    elif scoreInput == 5:
        fiveCount = lockedDice.count(5)
        fiveCount *= 5
        bonusList.append(fiveCount)
        totalLowerList.append(fiveCount)
        grandTotalList.append(fiveCount)

    elif scoreInput == 6:
        sixCount = lockedDice.count(6)
        sixCount *= 6
        bonusList.append(sixCount)
        totalLowerList.append(sixCount)
        grandTotalList.append(sixCount)

    elif scoreInput == 7:
        if 3 in dieCount:
            threeKind = sum(lockedDice)
        else:
            threeKind = 0
        totalUpperList.append(threeKind)
        grandTotalList.append(threeKind)

    elif scoreInput == 8:
        if 4 in dieCount:
            fourKind = sum(lockedDice)
        else:
            fourKind = 0
        totalUpperList.append(fourKind)
        grandTotalList.append(fourKind)

    elif scoreInput == 9:
        if 3 in dieCount and 2 in dieCount:
            fullHouse = 25
        else:
            fullHouse = 0
        totalUpperList.append(fullHouse)
        grandTotalList.append(fullHouse)

    elif scoreInput == 10:
        if 1 in lockedDice and 2 in lockedDice and 3 in lockedDice and 4 in lockedDice:
            smallStraight = 30
        elif 2 in lockedDice and 3 in lockedDice and 4 in lockedDice and 5 in lockedDice:
            smallStraight = 30
        elif 3 in lockedDice and 4 in lockedDice and 5 in lockedDice and 6 in lockedDice:
            smallStraight = 30
        else:
            smallStraight = 0
        totalUpperList.append(smallStraight)
        grandTotalList.append(smallStraight)

    elif scoreInput == 11:
        if 1 in lockedDice and 2 in lockedDice and 3 in lockedDice and 4 in lockedDice and 5 in lockedDice:
            largeStraight = 40
        elif 2 in lockedDice and 3 in lockedDice and 4 in lockedDice and 5 in lockedDice and 6 in lockedDice:
            largeStraight = 40
        else:
            largeStraight = 0
        totalUpperList.append(largeStraight)
        grandTotalList.append(largeStraight)

    elif scoreInput == 12:
        if 5 in dieCount:
            yahtzee = 50
        else:
            yahtzee = 0
        totalUpperList.append(yahtzee)
        grandTotalList.append(yahtzee)

    elif scoreInput == 13:
        chance = sum(lockedDice)
        totalUpperList.append(chance)
        grandTotalList.append(chance)

    totalLower = sum(totalLowerList)
    totalUpper = sum(totalUpperList)
    grandTotal = sum(grandTotalList)
    bonus = sum(bonusList)

    displayScores()

    turnCounter += 1

