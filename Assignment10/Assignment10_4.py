from sys import *
from shutil import copyfile


import os
def Filecopy(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    if exists:
        os.mkdir(argv[2])
        flag = os.path.isabs(argv[2])
        if flag == False:
            temppath = os.path.abspath(argv[2])
        for foldername ,subfolder,filename in os.walk(path):
            print("current folder is:"+foldername)
            for subf in subfolder:
                print("subfolder of"+foldername+"is :"+subf)
                for file in filename:
                    s = file.split('.')

                    print(file)
                    if s[1] == argv[3][1:]:
                        filepath = foldername
                        src = os.path.join(filepath, file)
                        dst = os.path.join(temppath, file)
                        copyfile(src, dst)




                print(' ')
    else:
        print("invalid path")


def main():
    if len(argv)!=4:
        print("invalid number of argument")
        exit()
    if argv[1]=="-h":
        print("this script is designed for copy files to another directory")
        exit()
    if argv[1]=="-u":
        print("usage :Application_name AbsolutePath_of_directory  directory_name_to_copy_files")
        exit()

    try:
        Filecopy(argv[1])
    except ValueError:
        print("Error: Invalid datatype if inpute")
    except Exception as E:
        print("invalid inpute"+E)
    # if len(argv)<1 or len(argv)>3:
    #     print("invalid no of arguments")



if __name__=="__main__":
    main()