import random


def coin_toss(heads_prob=0.5):
    """ Return heads or tails with a specified probability """
    c = random.random()
    if c < heads_prob:
        return "head"
    else:
        return "tail"
