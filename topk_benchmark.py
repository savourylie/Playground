import heapq
import time

import bottleneck as bn
import numpy as np


def top_k_numpy(ndarr, k=10):

    return np.sort(ndarr)[-k:]


def top_k_heapq(ndarr, k=10):

    return heapq.nlargest(k, ndarr)


def top_k_bottleneck(ndarr, k=10):
    return bn.partition(ndarr, ndarr.size - k)[-k:]

if __name__ == '__main__':
    n = 100000000
    k = 3
    ndarr = np.random.rand(n)

    start_time = time.time()

    print(top_k_numpy(ndarr, k))

    print(time.time() - start_time)

    start_time = time.time()

    print(top_k_heapq(ndarr, k))

    print(time.time() - start_time)

    start_time = time.time()

    print(top_k_bottleneck(ndarr, k))

    print(time.time() - start_time)