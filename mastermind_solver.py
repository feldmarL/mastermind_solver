from itertools import permutations
import random

comb = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
    
def createProp():
    return comb[random.randint(0, (len(comb) - 1))]

def enterResult():
    if (len(comb) > 1):
        currentProp = createProp()
    else:
        currentProp = comb[0]
    print(f"Here is my guess : {currentProp}")
    result = "9,9"
    while (int(result[0]) > 4 or int(result[0]) < 0 or int(result[2]) > 4 or int(result[2]) < 0 or len(result) > 3 or ((int(result[0]) + int(result[2])) > 4)):
        result = str(input("Enter result (goodPlace,badPlace | eg. : 1,2) : "))
    if (int(result[0]) == 4):
        print(f"I've won ! You code was {currentProp}", end="")
        exit()
    else:
        getResult(result, currentProp)
        return True

def score(prop, code):
    good = 0
    bad = 0
    for i in range(4):
        if (int(prop[i]) == int(code[i])):
            good += 1
        elif (prop[i] in code):
            bad += 1
    return good, bad

def getResult(result, currentProp):
    i = 0
    while i < len(comb):
        s = score(currentProp, comb[i])
        if ((int(s[0]) != int(result[0])) or (int(s[1]) != int(result[2]))):
            comb.pop(i)
        else:
            i += 1

while (enterResult()):
    enterResult()
