import pandas as pd

visits = pd.read_csv('./analysis/data/pagevisitsfunnel/visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('./analysis/data/pagevisitsfunnel/checkouts.csv',
                        parse_dates=[1])

#print(visits)
#print(checkouts)

print("### Merge data from visits and checkout datasets ###")
v_to_c = pd.merge(visits,checkouts)
v_to_c['time'] = v_to_c['checkout_time'] -v_to_c['visit_time']
print(v_to_c.head(10))
print('####################################################')
print('### Mean Time between checkout and visit start ###')
print(v_to_c.time.mean())
print('#############################################')

