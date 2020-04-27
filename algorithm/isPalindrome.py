#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] å›žæ–‡æ•°
#

# @lc code=start


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        low, high = 0, len(s) - 1
        isTrue = True
        while low < high:
            isTrue = isTrue and (s[low] == s[high])
            low += 1
            high -= 1

        return isTrue


if __name__ == "__main__":
    print(Solution().isPalindrome(-121))


# @lc code=end
