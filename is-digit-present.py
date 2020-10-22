# Python program to print the number which 
# contain the digit d from 0 to n 
  
# Returns true if d is present as digit 
# in number x. 
def isDigitPresent(x, d): 
    # Breal loop if d is present as digit 
    if (x > 0): 
        if (x % 10 == d): 
            return(True)
        else:
            return(False)
    else:
            return(False)
  
# function to display the values 
def printNumbers(n, d): 
    # Check all numbers one by one 
    for i in range(0, n+1):
        # checking for digit 
        if (i == d or isDigitPresent(i, d)): 
            print(i,end=" ") 
  
# Driver code 
n = 20
d = 5
print("n is",n)
print("d is",d)
print("The number of values are") 
printNumbers(n, d) 

'''
******************* output **********************
n is 47
d is 7
The number of values are
7 17 27 37 47

n is 20
d is 5
The number of values are
5 15 

'''
