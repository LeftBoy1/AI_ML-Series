#Subplot is used to display number of graphs in  a single window



# plt.subplot(nrows, ncols, index)
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [5,15,10,20]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title('Line Chart')

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title('Bar Chart')
plt.show()













# (Using Object Oriented API)
# fig, ax = plt.subplots(nrows, ncols, figsize= (width, height))
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize= (10,5))

x = [1,2,3,4]
y = [5,15,10,20]

ax[0].plot(x, y, color = 'blue')
ax[0].set_title('Line Plot')

ax[1].bar(x, y, color = 'green')
ax[1].set_title('Bar Chart')

plt.suptitle("Comparison of Line and Bar Charts")
plt.tight_layout()
plt.show()










import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [5,15,10,20]

plt.subplot(1, 3, 1)                    
plt.plot(x, y)
plt.title('Line Chart')

plt.subplot(1, 3, 2)
plt.bar(x, y)
plt.title('Bar Chart')

plt.subplot(1, 3, 3)
plt.pie(y, labels=x, autopct='%.1f%%')
plt.title('Pie Chart')

plt.tight_layout()
plt.show()


''' using 3 in middile of subplot instead of 2 in (1,3,1) , (1,3,2) , (1,3,3) becuase we are showing 3 graphs in a single window 
    so if we want 4 graphs in a single window then we have to write (1,4,1) , (1,4,2) , (1,4,3) , (1,4,4)'''