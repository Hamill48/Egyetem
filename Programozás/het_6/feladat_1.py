import math

positiveNumbers = []
negativeNumbers = []
negativeNumbersMultipled = []
allNumbers = []

for i in range(-100, 100):
    if i > 0:
        positiveNumbers.append(i)
    if i < 0:
        negativeNumbers.append(i)
    allNumbers.append(i)


def multiplyList():
    result = 1
    for i in negativeNumbers:
        result = i * result
    negativeNumbersMultipled.append(result)


def positiveNumbersAv():
    result = (sum(positiveNumbers) / len(positiveNumbers))
    return result

def rootNumbers():
    result = 0
    for i in positiveNumbers:
        root = math.sqrt(i)
        if root.is_integer():
            result += 1
        else:
            continue
    return result

def primeNumbers():
    result = 0
    for number in allNumbers:
        divider = 0
        for i in range(number + 1):
            if i == 0:
                continue
            elif number % i == 0:
                divider += 1
        if divider == 2:
            result += 1
    return result

print(positiveNumbersAv())
print(rootNumbers())
print(primeNumbers())