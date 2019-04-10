from sklearn.feature_extraction import DictVectorizer

# 数据
data = [{'city':'杭州','wu':'一般'},{'city':'上海','wu':'无'},{'city':'北京','wu':'严重'},{'city':'石家庄','wu':'特别严重'}]
print(data)

# 创建字典特征提取器
dvt = DictVectorizer(sparse=False)
# 特征转化，建立数据key 和 values的矩阵，完成特征的提取
# data必须是可迭代对象 ，可以是列表或者元组
data_fit = dvt.fit_transform(data)
# 打印数据的特征

print(dvt.get_feature_names())
# 将稀疏矩阵转为数组，one-hot编码
print(data_fit)

# 将经过转换之后的数据，换回原来的形式
print(dvt.inverse_transform(data_fit))


