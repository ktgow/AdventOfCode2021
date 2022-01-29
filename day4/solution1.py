import logging
import sys
import unittest


class Board(object):
    def __init__(self, inputLines: str):
        self.board = []
        self.entryCalled = []
        for line in inputLines:
            elements = [int(s) for s in line.split(' ') if s]
            assert len(elements) == 5
            self.board.append(elements)

            called = [False] * len(elements)
            self.entryCalled.append(called)
        assert len(self.board) == 5

    def CallNumber(self, number: int) -> bool:
        logging.debug('Board: %s', self.board)
        for rowIndex, row in enumerate(self.board):
            for columnIndex, entry in enumerate(row):
                if entry == number:
                    self.entryCalled[rowIndex][columnIndex] = True

        return self.CheckForWinner()

    def CheckForWinner(self):
        for row in self.entryCalled:
            # Check if every entry in this row has been called
            if all(row):
                return True
        for columnIndex in range(len(self.board[0])):
            column = []
            for row in self.entryCalled:
                column.append(row[columnIndex])
            if all(column):
                return True

    def CalculateScore(self, lastNumber):
        unmarkedSum = 0
        for boardRow, calledRow in zip(self.board, self.entryCalled):
            for number, called in zip(boardRow, calledRow):
                if not called:
                    unmarkedSum += number
        return unmarkedSum * lastNumber


def LoadInput(inFile):
    numbersLine = inFile.readline()
    calledNumbers = [int(s) for s in numbersLine.split(',')]

    boards = []
    while True:
        emptyLine = inFile.readline()
        if emptyLine == '':
            # End of file.
            break

        boardLines = []
        for rowNum in range(5):
            line = inFile.readline().strip()
            assert(len(line)) > 0
            boardLines.append(line)
        board = Board(boardLines)
        boards.append(board)

    return calledNumbers, boards


def PlayGame(calledNumbers, boards):
    for number in calledNumbers:
        for board in boards:
            winner = board.CallNumber(number)
            if winner:
                return board.CalculateScore(number)

    
def main():
    with open('input.txt') as inFile:
        calledNumbers, boards = LoadInput(inFile)
    result = PlayGame(calledNumbers, boards)
    print('Result: %d' % result)


class Testing(unittest.TestCase):
    def test_sample_input(self):
        with open('test.txt') as inFile:
            calledNumbers, boards = LoadInput(inFile)
        result = PlayGame(calledNumbers, boards)
        self.assertEqual(result, 4512)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        sys.argv.pop()
        unittest.main()
    else:
        main()

