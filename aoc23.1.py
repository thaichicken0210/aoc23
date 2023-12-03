input = []
with open("inputs\\aoc23.input1.txt") as f:
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
# print(sum(calinteger))

# PART TWO

#find and replace all text numbers with digits

# find the new first and last digit
calibration2 = []
for i in range(1000):
  test_string = input[i]
  
  numbers = []
  for char in test_string:
    if char.isdigit():
     numbers.append(char)
  calibration2.append([numbers[0],numbers[-1]])
# print(calibration2)

# concatenate and convert to integers
calinteger2 = []
for k in range(1000):
  calinteger2.append(int(calibration[k][0]+calibration[k][1]))

# sum up all the integers
# print(sum(calinteger2))