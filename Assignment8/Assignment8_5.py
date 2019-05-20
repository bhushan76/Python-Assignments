import threading

def printval():
    for i in range(51):
        print(i)
def Rprintval():
    for i in range(50,-1,-1):
        print(i)

if __name__ == "__main__":

    thread1 = threading.Thread(target=printval, args=())
    thread2 = threading.Thread(target=Rprintval, args=())
# Will execute both in parallel
    thread1.start()
    thread1.join()
    thread2.start()
# Joins threads back to the parent process, which is this
# program

