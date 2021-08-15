import numpy as np

matrix_a = []

for i in range(3):
    a = []
    for j in range(3):
        a.append(int(input()))
    matrix_a.append(a)

print(matrix_a)

result = {
    'mean': [np.mean(matrix_a, axis=0).astype(float), np.mean(matrix_a, axis=1).astype(float), np.mean(matrix_a).astype(float)],
    'variance': [np.var(matrix_a, axis=0).astype(float), np.var(matrix_a, axis=1).astype(float), np.var(matrix_a).astype(float)],
    'standard deviation': [np.std(matrix_a, axis=0).astype(float), np.std(matrix_a, axis=1).astype(float), np.std(matrix_a).astype(float)],
    'max': [np.max(matrix_a, axis=0).astype(float), np.max(matrix_a, axis=1).astype(float), np.max(matrix_a).astype(float)],
    'min': [np.min(matrix_a, axis=0).astype(float), np.min(matrix_a, axis=1).astype(float), np.min(matrix_a).astype(float)],
    'sum': [np.sum(matrix_a, axis=0).astype(float), np.sum(matrix_a, axis=1).astype(float), np.sum(matrix_a).astype(float)]
}

print(result)
