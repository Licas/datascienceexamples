import pandas as pd

visits = pd.read_csv('./analysis/data/pagevisitsfunnel/visits.csv', parse_dates=[1])
cart = pd.read_csv('./analysis/data/pagevisitsfunnel/cart.csv', parse_dates=[1])
checkout = pd.read_csv('./analysis/data/pagevisitsfunnel/checkouts.csv', parse_dates=[1])
purchase = pd.read_csv('./analysis/data/pagevisitsfunnel/purchase.csv', parse_dates=[1])

#print(visits.head())
#print(cart.head())
#print(checkout.head())
#print(purchase.head())

#Left Join visits and cart (include visits rows without a corresponding entry in cart, but not the opposite)
v_to_c = pd.merge(visits, cart, how="left")
# Check which rows hasn't any cart_time value
not_cart = v_to_c[v_to_c['cart_time'].isnull()]
print('### Visits/Cart Merge ###')
print(v_to_c)
print("Visit/cart #rows: %d"%(len(v_to_c)))
print("Null cart time #rows: %d"%(len(not_cart)))

empty_percentage = float(len(not_cart))/len(v_to_c)
print("Percent of empty cart #rows: %.2f%%"%( empty_percentage *100))
print('##########################')

#Letf Join cart and checkout entries
cart_to_checkout = pd.merge(cart, checkout, how="left")
#print(cart_to_checkout)
#Calculate entries without checkout time
not_checkout = cart_to_checkout[cart_to_checkout['checkout_time'].isnull()]
#Compute percentage of empty checkouts
empty_percentage_checkout = float(len(not_checkout))/len(cart_to_checkout)
print("Percent of empty checkout time rows: %.2f"%( empty_percentage_checkout ))

#Left join all the datasets
all_data = visits.merge(cart,how="left").merge(checkout,how="left").merge(purchase,how="left")
print("### All datasets merge head ###")
print(all_data.head())
print('###############################')

all_data_len = float(len(all_data))

checkout_not_purchase = all_data[ (all_data['checkout_time'].notnull()) & (all_data['purchase_time'].isnull())]
print("Percentage of checkouts without purchase %f."% ( float(len(checkout_not_purchase)) / all_data_len))


null_cart = all_data[ all_data['cart_time'].isnull()]
print("Percentage of null cart step %f."% ( float(len(null_cart)) / all_data_len))

null_checkouts = all_data[ (all_data['checkout_time'].isnull()) & (all_data['cart_time'].notnull())]
print("Percentage of null checkout step %f."% ( float(len(null_checkouts)) / all_data_len))

null_purchase = all_data[ (all_data['purchase_time'].isnull()) & (all_data['checkout_time'].notnull())]
print("Percentage of null purchase step %f."% ( float(len(null_purchase)) / all_data_len))


all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print("### Time to purchase ###")
#print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())

