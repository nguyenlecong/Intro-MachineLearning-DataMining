import matplotlib.pyplot as plt
import ast
import numpy as np

# epochs
epochs = 4

# number col, row
n_col = 5
n_row = 12

# initial centroids
c1 = 1 # khởi tạo ngẫu nhiên giá trị trung tâm
c2 = 8
colors = ['w', 'r', 'g']
# two choosen colums
attr = ['tham gia/phút', 'chiều cao', 'thời gian chơi', 'tuổi', 'điểm/phút']
col1 = 0 # thuộc tính 1 
col2 = 1 # thuộc tính 2

# initializing matrix
data = np.zeros((n_row, n_col))

#loading data from csv file
f = open('baseball.csv', 'rt');
f.readline()
for i in range(n_row):
    line = f.readline()
    line = '[' + line + ']'
    dt = ast.literal_eval(line)
    for j in range(n_col):
        data[i,j] = dt[j]
f.close()
#print(data)

def k_means():
    c_1 = data[c1,:]
    c_2 = data[c2,:]
    ass_cens = np.zeros(n_row, dtype='int8')
    for e in range(epochs):
        print(ass_cens)
        ass_cens = np.multiply(ass_cens,0)
        for i in range(n_row):
            v = data[i,:]
            dist_1 = np.linalg.norm(v - c_1) # khoảng cách euclid
            dist_2 = np.linalg.norm(v - c_2)
            #print('dist_1 = '+str(dist_1))
            #print('dist_2 = '+str(dist_2))
            if dist_1 <= dist_2:
                ass_cens[i] = 1
            else:
                ass_cens[i] = 2
        num_c1 = 0.0 # đếm số phần tử cụm 1
        num_c2 = 0.0 # đếm số phần tử cụm 2
        c_1 = np.multiply(c_1,0.0)
        c_2 = np.multiply(c_2,0.0)
        #print(c_1)
        #print(c_2)
        for i in range(n_row):
            if ass_cens[i] == 1:
                num_c1 = num_c1 + 1
                c_1 = np.add(c_1, data[i,:])
            else:
                num_c2 = num_c2 + 1
                c_2 = np.add(c_2, data[i,:])
            #print('c_1: ' + str(c_1))
            #print('c_2: ' + str(c_2))
        c_1 = np.multiply(c_1,1.0/float(num_c1))
        c_2 = np.multiply(c_2,1.0/float(num_c2))
        #print('c_1: ' + str(c_1))
        #print('c_2: ' + str(c_2))
    return ass_cens, c_1, c_2
    
a_s, cd_1, cd_2 = k_means()

# plotting 2D on attributes
for i in range(n_row):
    plt.scatter(data[i,col1], data[i, col2], color=colors[a_s[i]], marker="*", s=15)

# annotating initial centroids
plt.annotate('$c_1$', (data[c1,col1], data[c1,col2]))
plt.annotate('$c_2$', (data[c2, col1], data[c2, col2]))

# annotating centroids
plt.scatter(cd_1[col1], cd_1[col2], color=colors[1], marker="o", s=25)
plt.annotate('$m_1$', (cd_1[col1],cd_1[col2]))
plt.scatter(cd_2[col1], cd_2[col2], color=colors[2], marker="o", s=25)
plt.annotate('$m_2$', (cd_2[col1],cd_2[col2]))

# x-axis label 
plt.xlabel(attr[col1]) 
# frequency label 
plt.ylabel(attr[col2]) 
# plot title 
plt.title('Biểu diễn cụm diểm dữ liệu trên 2 chiều thuộc tính')

#function to show the plot
plt.show() 






























































                
                             
                        













                
            

