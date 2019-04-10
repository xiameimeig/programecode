import pandas as pd

aisles = pd.read_csv('./instacart/aisles.csv')
order_products_prior = pd.read_csv('./instacart/order_products_prior.csv')
orders = pd.read_csv('./instacart/orders.csv')
products = pd.read_csv('./instacart/products.csv')

# asis--products
data = pd.merge(aisles,products,on=['aisle_id'])
data = pd.merge(data,order_products_prior,on=['product_id'])

data = pd.merge(data,orders,on=['order_id'])
print(data)
