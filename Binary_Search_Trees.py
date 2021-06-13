import sys
import random
import time

# Class Node it has 3 members data,left,right this will be used to consruct the BST as it is a group of nodes 
# Connected togther each with its own value. 
class Node:
      def __init__(self, data):  
          self.data = data  
          self.left = None  
          self.right = None  

#*************************************************************************************#


# This class is BST class it has a member called root that is the head of the tree itself 
# it has Instertion Function to insert to the left and right of the root node and then move on to the other 
# if the left and right nodes are already occpuied the binary search tree has its elements sorted from smallest the far left 
# to largest element on the far right
class Binary_Search_Tree:

    # Constructor of this class
    def __init__(self):  
        self.root = None
 
    # Insertion Function that inserts nodes into the tree by seeing its correct location and then inserting it
    # If the tree has no root yet it then sets the root for the tree
    def Insert_Into_Tree(self, data):  
        #check if the tree has root or no if no it sets the root
        if self.root == None:
            self.root = Node(data)
        else:
            # A variale that points to the root of the tree ( the top )
            CurrentNode = self.root
            # This while loop serves to continue running until the the new node has been set and then break from it 
            while 1:
                # Now we have 3 options (the data is smaller than the CurrentNode.data or larger or equal )
                # if it is smaller 
                if data < CurrentNode.data:
                    # if the current node still has a left node we go to that node until the next = None
                    if CurrentNode.left != None:
                        # go to the next 
                        CurrentNode = CurrentNode.left
                    else:
                        # if the next is equal to None we make the left of the current a node with the data we want to insert
                        CurrentNode.left = Node(data)
                        break
                # if it is smaller 
                elif(data > CurrentNode.data):
                    # if the CurrentNode still has a right node we go to that node until the next = None
                    if CurrentNode.right != None:
                        # go to the next 
                        CurrentNode = CurrentNode.right
                    else:
                        # if th nex is equal to None we make the right of the current a node with the data we want to insert
                        CurrentNode.right = Node(data)
                        break
                # the value is the same as node in the tree already so we break from the loop 
                else:
                    break

# ************************************************************************** #

    # This is Get Min Function By recursion it iterates until the next node is None. This Function only iterates
    # on the left side only because of the BST property that the left side of the tree is always smaller 
    # to to get the minimum we have to iterate until we reach the very last left element to get the minimum
    def Get_Min_Iteration(self):
        # Set the current node with the root top of tree
        CurrentNode=self.root
        # Iterate until the next left node is None and then return the data of this last node
        while CurrentNode.left != None:
            CurrentNode = CurrentNode.left
        return CurrentNode.data 

# ************************************************************************** #

    # This Function is like the iterative function but instead it calls recursively the next left node
    # The first node it begins with is the tree root and then checks next left node is not None so it recursively calls
    # the Get_Min_Recursive passing the next left element to begin with until it reaches the last left element and then returns the data
    def Get_Min_Recursive(self,CurrentNode):

        if(CurrentNode.left != None):
            return self.Get_Min_Recursive(CurrentNode.left)
        return CurrentNode.data

# ************************************************************************** #

# A testing function that inserts elements into the tree and call both get min function and also the elements that are inserted 
# are saved in an array so that we could compute the min of that array to compare the value with the Outputs from that Functions
def TestingFunction():

    c=True
    z=0
    # A while loop that continue working until a false result happens and breaks out of it
    while(c):
        # Creating a random array of integers with random sizes each new entry in the while loop
        n = random.randint(1,20)
        a = []
        tree = Binary_Search_Tree() 
        for i in range(0,n):
            x = random.randint(1,1000)
            # Insert in an array to get the min later
            a.append(x)
            # Instert into the tree
            tree.Insert_Into_Tree(x)
            
        minn=min(a)
        Output1=tree.Get_Min_Recursive(tree.root)
        Output2=tree.Get_Min_Iteration() 
        if(Output1==Output2==minn):
            z+=1
            print("Test Case {} is Correct with outputs: {}  {}  {} ".format(z,Output1,Output2,minn))
        else:
            print("Error not same answer: {}  {}  {} ".format(z,Output1,Output2,minn))
            c=False
        # time.sleep(0.95)

# ************************************************************************** #

# Get User input the user enters the data he wants
# Press Enter after each input to continue element by element
def Get_User_Input(tree):
    # The user first enters the number of elemnts he want to enter
    Size = int(input("Enter the number of elements you want to Enter: "))
    for i in range(Size):
        # If he is enetering the very first element it will say to him enter the Root element 
        if i==0:
            print("Enter Tree Root Element:")	
            tree.Insert_Into_Tree(int(input()))
            print("Enter the other Tree elements you want:")
        else:
            tree.Insert_Into_Tree(int(input()))


if __name__ == '__main__':

    # Create a tree
    BinaryST = Binary_Search_Tree() 

    #**************************************#
    # Steps to ENTER the INPUT   
    # Enter Number or elements first then press Enter key
    # Then enter the other elements in the tree and then Press Enter key after each element   
    #**************************************#
    Get_User_Input(BinaryST)

    #Print the minimum from both functions
    print("Minimum From Recursive Function is",BinaryST.Get_Min_Recursive(BinaryST.root))
    print("Minimum From Iterative Function is",BinaryST.Get_Min_Iteration())


    # A Testing function 
    # TestingFunction()
    