import sys
import numpy as np
import math


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# A function responsible to pad the arrays and make them a power of 2
def pad_arrays(MatrixA,MatrixB,n):

    # Calculate the new size of the matrix needed to pad it before dividing and conquering
    x=pow(2, math.ceil(math.log(n)/math.log(2)))
    # If the size is not a power of 2 the new size would be different then in Subtract the new size from that of the user input and 
    # decide by how much i need padding Ex: user enter size=6 the new size must be 8 so 8-6=2 i have to pad 2 rows and  2 columns 
    if x != n:
        x=x-n
        MatrixA=np.pad(MatrixA,((0,x),(0,x)), 'constant')
        MatrixB=np.pad(MatrixB,((0,x),(0,x)), 'constant')
    return MatrixA,MatrixB

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# A funtion that gets the user inputs to fill the matrices
def Get_User_Input():

    # Ask the user to input the size of the square matrix he wants
    Size = int(input("Enter the Size of the Sqaure Matrix: "))
    MatrixA=[]
    MatrixB=[]
    # Loop in range of 2 to allow the user to fill the 2 matrices
    for i in range(2):
        # A message for the user to Enter the Elements of Matrix 1 or Matrix 2
        print('Enter Elements of Matrix ', i+1)
        #Loop accoring to the size this one corresponds to the number of rows
        for k in range(Size):		 
            Matrix =[]
            # Loop to fill elements in each row 
            for j in range(Size):	 
                # A message for the user to keep trak of the current row and in which matrix
                print('Enter Matrix {} Row {} Column {} Element:'.format(i+1,k+1,j+1))
                Matrix.append(int(input()))
            # A condition to check which matrix to fill now 1 or 2
            if i == 0:
                MatrixA.append(Matrix)
            else:
                MatrixB.append(Matrix)
    # Change them into np matrices
    MatrixA=np.array(MatrixA)
    MatrixB=np.array(MatrixB)
    # return the 2 matrices and Size the user inpus will be later used in the Divide and Conquer
    return MatrixA,MatrixB,Size

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# The Naive Algorithm that consists of 3 nested loops that are used to multiply the matrices together
def Naive_Algorithm(MatrixA,MatrixB,inputlength):
    # create a numpy array to store the result in 
    R = np.zeros((inputlength,inputlength),dtype=int)
    # loop according to the size of the input matrix (rows)
    for row in range(inputlength):
        # loop according to the size of the input matrix (columns)
        for col in range(inputlength):
            # this loop is responisble for multiplying the elements and summation
            for k in range(inputlength):
                #add to the np array created 
                R[row][col] += MatrixA[row][k] * MatrixB[k][col]
    return R
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# A function that partitions the given Matrices into 4 Parts each and then return them to be used in the Divide_and_Conquer_PartitionWay function 
def Partition_Matrix(MatrixA,MatrixB,l):

    # Divide the Matricies into 4 parts using the partitionfunction
    #  A= [[A0 A1               B= [[B0 B1
    #       A2  A3]]                 B2  B3]]
    A0,B0=MatrixA[:int(l/2),:int(l/2)],MatrixB[:int(l/2),:int(l/2)]
    A1,B1=MatrixA[:int(l/2),int(l/2):],MatrixB[:int(l/2),int(l/2):]
    A2,B2=MatrixA[int(l/2):,:int(l/2)],MatrixB[int(l/2):,:int(l/2)]
    A3,B3=MatrixA[int(l/2):,int(l/2):],MatrixB[int(l/2):,int(l/2):]

    return A0,A1,A2,A3,B0,B1,B2,B3

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# The divide and Coquer using the partition way calls the partition function and then recursively calls itself to multiply the matrices
def Divide_and_Conquer_PartitionWay(MatrixA,MatrixB,inputlength):  

    # Reset the length of the passed array eache time it is l/2 of the original Legnth
    l = len(MatrixA)

    # Create a Matrix of zeros with the same Size of the passed arrays
    Output = np.zeros((l,l),dtype=int)

    # if the length of the passed Array is 1 that means that the Matrices have been partitioned until they became a single element and then
    # return the multiplication of this single element in Matrix A with that of Matrix B
    if l == 1:
        return MatrixA * MatrixB
    else:
       
        # Divide the Matricies into 4 parts using the partitionfunction
        #  A= [[A0 A1               B= [[B0 B1
        #       A2  A3]]                 B2  B3]]
        A0,A1,A2,A3,B0,B1,B2,B3=Partition_Matrix(MatrixA,MatrixB,l)

   

        # To calculate the Multiplication of Matrices Let Us call the resultant matrix R
        # R=  [[R0 R1
        #       R2  R3]]
        # R0 will equal to A0B0 + A1B2
        # R1 will equal to A0B1 + A1B3
        # R2 will equal to A2B0 + A3B2
        # R3 will equal to A2B1 + A3B3
        # For the multiplication to occur between the partitions it has to be recursively called into the function again until n=1 is reached
        # Translating these equations into code:

        Output[:int(l/2),:int(l/2)] =  Divide_and_Conquer_PartitionWay(A0,B0,inputlength) + Divide_and_Conquer_PartitionWay(A1,B2,inputlength)
        Output[:int(l/2),int(l/2):] =  Divide_and_Conquer_PartitionWay(A0,B1,inputlength) + Divide_and_Conquer_PartitionWay(A1,B3,inputlength)
        Output[int(l/2):,:int(l/2)] =  Divide_and_Conquer_PartitionWay(A2,B0,inputlength) + Divide_and_Conquer_PartitionWay(A3,B2,inputlength)
        Output[int(l/2):,int(l/2):] =  Divide_and_Conquer_PartitionWay(A2,B1,inputlength) + Divide_and_Conquer_PartitionWay(A3,B3,inputlength)

        # This final Line here serves to remove the paddings by subtracting the length of the passed padded matrices 
        # from that of the original user input for example if user inputs a matrix of size 3 it would be padded until it becomes 4 
        # so this line serves to remove the pad and outputs the multiplied matrix without the extra padding
        Output=Output[:(int(l)-(l-inputlength)),:(int(l)-(l-inputlength))]
        
    return Output

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# This Divide and Conquer Method uses Strassen's way to calculate the matrices by making less recursive calls bu more summation or subtractions
#Faster than Partition technique
def Fast_Divide_and_Conquer_Strassens(MatrixA,MatrixB,inputlength):  

    # Reset the length of the passed array eache time it is l/2 of the original Legnth
    l = len(MatrixA)

    # Create a Matrix of zeros with the same Size of the passed arrays
    Output = np.zeros((l,l),dtype=int)

    # if the length of the passed Array is 1 that means that the Matrices have been partitioned until they became a single element and then
    # return the multiplication of this single element in Matrix A with that of Matrix B
    if l == 1:
        return MatrixA * MatrixB
    else:
       
        # Divide the Matricies into 4 parts 
        #  A= [[A0 A1               B= [[B0 B1
        #       A2  A3]]                 B2  B3]]
        A0,A1,A2,A3,B0,B1,B2,B3=Partition_Matrix(MatrixA,MatrixB,l)


        #According to Strassen Theory we compute 7 different multiplications instead of 8 multiplications done by the partioning divide and conquer
        # in this way the number of multiplications done is decreased increasing the cost of additions and subtractions
        # M0 M1 M2 M3 M4 M5 M6
        M0,M1=Fast_Divide_and_Conquer_Strassens(A0,B1-B3,inputlength),Fast_Divide_and_Conquer_Strassens(A0+A1,B3,inputlength)
        M2,M3=Fast_Divide_and_Conquer_Strassens(A2+A3,B0,inputlength),Fast_Divide_and_Conquer_Strassens(A3,B2-B0,inputlength)
        M4,M5=Fast_Divide_and_Conquer_Strassens(A0+A3,B0+B3,inputlength),Fast_Divide_and_Conquer_Strassens(A1-A3,B2+B3,inputlength) 
        M6=Fast_Divide_and_Conquer_Strassens(A0-A2,B0+B1,inputlength)

        # Adding and Subtracting the Matrices genetrated to compute the output 
        # R=  [[R0 R1
        #       R2  R3]]
        Output[:int(l/2),:int(l/2)] =  M4 + M3 - M1 + M5
        Output[:int(l/2),int(l/2):] =  M0 + M1
        Output[int(l/2):,:int(l/2)] =  M2 + M3
        Output[int(l/2):,int(l/2):] =  M0 + M4 - M2 - M6

        # This final Line here serves to remove the paddings by subtracting the length of the passed padded matrices 
        # from that of the original user input for example if user inputs a matrix of size 3 it would be padded until it becomes 4 
        # so this line serves to remove the pad and outputs the multiplied matrix without the extra padding
        Output=Output[:(int(l)-(l-inputlength)),:(int(l)-(l-inputlength))]
        
    return Output



MatrixA,MatrixB,length=Get_User_Input()
MatrixA,MatrixB=pad_arrays(MatrixA,MatrixB,length)

Output1=Naive_Algorithm(MatrixA,MatrixB,length)
Output2=Divide_and_Conquer_PartitionWay(MatrixA,MatrixB,length)
Output3=Fast_Divide_and_Conquer_Strassens(MatrixA,MatrixB,length)


print(Output1)
print(Output2)
print(Output3)

#Testing it checks if the matrices are the same output for the 3 divde and conquer algorithms if both are true means the 3 ways are right
print(np.array_equal(Output1, Output2))
print(np.array_equal(Output2, Output3))




