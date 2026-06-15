
#CASE 2(BROADCASTING)
import numpy as np
restaurant_types = np.array(['chinese', 'burger', 'pizza', 'cafe'])
vectorised_upper = np.vectorize(str.upper)
print(vectorised_upper(restaurant_types))
