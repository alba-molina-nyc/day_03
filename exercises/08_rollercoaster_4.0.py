def photo_roller_coaster():
    print('welcome to the rollercoaster')
    height = int(input('what is your height in cm? '))
    bill = 0 

    if height >= 120:
        print('you can ride the roller coaster')
        age = int(input('what is your age? '))
        if age < 12:
            bill = 5
            print(f'your bill is {bill}')
        elif age >= 12 and age <= 18:
            bill = 7
            print(f'your bill is {bill}')
        elif age >= 45 and age <= 55:
            print(f'your bill is {bill}')
        else:
            bill = 12
            print(f'your bill is {bill}')
            
        wants_photo = input('Do you want your photo taken Y or N?: ')
        if wants_photo == 'Y':
            bill += 3
            print(f'your bill is {bill}')
        print(f'your bill is {bill}')
    else:
        print(f'you cannot ride the rollercoaster')

# separate price between 45 and 55 ride for free
if __name__ == '__main__':
    photo_roller_coaster()