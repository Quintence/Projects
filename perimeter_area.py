
print "X"*75
print """This program takes calculates the area
and perimeter of your rectangle.
Date Created: April 21st, 2017
Created by: Quinten"""
print "X"*75
print """Enter 1: for area and perimeter of a rectangle
Enter 2: for area and perimeter of a triangle using Heron's Formula"""
print "X"*75

"""This program takes calculates the area
and perimeter of your rectangle, square or triangle
Date Created: April 21st, 2017
Created by: Quinten"""
import math
#Gets the users name, along with the lengths.
name = raw_input("What is your Name? ")
choice = input("Enter 1 or 2: ")
#Prints their name.
print "Hi", name
def script():
    while True:
        if choice == 1:
            print "2.Area and perimeter of a rectangle"
            a = input("Enter one side length: ")
            b = input("Enter second side length: ")
            #calculates the users area and perimeter of the given lengths.
            area = a*b
            perimeter = ((2*a)+(2*b))    
            #Prints their name, length and area.
            print "Hi", name
            print "The area is", area, "and the perimeter is", perimeter
            end = raw_input("Click Y to close")
            if end == "Y":
                    break

script()

        
        


if choice == 2:
    print "2.Area and perimeter of a triangle"
    side_one = int(input("Enter first side length: "))
    side_two = int(input("Enter second side length: "))
    side_three = int(input("Enter third side length: "))
    perimeter_two = (side_one  + side_two + side_three)/2
    area_two = round(math.sqrt(perimeter_two * (perimeter_two - side_one)*(perimeter_two - side_two)*(perimeter_two - side_three)))
    
    print name, "the area of your triangle is", area_two , "with the perimeter of", perimeter_two