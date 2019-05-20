#Write a program which accept number from user and check whether that number is positive or negative or zero.
#---------------------------------------------------------------------------------------------------------
def check_number(x):
        
          if x>0:
                    print("Number is positive")
          elif x<0:
                    print("Number is  negative")
          elif x==0:
                    print("Number is  zero")

x=(int(input("Enter the  number")))
check_number(x)
