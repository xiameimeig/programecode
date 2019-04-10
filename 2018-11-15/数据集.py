from sklearn.datasets import load_iris,fetch_20newsgroups
from sklearn.model_selection import train_test_split

iris = load_iris()
# print(iris)
data_x = iris.data
label_y = iris.target

new = fetch_20newsgroups()
# print(new.data)
# print(new.target)
# 分训练集与测试集

X_train, X_test, y_train, y_test =train_test_split(data_x,label_y)


