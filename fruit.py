file = open('fruitlist.txt', 'w')


for n in range(1, 11):
    fruit = input("What fruit would you like to make a list of?")
    file.write(str(n) + '.' + str(fruit) + '\n')

file.close()
