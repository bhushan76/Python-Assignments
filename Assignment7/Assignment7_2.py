
class BankAccount:
    ROI = 10.5
    def __init__(self,name,Amount):
        self.name=name
        self.Amount=Amount

    def Display(self):
        print("name is:{0}\t amount is:{1}".format(self.name,self.Amount))
    def Deposit(self,depo):
        self.Amount+=depo
    def Withdraw(self,depo):
        self.Amount -= depo

    def CalculateIntrest(self,time):
        #print("book is:{0} \n auther is:{1} \n no of books:{2}".format(self.name,self.author,self.NoOfBooks))
        simple_interest = (self.Amount * time * BankAccount.ROI) / 100
        print("The simple interest is:", simple_interest)


def main():

    Obj1 = BankAccount("rahul",3000)
    Obj1.Display()

    Obj1.Deposit(3000)
    Obj1.Display()
    Obj1.Withdraw(2000)
    Obj1.Display()
    Obj1.CalculateIntrest(2)

    Obj1 = BankAccount("mahesh", 10000)
    Obj1.Display()
    Obj1.Deposit(2000)
    Obj1.Display()
    Obj1.Withdraw(5000)
    Obj1.Display()
    Obj1.CalculateIntrest(5)





if __name__=="__main__":
    main()


