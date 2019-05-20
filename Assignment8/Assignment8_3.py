import threading

def evenlist(num):
    num=list(num)
    sum=0
    for i in range(len(num)):
        if  num[i]%2==0:
            sum=sum+num[i]
    print("even",sum)
def oddlist(num):
    num = list(num)
    sum=0
    for i in range(len(num)):
        if num[i] % 2 != 0:
            sum = sum + num[i]
    print("odd",sum)
if __name__ == "__main__":
    num = [int(x) for x in input("enter numbers space separate").split()]
    thread1 = threading.Thread(target=evenlist, args=(num,))
    thread2 = threading.Thread(target=oddlist, args=(num,))
# Will execute both in parallel
    thread1.start()
    thread2.start()
# Joins threads back to the parent process, which is this
# program
    thread1.join()
    thread2.join()
    print(" exit fom main.")