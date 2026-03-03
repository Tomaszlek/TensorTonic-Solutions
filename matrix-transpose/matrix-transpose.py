import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A) #zmieniamy w Matrixa numpyowego
    num_rows, num_cols = A.shape #wyciagam sobie wymiary
    new_matrix = np.zeros((num_cols, num_rows)) # zapelniam tebele zerami
    for i in range(num_rows):
        for j in range(num_cols):
            new_matrix[j][i] = A[i][j] #swapijemy wiersz z kolumna

    return new_matrix
