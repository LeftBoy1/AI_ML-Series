# plt.plot(x, y, color='color name', linestyle= 'line_style', linewidth = value, marker= 'marker symbol', label= 'label name')

import matplotlib.pyplot as plt

x = [ 1,2,3,4]
y = [100,350,150,400]

plt.plot(x, y, color = 'blue', linestyle = '--', linewidth = '2', marker = 'o', label = "2025 Sales Data")
plt.show()







#plt.xlabel('Text')
#plt.ylabel('Text')
import matplotlib.pyplot as plt

x = [ 1,2,3,4]
y = [100,350,150,400]

plt.plot(x, y, color = 'blue', linestyle = '--', linewidth = '2', marker = 'o', label = "2025 Sales Data")
plt.xlabel("M o n t h s")
plt.ylabel("S a l e s   p e r   M o n t h")
plt.show()








#plt.title('Text')
import matplotlib.pyplot as plt

x = [ 1,2,3,4]
y = [100,350,150,400]

plt.plot(x, y, color = 'blue', linestyle = '--', linewidth = '2', marker = 'o', label = "2025 Sales Data")
plt.xlabel("M o n t h s")
plt.ylabel("S a l e s   p e r   M o n t h s")
plt.title('Sales Data Report')
plt.show()








#plt.legend(loc='upper left OR lower right', fontsize= value)           = use to display label
import matplotlib.pyplot as plt

x = [ 1,2,3,4]
y = [100,350,150,400]
x1 =  [1,2,3,4]
y1 = [500,400,200,333]
plt.plot(x, y, color = 'purple', linestyle = '--', linewidth = '2', marker = 'o', label = "2024 Sales Data")
plt.plot(x1, y1, color = 'blue', linestyle = '--', linewidth = '2', marker = 'o', label = "2025 Sales Data")

plt.xlabel("M o n t h s")
plt.ylabel("S a l e s   p e r   M o n t h")
plt.legend(loc='upper right', fontsize= 10)
plt.show()









# plt.grid(color= 'color name', linestyle= ':', linewitdh = value)              
import matplotlib.pyplot as plt

x = [ 1,2,3,4]
y = [100,350,150,400]

plt.plot(x, y, color = 'green', linestyle = '--', linewidth = '2', marker = 'o', label = "2025 Sales Data")
plt.xlabel("M o n t h s")
plt.ylabel("S a l e s   p e r   M o n t h")
plt.legend(loc='upper left', fontsize= 12)
plt.grid(color='grey', linestyle=':', linewidth=1)
plt.show()

  
  



  
  
#plt.xlim(start, end)       =    sets the limit of x axis
#plt.ylim(start, end)       =    sets the limit of y axis 
import matplotlib.pyplot as plt

x = [ 1,2,3,4]
y = [100,350,150,400]

plt.plot(x, y, color = 'green', linestyle = '--', linewidth = '2', marker = 'o', label = "2025 Sales Data")
plt.xlabel("M o n t h s")
plt.ylabel("S a l e s   p e r   M o n t h")
plt.legend(loc='upper left', fontsize= 12)
plt.grid(color='grey', linestyle=':', linewidth=1)
plt.xlim(1,10)
plt.ylim(100,500)
plt.show()







#plt.xticks()   =   changes the original values of x axis
#plt.yticks()   =   changes the original values of y axis
import matplotlib.pyplot as plt

x = [ 1,2,3,4]
y = [100,350,150,400]

plt.plot(x, y, color = 'green', linestyle = '--', linewidth = '2', marker = 'o', label = "2025 Sales Data")
plt.xlabel("M o n t h s")
plt.ylabel("S a l e s   p e r   M o n t h")
plt.legend(loc='upper left', fontsize= 12)
plt.grid(color='grey', linestyle=':', linewidth=1)
plt.xticks([1,2,3,4], ['M1', 'M2', 'M3', 'M4'])
plt.show()




#Using input() function - 

import matplotlib.pyplot as plt

# map() - Apply int() to each element in the list (in short input() function takes numbers as a string, so to make numbers as a numbers not string , map() is used.)
#list() - makes input a list 
x = list(map(int, input("Enter x values: ").split())) 
y = list(map(int, input("Enter y values: ").split()))

plt.plot(x, y, color='green', linestyle='--', linewidth=2,
         marker='o', label="2025 Sales Data")

plt.xlabel("M o n t h s")
plt.ylabel("S a l e s   p e r   M o n t h")
plt.legend(loc='upper left', fontsize=12)
plt.grid(color='grey', linestyle=':', linewidth=1)
plt.show()
