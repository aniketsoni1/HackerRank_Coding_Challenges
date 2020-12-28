<h1>Palindrome Number</h1><br/><br/>
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.<br/>

<b>Follow up:</b> Could you solve it without converting the integer to a string?<br/><br/>

 

<b>Example 1:</b><br/>

Input: x = 121<br/>
Output: true<br/><br/>

<b>Example 2:</b><br/>

Input: x = -121<br/>
Output: false<br/>
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.<br/><br/>

<b>Example 3:</b><br/>

Input: x = 10<br/>
Output: false<br/>
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.<br/><br/>

<b>Example 4:</b><br/>

Input: x = -101<br/>
Output: false<br/><br/>
 

<b>Constraints:</b><br/>

-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1
<br/>

<code>

	class Solution:
	    def isPalindrome(self, x: int) -> bool:
	        if x < 0:
	            return False

	        if x != 0 and x % 10 == 0:
	            return False

	        a = x
	        b = 0
	        while b < a:
	            b *= 10
	            b += a % 10
	            a -= a % 10
	            a /= 10

	        if int(a) == int(b):
	            return True

	        b -= b % 10
	        b /= 10
	        if int(a) == int(b):
	            return True

	        return False

</code>

