## This is a program to calculate the area of a room.
## The program first takes 3 inputs (length, breadth and height),
## Calculates the area of according the the provided input
## and then prints out the results with a formatted string.
## We will create a simple function to achieve this.

def get_area(length, breadth, height):
    '''
    This function takes 3 arguments (length, breadth and height)
    and calculates the area of the room.
    '''
    area = length * breadth * height
    return area

def get_num(num):    
    while True:
        try:
            int(num)
            return int(num)
        except ValueError:
            print("Please only enter whole numbers")
            num = input("Please try again")

            


length = get_num(input("Please input the length of the room (in cm): "))
breadth = get_num(input("Please input the breadth of the room (in cm): "))
height = get_num(input("Please input the height of the room (in cm): "))

area = get_area(length, breadth, height)

print(f"The area of your room is: {area} cms")
