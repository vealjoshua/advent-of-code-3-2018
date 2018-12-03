highestW = 0
highestH = 0
totalSqIFabricWithinTwoClaims = 0
fabric = [[0] * 1000] * 1000

claims = open('resources/claims.txt', 'r')

for claim in claims:
    inchesFromTop = int(claim
                        .split('@')[1]
                        .split(',')[1]
                        .split(':')[0]
                        .strip())
    inchesFromLeft = int(claim
                         .split('@')[1]
                         .split(',')[0]
                         .strip())
    height = int(claim
                 .split(':')[1]
                 .split('x')[1]
                 .strip())
    width = int(claim
                .split(':')[1]
                .split('x')[0]
                .strip())

    while (height + inchesFromTop > len(fabric)):
        fabric.append([0] * 1000)
    while (width + inchesFromLeft > len(fabric[0])):
        for row in fabric:
            row.append([0] * 1000)

    for h in range(height):
        for w in range(width):
            fabric[inchesFromTop + h][inchesFromLeft + w] += 1

for row in range(len(fabric)):
    for column in range(len(fabric[row])):
        if (fabric[row][column] >= 2):
            totalSqIFabricWithinTwoClaims += 1

print(totalSqIFabricWithinTwoClaims)
