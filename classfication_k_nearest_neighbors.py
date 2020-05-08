import numpy as np

# k nearest neighbor
k_nn = 3
# number col, row, predict colum
p_col = 4
n_col = 5
n_row = 14
# initializing matrix
data = np.empty([n_row, n_col], dtype = '<U10') # unicode maximum 10 characters
#loading data from csv file
f = open('tennis.csv', 'rt');
attr = f.readline() # outlook, temp, humidity, windy, play
attr = attr.rstrip() # remove \n
attr = attr.split(',') # become a list
for i in range(n_row):
    line = f.readline()
    line = line.rstrip()
    line = line.split(',')
    data[i,:] = np.array(line)
    # print(line)
f.close()
def k_nearest_neigbor(x_t, k):
    # taking hamming distances
    d_hamming = [0.0]*n_row
    for i in range (n_row):
        d_h = 0.0
        for j in range (n_col - 1):
            if x_t[j] != data[i,j]:
                d_h += 1
        d_hamming[i] = d_h
    print('Hamming distance between ' + str(x_t) + ' and trai. samp. are ' + str(d_hamming))
    indices = list(range(n_row))
    # selecting k nearest neigbors (selection sort)
    for i in range(k):
        i_min = i
        for j in range(i+1, len(d_hamming)):
            if d_hamming[i_min] > d_hamming[j]:
                i_min = j
        d_hamming[i_min], d_hamming[i] = d_hamming[i], d_hamming[i_min] # swap
        indices[i_min], indices[i] = indices[i], indices[i_min]
    # print(indices) # k smallest hamming distances # k first values
    k_nn = indices[:k]
    print('k nearest neigbor are ' + str(k_nn))
    voting = [0,0] # 0: yes, 1: no
    for i in range(len(k_nn)):
        if data[k_nn[i], p_col] == 'yes':
            voting[0] += 1
        else:
            voting[1] += 1
    print(' of voting decison yes = ' + str(voting[0]) + ', no = ' + str(voting[1]))
    if voting[0] > voting[1]:
        return 'yes'
    else:
        return 'no'
x_t = ['sunny', 'mild', 'normal', 'true']
dec = k_nearest_neigbor(x_t, k_nn)
print('k nearest neigbor answer is ' + str(dec) + ' for playing tennis')
















    
