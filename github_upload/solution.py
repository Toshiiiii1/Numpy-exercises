import numpy as np

if __name__ == "__main__":
    arr = np.array((np.arange(1,7), np.arange(1,7)), dtype=int)
    if (0 in arr):
        print("yes")
    else:
        print("no")