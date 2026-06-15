# plt.hist(data, color= 'color name', bins= 'numbers of bins', edgecolor = "color name")
import matplotlib.pyplot as plt



'''histogram shows the distribution of numerical data, not categories.
    Like - 
            How many students scored between 0-20?
            How many scored between 20-40?
            Which score range has the most students?'''
scores = [12,43,76,23,65,75,12,53,97,12,65,78,24,80,56,23,76,21]

plt.hist(scores, bins = 5, color = 'red', edgecolor = 'black')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.title("Score Distribution of Students")
plt.show()              #See x-axis then you find what is difference between histogram and bar graph