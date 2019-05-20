from sys import *
import os
def DirectoryWatcher(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    if exists:
        for foldername ,subfolder,filename in os.walk(path):
            print("current folder is:"+foldername)
            for subf in subfolder:
                print("subfolder of"+foldername+"is :"+subf)
                for file in filename:

                    print(file)
                    filepath = foldername
                    #foldername = subdir.split(os.sep)[-1]
                    a=file.split('.')
                    if a[1]==argv[2][1:]:
                        base = os.path.splitext(file)[0]
                        file_path = os.path.join(filepath, file)
                        new_name = os.path.join(filepath, base + argv[3])
                        os.rename(file_path, new_name)


                        # #newfilepath = foldername + os.sep + subf + os.sep + base + argv[3]
                        # newfilepath = filepath.replace(file, base + argv[3])
                        # os.rename(filepath, newfilepath)

                        #print("file inside "+ foldername+"is"+file)
                print(' ')
    else:
        print("invalid path")


def main():
    if len(argv)!=4:
        print("invalid number of argument")
        exit()
    if argv[1]=="-h":
        print("this script is designed for traverse specific directory")
        exit()
    if argv[1]=="-u":
        print("usage :Application_name AbsolutePath_of_directory first_extention second_extention")
        exit()

    try:
        DirectoryWatcher(argv[1])
    except ValueError:
        print("Error: Invalid datatype if inpute")
    except Exception as E:
        print("invalid inpute"+E)
    # if len(argv)<1 or len(argv)>3:
    #     print("invalid no of arguments")



if __name__=="__main__":
    main()