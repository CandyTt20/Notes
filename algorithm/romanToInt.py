#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d1 = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'],
                      [1, 5, 10, 50, 100, 500, 1000]))
        d2 = dict(zip(['IV', 'IX', 'XL', 'XC', 'CD', 'CM'],
                      [4, 9, 40, 90, 400, 900]))
        key_1, key_2 = 0, 2
        result = 0
        while key_2 < len(s)+1:
            if s[key_1: key_2] in d2:
                result += d2[s[key_1: key_2]]
                key_1 += 2
                key_2 += 2

            else:
                result += d1[s[key_1]]
                key_1 += 1
                key_2 += 1

        if key_1 == len(s) - 1:
            return result + d1[s[key_1]]
        else:
            return result


# @lc code=end

if __name__ == "__main__":
    print(Solution().romanToInt("LVIII"))
