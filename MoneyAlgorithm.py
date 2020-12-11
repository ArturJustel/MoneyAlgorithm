import sys
import math

#The following function creates an adjacency matrix to represent a directed graph.
def InputMaker():

    # file = open('sample-2.in', 'r')
    file = sys.stdin

    products, devider = map(int,file.readline().split())
    priceArray = list(map(int,file.readline().split()))
    file.close()
    return products,devider,priceArray

def Algorithm(priceArray,devider,products):
    total = 0
    rest = 0
    for index,n in enumerate(priceArray):
        if  index < len(priceArray)-2 and priceArray[index+2] > roundup(priceArray[index+2]):
            total = total + n
        else:
            splitArr(priceArray, products, index)
    for n in priceArray:
        rest = rest + n
    total = roundup(total) + roundup(rest)
    sys.stdout.write(str(total))

def splitArr(arr, n, k):  
    for i in range(0, k):  
        arr.pop(0)
          
def roundup(x):
    return int(math.floor(x / 5.0) * 5)

if __name__ == "__main__":
    products,devider,priceArray = InputMaker()
    Algorithm(priceArray,devider,products)