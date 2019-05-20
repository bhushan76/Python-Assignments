import threading

def even():
    for i in range(1,11):
        if i%2==0:
            print(i)
def odd():
    for i in range(1,10):
        if i%2!=0:
            print(i)

if __name__ == "__main__":

    thread1 = threading.Thread(target=even, args=())
    thread2 = threading.Thread(target=odd, args=())
# Will execute both in parallel
    thread1.start()
    thread2.start()
# Joins threads back to the parent process, which is this
# program
    thread1.join()
    thread2.join()