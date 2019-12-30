import pandas as pd

user_visits = pd.read_csv('./analysis/data/page_visits.csv')

print(user_visits.head())

print('### User Visits - Group by UTM Source and count ###')
click_source = user_visits.groupby('utm_source').id.count().reset_index().rename(columns={'id':'count'})
print(click_source)
print('##################################################')

print('### User Visits - Group by UTM Source and Month and count ###')
click_source_by_month = user_visits.groupby(['utm_source','month']).id.count().reset_index().rename(columns={'id':'count'})
print(click_source_by_month )
print('#############################################################')

print('### User Visits - Pivot table by  UTM Source(rows) and Month(columns) and count ###')
click_source_by_month_pivot = click_source_by_month.pivot(columns='month',index='utm_source',values='count').reset_index()

print(click_source_by_month_pivot)