import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print ' '.join(reversed(test.split()))
test_cases.close()
