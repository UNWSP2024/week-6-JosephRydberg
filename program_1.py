from random import randrange
#Random Dice Average Joseph Rydberg 10/7/2024

def randDice():
    num1 = randrange(1, 7, 1)
    num2 = randrange(1, 7, 1)
    return num1 + num2

def main():
    totalRolls = 0
    totalValue = 0
    while totalRolls < 100:
        totalRolls += 1
        totalValue += randDice()

    if totalRolls == 100:
        print(totalValue / totalRolls)

main()