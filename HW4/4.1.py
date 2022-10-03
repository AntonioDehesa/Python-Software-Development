from collections import Counter
from random import randrange

def rollDice(rolls: int = 0):
    results = []
    for _ in range(rolls):
        results.append(randrange(6) + 1)
    return Counter(results)

def countRollResults(rolls: Counter, *args: int):
    if args:
        return rolls.most_common(args[0])    
    return rolls.most_common()


if __name__ == "__main__":
    rolls = rollDice(100)
    print(countRollResults(rolls,3))