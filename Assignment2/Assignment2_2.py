#Write a program which accept one number and display below pattern.

#--------------------------------------------------------------------------
def PrintPattern(x):
          for i in range(x):
                    for j in range(x):
                              print("*",end="  ")
                    print("\n")


S
x=(int(input("Enter the  number")))
PrintPattern(x)
