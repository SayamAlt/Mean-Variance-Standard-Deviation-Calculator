import numpy as np

list_a = [int(num) for num in input().split()]

list_a = np.reshape(list_a, (3, 3))

result = {
    'mean': [np.mean(list_a, axis=0).astype(float), np.mean(list_a, axis=1).astype(float), np.mean(list_a).astype(float)],
    'variance': [np.var(list_a, axis=0).astype(float), np.var(list_a, axis=1).astype(float), np.var(list_a).astype(float)],
    'standard deviation': [np.std(list_a, axis=0).astype(float), np.std(list_a, axis=1).astype(float), np.std(list_a).astype(float)],
    'max': [np.max(list_a, axis=0).astype(float), np.max(list_a, axis=1).astype(float), np.max(list_a).astype(float)],
    'min': [np.min(list_a, axis=0).astype(float), np.min(list_a, axis=1).astype(float), np.min(list_a).astype(float)],
    'sum': [np.sum(list_a, axis=0).astype(float), np.sum(list_a, axis=1).astype(float), np.sum(list_a).astype(float)]
}

print(result)
