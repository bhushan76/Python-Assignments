
class Arithmatic:

    def __init__(self):
        self.value1=0
        self.value2=0
    def Accept(self):
        print("enter 1st number")
        self.value1=int(input())
        print("enter 2nd number")
        self.value2 = int(input())
    def Addition(self):
        return self.value1+self.value2
    def Subtraction(self):
        return self.value1-self.value2
    def multiplication(self):
        return self.value1*self.value2
    def division(self):
        return self.value1 / self.value2



def main():
    Obj1 = Arithmatic()
    Obj2 = Arithmatic()

    Obj1.Accept()
    print("Addition  is:{0} \n subtraction is:{1} \n multiplication is:{2} \n Division is:{3}".format(Obj1.Addition(),Obj1.Subtraction(),Obj1.multiplication(),Obj1.division()))

    Obj2.Accept()
    print("Addition  is:{0} \n subtraction is:{1} \n multiplication is:{2} \n Division is:{3}".format(Obj2.Addition(),Obj2.Subtraction(),Obj2.multiplication(),Obj2.division()))


if __name__=="__main__":
    main()


