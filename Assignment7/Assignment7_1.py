
class BookStore:
    NoOfBooks = 0
    def __init__(self,name,auther):
        self.name=name
        self.author=auther
        BookStore.NoOfBooks+=1


    def Display(self):
        print("book is:{0} \n auther is:{1} \n no of books:{2}".format(self.name,self.author,self.NoOfBooks))


def main():

    Obj1 = BookStore('LinuxSystemProgramming', 'RobertLove')
    Obj1.Display()  # Linux System Programming by Robert Love. No of books : 1
    Obj2 = BookStore('C Programming', 'Dennis Ritchie')
    Obj2.Display()
    Obj3 = BookStore('C Programming', 'Dennis Ritchie')
    Obj3.Display()




if __name__=="__main__":
    main()


