<h1>Migratory Birds</h1>

You have been asked to help study the population of birds migrating across the continent. Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. You would like to be able to find out which type of bird is most common given a list of sightings. Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number.<br/><br/>

For example, assume your bird sightings are of types arr = [1,1,2,2,3]. There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.<br/><br/>

<b>Function Description</b><br/>
Complete the migratoryBirds function in the editor below. It should return the lowest type number of the most frequently sighted bird.<br/>

migratoryBirds has the following parameter(s):

* arr: an array of integers representing types of birds sighted<br/><br/>

<b>Input Format</b><br/>
The first line contains an integer denoting n, the number of birds sighted and reported in the array arr.<br/>
The second line describes arr as n space-separated integers representing the type numbers of each bird sighted.<br/><br/>

<b>Constraints</b><br/>
* 5 <= n <= 2 x 10<sup>5</sup><br/>
* It is guaranteed that each type is 1, 2, 3, 4 or 5.<br/><br/>

<b>Output </b><br/>
Print the type number of the most common bird; if two or more types of birds are equally common, choose the type with the smallest ID number.<br/><br/>

<b>Sample Input 0</b><br/>
6<br/>
1 4 4 4 5 3<br/><br/>

<b>Sample Output 0</b><br/>
4<br/><br/>

<b>Explanation 0</b><br/>
The different types of birds occur in the following frequencies:<br/>

* Type 1: 1 bird<br/>
* Type 2: 0 birds<br/>
* Type 3: 1 bird<br/>
* Type 4: 3 birds<br/>
* Type 5: 1 bird<br/><br/>

The type number that occurs at the highest frequency is type 4, so we print 4 as our answer.<br/><br/>

<b>Sample Input 1</b><br/>
11<br/>
1 2 3 4 5 4 3 2 1 3 4<br/><br/>

<b>Sample Output 1</b><br/>
3<br/><br/>

<b>Explanation 1</b><br/>
The different types of birds occur in the following frequencies:<br/>

* Type 1: 2<br/>
* Type 2: 2<br/>
* Type 3: 3<br/>
* Type 4: 3<br/>
* Type 5: 1<br/><br/>
Two types have a frequency of 3, and the lower of those is type 3.<br/><br/>


<code>
	#!/bin/python3

	import math
	import os
	import random
	import re
	import sys

	# Complete the migratoryBirds function below.
	def migratoryBirds(arr):
	    a=[]
	    l=len(arr)
	    v=0
	    for i in range(1,10):
	        v=0
	        for j in range(0,l):
	            if(i==arr[j]):
	                v=v+1
	        a.append(v)
	    
	    b=[]
	    for i in a:
	        b.append(i)
	    for h in range(0,len(b)):
	        for i in range(0,len(b)):
	            for j in range(0,len(b)):
	                if(i!=j):
	                    if(b[i]<b[j]):
	                        temp=b[i]
	                        b[i]=b[j]
	                        b[j]=temp
	    value=b[len(b)-1]
	    
	    c=[]
	    for i in range(0,len(a)):
	        if(value==a[i]):
	            c.append(i+1)
	    return c[0]
	if __name__ == '__main__':
	    fptr = open(os.environ['OUTPUT_PATH'], 'w')

	    arr_count = int(input().strip())

	    arr = list(map(int, input().rstrip().split()))

	    result = migratoryBirds(arr)

	    fptr.write(str(result) + '\n')

	    fptr.close()

</code>