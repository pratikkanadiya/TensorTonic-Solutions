import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    pos = np.arange(seq_len).reshape(-1, 1)
    
    i = np.arange((d_model  + 1) // 2)
    
    denom = np.pow(base, (2 * i) / d_model)
    
    angles = pos / denom
    
    pe = np.zeros((seq_len, d_model), dtype=float)

    pe[:, 0::2] = np.sin(angles[:, : (d_model + 1)//2])

    pe[:, 1::2] = np.cos(angles[:, : d_model//2])

    return pe
    
seq_len, d_model = 3, 4
print(positional_encoding(seq_len, d_model))