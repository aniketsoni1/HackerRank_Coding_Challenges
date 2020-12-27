<h1> Reverse Integer: </h1>
Given a 32-bit signed integer, reverse digits of an integer.
</br></br>
<b>Note:</b> </br>
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2<sup>31</sup>,  2<sup>31</sup> − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
</br></br></br>
<b>Example 1:</b> </br>
Input: x = 123 </br>
Output: 321
</br></br>
<b>Example 2:</b> </br>
Input: x = -123 </br>
Output: -321
</br></br>
<b>Example 3:</b> </br>
Input: x = 120 </br>
Output: 21
</br></br>
<b>Example 4:</b> </br>
Input: x = 0 </br>
Output: 0
 </br></br>
<b>Constraints:</b> </br>
-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1
</br> </br>

<b>Solution: </b>

<code>
  class Solution:
  
      def reverse(self, x: int) -> int:

          neg = False
          if x < 0:
              neg = True

          return_int = 0
          rev_x = abs(x)
          while rev_x != 0:
              return_int *= 10

              if return_int > 2147483648:
                  return 0

              return_int += rev_x % 10
              rev_x -= rev_x % 10
              rev_x /= 10

          if not neg and return_int > 2147483647:
              return 0

          if neg:
              return_int *= -1

          return int(return_int)
        
</code>
