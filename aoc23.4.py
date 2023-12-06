input = []
with open("inputs\\aoc23.input4.txt") as f:
  input = [line.strip() for line in f.readlines()]
mini = input[0:3]
# print(mini)

# split each card into a list of winning numbers (strings) and a list of "your" numbers (strings)
newmini = []
newminiY = []
newest = []
for m in range(len(mini)):
  newminiX = mini[m].split(": ")
  newminiY.append(newminiX)
  newminiY[m].pop(0)
 # newminiY now has [['## ## ## | ## ## ## ##'], ['## ## ## | ## ## ## ##']]
 # aka each item is a single-item list containing the whole string from a given card


# compare "your" number strings against winning number strings
# countif there are matches = n
  # if n = 0, append 0 to "TotalPoints" list
  # if n > 0, append 2^(n-1) to "TotalPoints" list
# print(sum(TotalPoints))