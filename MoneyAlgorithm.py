import sys

#The following function creates an adjacency matrix to represent a directed graph.
def InputMaker():

    file = open('sample-1.in', 'r')
    # file = sys.stdin

    products, devider = map(int,file.readline().split())
    priceArray = list(map(int,file.readline().split()))
    file.close()
    return products,devider,priceArray

if __name__ == "__main__":
    products,devider,priceArray = InputMaker()
    print(products)
    print(devider)
    print(priceArray)