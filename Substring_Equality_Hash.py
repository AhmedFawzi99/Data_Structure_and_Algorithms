# python3

import sys
import random


class Solver:
	def __init__(self, s):
		# define the variables 
		self.s = s
		# define m1 as 10^9 + 7 and m2 as 10^9 + 9
		self.m1=1000000007
		self.m2=1000000009
		# generate a random number from 1-10^9
		self.random_x=random.randint(1,1000000000)
		# compute the hash table array using compute_hashvalues 
		self.hashtable1,self.hashtable2=self.compute_hashtable(self.s)
	
	# this function is used to compute the hash values table 
	def compute_hashtable(self,s):
		size=len(s)
		# intialize the array with the size of the input
		hashtable1,hashtable2 = [[] for _ in range(size)],[[] for _ in range(size)]
		# intialize the first element with 0
		hashtable1[0],hashtable2[0]=0,0
		# fill the table with hash values 
		for i in range(1, size):
			hashtable1[i] = (self.random_x * hashtable1[i - 1]  + ord(s[i - 1])) % self.m1
			hashtable2[i] = (self.random_x * hashtable2[i - 1]  + ord(s[i - 1])) % self.m2
		return hashtable1,hashtable2
	
	# this function is used to compute the hash values of the substrings using the precomputed hash values
	def compute_hashvalues_substrings(self,start,l):
		y = pow(self.random_x, l)
		# according to the property that H=h[a+1]-(x^l)*h[a]
		hashvalue1 = (self.hashtable1[start + l] - y * self.hashtable1[start]) %  self.m1
		hashvalue2 = (self.hashtable2[start + l] - y * self.hashtable2[start]) %  self.m2
		return hashvalue1,hashvalue2



	# this function checks whether the hashvalues of the substrings are the same if so it returns True else False
	def ask(self, a, b, l):
		# Call compute_hashvalues_substrings 
		hashvalue_a_m1,hashvalue_a_m2=self.compute_hashvalues_substrings(a,l)
		hashvalue_b_m1,hashvalue_b_m2=self.compute_hashvalues_substrings(b,l)
		# check if equal 
		if hashvalue_a_m1 == hashvalue_b_m1 and hashvalue_a_m2==hashvalue_b_m2:
			return True
		else:
			return False

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
