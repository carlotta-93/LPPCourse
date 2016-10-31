import random


def coin_toss(head_prob):
    """ ddddddddddd """
    c = random.random()
    if c < head_prob:
        return "head"
    else:
        return "tail"

# print coin_toss(heads_prob=0.6)


def coin_toss(heads_prob=0.5):
    c = random.random()
    if c < heads_prob:
        return "head"
    else:
        return "tail"


print coin_toss(heads_prob=0.6)
print coin_toss()
