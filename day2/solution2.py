def main():
    horizontal = 0
    aim = 0
    depth = 0
    for line in open('input.txt'):
        command, value = line.split(' ')
        value = int(value)
        if command == 'forward':
            horizontal += value
            depth += value * aim
        elif command == 'down':
            aim += value
        elif command == 'up':
            aim -= value
    print('Horizontal %d, Depth %d, Aim %d, Multiplied %d' %
          (horizontal, depth, aim, horizontal * depth))


if __name__ == '__main__':
    main()
