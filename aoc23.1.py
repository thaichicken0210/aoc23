input = []
with open("aoc23.input1.txt") as f:
  input = [line.strip() for line in f.readlines()]

# for each string in the calibration document
# find the first and last digit
calibration = []
for i in range(1000):
  test_string = input[i]
  
  numbers = []
  for char in test_string:
    if char.isdigit():
     numbers.append(char)
  calibration.append([numbers[0],numbers[-1]])
# print(calibration)

# concatenate those digits into new strings
calinteger = []
for j in range(1000):
  calinteger.append(int(calibration[j][0]+calibration[j][1]))

# change the new strings to integers
#     jk didn't need to do that bc i could build it in in line 21

# sum up all the integers
print(sum(calinteger))