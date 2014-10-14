import sys
newFile = open(sys.argv[1], 'r')
for line in newFile:
    sequence = line.strip().split(',')
    uniqueElements = []
    [uniqueElements.append(i) for i in sequence if not uniqueElements.count(i)]
    print(",".join(uniqueElements))
newFile.close()
