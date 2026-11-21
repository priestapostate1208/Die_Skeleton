import math
numbers=[]
#inputted_number= int(0)
average = float(0)
counter=0
inputted_number = input("Please input a number (or press 'Enter' to quit): ")
while inputted_number != "":
    numbers.append(int(inputted_number))
    counter+=1
    average = sum(numbers)/len(numbers)
    print (average)
    print (numbers)
    inputted_number = int(input("Please input a number (or press 'Enter' to quit): "))
else:
    print("Quitting - have a nice day!")
