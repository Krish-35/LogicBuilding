#If n is odd → Weird
# If n is even and:
#   2 ≤ n ≤ 5 → Not Weird
#   6 ≤ n ≤ 20 → Weird
#   n > 20 → Not Weird

def check_weird(n):
    if n % 2 == 1:
        print("weird")
    elif n % 2 and 2<=n<=5:
        print("Not Weird")
    elif n%2 and 6 <= n <=20:
        print("Weird")
    elif n%2 and n>20:
        print("Not Weird")
        
check_weird(23)
check_weird(3)