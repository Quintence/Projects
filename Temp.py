#This program converts the users temperature in celsius to fahenheit
import math

print "X" * 46
print "Temperature Converter"
print "Press 1 for Celsius to Fahrenheit"
print "Press 2 for Fahrenheit to Celsius"
print "Press 3 for Celsius to Kelvin"
print "Press 4 for Fahrenheit to Kelvin"
print "Press 0 to exit"
print "X" * 46

choice = input("Enter a value: ")
#converts celsius to fahrenheit
if choice == 1:
    print "1. Celsius to Fahrenheit"
    CtoF = input("Temperature in Celsius? ")
    tempF = round((CtoF * 1.8) + 32)
    print "Your temperature in Fahrenheit is", tempF, "°"
    
    
#converts fahrenheit to celsius
if choice == 2:
    print "2. Fahrenheit to Celsius"
    FtoC = input("Temperature in Fahrenheit? ")
    tempC = round((FtoC - 32) / 1.8)
    print "Your temperature in Celsius is", tempC, "°"
    
#Converts celsius to kelvin 
if choice == 3:
    print "3. Celsius to Kelvin"
    CtoK = input("Temperature in Celsius? ")
    tempK = round(CtoK + 273.15)
    print "Your temperature in Kelvin is", tempK
    

#converts fahrenheit to celsius, then to kelvin
if choice == 4:
    print "4. Fahrenheit to Kelvin"
    FtoK = input("Temperature in Fahrenheit? ")
    FtokC = ((FtoK - 32) / 1.8)
    Ftok = round(FtokC + 273.15)
    print "Your temperature in Kelvin is", Ftok 
    
    