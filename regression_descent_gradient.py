import matplotlib.pyplot as plt
import numpy as np

# training set
# D = {(4,3), (7,4), (9,6)}
# x values
x = [4.0, 7.0, 9.0]
# y values
y = [3.0, 4.0, 6.0]

'''
A linear regression model
f(x;w) = xw + b
L(D;w) = sum(f(x;w) - y)**2
Desent gradient algorithm (Batch mode)
t <- 0
do
w(t+1) <- w(t) - learning_rate*L'(w(t))
while(obj_fuction > epsilon)
'''
epsilon = 0.423
learning_rate = 1e-4
epochs = 1000

# first order derivative
def first_order_weight(w,b):
    fow = 0.0
    for i in range(len(x)):
        fow += 2*(w*x[i]+b-y[i])*x[i]
#    fow /= len(x)
    return fow

# first order derivative
def first_order_bias(w,b):
    fob = 0.0
    for i in range(len(x)):
        fob += 2*(w*x[i]+b-y[i])
#    fob /= len(x)
    return fob

def obj_function(w,b):
    of = 0.0
    for i in range(len(x)):
        of += (w*x[i]+b-y[i])**2
    return of

# descent gradient algorithm
def descent_gradient():
    w = 0.0 # initial values
    b = 0.0
    for i in range(epochs):
        print(obj_function(w,b))
        w = w - learning_rate*first_order_weight(w,b)
        b = b - learning_rate*first_order_bias(w,b)
    return w,b

w_star, b_star = descent_gradient()
# w_star = 0.0
# b_star = 0.0
print('w*='+str(w_star))
print('b*='+str(b_star))

# plotting points as a scatter plot 
plt.scatter(x, y, label= "điểm dữ liệu", color= "green",  
            marker= "*", s=15) 
# fx values
fx = np.arange(0.8, 10.2, 0.1)
# fy values
fy = fx*0
# fullfill fy
for i in range(len(fx)):
 fy[i] = w_star*fx[i] + b_star # f(x;w)=w*x + b

# potting the points 
plt.plot(fx, fy, label= "hồi quy tuyến tính", color= "blue")

# x-axis label 
plt.xlabel('x - trục') 
# frequency label 
plt.ylabel('y - trục') 
# plot title 
plt.title('Regressoion Descent Gradient') 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show() 
































