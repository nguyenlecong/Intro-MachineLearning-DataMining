from ete3 import Tree
import numpy as np
import ast

# max distance
max_dis = 1e+4
#epochs
epochs = 4
#number col, row
n_col = 4
n_row = 8
#initializing matrix
data = np.zeros((n_row, n_col))
#loading data from csv file
f = open('baseball.csv','rt');
f.readline()
for i in range(n_row):
    line = f.readline()
    line = '['+line+']'
    dt = ast.literal_eval(line)
    for j in range(n_col):
        data[i,j] = dt[j]
f.close()
#print(data)
clustering = np.zeros(n_row,dtype='int')
for i in range(n_row):
    clustering[i] = i
print(clustering)

# must save newick
newick = np.empty(n_row, dtype='<U50')
for i in range(n_row):
    newick[i] = str(i)

def agg_clus():
    for c in range(n_row -1):
        min_dist = max_dis
        min_i = 0
        min_j = 1
        for i in range(n_row):
            for j in range(i+1,n_row):
                if clustering[i] != clustering[j]:
                    dist = np.linalg.norm(data[clustering[i],:]-data[clustering[j],:])
                    #print('dist['+str(clustering[i])+','+str(clustering[j])+']='+str(dist))
                    if min_dist>dist:
                        min_dist = dist
                        min_i = clustering[i] # don't use tabs
                        min_j = clustering[j] # instead use space
        print(min_i,min_j)
        # to construct a newick format
        newick[min_i] = "("+newick[min_i]+","+newick[min_j]+")"
        # Re-assignn clustering and centroid
        mean = np.zeros(n_col)
        card = int(0)
        for i in range(n_row):
            if clustering[i] == min_i or clustering[i] == min_j:
                mean = np.add(mean, data[clustering[i]])
                card = card + 1
                clustering[i] = min_i
                mean = np.multiply(mean, 10./float(card))
        for i in range(n_row):
            if clustering[i] == min_i:
                data[clustering[i]] = np.multiply(data[clustering[i]], 0.0)
                data[clustering[i]] = np.add(data[clustering[i]],mean)
        print(clustering)

agg_clus()
#newick string
nw = newick[0]+";"
#print(nw)
#plot using pyqt5 and ete3
t = Tree(nw)
#print(t) # console version
t.show() #GUI version




























