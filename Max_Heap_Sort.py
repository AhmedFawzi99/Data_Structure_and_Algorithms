#python3
import sys

## this is the main function that calls the Heapify function so it itirates acrros all the array level by level 
def Build_Heap(Array):
    ## start running the algorithm from the first non-leaf node
    i=(len(Array) // 2 - 1)

    while i>=0:
        Max_Heapify(Array, i,len(Array))
        i=i-1

## this function Heapify serves to iterate across parent nodes comparing each with their children 
## then it swaps the nodes to make max heap 
def Max_Heapify(Array,i,size):
    maxindex = i

    ## Get the Index of the left of the current node 
    leftindex = 2 * i + 1
    ## Make a check to determine if left node is larger than the current node if yes so the maximum index will be the left index
    if (leftindex < size and Array[leftindex] > Array[maxindex]): maxindex = leftindex

    ## Get the Index of the Right of the current node 
    rightindex = 2 * i + 2
    ## Make a check to determine if right node is larger than the current node if yes so the maximum index will be the right index
    if (rightindex < size and Array[rightindex] > Array[maxindex]): maxindex = rightindex

    ## if the current maximum node index has changed from the current index we swap the nodes and then 
    ## we call the Max_Heapify Recursively passing the new max index to start with and do the same checks again 
    if (maxindex != i):
        Swap_Data(Array,i,maxindex)
        Max_Heapify(Array, maxindex,size)

## Swap the data to make the heap
def Swap_Data(Array,i,maxindex):
    ## swapping the maximum with the the current node
    temp = Array[maxindex]
    Array[maxindex] = Array[i]
    Array[i] = temp

## the main function that is responsible to build and sort ascendingly
def heap_sort(Array):
    Build_Heap(Array)
    ReduceandSort(Array)
    
## this function reduces the array then calls Max_Heapify again on the reduced array 
def ReduceandSort(Array):
    n=len(Array)
    for i in range(n-1, 0, -1):
        Swap_Data(Array,i,0)
        Max_Heapify(Array, 0, i)

### DO NOT CHANGE INPUT/OUTPUT FORMAT ####

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    heap_sort(a)
    for x in a:
        print(x, end=' ')

