#ABRAHAM MCOGOL
#254790463533
#abramogol@gmail.com
#Please run everything in terminal for the sake of my return values
# validation of a credit card number

def validate_credit_card(n):
    digits = [int(x) for x in str(n)]
    for x in range(len(digits)-2, -1, -2):
        digits[x] = sum(map(int, str(digits[x] * 2)))

    print(sum(digits) % 10 == 0)
    return sum(digits) % 10 == 0
    
validate_credit_card(891)

