import random
import string

target = "To be or not to be"  # Length 18


def FitnessFunction(randomString):
    correct_list = []

    # Tilføjer 1 til correct_list, hvis char'en passer til char'en på target tekst-strengen. Ellers tilføjes 0 på denne plads i correct_list.
    for i in range(len(target)):
        if randomString[i] == target[i]:
            correct_list.append(1)
        else:
            correct_list.append(0)
    return correct_list


def GeneratingRandomString(highestFitness):
    newstring = []

    for i in range(len(target)):
        if highestFitness[i] != target[i]:
            char = ''.join(random.choice(string.ascii_letters + ' '))
            newstring.append(char)
        else:
            newstring.append(highestFitness[i])

    return newstring


def TenThousandRandomStringsAndFitnessFunction():
    randomStrings = []
    highestFitness = [0] * len(target)

    # Generate 10000 random strings, calculate score, store it in object of RandomString and saves it in list
    for i in range(10000):
        randomString = GeneratingRandomString(highestFitness)
        score = FitnessFunction(randomString).count(1)
        r = RandomString(randomString,score)
        randomStrings.append(r)

    rmax = RandomString("",0)

    for i in randomStrings:
        if i.score > rmax.score:
            rmax = i

    print(rmax.random_string)
    print(str(rmax.score))



class RandomString():
    def __init__(self, random_string, score):
        self.random_string = random_string
        self.score = score


def HillClimbing():
    randomStrings = []
    highestFitness = [0]*len(target)
    highestFitnessStr = ""
    iterations = 0

    while(highestFitnessStr != target):
        for i in range(10000):
            randomString = GeneratingRandomString(highestFitness)
            score = FitnessFunction(randomString).count(1)
            r = RandomString(randomString, score)
            randomStrings.append(r)

        rmax = RandomString("", 0)

        # Find RandomString-element with highest score
        for i in randomStrings:
            if i.score > rmax.score:
                rmax = i

        highestFitness = rmax.random_string
        highestFitnessStr = ''.join(highestFitness)
        iterations += 1

    print(highestFitnessStr + "\nIterationer: " + str(iterations))


def crossOver(a,b):

    length = int(len(a.random_string) / 2)
    string1_1 = a.random_string[:length]
    string1_2 = a.random_string[length:]
    string2_1 = b.random_string[:length]
    string2_2 = b.random_string[length:]

    string1 = string1_1 + string2_2
    string2 = string2_1 + string1_2

    children = [string1,string2]
    rand = random.randint(0,len(children)-1)

    return children[rand]


def createProbabilityList(randomStrings):
    probabilityList = []

    for i in randomStrings:
        for j in range(i.score):
            probabilityList.append(i)

    return probabilityList


def mutateChild(child, rate):

    mutatedChild = []

    for i in range(len(child)):
        rand = random.randint(0, 100)
        if rand < (rate * 100):
            char = ''.join(random.choice(string.ascii_letters + ' '))
            mutatedChild.append(char)
        else:
            mutatedChild.append(child[i])

    return mutatedChild



def GA():
    randomStrings = []
    highestFitness = [0]*len(target)
    highestFitnessStr = ""
    iterations = 0

    for i in range(1000):
        randomString = GeneratingRandomString(highestFitness)
        score = FitnessFunction(randomString).count(1)
        r = RandomString(randomString, score)
        randomStrings.append(r)

    randomStrings.sort(key=lambda x: x.score, reverse=True)

    counter = 0
    children = []

    while highestFitnessStr != target:

        if counter >= 1000:
            children.sort(key=lambda x: x.score, reverse=True)
            randomStrings = children
            iterations = iterations + 1
            highestFitnessStr = ''.join(randomStrings[0].random_string)
#            print("-------------------- Iteration -------------------------")
#            print(iterations)
#            print(highestFitnessStr)
            counter = 0

        # Hvert string gemmes med antallet af dens fitness-score, således at en string med en høj score vil optage flere pladser end en string med en lavere fitness
        probabilityList = createProbabilityList(randomStrings[:5])
        rand1 = random.randint(0,len(probabilityList)-1)
        a = probabilityList[rand1]
        rand2 = random.randint(0,len(probabilityList)-1)
        b = probabilityList[rand2]
        child = crossOver(a,b)
        mutatedChild = mutateChild(child,rate=0.02)
        mutatedChild_score = FitnessFunction(mutatedChild).count(1)
        r = RandomString(mutatedChild, mutatedChild_score)
        children.append(r)

        counter = counter + 1

    print(highestFitnessStr)
    print("Iterationer: " + str(iterations))



print("Opgave 3.b:")
TenThousandRandomStringsAndFitnessFunction()

print("\nOpgave 3.c:")
HillClimbing()

print("\nOpgave 3.d:")
# Tilføj argumenter til GA
GA()



