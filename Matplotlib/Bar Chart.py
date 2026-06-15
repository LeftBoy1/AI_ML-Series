# plt.bar(x, height, color= 'color name', width = value, label = 'label name') 


import matplotlib.pyplot as plt

# Horizontal Graph
x = [ 1,2,3,4]
y = [100,350,150,400]

plt.bar(x, y, color = 'orange', label = "2025 Sales Data")
plt.xlabel("M o n t h s")
plt.ylabel("S a l e s   p e r   M o n t h")
plt.legend()
plt.title('Products Comparison')
plt.show()








import matplotlib.pyplot as plt

# Vertical Graph
x = [ 1,2,3,4]
y = [100,350,150,400]

plt.barh(x, y, color = 'orange', label = "2025 Sales Data")
plt.xlabel("M o n t h s")
plt.ylabel("S a l e s   p e r   M o n t h")
plt.legend()
plt.title('Products Comparison')
plt.show()
