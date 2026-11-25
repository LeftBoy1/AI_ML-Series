import numpy as np
import matplotlib.pyplot as plt

# Data Structure: Restaurant_ID, 2021, 2022, 2023, 2024
sales_data = np.array([[1, 1200, 4324, 42203, 328723],   #Burger King
              [2, 2323, 42323, 67676, 76773],           #PizzaHut
              [3, 2321, 65768, 86867, 52644],           #Dominoes
              [4, 8797, 51685, 21545, 54795],           #Apple
              [5, 3322, 57754, 14545, 32233]])          #Samsung


print(f"Shape: {sales_data.shape}")
print(f"Size: {sales_data.size}")
print(f"Dimension: {sales_data.ndim}")
print(f"3RD SALES DATA: {sales_data[:1]}\n")
print(f"3RD SALES DATA: {sales_data[1]}\n")
print(f"3RD SALES DATA: {sales_data[:, 1:]}")   #1st column not shown





#Total per Year  
year_total = np.sum(sales_data[:, 1:] , axis = 0)           #0 for column and 1 for rows
print(year_total)

#Total Companies Networth
total_networth = np.sum(sales_data[:,1:], axis = 1)
print(total_networth)

#Minimum sales per Restaurant
mini_sales = np.min(sales_data[:, 1:], axis = 1)
print(mini_sales)

#Maximum sales per Year
max_sales = np.max(sales_data[:,1:], axis = 0)
print(max_sales)

#AVG. sales per Restuarant
avg_sales = np.mean(sales_data[:,1:], axis = 1)
print(avg_sales)

#Cumulative Sales
cum = np.cumsum(sales_data[:,1:], axis = 1)
print(cum)

plt.figure(figsize=(10 , 6))
plt.plot(np.mean(cum, axis = 0))
plt.title("AVG. Cumulative Sales")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()