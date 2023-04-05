import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1112920502 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    from scipy.stats import t
    n = len(x)
    s = np.std(x, ddof=1)
    t_value = t.ppf((1 + p) / 2, n - 1)
    delta = t_value * s / np.sqrt(n)
    return (np.mean(x) - delta, np.mean(x) + delta)
    
