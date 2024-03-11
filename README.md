# UCDavis EEC289_hw3

I use Simulated Annealing (SA) algorithm to solve the Traveling Salesman Problem (TSP). The algorithm is implemented by Python. I found the my loading function to load the data from the two given .txt file is slow but the saving and loading function by Numpy is quick. So I use a pre-loading function to save the excution time. 

## How to use
- Run `preLoad.py` to preload the distance data from `1000_euclidianDistance.txt` and `1000_randomDistance.txt`. The preloaded data is stored in the `eu_my_array_file.txt` and `rd_my_array_file.txt` as the form of numpy matrix.
- Run `algImp.py` and wait, the progress is printed in the terminal. If the number shown in the terminal is smaller to 1 or the excution time is over 15 minute, the program will stop.
- The runtime results are printed in the rerminal directly. The optimized sequence of node is stored in the `solution.txt`. And the trend of the solution is shown by a plot.
