
def main():
    numTotal = 0
    countOnes = None
    for line in open('input.txt'):
        line = line.strip()
        if not numTotal:
            bits = len(line)
            countOnes = [0] * bits
        for index, bit in enumerate(line):
            if bit == '1':
                countOnes[index] += 1
        numTotal += 1

    resultGamma = 0
    resultEpsilon = 0
    for ones in countOnes:
        resultGamma <<= 1
        resultEpsilon <<= 1
        if ones > numTotal / 2:
            resultGamma += 1
        else:
            resultEpsilon += 1

    print('Gamma %s (%d), Epsilon %s (%d), result %d' %
          (bin(resultGamma), resultGamma,
           bin(resultEpsilon), resultEpsilon,
           resultGamma * resultEpsilon))


if __name__ == '__main__':
    main()
