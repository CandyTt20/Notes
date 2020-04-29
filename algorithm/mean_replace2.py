






import numpy as np

a = np.arange(12).reshape(3, 4).astype(float)
a[[1, 2], [1, 2]] = np.nan

def replace(x):
    for i in range(x.shape[1]): #! 取出一列
        colum = x[:, i]   #! 设此列为column
        if np.count_nonzero(colum != colum) != 0: #! 如果这列有nan
            colum[colum != colum] = colum[colum == colum].mean()
            #? 将此列平均值赋给nan
            x[:, i] = colum #? 将替换后的列作为新列
    return x #? 返回操作后的array

if __name__ == "__main__":
    print(a)
    print(replace(a))
