def love_calculator():
    print('welcome to the love calculator!')
    name1 = input('what is your name? \n')
    name2 = input('what is your lovers name? \n')
    name = list(name1 + name2)
    true_counter = 0
    love_counter = 0

    for i in name:
        if i == 'T' or i == 'R' or i == 'U' or i == 'E':
            true_counter = true_counter + 1
         
        elif i == 'L' or i == 'O' or i == 'V' or i == 'E':
            love_counter = love_counter + 1
           

    percentage = int(f'{str(true_counter)}{str(love_counter)}')



    if percentage < 10 or percentage > 90:
        print(f'the percentage is {percentage}, you go together like coke and mentos')
    elif percentage >= 40 and percentage <= 50:
        print(f'the percentage is {percentage}, you are alright together')
    else:
        print(f'the percentage is {percentage}')


    

    

        

    

            
                
if __name__ == '__main__':
    love_calculator()