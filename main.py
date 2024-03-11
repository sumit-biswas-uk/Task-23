def get_area(length, breadth, height):
    area = length * breadth * height
    return area

length = int(input("Please input the length of the room (in cm): "))
breadth = int(input("Please input the breadth of the room (in cm): "))
height = int(input("Please input the height of the room (in cm): "))

area = get_area(length, breadth, height)

print(f"The area of your room is: {area} cms")
