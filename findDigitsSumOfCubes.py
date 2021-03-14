def findDigitsSumOfCubesBruteForce(limit, debug=False):
    digits = []
    for a in range(limit):
        for b in range(limit):
            for c in range(limit):
                for d in range(limit):
                    if a**3 + b**3 == c**3 + d**3:
                        digits.append((a,b,c,d))
                        if debug:
                            print((a,b,c,d))
    return digits

def findDigitsSumOfCubes(limit, debug=False):
    digitCombinations = []
    sums = dict()
    for a in range(limit):
        for b in range(limit):
            sumValue = a**3 + b**3
            if sumValue in sums:
                for pair in sums[sumValue]:
                    c, d = pair
                    digitCombinations.append((a,b,c,d))
                    if debug:
                        print((a,b,c,d))
            else:
                sums[sumValue] = set()
            sums[sumValue].update([(a, b)])

    return digitCombinations

combinations = findDigitsSumOfCubes(1000)
print('Total %d' % len(combinations))
