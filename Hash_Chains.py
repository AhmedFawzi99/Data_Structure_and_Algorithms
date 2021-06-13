# python3

# gets the query type and index if passed with check
class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # create the hash table it is an array if m lists( chains ) of objects
        self.h_table = [[] for _ in range(bucket_count)]
        # a boolean to check if it is already there or no
        self.istherealready=False
        # hash_position ( hash key )
        self.hash_position=-1
    ## Transforming key input to a hash vaue using has function
    def _hash_func(self, s):
        hvalue = 0
        # generating the value by computing it for each letter in the string then multiply and add it to
        # an integer representing the Unicode code point of the character
        for c in reversed(s):
            hvalue = (hvalue * self._multiplier + ord(c)) % self._prime
        return hvalue % self.bucket_count

    
    # this function check if the variable self.istherealready is True or False is true so we print Yes else NO it is not found
    def find(self):
        print('yes' if self.istherealready!= False else 'no')


    # This is print the chain function that is used in check it prints the passed objects
    # which are the data if found in that place 
    def print_chain(self, chain):
        print(' '.join(chain))

    # This function serves to add or delete the passed string 
    # it checks for which type is enterd either delete or add then it goes to that place in the hash table and then add or deletes the value 
    def add_delete(self,data,s):
        # check if add and also is not there before
        if s=='add' and self.istherealready == False :
            self.h_table[self.hash_position].insert(0,data)
        # check if delete and also is there before
        elif s=='del' and self.istherealready != False:
            self.h_table[self.hash_position].remove(data)

    # function to read the input query ( add,del,find,check )
    def read_query(self):
        return Query(input().split())

    # this fucntion serves to check if the string is already there or no to be able to find add, or delete according to the result from this function
    def alreadythere(self,string):
        # check if the string is there in that position
        if string in self.h_table[self.hash_position]:
            self.istherealready=True
        else:
            self.istherealready=False



    # this is the most important function it calls the remaining functions depending on the input query
    def process_query(self, query):
        if query.type == "check":
            # for each value in this current location we want to check on we pass it to the print chain function to print
            self.print_chain(cur for cur in self.h_table[query.ind])
        else:
            # we compute first the hash value ( position to go to ) by passing the string to the _hash_function
            self.hash_position= self._hash_func(query.s)
            #check if the passed string is already there
            self.alreadythere(query.s)
            # if the query type is find we call the find function to print yes if found and no if not
            if query.type == 'find':
                self.find()
            # The add fucntion it takes the string it wants to insert in then we insert from the begining 
            elif query.type == 'add':
                    self.add_delete(query.s, query.type)
            # del has been input and we wan to delete a string 
            elif query.type == 'del':
                    self.add_delete(query.s, query.type)

    # calls the procces query multiple times according to user input
    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

