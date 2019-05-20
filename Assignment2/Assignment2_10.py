#Write a program which accept number from user and return addition of digits in that number.
#--------------------------------------------------------------------------------------------


def Number(n):
                    j=0
                    while n>0:
                              j+=n%10
                              n=n//10
                    return j

x=(int(input("Enter the number")))
y=Number(x)
print("Number of digit=",+y)
