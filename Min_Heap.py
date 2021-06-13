# python3

# this is the main function that calls the Heapify function so it itirates acrros all the array level by level 
def build_heap(Array):
    # an array to save the swaps in
    swaps = []
    ## start running the algorithm from the first non-leaf node
    i=(len(Array) // 2 - 1)
    while i>=0:
        Min_Heapify(Array, i, swaps)
        i=i-1
    return swaps

## this function Heapify serves to iterate across parent nodes comparing each with their children 
## then it swaps the nodes to make min heap 
def Min_Heapify(Array, i, swaps):
    minindex = i

    ## Get the Index of the left of the current node 
    leftindex = 2 * i + 1
    ## Make a check to determine if left node is smaller than the current node if yes so the minimum index will be the left index
    if (leftindex < len(Array) and Array[leftindex] < Array[minindex]): minindex = leftindex

    ## Get the Index of the Right of the current node 
    rightindex = 2 * i + 2
    ## Make a check to determine if right node is smaller than the current node if yes so the minimum index will be the right index
    if (rightindex < len(Array) and Array[rightindex] < Array[minindex]): minindex = rightindex

    ## if the current minimum node index has changed from the current index we swap the nodes and then 
    ## we call the Min_Heapify Recursively passing the new min index to start with and do the same checks again 
    if (minindex != i):
        Set_and_Swap_Data(Array,i,minindex,swaps)
        Min_Heapify(Array, minindex, swaps)


# this function is responsible to save the swaps that happend and swap the data also
def Set_and_Swap_Data(Array,i,minindex,swaps):
    # swapping the minimum with the the current node
    temp = Array[minindex]
    Array[minindex] = Array[i]
    Array[i] = temp
    # save the swaps that happened into and array
    swaps.append((i, minindex))


def main():
    #####   DO NOT CHANGE THE CODE IN THIS PART #########
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
