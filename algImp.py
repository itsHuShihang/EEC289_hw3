import numpy as np
import matplotlib.pyplot as plt
import pdb
import time


def initpara():
    alpha = 0.99
    t = (1,1000)
    markovlen = 1000
 
    return alpha,t,markovlen

num = 1000
dist_array = np.loadtxt("eu_my_array_file.txt",dtype=float,delimiter=',')
 
 
new_solution = np.arange(num)
 
current_solution = new_solution.copy()
current_value =99999
 
best_solution = new_solution.copy()
best_value = 99999
 
alpha,target_time,markovlen = initpara()
run_time = target_time[1]

start = time.time()
end = time.time()
result = [] # store the best results during the iteration
# while run_time > target_time[0]:
#     if end >= (start+14*60):
#         break
while (end-start)<14.5*60:
    for i in np.arange(markovlen):
 
        # two kinds of exchange methods
        if np.random.rand() > 0.5:# exchange the sequence of two nodes
            # np.random.rand() can generate the random number between 0 to 1
            while True:# generate two random numbers
                loc1 = np.int64(np.ceil(np.random.rand()*(num-1)))
                loc2 = np.int64(np.ceil(np.random.rand()*(num-1)))
                if loc1 != loc2:
                    break
            new_solution[loc1],new_solution[loc2] = new_solution[loc2],new_solution[loc1]
        else: # exchange of three nodes
            while True:
                loc1 = np.int64(np.ceil(np.random.rand()*(num-1)))
                loc2 = np.int64(np.ceil(np.random.rand()*(num-1))) 
                loc3 = np.int64(np.ceil(np.random.rand()*(num-1)))
 
                if((loc1 != loc2)&(loc2 != loc3)&(loc1 != loc3)):
                    break
 
            # let loc1<loc2<loc3
            if loc1 > loc2:
                loc1,loc2 = loc2,loc1
            if loc2 > loc3:
                loc2,loc3 = loc3,loc2
            if loc1 > loc2:
                loc1,loc2 = loc2,loc1
 
            # inject the data of [loc1,loc2) behind the loc3
            tmplist = new_solution[loc1:loc2].copy()
            new_solution[loc1:loc3-loc2+1+loc1] = new_solution[loc2:loc3+1].copy()
            new_solution[loc3-loc2+1+loc1:loc3+1] = tmplist.copy()  
        new_value = 0
        for i in range(num-1):
            new_value += dist_array[new_solution[i]][new_solution[i+1]]
        new_value += dist_array[new_solution[0]][new_solution[51]]

        if new_value<current_value: # accept this value
           
            # update solutioncurrent and solutionbest
            current_value = new_value
            current_solution = new_solution.copy()
 
            if new_value < best_value:
                best_value = new_value
                best_solution = new_solution.copy()
        else:# accept this value with probbility
            if np.random.rand() < np.exp(-(new_value-current_value)/run_time):
                current_value = new_value
                current_solution = new_solution.copy()
            else:
                new_solution = current_solution.copy()
    run_time = alpha*run_time
    result.append(best_value)
    end = time.time()
    print (run_time) # show the progress of the program

best_solution_store = best_solution.reshape(1,1000)
np.savetxt("solution.txt",best_solution_store,fmt='%i')

# show the results
print("best_solution:",best_solution)
print("shape:",np.shape(best_solution))
print("best_result:",result[-1])
print("exe time:",(end-start),"second")
print("exe time:",(end-start)/60,"minute")
print("cycle:",len(result))
plt.plot(np.array(result))
plt.ylabel("bestvalue")
plt.xlabel("t")
plt.show()