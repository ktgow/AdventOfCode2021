def main():
    prev_value = None
    num_increasing = 0;
    for line in open('input.txt'):
        value = int(line)
        if prev_value is not None and value > prev_value:
            num_increasing += 1
        prev_value = value

    print('Num increasing: %s' % num_increasing)


if __name__ == '__main__':
    main()
