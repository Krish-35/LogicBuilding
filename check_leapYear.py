def is_leap(year):
    if (year % 4 == 0 and year %100 !=0)or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
        
is_leap(2002)
is_leap(2024)
is_leap(1900)