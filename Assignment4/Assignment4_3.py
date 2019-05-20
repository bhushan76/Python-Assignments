from functools import reduce

def main():

    arr=[int(x) for x in input("enter space saperated numeric value").split()]

    Arr1 = list(filter(lambda no:  no>=70 and no<=90, arr))
    addArray = list(map(lambda no: no + 10, Arr1))
    #print(ModArray)
    product = reduce(lambda a, b: a * b, addArray)
    print(product)


if __name__=='__main__':
    main();
