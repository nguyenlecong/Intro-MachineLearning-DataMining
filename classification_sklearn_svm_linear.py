from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

# linear sperable training set   
# [x1,x2] values 
x_1 = [0.5,1.5,1.0,0.75,0.6,0.77,1.5,1.3,4.0,3.3,4.5,4.5,3.9,5.0,3.5,4.0]  
x_2 = [1.5,2.5,2.5,2.0,1.9,2.5,3.0,3.3,1.0,0.3,1.2,0.5,0.7,1.0,0.2,0.3]

# y values 
y=[-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1] 




'''
A support vector machine classifiction SVC
f(x;w) = sign(sum alpha_i K(x_i,w)+b)
L(D;w)=max(0,1-y*f(x;w)) hinge loss
sklearn.fit() learning algorithm 
'''			
# numpy array 
X = []
for i in range(len(x_1)):
 X.append((x_1[i],x_2[i]))

X = np.array(X)
y = np.array(y)

clf = svm.SVC(kernel='linear',C=1000)
clf.fit(X, y)

print(clf.support_vectors_)

# plot color bar
fig = plt.figure()

# get left half and right half
mid = len(x_1)//2 # floor division
x_1_first = x_1[:mid]
x_2_first = x_2[:mid]
x_1_second = x_1[mid:]
x_2_second = x_2[mid:]  
# plotting points as a scatter plot 
plt.scatter(x_1_first, x_2_first, label= "điểm dữ liệu âm", color= "r",  
            marker= "*", s=30) 
plt.scatter(x_1_second, x_2_second, label= "điểm dữ liệu dương", color= "g",  
            marker= "*", s=30)

# plot the decision function
ax = plt.gca()
min = np.minimum(X[:,0].min(),X[:,1].min())
max = np.maximum(X[:,0].max(),X[:,1].max())
# create grid to evaluate model
xx = np.linspace(min-0.1,max+0.1, 50)
yy = np.linspace(min-0.1,max+0.1, 50)
XX, YY = np.meshgrid(xx, yy)
xy = np.c_[XX.ravel(), YY.ravel()]

Z = clf.decision_function(xy).reshape(XX.shape)

im = ax.imshow(Z, interpolation='nearest',
           extent=(XX.min(), XX.max(), YY.min(), YY.max()), aspect='auto',
           origin='lower', cmap=plt.cm.Spectral)

# plot decision boundary and margins
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])
# plot support vectors
ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')

# Add a color bar which maps values to colors.
fig.colorbar(im, shrink=0.5, aspect=5)
# x-axis label 
plt.xlabel('x1 - trục') 
# frequency label 
plt.ylabel('x2 - trục') 
# plot title 		   
plt.title('Giải thuật máy học vec tơ với nhân tuyến tính')
# legend
plt.legend()
plt.show()



'''
# get left half and right half
mid = len(x_1)//2 # floor division
x_1_first = x_1[:mid]
x_2_first = x_2[:mid]
x_1_second = x_1[mid:]
x_2_second = x_2[mid:]  
# plotting points as a scatter plot 
plt.scatter(x_1_first, x_2_first, label= "điểm dữ liệu âm", color= "r",  
            marker= "*", s=15) 
plt.scatter(x_1_second, x_2_second, label= "điểm dữ liệu dương", color= "g",  
            marker= "*", s=15)


# fx values
fx_1 = np.arange(0, 5, 0.1)
# fy values
fx_2 = fx_1*0
# fullfill fy
for i in range(len(fx_1)):
 fx_2[i] = (-w_1_star*fx_1[i]-b_star)/w_2_star # w_1*x_1 + w_2*x_2 + b = 0

# potting the points 
plt.plot(fx_1, fx_2, label= "đường quyết định tuyến tính ", color= "blue")

# x-axis label 
plt.xlabel('x1 - trục') 
# frequency label 
plt.ylabel('x2 - trục') 
# plot title 
plt.title('Giải thuật máy học vec tơ với hàm quyết định tuyến tính!') 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show()
'''