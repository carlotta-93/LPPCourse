import random


def die():
    x = random.randint(1, 6)
    return x


def dice():
    die1 = die()
    die2 = die()
    print die1, die2
    return die1 + die2

print dice()
