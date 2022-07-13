import numpy as np

if __name__ == "__main__":
    arr1 = np.array([1,2,3,4])
    arr2 = np.array([-np.inf, 0, 1, np.inf])
    
    print(np.isinf(arr1))
    print(np.isinf(arr2))