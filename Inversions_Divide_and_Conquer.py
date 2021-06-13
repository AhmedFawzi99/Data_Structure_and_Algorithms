# Uses python3
import sys
import numpy as np
import random


#***********************************************************************************************************#

#This is the Naive inversion Counting Algorithm Function that uses 2 nested while loops and then compares elements to calculate
# the number of inversions 
def NaiveAlgorithmCountInversions(A):
    #The inverse Counter variable
    counter = 0
    n = len(A)
    i=0
    #The First while loop begins with the first element and then stops at the element before the last
    while i < n - 1:
        # j is the index of the element after the fist one 
        j=i+1
        # The second while loop compares the i element with the rest of the array and then increases the counter if it is larger
        while j < n:
            #The check that if the i element is greater than any element the counter increases
            if A[i] > A[j]:
                counter += 1
            j+=1
        i+=1   
    return counter

#***********************************************************************************************************#

# This Function is the divide and conquer merge sort i takes the Array and an array of data( Start index and End index) 
# It is responsible to recursively call itself until the Start Index and the End index are equal this means that is is a single element 
def MergeSortAlgorithm(A,data):

    #The DataGetter is a simple function takes the array of data and then returns the Start and End indecies
    Start,End=DataGetter(data)

    # The intialization of the inverse counter
    counter = 0
    
    # This check says that we continue recurseviely calling and dividing ( getting the new left and right )
    # as long as the Start is less than the End ( not a single element )
    if Start < End:
        
        #This line here serves to call Array Getter Function that returns 3 dataarrays
        #The First Return is the LeftData Array (Start,Mid)
        #The Second Return is the RightData Array (Mid+1,End)
        #The Third Return is the Merging Data neeeded (Start,End) with each recursize call these data change according to inputs

        LeftDataArray,RightDataArray,MergeDataArray=ArrayGetter(Start,End)

        # This line calls the MergeSortAlgorithmFunction for the LeftArray and For the RightArray
        # Also the MergeandCount is Called to sort and count and merge the array
        # The Outputs of this recursions is added together and the inversion count is calculated

        counter = MergeSortAlgorithm(A,LeftDataArray) + MergeSortAlgorithm(A,RightDataArray) + MergeAndCount(A,MergeDataArray)


    return counter

#***********************************************************************************************************#

#This Functions is responsible for sorting,Merging and Counting the Number of Inversions 
def MergeAndCount(A,data):

    #Getting the Start and End indices
    Start,End=DataGetter(data)
   
    #Calculating the Mid Floor Division to be able to make 2 subarrays LeftSubArray and RightSubArray
    mid = (Start + End)//2

    #Calculating the Mid to be able to make 2 subarrays LeftSubArray and RightSubArray
    LeftSubArray = A[Start:mid+1]
    RightSubArray = A[mid+1:End+1]

    #Variable Intializations to start the while loop and compare elements
    counter = 0
    i = j = 0   # used for thr loops  
    k = Start   # used to put elements int the Array a variable intialized to be as the starting index


    #A while loop that is responsible for checking first that the i and j variables
    #are less than the lens of the left and right subarrays so that it breaks when one of them finishes loopinf or both
    #in this while loop the element of left subarray is compared to that of the right if it is greater it we put in that place 
    #of Array A the smaller element ( this means an inversion occured ) then we increase the inversion counter 
    #by a factor of 
    while i < len(LeftSubArray) and j < len(RightSubArray): 

        #checks id leftarray element is smaller if so put that element in Array A and increase the i and k  values  
        if LeftSubArray[i] <= RightSubArray[j]:
            A[k] = LeftSubArray[i]
            i += 1
            k += 1
        #if it is larger inversion will happen so we put the smaller element of Right Array in Array A[k]
        # and increase the inversion counter by len(LeftSubArray) -i this is because the arrays are sorted with each recursion already so if the first 
        # element in LeftSubArray is greater the remaining elements in LeftSubArray is also greater than the Right Element
        # so the right element will be inverted len(LeftSubArray)-i times until it becomes in the RightPlace
        # EX: LeftSubArray=[5 6 7] ,RightSubArray=[2 8 10] ,i=j=0
        # 5>2 so 2 will be inverted 3 times len(left)=3 and i=0 so 3-0=3
        # Summary to all of that:
        # if LeftSubArray[i] > RightSubArray[j], then there are len(LeftSubArray)-i inversions
        else:
            A[k] = RightSubArray[j]
            counter += len(LeftSubArray) -i
            j += 1
            k += 1
    
    #The for loop exits when either the i or j is greater than their lengths 
    # so if i is still less than the legth of leftsubarray this means there are still elements in LeftSubArray
    # not looped on so we merge them with the Sorted Array A
    if i < len(LeftSubArray):
        A[k: k +  len(LeftSubArray) - i] = LeftSubArray[i:]
    #the same is for the RightSubArray is their is still remaining Elements not looped on we merge them with Array A
    if j< len(RightSubArray):
        A[k: k +  len(RightSubArray) - j] = RightSubArray[j:]

    return counter

#***********************************************************************************************************#

# This Function serves to return the data for the LeftArray , The RightArray and the MergeandCount data needed
def ArrayGetter(Start,End):
    
    #Mid is calculated using Floor Division with each call according to inputs of the Start index and End Index 
    mid = (Start + End)//2

    #The First Return is the LeftData Array (Start,Mid)
    LeftDataArray=[Start,mid]

    #The Second Return is the RightData Array (Mid+1,End)
    RightDataArray=[mid+1,End]

    #The Third Return is the Merging Data neeeded (Start,End) with each recursize call these data change according to inputs
    MergeDataArray=[Start,End]
    return LeftDataArray , RightDataArray , MergeDataArray

#***********************************************************************************************************#

#The DataGetter is a simple function takes the array of data and then returns the Start and End indecies
def DataGetter(data):
    return data[0],data[1]

#***********************************************************************************************************#

# A Testing Function to check results with the naive Algorithm
def TestingFunction():

    c=True
    z=0
    # A while loop that continue working until a false result happens and breaks out of it
    while(c):
        # Creating a random array of integers with random sizes each new entry in the while loop
        n = random.randint(0,20)
        a = []

        for i in range(0,n):
            x = random.randint(1,30)
            a.append(x)

        b = n * [0]
        Output1=NaiveAlgorithmCountInversions(a)
        Output2=MergeSortAlgorithm(a,[0,len(a)-1])
        # Checking if the outputs are the same or no 
        if(Output1==Output2):
            z+=1
            print("Test Case {} is Correct with outputs: {}  {}".format(z,Output1,Output2))
        else:
            print("Error not same answer")
            c=False

#***********************************************************************************************************#        

if __name__ == '__main__':
    # DO NOT change this code
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(MergeSortAlgorithm(a,[0,len(a)-1]))

    # Testing Function compares the outputs and prints 
    # TestingFunction()

    