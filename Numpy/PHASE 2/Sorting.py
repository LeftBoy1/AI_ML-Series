'''Sorting in NumPy is used to arrange data in a specific order
Why sorting is used -
                    1️⃣ Data analysis -
                                        Find minimum / maximum
                                        Understand distribution
                                        Detect outliers

                    2️⃣ Machine Learning -
                                        Preprocessing datasets
                                        Rank predictions
                                        Feature analysis

                    3️⃣ Searching efficiency -
                                        Binary search requires sorted data
                                        Faster lookups

                    4️⃣ Presentation & reporting -
                                        Make data readable
                                        Ordered results
                    '''

# 1D Sorted
import numpy as np
arr1 = np.array([2,3,4,1,2,4,6,0,1,7,9])
print("Sorted:",np.sort(arr1))


# 2D Sorted
import numpy as np
arr2 = np.array([[2,3,1],   #0th row
                [3,1,2],   #1st row
                [1,2,3]])   #2nd row
print("2D Sorted:",np.sort(arr2, axis = 1))

'''
| Axis       | Direction     | Meaning         |
| ---------- | ------------- | --------------- |
| `axis = 0` | ⬇️ Vertical   | **Column-wise** |
| `axis = 1` | ➡️ Horizontal | **Row-wise**    |

'''