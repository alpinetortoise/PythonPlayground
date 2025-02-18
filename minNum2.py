myList = [1,0,24,9,31]
minSet = False
minNumber = 0
for number in myList:
    if number < minNumber OR minNumber == 0:
        minNumber = number

print("The minimum number in the list was: {}".format(minNumber))
