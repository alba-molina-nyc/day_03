def bmi_calculator():
    height = input('please enter your height in m: ')
    weight = input('please enter your weight in kg: ')
    bmi = float(weight) / float(height) ** 2
    bmi_as_int = int(bmi)
    # print(f'your bmi is {bmi}')
    # print(f'your bmi as int is {bmi_as_int}')

    if bmi_as_int <= 18:
        print('you are underweight')
    elif bmi_as_int > 18 and bmi_as_int < 25:
        print('you have a normal weight')
    elif bmi_as_int > 25 and bmi_as_int < 30:
        print('you are overweight')
    elif bmi_as_int > 30 and bmi_as_int < 35:
        print('you are obese')
    else:
        print('you are clinically obese')


if __name__ == '__main__':
    print(bmi_calculator())


    # please enter your weight in kg: 66.6781
    # please enter your height in m: 1.63