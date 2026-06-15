# plt.scatter(x, y, color= 'color name', marker = 'marker style', label = 'label name')


#Case 1 
import matplotlib.pyplot as plt

hrs = [1,2,3,4,5,6,7,8]
scores = [55,59,60,66,75,78,98,112]
plt.scatter(hrs, scores, color= 'orange', marker = 'o', label = 'Student Data')
plt.title('Scores According to Hours Studing')
plt.xlabel('Hours Study')
plt.ylabel('Exam Scores')
plt.grid(True)
plt.legend()
plt.show()








#Case 2 (Grouping)
import matplotlib.pyplot as plt

plt.scatter([1,2,3], [55,60,78], color= 'blue', marker = 'o', label = 'Class A')
plt.scatter([1,2,3], [32,89,98], color= 'green', marker = 'o', label = 'Class B')

plt.title('Comparison between Class A and Class B')
plt.xlabel('Hours Study')
plt.ylabel('Exam Scores')
plt.grid(True)
plt.legend()
plt.show()