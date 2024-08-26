#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0
    if len(coins) == 0:
        return 0
    coins.sort()
    coins.reverse()
    change = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            change += 1
    if total != 0:
        return -1
    return change