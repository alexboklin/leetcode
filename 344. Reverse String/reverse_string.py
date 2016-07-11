# Solution for cheaters
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


# Solutions for regular fellas -- with comprehension...
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''.join([s[-i] for i in range(1, len(s) + 1)])
        return res



# ... iterative
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


# ... and with tail recursion
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def accumulate(acc, src):
            if len(src) == 0:
                return acc
            return accumulate(acc + src[len(src) - 1], src[:len(src) - 1])         


        return accumulate("", s)

