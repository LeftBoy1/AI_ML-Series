# plt.scatter(x, y, color= 'color name', marker = 'marker style', label = 'label name')


#Case 1 
import matplotlib.pyplot as plt

hrs = [1,2,3,4,5,6,7,8]
scores = [55,59,60,66,75,78,98,112]
plt.plot(hrs, scores, color= 'orange',linestyle = '--', linewidth = 2, marker = 'o', label = 'Student Data')
plt.title('Scores According to Hours Studing')
plt.xlabel('Hours Study')
plt.ylabel('Exam Scores')
plt.grid(True)
plt.legend()
plt.show()

