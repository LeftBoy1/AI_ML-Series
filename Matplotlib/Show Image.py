import matplotlib.pyplot as plt

img = plt.imread("o.jpg")

plt.imshow(img)
plt.axis('off')   # hides x and y axis
plt.show()
