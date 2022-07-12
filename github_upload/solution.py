import numpy as np

if __name__ == "__main__":
    arr1 = np.array([0,0,0,0], dtype=int)
    arr2 = np.array([0,0,0,1], dtype=int)
    print(np.any(arr1))
    print(np.any(arr2))