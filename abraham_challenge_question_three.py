#ABRAHAM MCOGOL
#254790463533
#abramogol@gmail.com
#Please run everything in terminal for the sake of my return values

#I WAS EXPECTED TO DO THIS IN JS HOWEVER I KEPT GETTING ERRORS SO I DECIDED TO DO IT IN PYTHON


# This palindrome should be in js but I thought I should do it in py just for ease
def palindromeChainLength():
	n=int(input("Enter number:"))
	temp=n
	rev=0
	while(n>0):
		dig=n%10
		rev=rev*10+dig
		n=n//10
	if(temp==rev):
		print("The number is a palindrome!")
	else:
		print("The number isn't a palindrome!")

palindromeChainLength()