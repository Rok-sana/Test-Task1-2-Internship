import time

def sum_to_n(N):
    start_time = time.time()
    result = 0
    if N <= 10**25:
        result = (N * (N+1)) // 2
    end_time = time.time()
    print("Execution time:", end_time - start_time, "seconds")
    return result

N = int(input("Enter a positive integer N: "))
print("Sum from 1 to N:", sum_to_n(N))