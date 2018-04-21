#ABRAHAM MCOGOL
#254790463533
#abramogol@gmail.com
#Please run everything in terminal for the sake of my return values
# Three and five sum
def three_n_five(n):
    lst = [num for num in range(n) if num%3==0 or num%5==0]
    print(sum(lst))
    return sum(lst)


