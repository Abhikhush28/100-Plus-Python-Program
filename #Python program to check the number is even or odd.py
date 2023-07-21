#Python program to check the number is even or odd

num = int(input("Enter the number"))

if num % 2 == 0:
    print("The number is even")
else:
    print('The number is odd')



#Python program to check the number is even or odd
# using Function


def OddEvenCheck(num):
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print('The number is odd')
        
num1 = int(input("Enter the number"))
OddEvenCheck(num1)

