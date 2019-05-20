from itertools import permutations



def main():
    str = input("enter word")
    perms = [''.join(p) for p in permutations(str)]
    print(perms)


if __name__ == "__main__":
    main()