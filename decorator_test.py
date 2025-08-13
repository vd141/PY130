from time import perf_counter
from functools import lru_cache

def time_runs(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        return_value = func(*args, **kwargs)
        print(f"The function ran in {perf_counter()-start} seconds")
        return return_value

    return wrapper

@lru_cache
@time_runs
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True

print('first call')
# The first function call
is_prime(73729261)
# The function ran in 2.1655370840016985 seconds

print('second call')
# The second function call
is_prime(73729261)
# The function ran in 8.330098353326321e-07 seconds