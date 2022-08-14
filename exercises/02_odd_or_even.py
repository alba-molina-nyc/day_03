def odd_or_even_nums():
    number = int(input('which number do you want to check'))
    if number % 2 == 0:
        print(f'{number} is an even number')
    else:
        print(f'{number} is NOT an even number')

    return number


if __name__ == '__main__':
    # print(trapping_water_problem([1, 0, 2, 1, 3, 1, 2, 0, 3]))
    odd_or_even_nums()
