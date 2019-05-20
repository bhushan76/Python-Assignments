
class Circle:
    PI=3.14
    def __init__(self):
        self.r=0.0
        self.a=0.0
        self.c=0.0
    def Accept(self):
        print("enter value of radius")
        self.r=float(input())
    def CalculateArea(self):
        self.a= self.PI* self.r**2
    def Calculatecircumference(self):
        self.c= self.PI*self.r*2
    def Display(self):
        print("area is:{0} \n circumference is:{1}".format(self.a,self.c))


def main():
    Obj1 = Circle()
    Obj2 = Circle()

    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.Calculatecircumference()
    Obj1.Display()

    Obj2.Accept()
    Obj2.CalculateArea()
    Obj2.Calculatecircumference()
    Obj2.Display()

if __name__=="__main__":
    main()


