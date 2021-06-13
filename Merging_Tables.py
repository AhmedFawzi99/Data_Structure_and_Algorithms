# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    # this function serves to merge the tables together but it has to go throught so proccesses to do that
    def merge(self, dst, src):
        #Get the parent for the Source and Destination Tables
        src_parent = self.Get_Parent_Compress(src)
        dst_parent = self.Get_Parent_Compress(dst)

        # if the same table is being merged with itself return
        if src_parent == dst_parent:
            return False

        # to merge the tables we have first to update the rank and the number of rows of the parent table to be higher in rank
        self.Update_Rank_RowCount_Max(dst_parent,src_parent)
        
        return True

    # this if the updat rank , row count function( most important function) and then calculate new max
    def Update_Rank_RowCount_Max(self,dst_parent,src_parent):
        
        # this function has 3 checks to do 
        # the first is that the rank of the destination is lower than the source 
        # in this case we make the parent the source and update the rows of the source 
        # then we calculate the new maximum
        if self.ranks[dst_parent] < self.ranks[src_parent]:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] += self.row_counts[dst_parent]
            self.row_counts[dst_parent] = 0
            self.Update_Maximum(src_parent)

        # the first is that the rank of the destination is greater than the source 
        # in this case we make the parent the destination and update the rows of the destination table
        # then we calculate the new maximum
        elif self.ranks[dst_parent] > self.ranks[src_parent]:
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.row_counts[src_parent] = 0
            self.Update_Maximum(dst_parent)

        # in this case both ranks are equal so it doesnot matter which to be the parent but lets make it the destination 
        # we increase the rank by one here since they are similar 
        # then we calculate the new row count and maximum
        else:
            self.parents[src_parent] = dst_parent
            self.ranks[dst_parent] = self.ranks[dst_parent] + 1
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.row_counts[src_parent] = 0
            self.Update_Maximum(dst_parent)
        
    # This function serves to get the parent of the passed table and also compresses the path an important step 
    def Get_Parent_Compress(self, table):

        # An array to store the path we moved in so that we could later use to compress the path
        pathtoroot=[]

        # Call function get root parent that recursively calls itself until it finds the parent
        root_parent,pathtoroot=self.Find_Root_Parent(table,pathtoroot)

        # the return of find root parent is the path to the root so we could use it to compress the path 
        # we path the root parent and the path to the compress function to compress
        self.Compress_Path(pathtoroot,root_parent)
        
        return root_parent

    # this function serves to find the root parent of the table
    def Find_Root_Parent(self,table,pathtoroot):

        # checks if it is the parent itself
        if self.parents[table] == table:
            return self.parents[table] , pathtoroot
        else:
            # if no we append the path to the root
            pathtoroot.append(self.parents[table])
            #recursively call the function until we find the root parent
            self.parents[table] , pathtoroot=self.Find_Root_Parent(self.parents[table],pathtoroot)
        return self.parents[table] , pathtoroot

    # compress the path by looping on the path array and setting the paren to the root directly
    def Compress_Path(self,pathtoroot,parent):
        for i in pathtoroot:
            self.parents[i] = parent
    
    # update the maximum function
    def Update_Maximum(self,parent):
        if self.max_row_count < self.row_counts[parent]:
            self.max_row_count = self.row_counts[parent]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    Output=[]
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        Output.append(db.max_row_count)
    for i in Output:
        print(i)

if __name__ == "__main__":
    main()
