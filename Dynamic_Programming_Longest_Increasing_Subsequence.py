import sys


# This Function uses DP technique to Get the Length of the Longest Increasing SubSequence
# This problem has Overlapping Substructure property and recomputation of same subproblems 
# This can be avoided by either using Memoization or Tabulation.
def Longest_Increasing_Subsequence_DP(Array,Size):
    
    # Intializing Variables one for i the first loop in the code the other is the Length of the LIS 
    # Why is LISlength intialized by 1 cause the constraints difined were 1 ≤ 𝑛 ≤ 500
    # so the LISlength is 1 from the begining
    i,LISlength=1,1
    IndexofSubSeqArr=0

    # This Part Intializes a List of Empty Lists this will store the different subsequences at each loop after checking conditions
    SubSeqsArr= [[] for i in range(Size)]
    # Appeding the first list in SubSeqArr with the first element in the input Array to make the first 
    # subsequence corresponds to the first element 
    SubSeqsArr[0].append(Array[0])
       
    # A while loop that begins from i=1 and loops on the input Array
    while(i<Size):
        # Intialize j variable with each loop
        j=0
        # The Second Loop begins from j=0 up to the i variable 
        # We use it to compare the elements before the Array[i] 
        while(j<i):
            # This conditions serves to check 2 things:
            # The First is that the Array[i] element is greater than its Pervious elements Array[j] in each loop 
            # The second is that the len of the current SubSeqsArr[i] is smaller than the previous SubSeqsArr[j] not greater 
            if Array[i] > Array[j] and  (len(SubSeqsArr[i]) < len(SubSeqsArr[j]) + 1) :
                # If the conditions are both True we put the SubSeqsArr[j] in SubSeqsArr[i]
                # This puts the Elements there and in the same time the subseqlength would change allowing the check to differ in the next loop 
                # *** This part SubSeqsArr[i] = SubSeqsArr[j] *** only makes SubSeqsArr[i] referes to the same adress of SubSeqsArr[j] 
                # so it continues to refrence to best SubSeqsArr[j] in the loop.
                # This is done so that the complexity of the Algorithm stays the same but this will cause a problem as they will be pointing 
                # to the same object so to solve this after the loop finishes i make SubSeqsArr[i] = list(SubSeqsArr[i])
                # This will now put the elements in that place with a different refrence 
                SubSeqsArr[i] = SubSeqsArr[j]
            j+=1
        # The solution to the above problem i put it after the Loop to prevent the complexity from changing to n*n*n=n^3
        SubSeqsArr[i] = list(SubSeqsArr[i])
        # After that we append the Element of Array[i] after making sure that SubSeqsArr[i] elements are in increasing order
        SubSeqsArr[i].append(Array[i])
        # This condition is responsible for 2 things:
        # The first is that it  compare the LISlength variable to the length of SubSeqsArr[i] if LISlength variable is smaller 
        # I assign the new legth : LISlength=len(SubSeqsArr[i])
        # The second is that if the LISlength changes it also keeps track of the Index of this SubSeqsArr
        # The will refer to the Longest Increasing Subsequence 
        if(len(SubSeqsArr[i])>LISlength):
            LISlength=len(SubSeqsArr[i])
            IndexofSubSeqArr=i
        i+=1

    # This line serves to remove the [] and , from the List to retrun it exactly as required by the Assignment Statement
    SubSequence=str(SubSeqsArr[IndexofSubSeqArr]).strip('[]').replace(',', '')

    return LISlength,SubSequence


if __name__ == '__main__':
    # DO NOT change this code
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    LISlength,SubSequence=Longest_Increasing_Subsequence_DP(a,n)
    print(LISlength)
    print(SubSequence)