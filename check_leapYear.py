#1.Basic If-Else Method
year = int(input("Enter a year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#2.Using Function
def is_leap(year):
    if (year % 4 == 0 and year %100 !=0)or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
        
is_leap(2002)
is_leap(2024)
is_leap(1900)

#3.Using Nested If statements 
year = int(input("Enter a year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#4.Using python's calender Module
import calendar

year = int(input("Enter a year: "))
if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#5.Leap year for a Range of Years
start_year = int(input("Enter start year: "))
end_year = int(input("Enter end year: "))

print("Leap years between", start_year, "and", end_year, "are:")

for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)
