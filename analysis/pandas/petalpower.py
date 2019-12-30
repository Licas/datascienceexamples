import pandas as pd

inventory = pd.read_csv('./analysis/data/petalpower.csv')
print('### PetalPower Head 10 ###')
print(inventory.head(10))
print('##########################')

staten_island = inventory[0:10]
#Product Descriptions from products sold in Staten Island 
print('### Product Descriptions from products sold in Staten Island ###')
product_request = staten_island['product_description']
print(product_request)
print('################################################################')

print('### Seeds sold in Brooklyn ###')
seed_request = inventory.loc[(inventory.location == 'Brooklyn' ) & (inventory.product_type == 'seeds')]
print(seed_request)
print('###############################')

print('### Check products not in stock ###')
inventory['in_stock'] = inventory.apply(lambda row: True \
    if row.quantity > 0 \
    else False, axis=1)
print(inventory[inventory['in_stock'] == False])
print('###############################')

print('### Compute products total value, print only in stock')
inventory['total_value'] = inventory['price'] * inventory['quantity'] 
print(inventory[inventory['in_stock']==True])
print("Sum of in stock products is %.2f"%(inventory[inventory['in_stock']==True].total_value.sum()))
print('###############################')

print('### Get products full description ###')
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type, row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory)
print('####################################')