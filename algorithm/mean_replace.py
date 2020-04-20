import numpy as np

#! the origional array which embrace nan
t = [1.2, 4, 3, 5, np.nan, 2, np.nan, 3.7]
x = np.array(t)

#! calculate the number without nan
num = x.size - np.count_nonzero(np.isnan(x))

#! save the origional array
x_result = x.copy()

#! create the new array with nan -> 0
x[np.isnan(x)] = 0

#! obtain the mean
_mean = np.sum(x)/num

#! replace nan with mean and get the results
x_result[np.isnan(x_result)] = _mean




# print(x)
