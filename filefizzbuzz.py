
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if test:
        # 'test' represents the test case, do something with it
        testSplit = test.split(' ')
        x = int(testSplit[0])
        y = int(testSplit[1])
        n = int(testSplit[2])
        res = ''
        for i in range(1, n+1):
            if i % x == 0 and i % y == 0:
                res += 'FB '
            elif i % x == 0:
                res += 'F '
            elif i % y == 0:
                res += 'B '
            else:
                if i == n:
                    res += str(i)
                else:
                    res += str(i) + ' '
        print res.strip()

test_cases.close()
