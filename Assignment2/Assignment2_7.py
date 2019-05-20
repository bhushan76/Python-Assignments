#Write a program which accept one number and display below pattern.

#-------------------------------------------------------------------
def Number(n):
          for i in range(n):
                    j=1
                    while j<=n:
                              print(j,end=" ")
                              j+=1
                    print("\n")

x=(int(input("Enter the  number")))
Number(x)
