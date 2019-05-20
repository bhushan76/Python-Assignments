def Count_Total_Words(str1):
    total = 1
    for i in range(len(str1)):
        if(str1[i] == ' ' or str1 == '\n' or str1 == '\t'):
            total = total + 1
    return total




def main():
    string = input("Please Enter your Own String : ")
    leng = Count_Total_Words(string)
    print("Total Number of Words in this String = ", leng)

    # count=1;
    # str=str.strip()
    # lst=str.split()
    # print(len(str))
    # for i in range(len(str)):
    #     if str[i]==' ':
    #         count+=1
    #
    # print(count)


if __name__ == "__main__":
    main()