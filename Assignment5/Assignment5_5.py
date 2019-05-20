def remove_at(i, s):
    return s[:i] + s[i+1:]



def main():
    str = input("enter word")
    a=0;
    for i in range(len(str)):
        a=a+ord(str[i])

    print(a/len(str))
if __name__ == "__main__":
    main()