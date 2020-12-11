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

def Algorithm(priceArray,devider,products,divCounter,total,rest):
    for index,n in enumerate(priceArray):
        if  index < len(priceArray)-2 and priceArray[index+2] >= roundup(priceArray[index+2]):
            total = total + n
        elif divCounter < devider:
            splitArr(priceArray, products, index)
            Algorithm(priceArray,devider,len(priceArray),divCounter+1,total,rest)
    for n in priceArray:
        rest = rest + n
    return  roundup(total) + roundup(rest)

def splitArr(arr, n, k):  
    for i in range(0, k):  
        arr.pop(0)
          
def roundup(x):
    return int(math.floor(x / 5.0) * 5)

if __name__ == "__main__":
    products,devider,priceArray = InputMaker()
    total = Algorithm(priceArray,devider,products,0,0,0)
    sys.stdout.write(str(total))