import csv
# Open file to be Object
exampleFile = open('example.csv')
# Read from csv function
exampleReader = csv.reader(exampleFile)
# Change to list type
exampleData = list(exampleReader)
print(exampleData)
# Read list[row][cloumn] 
x = exampleData[0][0]
print(x)
x = exampleData[0][1]
print(x)
x = exampleData[0][2]
print(x)
x = exampleData[1][1]
print(x)
x = exampleData[6][1]
print(x)
# show every row
for row in exampleData:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))