import matplotlib.pyplot as plt 
import numpy as np


# linear sperable training set   
# [x1,x2] values 
x_1 = [0.5,1.5,1.0,0.75,0.6,0.77,1.5,1.3,4.0,3.3,4.5,4.5,3.9,5.0,3.5,4.0]  
x_2 = [1.5,2.5,2.5,2.0,1.9,2.5,3.0,3.3,1.0,0.3,1.2,0.5,0.7,1.0,0.2,0.3]  
# y values 
y=[-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0] 





'''
A linear classification model
f(x;w) = sign(x_1*w_1+x_2*w_2+b)
L(D;w)=max(0,1-y*f(x;w))
Perceptron algorithm (instance mode)
t<-0
do
w(t+1) <- w(t) - learning_rate*L'(w(t))
while(t > epochs)
'''			
epsilon = 0.423
learning_rate = 1
epochs = 100

def sign_dec(d):
 if d >= 0.0:
  return 1.0
 else:
  return -1.0

def max(a,b):
 if a>=b:
  return a
 else:
  return b

def obj_function(w_1,w_2,b):
 of = 0.0
 for i in range(len(x_1)):
  of += max(0.0,1.0-sign_dec(w_1*x_1[i]+w_2*x_2[i] + b)*y[i])/2.0
 return of
 
# perceptron algorithm 
def perceptron():
 w_1 = 0# initial values
 w_2 = 0
 b = 0.0
 print('obj_function='+str(obj_function(w_1,w_2,b)))
 for e in range(epochs):
  for i in range(len(x_1)):   
   if sign_dec(w_1*x_1[i]+w_2*x_2[i] + b)!= y[i]:
    w_1 = w_1 + learning_rate*y[i]*x_1[i]
    w_2 = w_2 + learning_rate*y[i]*x_2[i]
    b = b + learning_rate*y[i]
  #print(w_1,w_2,b)
 return w_1,w_2,b

w_1_star, w_2_star, b_star = perceptron()

#w_1_star=w_2_star=b_star = 0.0

print('w_1*='+str(w_1_star))
print('w_2*='+str(w_2_star))
print('b*='+str(b_star))
print('obj_function='+str(obj_function(w_1_star,w_2_star,b_star)))


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
            marker= "*", s=15) 
plt.scatter(x_1_second, x_2_second, label= "điểm dữ liệu dương", color= "g",  
            marker= "*", s=15)

# numpy array 
X = []
for i in range(len(x_1)):
 X.append((x_1[i],x_2[i]))

X = np.array(X)
y = np.array(y)

# get axis
ax = plt.gca()
min = np.minimum(X[:,0].min(),X[:,1].min())
max = np.maximum(X[:,0].max(),X[:,1].max())
# create grid to evaluate model
xx = np.linspace(min-0.1,max+0.1, 50)
yy = np.linspace(min-0.1,max+0.1, 50)
YY, XX = np.meshgrid(yy, xx)

Z = np.zeros([len(xx),len(yy)])
for i in range(len(xx)):
 for j in range(len(yy)):
  Z[i,j] = xx[i]*w_1_star+yy[j]*w_2_star + b_star 
print(np.shape(Z))

im = ax.imshow(Z, interpolation='nearest',
           extent=(XX.min(), XX.max(), YY.min(), YY.max()), aspect='auto',
           origin='lower', cmap=plt.cm.terrain)

# plot decision boundary and margins
ax.contour(XX, YY, Z, colors='k', levels=[0], alpha=0.5,
           linestyles=['-'])

# Add a color bar which maps values to colors.
fig.colorbar(im, shrink=0.5, aspect=5)
# x-axis label 
plt.xlabel('x1 - trục') 
# frequency label 
plt.ylabel('x2 - trục') 
# plot title 		   
plt.title('Giải thuật Perceptron với hàm quyết định tuyến tính!')
# legend
plt.legend()
plt.show()

'''
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
plt.title('Giải thuật Perceptron với hàm quyết định tuyến tính!') 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show()
'''