# Case 1
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y)          
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()


#Case 2
import matplotlib.pyplot as plt

p = [5,10,15,20,25,30,35,40,45,50,55,60,65]
q = [2323,3232,6,4343,1313,87,334,232,5544,212,1212,44,12]
plt.plot(p, q)
plt.show()



#Case 3
import matplotlib.pyplot as plt

x = [2020, 2021, 2022, 2023, 2024, 2025]
y = [123,1212,5453,3457,56564,34212]

plt.plot(x,y)
plt.title("Phones Sales Per Year")
plt.xlabel('Y E A R')
plt.ylabel('No. Of Phones Sales')
plt.show()