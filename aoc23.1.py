input = []
with open("inputs\\aoc23.input1.txt") as f:
  input = [line.strip() for line in f.readlines()]

# for each string in the calibration document
# find the first and last digit
calibration = []
for i in range(len(input)):
  test_string = input[i]
  
  numbers = []
  for char in test_string:
    if char.isdigit():
     numbers.append(char)
  calibration.append([numbers[0],numbers[-1]])
# print(calibration)

# concatenate those digits into new strings
calinteger = []
for j in range(len(calibration)):
  calinteger.append(int(calibration[j][0]+calibration[j][1]))

# change the new strings to integers
#     jk didn't need to do that bc i could build it in in line 21

# sum up all the integers
# print(sum(calinteger))

# PART TWO

#find and replace all text numbers with digits
alldigits = []
# mini = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']
# for m in range(len(mini)):
#   newmini1 = mini[m].replace('one','o1ne')
#   newmini2 = newmini1.replace('two','t2wo')
#   newmini3 = newmini2.replace('three','t3hree')
#   newmini4 = newmini3.replace('four','f4our')
#   newmini5 = newmini4.replace('five','f5ive')
#   newmini6 = newmini5.replace('six', 's6ix')
#   newmini7 = newmini6.replace('seven','s7even')
#   newmini8 = newmini7.replace('eight','e8ight')
#   newmini9 = newmini8.replace('nine','n9ine')
#   alldigits.append(newmini9)

for m in range(len(input)):
  newinput1 = input[m].replace('one','o1ne')
  newinput2 = newinput1.replace('two','t2wo')
  newinput3 = newinput2.replace('three','t3hree')
  newinput4 = newinput3.replace('four','f4our')
  newinput5 = newinput4.replace('five','f5ive')
  newinput6 = newinput5.replace('six', 's6ix')
  newinput7 = newinput6.replace('seven','s7even')
  newinput8 = newinput7.replace('eight','e8ight')
  newinput9 = newinput8.replace('nine','n9ine')
  alldigits.append(newinput9)

# print(alldigits)



# find the new first and last digit
calibration2 = []
for i in range(len(alldigits)):
  test_string = alldigits[i]
  
  numbers = []
  for char in test_string:
    if char.isdigit():
     numbers.append(char)
  calibration2.append([numbers[0],numbers[-1]])
# print(calibration2)

# concatenate and convert to integers
calinteger2 = []
for k in range(len(calibration2)):
  calinteger2.append(int(calibration2[k][0]+calibration2[k][1]))

# sum up all the integers
print(sum(calinteger2))