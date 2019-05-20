#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

#---------------------------------------------------------------------------------------------------------------------------------------------
def Number(x):
        
          if (x%5 ==0):
                    print("Number is divisible by 5")
          else:
                    print("Number is  not divisible by 5")


x=(int(input("Enter the  number")))
Number(x)
