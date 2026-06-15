import matplotlib.pyplot as plt

img = plt.imread("line_plot.png")

plt.imshow(img)
plt.axis('off')   # hides x and y axis
plt.show()
