# 标准化问题
from sklearn.preprocessing import StandardScaler

data = [[1600, 50, 2],
        [180 ,1 , 0],
        [189 ,0  ,0]]


ss = StandardScaler()
data_new = ss.fit_transform(data)
print(data_new)

# 归一化结果
# [[1.         1.         1.        ]
#  [0.         0.02       0.        ]
#  [0.00633803 0.         0.        ]]