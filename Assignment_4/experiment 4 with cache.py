import time
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Measuring execution time
start_time = time.perf_counter()
result = fib(15)
end_time = time.perf_counter()

print(f"fib(15) = {result}")
print(f"Execution Time: {(end_time - start_time) * 1000:.6f} ms")
