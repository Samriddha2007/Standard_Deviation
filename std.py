import math
import csv
with open('class1.csv',newline='') as file:
    reader = csv.reader(file)
    fileData = list(file)

data = fileData[0]

def mean(data):
    n = len(data)
    sum = 0
    for i in data:
        sum = sum+ int(i)

    mean = sum/n
    return mean

squaredList = []


for j in data:
    a = int(j)-mean(data)
    a = a**2
    squaredList.append(a)

total = 0

for x in squaredList:
    total = total + x

result = total/(len(data)-1)
std = math.sqrt(result)
print(std)



