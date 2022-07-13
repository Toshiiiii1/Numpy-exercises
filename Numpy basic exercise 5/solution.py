import numpy as np

if __name__ == "__main__":
    arr1 = np.array([1,2,3,4], dtype=int)
    arr2 = np.array([1,2,np.nan,np.inf])
    
    print(np.isfinite(arr1))
    print(np.isfinite(arr2))