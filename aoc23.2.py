input = []
with open("inputs\\aoc23.input2.txt") as f:
  input = [line.strip() for line in f.readlines()]

# convert input to some useable format
  # each item in input is a semicolon-separated list
  # the format needs to beconverted into a list of lists
  # regex replace ': ' with ': [' and '; ' with '], [' and end-of-line with ']'
  # no, that's messy bc then there are still numbers stored as strings
  # each item in input should become a list of dictionaries?
mini = input[0:5]
GameList = []
newminiY = []
PullList = []
for m in range(len(mini)):
  newminiX = mini[m].split(": ")
  newminiY.append(newminiX)
  newminiY[m].pop(0)
  newminiZ = newminiY[m][0]
  GameList.append(newminiZ)
  # list "GameList" has items that are a whole game's worth of pulls
  # i.e. ['2 red, 2 green; 1 red', '5 green, 4 red; 7 blue']

for i in range(len(GameList)):
  PullList.append(GameList[i].split("; "))
  # list "PullList" now contains smaller lists, each containing strings of pulls
  # i.e. [['2 red, 2 green', '1 red'], ['5 green, 4 red', '7 blue']]
  # where this^ is game 1           and         ^this is game 2


final_list = []
semifinal_list = []
for j in range(len(PullList)):
  for h in range(len(PullList[j])):
    semifinal_list.append(PullList[j][h].split(", "))
    # semifinal_list now contains all pulls separated by color but not by game
    # i.e. [['2 red', '2 green'], ['1 red'], ['5 green', '4 red'], ['7 blue']]
    # but what i want is an extra bracket   ^splitting it here
    # which i can't do bc not every game has the same number of pulls
# print(semifinal_list)

## stuff below here is bits i might need later but can't use yet bc the top part is broken

# for k in range(len(semifinal_list)):
#   final_list.append(semifinal_list[k].split(" "))
# print(mini[0])
# print(newest[0])
# print(newest[0][0].split(", "))

# def convert(lst):
#   res_dict = {}
#   for i in range(0, len(lst), 2):
#     res_dict[lst[i]] = lst[i + 1]
#   return res_dict
 
# lst = ['a', 1, 'b', 2, 'c', 3]
# print(convert(lst))