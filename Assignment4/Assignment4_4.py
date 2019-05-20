from functools import reduce

def main():

    arr=[int(x) for x in input("enter space saperated numeric value").split()]

    evenArr = list(filter(lambda no:  no%2==0, arr))
    ModArray = list(map(lambda no: no**2, evenArr))
    print(ModArray)
    sum = reduce(lambda a, b: a + b, ModArray)
    print(sum)


if __name__=='__main__':
    main();
