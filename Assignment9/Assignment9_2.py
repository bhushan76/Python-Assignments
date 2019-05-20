import sys
import os.path




def main():


    if os.path.exists(sys.argv[1]):
        print("file exist")
    else:
        print("file does not exist")


    fd = open(sys.argv[1],'r')
    print("Information about file : ",fd)
    print("Contents of Whole file")
    print(fd.read())
    print("Reading single line from file")
    fd.seek(0)
    print(fd.readline())
    # print("Current file position is",fd.tell()) # get the current file position
    # fd.seek(0) # bring file cursor to initial position
    # print("Contents of Whole file")
    # print(fd.read())
    # fd.close()
    # fd = open("Marvellous.txt",'a+r')
    # fd.write("Python : Automation and Machine Learning\n")
    # fd.write("Angular : Web Development\n")
    # fd.seek(0)
    # print(fd.read())
    fd.close()

if __name__=="__main__":
    main()