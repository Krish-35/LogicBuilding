def check_div(num):
    if num % 5 == 0 and num % 11 ==0:
        print(f"{num} is divisible by both 5 and 11.")
    else:
        print(f"{num} is NOT divisible by both 5 and 11")
        
check_div(32)
check_div(25)
check_div(55)