def love_calculator():
    print('welcome to the love calculator!')
    name1 = input('what is your name? \n')
    name2 = input('what is your lovers name? \n')
    name = list(name1 + name2)
    # print(name)
    true_counter = 0
    love_counter = 0
    # count number of times T R U E L O V E occurs in your name whatever 
    # percentage 

    for i in name:
        if i == 'T' or i == 'R' or i == 'U' or i == 'E':
            true_counter = true_counter + 1
            print(f'{true_counter} @ {i} for TRUE')
          
        elif i == 'L' or i == 'O' or i == 'V' or i == 'E':
            love_counter = love_counter + 1
            print(f'{love_counter} @ {i} for LOVE')
        
    print(f'{true_counter}{love_counter}%')
    # return true_counter + love_counter + '%'
    

            
                
if __name__ == '__main__':
    love_calculator()