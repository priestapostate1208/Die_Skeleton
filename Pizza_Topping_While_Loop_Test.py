print("1 - cheese\n2 - veggie\n3 - salami\n4 - quit")
topping_choice= input("Enter your choice [1 - 4]:  ")
while topping_choice not in ['1','2','3','4']:
    print("This is an invalid choice: please enter a selection from 1 - 4." )
    topping_choice= input("Enter your choice [1 - 4]:  ")
    
if topping_choice =='4':
    print(f"Have a good day!")
else:
    print("Your pizza will be ready shortly!")
