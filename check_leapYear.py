#1.Basic If-Else Method
#Time Complexity: O(1) — Only 3 modulus and a few logical operations.
#Space Complexity: O(1) — One integer variable year.
year = int(input("Enter a year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#2.Using Function
# Time Complexity: O(1) — Same logic as above.
# Space Complexity: O(1) — Extra for function call (but constant).
def is_leap(year):
    if (year % 4 == 0 and year %100 !=0)or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
        
is_leap(2002)
is_leap(2024)
is_leap(1900)

#3.Using Nested If statements 
# Time Complexity: O(1) — At most 3 modulus and comparisons.
# Space Complexity: O(1) — Same.
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
# Time Complexity: O(1) — Internally uses same logic.
# Space Complexity: O(1) — Only loads a lightweight module, no extra data used.
import calendar

year = int(input("Enter a year: "))
if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#5.Leap year for a Range of Years
# Time Complexity: O(n) — where n = end - start + 1
# Space Complexity: O(1) — Only one loop variable; no extra memory used.
start_year = int(input("Enter start year: "))
end_year = int(input("Enter end year: "))

print("Leap years between", start_year, "and", end_year, "are:")

for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)
