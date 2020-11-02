from itertools import permutations
import random

comb = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
finalCode = ""

def enterCode():
    finalCode = int(input("Enter your code (4 unique digits) : "))
    if (finalCode < 1234 or finalCode > 9876):
        print("Enter a correct code (4 unique digits)")
        exit()
    
def createProp():
    return comb[random.randint(0, (len(comb) - 1))]

def enterResult():
    if (len(comb) > 1):
        currentProp = createProp()
    else:
        currentProp = comb[0]
    print("Here is my guess :")
    print(currentProp)
    result = str(input("Enter result (goodPlace,badPlace | eg. : 1,2) : "))
    results = (result.split(','))
    if (int(results[0]) > 4 or int(results[0]) < 0 or int(results[1]) > 4 or int(results[1]) < 0 or len(results) > 2 or ((int(results[0]) + int(results[1])) > 4)):
        print("Enter a correct result (goodPlace,badPlace | eg. : 1,2)")
        quit()
    if (int(results[0]) == 4):
        print("I've won !", end="")
        exit()
    else:
        getResult(results, currentProp)
        return True

def score(prop, code):
    good = 0
    bad = 0
    i = 0
    for i in range(4):
        if (int(prop[i]) == int(code[i])):
            good += 1
        elif (prop[i] in code):
            bad += 1
    return good, bad

def getResult(results, currentProp):
    rmvList = []
    for newProp in comb:
        s = score(currentProp, newProp)
        if ((int(s[0]) != int(results[0])) or (int(s[1]) != int(results[1]))):
            rmvList.append(newProp)

    for i in range(len(rmvList)):
        comb.remove(rmvList[i])

enterCode()
while (enterResult()):
    enterResult()