# regression lagrange (hoi suy lagrange)

import matplotlib.pyplot as plt
import numpy as np

# training set
# D = {(4,3),(7,4),(9,6)}

'''
# x values
x = [4.0, 7.0, 9.0]
# y values
y = [3.0, 4.0, 6.0]
'''

# x values
x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
# y values
y = [2.0, 4.0, 5.0, 7.0, 6.0, 8.0, 9.0, 11.0, 12.0, 12.0]


#lagrange interpolation (noi suy lagrange)
def lagrange (v):
    h=0.0
    for i in range(len(x)):
        t = y[i]
        for j in range(len(y)):
            if i != j:
                t *= (v-x[j])/(x[i]-x[j])
        h += t
    return h

#test lagrange interpolation
for i in range(len(x)):
    print('lagrange(' + str(x[i]) + ') = ' + str(lagrange(x[i])))
print('===================')

def obj_function():
    of = 0.0
    for i in range(len(x)):
        of += (lagrange(x[i])-y[i])*(lagrange(x[i])-y[i])
    return of
print('tong binh phuong loi obj_function = ' + str(obj_function()))

# plotting points as a scatter plot
plt.scatter(x, y, label = "điểm dữ liệu", color = "green", marker = "*", s = 15)

# fx values
fx = np.arange(0.8, 10.2, 0.1)
#fy values
fy = fx*0
#fullfill fy
for i in range(len(fx)):
    fy[i] = lagrange(fx[i])

# plotting the points
plt.plot(fx, fy, label = "nội suy lagrange", color = "blue")

# x-axis label
plt.xlabel('trục - x')
#frequency label
plt.ylabel('trục - y')
#plt.title
plt.title('Hàm nội suy lagrange')
#showing legend
plt.legend()

#funtion to show the plot
plt.show()
