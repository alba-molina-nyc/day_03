# def order_pizza():
#     print('welcome to Python Pizza Deliveries')
#     size = input('what size pizza do you want S, M, or L?: ')
#     add_pepperoni = input('do you want pepperoni? Y or N: ')
#     extra_cheese = input('do you want extra cheese? Y or N: ')
#     price = 0

#     if size == 'S':
#         price = 15
#         print(f'small pizza ${price}')
#         if add_pepperoni == 'Y':
#             price += 2
#             print(f'add pepperoni + pepperoni ${price}')
#         if extra_cheese == 'Y':
#             price +=1
#             print(f'add pepperoni + extra cheese ${price}')
#     elif size == 'M':
#         price = 20
#         print(f'medium pizza ${price}')
#         if add_pepperoni == 'Y':
#             price += 3
#             print(f'add pepperoni + pepperoni ${price}')
#         if extra_cheese == 'Y':
#             price +=1
#             print(f'add pepperoni + extra cheese ${price}')
#     elif size == 'L':
#         price = 25
#         print(f'large pizza ${price}')
#         if add_pepperoni == 'Y':
#             price += 3
#             print(f'add pepperoni + pepperoni ${price}')
#         if extra_cheese == 'Y':
#             price +=1
#             print(f'add pepperoni + extra cheese ${price}')
#     else:
#         print(f'something else')

def order_pizza():
    print('welcome to Python Pizza Deliveries')
    size = input('what size pizza do you want S, M, or L?: ')
    add_pepperoni = input('do you want pepperoni? Y or N: ')
    extra_cheese = input('do you want extra cheese? Y or N: ')
    bill = 0

    if size == 'S':
        bill = 15
        print(f'small pizza ${bill}')
       
    elif size == 'M':
        bill = 20
        print(f'medium pizza ${bill}')
        
    else: 
        bill = 25
        print(f'large pizza ${bill}')
    
    
    if add_pepperoni == 'Y':
        if size == 'S':
            bill += 2
        else:
            bill += 3
    if extra_cheese == 'Y':
        bill += 1
    print(f'your final bill is ${bill}')

if __name__ == '__main__':
    order_pizza()