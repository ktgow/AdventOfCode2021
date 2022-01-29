def main():
    all_values = [int(line) for line in open('input.txt')]
    prev_window = None
    num_increasing = 0
    for i in range(len(all_values) - 2):
        window = all_values[i:i+3]
        if prev_window is not None:
            prev_sum = sum(prev_window)
            new_sum = sum(window)
            if new_sum > prev_sum:
                num_increasing += 1
        prev_window = window

    print('Num increasing: %s' % num_increasing)


if __name__ == '__main__':
    main()
