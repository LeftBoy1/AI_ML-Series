import numpy as np

#CASE 1
vector1 = np.array([1,2,3,4,5])
vector2 = np.array([6,7,8,9,10])
print(vector1+vector2)
print(vector1*vector2)
print(vector1/vector2)
print(np.dot(vector1, vector2))     #.dot() - It multiplies corresponding elements and adds them.
'''dot of vector1 and vector2 - 
            1*6 = 6
            2*7 = 14
            3*8 = 24
            4*9 = 36
            5*10 = 50
            
            then,  6+14+24+36+50 = 130'''




angle1 = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))      #arccos = cos^(-1)
angle2= np.cos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
'''This is directly based on the dot product formula:
        cos(θ) = (a.b) / (|a||b|)
        
            where, a.b = dot product of a and b variable
                   |a||b| = magnitude/lenght of a and b variable 
                   
                   
    
    so, np.linalg.norm = Computes the length (magnitude) of each vector
        np.dot() = Computes the dot product
        '''
                           
print(angle1)
print(angle2)




#CASE 2(BROADCASTING)
import numpy as np
restaurant_types = np.array(['chinese', 'burger', 'pizza', 'cafe'])
vectorised_upper = np.vectorize(str.upper)      #np.vectorize() is a shortcut to apply a function to every element without writing a loop
print(vectorised_upper(restaurant_types))
# It is used to apply str.upper() to every element of the NumPy array at once, without writing a loop.





#CASE 3
# Data Structure: Restaurant_ID, 2021, 2022, 2023, 2024
import numpy as np
sales_data = np.array([[1, 1200, 4324, 42203, 328723],   #Burger King
              [2, 2323, 42323, 67676, 76773],           #PizzaHut
              [3, 2321, 65768, 86867, 52644],           #Dominoes
              [4, 8797, 51685, 21545, 54795],           #Apple
              [5, 3322, 57754, 14545, 32233]])          #Samsung

monthly_avg = sales_data[:,1:] / 12
print(monthly_avg)