
# plt.subplot(nrows, ncols, index)
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [5,15,10,20]

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title('Line Chart')

plt.subplot(1, 2, 1)
plt.bar(x, y)
plt.title('Bar Chart')
plt.show()

