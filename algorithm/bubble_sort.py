def bubble_sort(l):
    #? 冒泡排序（顺序表）
    for k in range(len(l)-1):
        for i in range(len(l)-1-k):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                i += 1
    return l
            
                
l=[4,5,2,7,8]
print(bubble_sort(l))