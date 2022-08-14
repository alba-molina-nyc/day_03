print('welcome to the rollercoaster')
height = int(input('what is your height in cm? '))




# check if height is > 120

if height >= 120:
    print('you can ride the roller coaster')
    age = int(input('what is your age? '))
    if age <= 18:
        print('you can ride the roller coaster and your ticket is $7')
    else:
        print('you can ride the roller coaster and your ticket costs $12')
else:
    print('you cannot ride the rollercoaster')