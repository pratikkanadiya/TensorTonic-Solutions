import numpy as np

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if(norm_a == 0 or norm_b == 0):
        return 0.0
    else:
        return dot / (norm_a * norm_b)

    a = [1, 2, 3]
    b = [2, 4, 6]
    print(cosine_similarity(a, b))