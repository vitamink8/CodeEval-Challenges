""" Having a string representation of a set of numbers you need to print
 this numbers.

All numbers are separated by semicolon. There are up to 20 numbers in one line. The numbers are "zero" to "nine"
"""

numDict = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5,
           "six":6, "seven":7, "eight":8, "nine":9}

def wordInt(words):
    splitWords = words.strip().split(";")
    res = ''
    for word in splitWords:
        res += str(numDict[word])
    return res
