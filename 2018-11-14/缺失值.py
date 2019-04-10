from sklearn.preprocessing import Imputer
import numpy as np
data = [[1,2,3],[4,5,6],[np.nan,6,4],[4,5,6]]
print(data)

it = Imputer(strategy='most_frequent',axis=1)
# missing_values="NaN", strategy="mean",axis=0, verbose=0, copy=True
# '''        - If "mean", then replace missing values using the mean along
#           the axis.
#         - If "median", then replace missing values using the median along
#           the axis.
#         - If "most_frequent", then replace missing using the most frequent
#           value along the axis.
#
#     axis : integer, optional (default=0)
#         The axis along which to impute.
#
#         - If `axis=0`, then impute along columns.
#         - If `axis=1`, then impute along rows.'''
data = it.fit_transform(data)
print(data)