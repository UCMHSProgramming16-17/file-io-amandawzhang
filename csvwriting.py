# import module
import csv
import math

# create file
csvfile = open('test.csv', 'w')

# create csvwritier
csvwriter = csv.writer(csvfile, delimiter = ',')

# write information
csvwriter.writerow(['Blah', 'Ugh', 'Jeez', 'Help', 'uhhhhhhhhh'])
csvwriter.writerow(['a', 'b', 'hypotenuse'])
for a in range (1,101):
    for b in range (1,101):
        hypotenuse = math.sqrt(a ** 2 + b ** 3)
        csvwriter.writerow(a, b, hypotenuse)
# close file
csvfile.close()