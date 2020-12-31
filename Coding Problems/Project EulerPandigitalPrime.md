<h1>Project Euler: Pandigital prime</h1><br/>
We shall say that an -digit number is pandigital if it makes use of all the digits 1 to  exactly once. For example,  is a -digit pandigital and is also prime.<br/>
<br/>
What is the largest <b>n</b>-digit pandigital prime <b><=N</b>? If there is none, print -1<br/><br/>

<b>Input Format</b><br/>

First line contains <b>T</b> that denotes the number of test cases. This is followed by <b>T</b> lines, each containing an integer, <b>N</b>.<br/>
<br/>
<b>Constraints</b><br/>

1<=T<=10<sup>5</sup><br/>
10<=N<=10<sup>10</sup>-1
<br/><br/>
<b>Output Format</b><br/>

Print the required answer for each test case.<br/><br/>

<b>Sample Input</b>
<br/>
2<br/>
100<br/>
10000<br/><br/>

<b>Sample Output</b><br/>

-1<br/>
4231<br/><br/>

<code>

	# Enter your code here. Read input from STDIN. Print output to STDOUT

	from itertools import permutations  
	from bisect import bisect_left

	# Function to determine a prime number 
	# Time complexity = O(sqrt(n))
	def isPrime(n):
	  if n == 2 or n == 3: return True
	  if n%2 == 0 or n < 2: return False
	  for i in range(3, int(n**0.5)+1, 2): # Only odd numbers
	    if n%i == 0:
	      return False    

	  return True

	def Pandigital_Prime():
	  # Create all permutation of numbers
	  # Time complexity = O(m) = O(1! + 2! +...+ 9! = 409113)
	  permTuples = []
	  for i in range(2,10):
	    perm = list(permutations(range(1,i+1)))
	    permTuples += perm

	  # Convert tuples to integer
	  # Time complexity = O(m)
	  permNums = []
	  for i in permTuples:
	    num = int(''.join([str(j) for j in i]))
	    permNums.append(num)

	  # For every element in the list we'll check if it's prime or not
	  # Time complexity = O(m^1.5)
	  primes = []
	  for i in permNums:
	    if isPrime(i) == True:
	      primes.append(i)
	    
	  # Sort the list for better access of index 
	  # Time complexity = O(mlogm)
	  primes.sort()
	  
	  return primes
	  
	if __name__ == '__main__':
	  primes = Pandigital_Prime()
	  
	  for _ in range(int(input())):
	    n = int(input())
	    
	    # Use Binary Search Tree to find the closest prime to n
	    # Time complexity = O(logm)
	    idx = bisect_left(primes, n) 
	    if idx<len(primes) and primes[idx] <= n:
	      print(primes[idx])
	    elif primes[idx-1] <= n:
	      print(primes[idx-1])
	    else:
	      print(-1)

</code>
