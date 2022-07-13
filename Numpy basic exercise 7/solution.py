import numpy as np

if __name__ == "__main__":
    arr1 = np.array([1,2,3,4])
    arr2 = np.array([np.nan, 0, 1, np.nan])
    
    print(np.isnan(arr1))
    print(np.isnan(arr2))