import numpy as np

if __name__ == "__main__":
    arr = np.array([1+2j, 2+3j, 3+0j])
    print(np.iscomplex(arr))
    print(np.isreal(arr))
    print(np.isscalar(arr))