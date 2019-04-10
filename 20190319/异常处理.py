# try:
#     a = int(input('请输入被除数'))
#     b = int(input('请输入除数'))
#     print(c)
#     print(a/b)
#     print('##########################')
# # except:
# # #     print('数据错误')
# except Exception as e:
#     print(e)



def multipliers():
    return [lambda x : i * x for i in range(4)]
# print([m(2) for m in multipliers()])
# ret = multipliers()
# for i in ret:
#     print(i)