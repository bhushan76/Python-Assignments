#  Write a program which contains one function named as ChkNum() which accept one
#  parameter as number. If number is even then it should display “Even number” otherwise  display “Odd number” on console.


def ChkNum(x):
        
          if (x%2 ==0):
                    print("Number is even")
          else:
                    print("Number is  odd")


x=(int(input("please Enter the number")))
ChkNum(x)
