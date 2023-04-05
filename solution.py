import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1112920502 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    from scipy.stats import t
    n = len(x)
    X_ = np.mean(x)
    s = np.sqrt(np.sum((x - X_)**2) / (n - 1))
    t_p = t.ppf(1 - p/2, n - 1)
    delta = t_p * s / np.sqrt(n)
    return (X_ - delta, X_ + delta)
    
