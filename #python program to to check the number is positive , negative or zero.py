#python program to to check the number is positive , negative or zero

def NumberCheck(a):
    
    #checking the number is positive
    if a > 0:
        print("The number is positive")
    elif a < 0: 
        print("The number is Negative")
    else:
        print("The number is Zero")
        
        
num = float(input("Enter the number"))
NumberCheck(num)
