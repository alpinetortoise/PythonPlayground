print("Hello, I like neovim!")

num = 0

for i in range (0, 10):
    num = num + 2
    print ("the {}th product of 2 is {}".format(i, num))

print(int (float("201") == 201))

myList = [1,5,24,9,31]
minNum = myList[0]
for number in myList:
    if number < minNum:
        minNum = number

print ("The smallest number in the list was: {}".format(minNum))
