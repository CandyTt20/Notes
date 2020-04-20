class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        note = -1
        for i in range(len(s)):
            if l.find(s[i]) != -1:
                l = l[l.find(s[i]) + 1:]
            l.append(s[i])


l = ['a', 'b']
print(l.index('a')+1)
print(l[1:])
