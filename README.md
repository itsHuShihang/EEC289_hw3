# UC Davis EEC289_hw3

I use the **Simulated Annealing (SA)** algorithm to solve the **Traveling Salesman Problem (TSP)**. The algorithm is implemented by Python. I found that my loading function to load the data from the two given .txt files is slow but the saving and loading function by Numpy is quick. So I use a pre-loading function to save the execution time. 

## How to use
- Run `preLoad.py` to preload the distance data from `1000_euclidianDistance.txt` and `1000_randomDistance.txt`. The preloaded data is stored in the `eu_my_array_file.txt` and `rd_my_array_file.txt` in the form of Numpy Array.
- Run `algImp.py` and wait, the progress is printed in the terminal. If the number shown in the terminal is smaller than 1 or the execution time is over 15 minutes, the program will stop.
- The runtime results are printed in the terminal directly. The optimized sequence of nodes is stored in the `solution.txt`. The trend of the solution is shown by a plot.
