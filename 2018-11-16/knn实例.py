import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

data = pd.read_csv('train_demo.csv')
# print(data)
time_stamp = data['time']
# print(time_stamp)
time_value = pd.to_datetime(time_stamp,unit='s')
# print(time_value)

time_data = pd.DatetimeIndex(time_value)
data['weekday']=time_data.weekday
data['month']=time_data.month
data['day']=time_data.day

data.drop(labels=['time'],axis=1)
# 默认为行，在原始数据上做操作
place_count = data.groupby('place_id').count()

index_values = place_count[place_count.row_id > 20].reset_index()
data = data[data['place_id'].isin(index_values.place_id)]
# print(data)

data = data.query('x <1 & y<1')
# print(data)

x = data.drop(['place_id','time','row_id','accuracy'],axis=1,inplace=False)
y = data['place_id']

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

knn = KNeighborsClassifier()
knn.fit(X_train,y_train)
y_predict = knn.predict(X_test)
# print(knn.score(X_test,y_test))
print(classification_report(y_test,y_predict))
