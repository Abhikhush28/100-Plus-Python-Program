# Python program to Convert kilometer to miles 
# 1 kilometer equals 0.62137
# so, Miles = kilometer * 0.62137
# and , kilometer = miles/0.62137

kilometer_1 = float(input("Enter the car speed as unit of kilometer"))
conversation_unit = 0.62137
 
Miles = kilometer_1 * conversation_unit
 
print("The number of miles is ", Miles)


# Python program to Convert kilometer to miles 
# 1 kilometer equals 0.62137
# so, Miles = kilometer * 0.62137
# and , kilometer = miles/0.62137
# using Function

def kilometer_2(km):
    conversation_ratio = 0.62137
    miles = km * conversation_ratio
    
    print("The speed of the car in the value of miles", miles)

kilometer3 = int(input("Enter the speed of the car as kilometer"))
kilometer_2(kilometer3)
