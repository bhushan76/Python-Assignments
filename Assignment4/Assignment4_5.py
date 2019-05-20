from functools import reduce
def is_prime(num):
   for j in range(2, num):
      if num % j == 0:
         return False
   else:
      return True

def main():

    arr=[int(x) for x in input("enter space saperated numeric value").split()]

    pArr = list(filter(is_prime, arr))
    print(pArr)
    ModArray = list(map(lambda no: no*2, pArr))
    print(ModArray)
    sum = reduce(lambda x,y: x if x > y else y, ModArray)
    print(sum)


if __name__=='__main__':
    main();
