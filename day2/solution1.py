def main():
    horizontal = 0
    depth = 0
    for line in open('input.txt'):
        command, value = line.split(' ')
        value = int(value)
        if command == 'forward':
            horizontal += value
        elif command == 'down':
            depth += value
        elif command == 'up':
            depth -= value
    print('Horizontal %d, Depth %d, Multiplied %d' %
          (horizontal, depth, horizontal * depth))


if __name__ == '__main__':
    main()
