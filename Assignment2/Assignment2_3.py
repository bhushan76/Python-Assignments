#Write a program which accept one number from user and return its factorial.

#----------------------------------------------------------------
def Factorial(n):
          i=1
          while n>0:
                    i=i*n
                    n=n-1
          return i

x=(int(input("Enter the number")))
print("Factorial ",x,Factorial(x))
         
