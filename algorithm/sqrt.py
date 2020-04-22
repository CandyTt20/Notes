
#! 牛顿迭代法


def sqrt(k):
    x = k
    while x * x - k > 1e-6:
        x = (x + k / x) / 2
    return x


print(sqrt(2))
