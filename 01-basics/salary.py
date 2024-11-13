# -*- coding: utf-8 -*-
"""
Functions Exercise


Write a script that calls 5 unique functions. Here's what each function should do:
    
    1. get_employee_information()
      - Should prompt the employee for their Name, Hourly Pay, and Hours Worked
      - Should return all three values
    
    2. calculate_overtime_hours()
      - Should take in the hours worked as an argument
      - Should return two values. Non-overtime hours and overtime hours (If no overtime hours, return 0)
      
    3. calculate_standard_pay()
      - Should take in the non-overtime hours and hourly_pay values, and return the calculated standard pay
      
    4. calculate_overtime_pay()
      - Should take in the overtime hours and hourly_pay values
      - Should calculate overtime pay as time and a half
      - Should ONLY be called if there are overtime hours
      
    5. display_total_pay()
      - Should take in the name, overtime pay, and standard pay
      - Should sum the standard and overtime pay
      - Should print out the following:
          "The weekly pay for <name> is $<amount>."

"""



def get_employee_information():
    name = input("What is your name? ")
    hours = 
    hourly_pay = 
    return 

def calculate_overtime_hours(hours_worked):
    


def calculate_standard_pay(hours, hourly_pay):
    return hours * hourly_pay
    
def calculate_overtime_pay(hours, hourly_pay):
    return hourly_pay * 1.5 * hours

# Create the function to display the total pay


name, hours, hourly_pay = get_employee_information()

hours, overtime_hours = calculate_overtime_hours(hours)

standard_pay = calculate_standard_pay(hours, hourly_pay)

overtime_pay = 0
if overtime_hours:
    overtime_pay = calculate_overtime_pay(hourly_pay, overtime_hours)

display_total_pay(name, standard_pay, overtime_pay)

