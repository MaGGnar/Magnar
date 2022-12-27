import numpy 

print("Hello Magnar")

def randomNumber():
    numberToPrint = numpy.random.randint(1,7)
    # print(numberToPrint)
    return numberToPrint

def spinToTake():
    spin = randomNumber() * 180
    return spin

def iterator():
    i = 0
    for i in range(20):
        randomNumber()

# tricks = ["rodeo", "cork", "bio", "d-spin"]

# trickToTake = numpy.random(tricks)
# print(trickToTake)

# iterator()
print("spin to take")
print(spinToTake())

