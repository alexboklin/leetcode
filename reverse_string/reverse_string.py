# Solution for cheaters
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


# Solution for regular fellas -- accepted
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''.join([s[-i] for i in range(1, len(s) + 1)])
        return res



# Slow
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        
        for i in range(1, len(s) + 1):
        	res += s[-i]
        
        return res 
