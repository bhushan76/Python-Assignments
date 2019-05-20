class Demo:
    value=10
    def __init__(self,num1,num2):
        self.i=num1
        self.j=num2
    def Fun(self):
        print(self.i)
        print(self.j)
    def Gun(self):
        print(self.i)
        print(self.j)

def main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__=="__main__":
    main()