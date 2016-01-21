test = "10,4"

testSplit = test.split(',')
n = int(testSplit[0])
m = int(testSplit[1])
print n - (n // m * m)
