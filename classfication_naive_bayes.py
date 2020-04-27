import ast
import numpy as np

# max distance
max_dis = 1e+4
# epochs
epochs = 4
# number col, row, predict colum
p_col = 4
n_col = 5
n_row = 14
# initializing matrix
data = np.empty([n_row, n_col], dtype = '<U10') # unicode maximum 10 characters
# loading data from csv five
f = open('tennis.csv','rt');
attr = f.readline() # outlook, temp, humudity, windy, play
attr = attr.rstrip()
attr = attr.split(',') #become a list
for i in range(n_row):
    line = f.readline()
    line = line.rstrip() #remove \n
    line = line.split(',')
    data[1,:] = np.array(line)
    print(data)
f.close()
'''
#printing data
for i in range(n_row):
    for j in range(len(attr)):
        print(data[i,j], end = ',')
    print(end = '\n')
'''
def tennis_naive_bayes(x_t, y_t): #a test sample, dictionary
    Bayes_Rule = 1.0
    Prob_Y = 0.0
    for i in range(n_row):
        if y_t[0] == data[i,p_col]:
            Prob_Y += 1.0
    # print('P(Y='+y_t[0]+')='+str(Prob_Y))
    for j in range(n_col-1):
        Prob_X_Y = 0.0
        for i in range(n_row):
            if x_t[j] == data[i,j] and y_t[0] == data[i, p_col]:
                Prob_X_Y += 1.0
        # print('P(X='+x_t[j]+'|Y='+y_t[0]+')='+str(Prob_X_Y)+'')
        Prob_X_Y /= Prob_Y
        Bayes_Rule *= Prob_X_Y
    Prob_Y /= float(n_row)
    Bayes_Rule *= Prob_Y
    return Bayes_Rule
# x_t = ['sunny', 'mild', 'normal', 'true']
x_t = ['rainy','cool','high','true']
# yes
y_t = ['yes']
br_yes = tennis_naive_bayes(x_t,y_t)
print('p(Y='+y_t[0]+'X='+x_t[1]+','+x_t[2]+','+x_t[3]+'):'+str(br_yes))
'''
# no
y_t = ['no']
br_no = tennis_naive_bayes(x_t,y_t)
print('p(Y='+y_t[0]+'X='+x_t[1]+','+x_t[2]+','+x_t[3]+'):'+str(br_no))
'''

