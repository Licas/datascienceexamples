import pandas as pd

ad_clicks = pd.read_csv('./analysis/data/ad_clicks.csv')
print('### AB Test Head ###')
print(ad_clicks.head())
print('####################')

print('### AB Test - Clicks grouped by UTM Source ###')
utm_source_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print('##############################################')

print('###  Check the percent of people who clicked on ads from each utm_source ###')
#Add column "is_click" that checks if a user clicked the ad or not
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.isnull()
#Group the rows by UTM Source and click
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

clicks_pivot=clicks_by_source.pivot(
    columns='is_click',
    index='utm_source',
    values='user_id').reset_index()

clicks_pivot['percent_clicked'] = \
100*clicks_pivot[True] \
/ (clicks_pivot[False]+clicks_pivot[True])

print(clicks_pivot)
print('############################################################################')


# The column experimental_group tells us whether the user was shown Ad A or Ad B.

print('### Experimental - Group by A/B group and click status ###')
experimental = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
print(experimental)
print('####################')

print("### Create a pivot table for experimental groups with percentages")
experimental_pivot = experimental.pivot(
    columns="is_click",
    index="experimental_group",
    values="user_id").reset_index()
#print(experimental_pivot)

#Build A/B percentages by day
a_clicks = ad_clicks[ad_clicks['experimental_group']=='A' ]
b_clicks =  ad_clicks[ad_clicks['experimental_group']=='B']

a_clicks_byday = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()
b_clicks_byday = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()

a_clicks_byday_pivot = a_clicks_byday.pivot(
    columns='is_click',
    index='day',
    values='user_id')

b_clicks_byday_pivot = b_clicks_byday.pivot(
    columns='is_click',
    index='day',
    values='user_id')

a_clicks_byday_pivot['Click %'] = a_clicks_byday_pivot[True]*100 /  (a_clicks_byday_pivot[False]+a_clicks_byday_pivot[True])
b_clicks_byday_pivot['Click %'] = b_clicks_byday_pivot[True]*100 /  (b_clicks_byday_pivot[False]+b_clicks_byday_pivot[True])

print('### Pivot Table for Experimental "A" Group percentages ###')
print(a_clicks_byday_pivot)
print('### Pivot Table for Experimental "B" Group percentages ###')
print(b_clicks_byday_pivot)