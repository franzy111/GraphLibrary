import time


def test(count, func, *args, **kwargs):
    ans = func(*args, **kwargs)
    ans = func(*args, **kwargs)
    sum = 0
    for i in range(count):
        t = time.perf_counter()
        ans = func(*args, **kwargs)
        sum += time.perf_counter() - t
    return sum / count
