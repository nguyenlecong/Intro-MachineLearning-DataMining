import matplotlib.pyplot as plt 
from matplotlib import cm # for colormap
from matplotlib.ticker import LinearLocator, FormatStrFormatter #for design Z axis
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
epochs = 10

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



			
# plot 3D surface 
fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X_1 = np.arange(0.4, 4.6, 0.05)# must be equal size
X_2 = np.arange(0.4, 4.6, 0.05)
X,Y = np.meshgrid(X_1, X_2)
Z = np.zeros([len(X_1),len(X_2)])
for i in range(len(X_1)):
 for j in range(len(X_2)):
  Z[i,j] = sign_dec(X_1[i]*w_1_star+X_2[j]*w_2_star + b_star) 
print(np.shape(Z))

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.Spectral, linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.1, 1.1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)			

#Plot scatter point
# get left half and right half
mid = len(x_1)//2 # floor division
x_1_first = x_1[:mid]
x_2_first = x_2[:mid]
x_1_second = x_1[mid:]
x_2_second = x_2[mid:] 

X_first = np.array(x_1_first)
Y_first = np.array(x_2_first)
Z_first = np.zeros(len(x_1_first))

ax.scatter(X_first,Y_first,Z_first, color= "r",  
            marker= "*", s=30)

X_second = np.array(x_1_second)
Y_second = np.array(x_2_second)
Z_second = np.zeros(len(x_1_second))

ax.scatter(X_second,Y_second,Z_second, color= "b",  
            marker= "*", s=30)

# Add label on x,y axis
ax.set_xlabel('trục $x_1$')
ax.set_ylabel('trục $x_2$')

# plot title 
plt.title('Giải thuật Perceptron với hàm quyết định tuyến tính 3D!')
  
# function to show the plot 
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
plt.title('Giải thuật Perceptron với hàm quyết định tuyến tính!') 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show()
'''