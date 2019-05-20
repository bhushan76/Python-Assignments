def remove_at(i, s):
    return s[:i] + s[i+1:]



def main():
    str = input("enter word")
    pos= int(input("enter position"))
    str=remove_at(pos-1,str)
    print(str)


if __name__ == "__main__":
    main()