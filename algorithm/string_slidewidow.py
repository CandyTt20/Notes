class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        l = []

        for i in range(len(s)):
            if s[i] not in l:
                l.append(s[i])
            else:
                if ans < len(l):
                    ans = len(l)
                ind = l.index(s[i])+1
                l = l[ind:]
                l.append(s[i])
                
        if ans < len(l):
            ans = len(l)

        return ans


s = "a"
print(Solution().lengthOfLongestSubstring(s))
