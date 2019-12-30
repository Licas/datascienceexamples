import pandas as pd

orders = pd.read_csv('./analysis/data/shoefly.csv')

print(orders.head())

emails = orders.email 

frances_palmer = orders[(orders.first_name=='Frances') & (orders.last_name=='Palmer')]

comfy_shoes = orders[orders.shoe_type.isin(['clogs','boots','ballet flats'])]
print("---- CHECK ORDERS WITH SHOE TYPE IN clogs, boots, ballet flats")
print(comfy_shoes)


vegan_lambda = lambda row: 'vegan' \
  if row['shoe_material'] != 'leather' \
  else 'animal'

orders['shoe_source'] = orders.apply(vegan_lambda,axis=1)
print("---- ADDED SHOE SOURCE COLUMN ----")
print(orders.head())


salutation_lambda = lambda row: 'Dear Mr. ' + row['last_name']  \
    if row['gender'] == 'male' \
    else 'Dear Mrs. ' + row['last_name']

orders['salutation'] = orders.apply(salutation_lambda, axis=1)
print("---- ADDED SALUTATION COLUMN ----")

print(orders.head())