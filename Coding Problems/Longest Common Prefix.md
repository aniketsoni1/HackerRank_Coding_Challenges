<h1>Longest Common Prefix</h1><br/>
Write a function to find the longest common prefix string amongst an array of strings.<br/><br/>

If there is no common prefix, return an empty string "".<br/><br/>

<b>Example 1:</b><br/>

<b>Input:</b> strs = ["flower","flow","flight"]<br/>
<b>Output:</b> "fl"<br/><br/>

<b>Example 2:</b><br/>

<b>Input:</b> strs = ["dog","racecar","car"]<br/>
<b>Output:</b> ""<br/>
<b>Explanation:</b> There is no common prefix among the input strings.<br/><br/>
 

<b>Constraints:</b><br/>

0 <= strs.length <= 200<br/>
0 <= strs[i].length <= 200<br/><br/>
strs[i] consists of only lower-case English letters.<br/><br/>

<code>

	class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        for item in strs:
            if len(item)>len(prefix): prefix = item

        for item in strs:
            x = len(item)
            prefix = prefix[:x]
            while prefix!=item[:x]:
                x -= 1
                prefix = prefix[:x]
        return prefix

</code>