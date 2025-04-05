import numpy as np


def calculate(list) -> dict:
    """
    Using Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns,
    and elements in a 3 x 3 matrix.
    """
    # Check that lst has exactly 9 elements
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    # Create a 3x3 Numpy matrix from l
    matrix = np.array([list[:3], list[3:6], list[6:]])
    stats = {
        'mean': [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(),
                 np.mean(matrix).tolist()],
        'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(),
                     np.var(matrix).tolist()],
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(),
                               np.std(matrix).tolist()],
        'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(),
                np.max(matrix).tolist()],
        'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(),
                np.min(matrix).tolist()],
        'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(),
                np.sum(matrix).tolist()]
    }

    return stats
# t_lst = list(range(9))
# test = np.array([t_lst[:5:2], t_lst[1:6:2], t_lst[6:]])
# print(calculate(t_lst))
