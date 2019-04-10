'''
v = dict.fromkeys(['k1','k2'],[])v[‘k1’].append(666)print(v)v[‘k1’] = 777print(v)
'''
v = dict.fromkeys(['k1','k2'],[])
# Returns a new dict with keys from iterable and values equal to value.
print(v)
v['k1'].append(666)
print(id(v['k1']))
print(id(v['k2']))
print(v)
v['k1'] = 777
print(id(v['k1']))
print(v)