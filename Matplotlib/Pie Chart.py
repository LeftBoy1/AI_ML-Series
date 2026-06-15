# plt.pie(values, labels= 'lable_list', colors= 'color_list', autopct= '%1.1f%%')
import matplotlib.pyplot as plt

revenue = [300,452,100,200]
regions = ['North', 'South', 'East', 'West']

plt.pie(revenue , labels = regions , colors = ['red', 'blue', 'green', 'orange'] , autopct = '%.2f%%')

'''autopct(automatic percentage formatting) is only used in pie charts, and it controls how the percentage values are displayed on each slice.
            
            If we are not using autopct then , 
                example - showing percentage like - 33.333333333333333333333%
                
            If we are using autopct then , 
                example - showing percentage like - 33.33%
                
                
                
    Why we can't use ".2f" instead of "autopct"? - 
            Because , .2f formats numbers you already have while autopct formats numbers that Matplotlib calculates internally
'''


plt.title('Revenue Contribution by Region')
plt.show()