#ABRAHAM MCOGOL
#254790463533
#abramogol@gmail.com
#Please run everything in terminal for the sake of my return values
# moving zeros to the end

def zeros_to_end():
    lst = [1,2,4,0,3,0,4,3]
    evaluated = [i for i in lst if i!=0]
    zeros = [n for n in lst if n==0]
    for i in zeros:
        evaluated.append(i)


    print(evaluated)
    return evaluated

zeros_to_end()