<h1>Project Euler #42: Coded triangle numbers</h1><br/>
The n<sup>th</sup> term of a sequence of triangle numbers is given by,<br/>
t<sub>n</sub> = 1/2(n(n+1))
<br/>
so the first ten triangle numbers are:<br/>
1,3,6,10,15,21,28,36,45,55,...<br/>
You are given an integer. If it is a triangular number t<sub>n</sub>, print the term <b>n</b> corresponding to this number, else print -1<br/>


<b>Input Format</b><br/>

First line of input contains an integer  denoting the number of testcases. Each of the next  lines contains an integer.
<br/>
<b>Constraints</b>
<br/>
1<=T<=10<sup>5</sup><br/>
1<=t<sub>n</sub><=10<sup>18</sup><br/>


<b>Output Format</b><br/>

Print the answer corresponding to each test case in a new line.<br/>

<b>Sample Input</b><br/>

3<br/>
2<br/>
3<br/>
55<br/><br/>
<b>Sample Output</b><br/>

-1<br/>
2<br/>
10<br/>
<br/>



<code>
import math
def isTriang(K):
    x=(-1+math.sqrt(1+8*K))/2
    if x==int(x):
        return int(x)
    else:
        return -1

for _ in range(int(input())):
    t=int(input())
    print(isTriang(t))
</code>