import threading

def small(str):
    low=[c for c in str if c.islower()]
    print(len(low))

def capital(str):
    cap=[c for c in str if c.isupper()]
    print(len(cap))
def digit(str):
    #dig =[c for c in str if c.isdigit()]
    cnt=0
   # print(len(dig))
    for i in range(0,len(str)):
        if str[i].isdigit():
            cnt+=1

    print(cnt)
if __name__ == "__main__":
    str=input("enter values")

    thread1 = threading.Thread(target=small, args=(str,))
    thread2 = threading.Thread(target=capital, args=(str,))
    thread3 = threading.Thread(target=digit, args=(str,))
# Will execute both in parallel
    thread1.start()
    thread2.start()
    thread3.start()
# Joins threads back to the parent process, which is this
# program
    thread1.join()
    thread2.join()