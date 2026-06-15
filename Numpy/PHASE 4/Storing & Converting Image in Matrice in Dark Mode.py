import numpy as np
import matplotlib.pyplot as plt

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.random.rand(3,3)
arr3 = np.zeros((4,4))

np.save("Array1.npy",arr1)
np.save("Array2.npy",arr2)
np.save("Array3.npy",arr3)

load_arr1 = np.load('Array1.npy')
print(load_arr1)



#DARK MODE

try:
    logo = plt.imread('F:\\Devansh_Gupta\\AI + ML\\Numpy\\PHASE 4\\o.jpg')
    
    #Display
    plt.figure(figsize=(10, 6))
    plt.subplot(121)
    plt.imshow(logo)
    plt.title('Wallpaper')
    plt.grid(False)
    plt.axis('off')
    # plt.show()
    
    dark_logo = 1-logo 
    plt.subplot(122)
    plt.imshow(dark_logo)
    plt.title('Dark Wallpaper')
    plt.grid(False)
    plt.axis('off')
    plt.show()
    
    
except FileNotFoundError:
    print("Logo Not Found")