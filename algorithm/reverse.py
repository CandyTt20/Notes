class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        """

        s = ''
        if x<0:
            lt = [i for i in str(x)[1:]]
            while lt:
                s += str(lt.pop())
            if -int(s) < -2 ** 31:
                return 0
            else:
                return -int(s)
        else:
            lt = [i for i in str(x)]
            while lt:
                s += str(lt.pop())
            if int(s) > 2 ** 31 - 1:
                return 0
            else:
                return int(s)
if __name__ == "__main__":
    print(Solution().reverse(-123))