import sys


def CountOnesFromInput(values):
    countOnes = None
    for line in values:
        if countOnes is None:
            bits = len(line)
            countOnes = [0] * bits
        for index, bit in enumerate(line):
            if bit == '1':
                countOnes[index] += 1

    return countOnes


def KeepMostCommon(onesCount, totalLength):
    if onesCount >= totalLength / 2:
        return '1'
    return '0'


def KeepLeastCommon(onesCount, totalLength):
    if onesCount < totalLength / 2:
        return '1'
    return '0'


def FilterValues(values, KeepBitDecider):
    for bit in range(len(values[0])):
        if len(values) == 1:
            break
        countOnes = CountOnesFromInput(values)
        keep = KeepBitDecider(countOnes[bit], len(values))
        values = [field for field in values
                  if field[bit] == keep]
        print('Bit %d, keeping %s, %d values remaining' % (
            bit + 1, keep, len(values)))
    return values[0]


def main():
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    else:
        fileName = 'input.txt'
    values = [line.strip() for line in open(fileName)]

    oxygenField = FilterValues(values, KeepMostCommon)
    oxygenValue = int(oxygenField, 2)
    print('Oxygen %s (%d)' % (oxygenField, oxygenValue))

    # Now do the other one.
    co2Field = FilterValues(values, KeepLeastCommon)
    co2Value = int(co2Field, 2)
    print('CO2 %s (%d)' % (co2Field, co2Value))

    print('Life support rating: %d' % (oxygenValue * co2Value))

if __name__ == '__main__':
    main()
