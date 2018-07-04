print "X"*75
print '''This program takes your information and creates a secure password
for you too use'''
print """Date Created: April 22nd, 2017
Created by: Quinten"""
print "X"*75

'''This program takes your information and creates a secure password
for you too use'''

#Gets users information
name_first = raw_input("What is your first name? ")
name_last = raw_input("What is your last name? ")
date_year = str(input("What year were you born in? "))
date_day = str(input("What day were you born on? "))
special_character = raw_input("Enter a special character to make your password more secure: ")

#Makes the users last name capitalized
name_capital = name_last.upper()
name_lower = name_first.lower()

#Prints the secure password
print name_first, "Your new secure password is" 
print name_capital[:3] + name_lower[:3] + date_year[:2] + date_day + special_character