#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [1, 2, 3, 4, 5])))
print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))
print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))
print("Winner: {}".format(isWinner(4, [11, 30, 1, 7])))
print("Winner: {}".format(isWinner(1, [1])))
print("Winner: {}".format(isWinner(-1, [10])))

print("Winner: {}".format(isWinner(0, [0])))
print("Winner: {}".format(isWinner(5, [1, 2, 3, 4, 5])))