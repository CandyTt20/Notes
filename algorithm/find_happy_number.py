def squre_sum(num):
    sum_num = 0

    while num != 0:
        remain = num % 10
        num = num // 10
        sum_num += remain * remain
    return sum_num


def find_happy_number(num):
    # TODO: Write your code here
    frequency={}
    while True:
        k = squre_sum(num)
        if k != 1:
            if k not in frequency:
                frequency[k] = 0
                num = k
            else:
                return False
        else:
            return True
        
        



def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()

