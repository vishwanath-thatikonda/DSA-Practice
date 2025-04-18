import time
# def sum_of_n(n):
#     start = time.time()
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     end = time.time()
#     return sum, f"time needed to run sum_of_n : {end - start}"
    
# print(sum_of_n(5000000))

def sum_n(n):
    start = time.time()
    x =  (n * (n+1) ) / 2
    end = time.time()
    return x , f"time needed to run sum_of_n : {end - start}"

for i in range(5):
    print(sum_n(100000000))

    

