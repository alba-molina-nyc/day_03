def bmi_calculator():
    height = float(input('please enter your height in m: '))
    weight = float(input('please enter your weight in kg: '))
    bmi = weight / height ** 2
    bmi_as_int = int(bmi)
    # print(f'your bmi is {bmi}')
    # print(f'your bmi as int is {bmi_as_int}')

    if bmi <= 18:
        print(f'your bmi is {bmi} and you are underweight')
    elif bmi > 18.5:
        print(f'your bmi is {bmi} and you have a normal weight')
    elif bmi > 25:
        print(f'your bmi is {bmi} and you are overweight')
    elif bmi > 30:
        print(f'your bmi is {bmi} and you are obese')
    else:
        print(f'your bmi is {bmi_as_int} and you are clinically obese')


if __name__ == '__main__':
    bmi_calculator()


    # please enter your weight in kg: 66.6781
    # please enter your height in m: 1.63