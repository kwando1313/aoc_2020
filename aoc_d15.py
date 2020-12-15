import math
import itertools

my_file = open("day15.txt", "r")
#my_file = open("day15_sample.txt", "r")

content = my_file.readlines()

numbers = []

for c in content:
    numbers.append(int(c.strip("\n")))
game = []
print len(numbers)
i = 0
prev = {}
while i < 30000000:
    if i < len(numbers):
        game.append(numbers[i])
        prev[numbers[i]] = i
    elif i != 0 and game[i-1] in prev:
        most_recent = i - 1 - prev[game[i-1]]
        game.append(most_recent)
        prev[game[i-1]] = i - 1
    elif i != 0 and game[i-1] not in prev:
        game.append(0)
        prev[game[i-1]] = i - 1
    i = i + 1

#print game
print game[30000000-1]