from math import sin, pi
from random import random

def celciusToFahrenheit(numbers):
    return list(map(lambda x: (x*(9/5))+32, numbers))

if __name__ == "__main__":
    inputs = [random()*1000 for _ in range(10)]
    Fahrenheit = celciusToFahrenheit(inputs)
    print("Inputs")
    print(inputs)
    print("Fahrenheit")
    print(Fahrenheit)
    sinResults = list(map(lambda x: sin(x), inputs)) #We could just pass the function sin as is
    print("Sin of x of the numbers in the Fahrenheit list")
    print(sinResults)
    #we could have displayed them directly by passing lambda x: print(sin(x)), but this way
    #its easier to use the filter method
    sinResults = list(filter(lambda x: x >= 0 ,sinResults))
    print(sinResults)