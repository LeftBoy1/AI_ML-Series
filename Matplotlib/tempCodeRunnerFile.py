
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

