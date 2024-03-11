import numpy as np
import matplotlib.pyplot as plt
import pdb
import time

FILE_RD = "1000_randomDistance.txt"
FILE_EU = "1000_euclidianDistance.txt"
np.set_printoptions(threshold=np.inf)
node_array_rd=np.zeros((1,3))
node_array_eu=np.zeros((1,3))

def getdistmat(node_array):
    num = 1000
    dist_array = np.zeros((num,num)) #52X52距离矩阵
    for row in node_array:
        i = int(row[0]-1)
        j = int(row[1]-1)
        dist = row[2]
        dist_array[i][j]=dist_array[j][i]=dist
    return dist_array

#######################################################################
# random distance #
#######################################################################
start = time.time()

with open(FILE_RD) as f:
    cnt=0
    for line in f:
        if cnt>=2:
            print("progress:",cnt/499501)
            temp_list = []
            temp_list.extend([float(i) for i in line.split()])
            # print(temp_list)
            tt=np.zeros((1,3))
            tt[0]=np.array(temp_list)
            node_array_rd=np.append(node_array_rd,tt,axis=0)
        cnt+=1

node_array_rd=np.delete(node_array_rd,0,axis=0)
print("node_array_shape:",np.shape(node_array_rd))

dist_array_rd = getdistmat(node_array_rd) #得到距离矩阵
# print("distmat:",dist_array_rd) 
print("dismat_shape:",np.shape(dist_array_rd))

np.savetxt("rd_my_array_file.txt",dist_array_rd,fmt='%.2f',delimiter=',')

end = time.time() 
print("time:",end-start)
print("time:",(end-start)/60,"minute")
print("1000_randomDistance.txt read done")


#######################################################################
# euclidian distance #
#######################################################################
start = time.time()

with open(FILE_EU) as f:
    cnt=0
    for line in f:
        if cnt>=2:
            print("progress:",cnt/499501)
            temp_list = []
            temp_list.extend([float(i) for i in line.split()])
            # print(temp_list)
            tt=np.zeros((1,3))
            tt[0]=np.array(temp_list)
            node_array_eu=np.append(node_array_eu,tt,axis=0)
        cnt+=1

node_array_eu=np.delete(node_array_eu,0,axis=0)
print("node_array_shape:",np.shape(node_array_eu))

dist_array_eu = getdistmat(node_array_eu) #得到距离矩阵
# print("distmat:",dist_array) 
print("dismat_shape:",np.shape(dist_array_eu))

np.savetxt("eu_my_array_file.txt",dist_array_eu,fmt='%.2f',delimiter=',')

end = time.time() 
print("time:",end-start)
print("time:",(end-start)/60,"minute")
print("1000_euclidianDistance.txt read done")