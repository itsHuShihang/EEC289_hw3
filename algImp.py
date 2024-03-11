import numpy as np
import matplotlib.pyplot as plt
import pdb
import time


def initpara():
    alpha = 0.99
    # t = (1,1.5e12)
    t = (1,1000)
    markovlen = 1000
 
    return alpha,t,markovlen
num = 1000
dist_array = np.loadtxt("eu_my_array_file.txt",dtype=float,delimiter=',')
 
 
new_solution = np.arange(num)
#valuenew = np.max(num)
 
current_solution = new_solution.copy()
current_value =99999  #np.max这样的源代码可能同样是因为版本问题被当做函数不能正确使用，应取一个较大值作为初始值
#print(valuecurrent)
 
best_solution = new_solution.copy()
best_value = 99999
 
alpha,target_time,markovlen = initpara()
run_time = target_time[1]

start = time.time()
end = time.time()
result = [] #记录迭代过程中的最优解
# while run_time > target_time[0]:
#     if end >= (start+14*60):
#         break
while (end-start)<14.5*60:
    for i in np.arange(markovlen):
 
        #下面的两交换和三角换是两种扰动方式，用于产生新解
        if np.random.rand() > 0.5:# 交换路径中的这2个节点的顺序
            # np.random.rand()产生[0, 1)区间的均匀随机数
            while True:#产生两个不同的随机数
                loc1 = np.int64(np.ceil(np.random.rand()*(num-1)))
                loc2 = np.int64(np.ceil(np.random.rand()*(num-1)))
                ## print(loc1,loc2)
                if loc1 != loc2:
                    break
            new_solution[loc1],new_solution[loc2] = new_solution[loc2],new_solution[loc1]
        else: #三交换
            while True:
                loc1 = np.int64(np.ceil(np.random.rand()*(num-1)))
                loc2 = np.int64(np.ceil(np.random.rand()*(num-1))) 
                loc3 = np.int64(np.ceil(np.random.rand()*(num-1)))
 
                if((loc1 != loc2)&(loc2 != loc3)&(loc1 != loc3)):
                    break
 
            # 下面的三个判断语句使得loc1<loc2<loc3
            if loc1 > loc2:
                loc1,loc2 = loc2,loc1
            if loc2 > loc3:
                loc2,loc3 = loc3,loc2
            if loc1 > loc2:
                loc1,loc2 = loc2,loc1
 
            #下面的三行代码将[loc1,loc2)区间的数据插入到loc3之后
            tmplist = new_solution[loc1:loc2].copy()
            new_solution[loc1:loc3-loc2+1+loc1] = new_solution[loc2:loc3+1].copy()
            new_solution[loc3-loc2+1+loc1:loc3+1] = tmplist.copy()  
        new_value = 0
        for i in range(num-1):
            new_value += dist_array[new_solution[i]][new_solution[i+1]]
        new_value += dist_array[new_solution[0]][new_solution[51]]
       # print (valuenew)
        if new_value<current_value: #接受该解
           
            #更新solutioncurrent 和solutionbest
            current_value = new_value
            current_solution = new_solution.copy()
 
            if new_value < best_value:
                best_value = new_value
                best_solution = new_solution.copy()
        else:#按一定的概率接受该解
            if np.random.rand() < np.exp(-(new_value-current_value)/run_time):
                current_value = new_value
                current_solution = new_solution.copy()
            else:
                new_solution = current_solution.copy()
    run_time = alpha*run_time
    result.append(best_value)
    end = time.time()
    print (run_time) #程序运行时间较长，打印t来监视程序进展速度

best_solution_store = best_solution.reshape(1,1000)
np.savetxt("solution.txt",best_solution_store,fmt='%i')
#用来显示结果
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