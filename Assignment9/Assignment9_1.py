import sys
import os.path




def main():


    if os.path.exists(sys.argv[1]):
        print("file exist")
    else:
        print("file does not exist")



if __name__=="__main__":
    main()