import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1112920502 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    mu = 1/2 - np.exp(1) # смещение распределения
    var = (1/2 - np.exp(1))**2 # дисперсия распределения
    alpha = 1 - p
    n = len(x)
    t_stat = abs(norm.ppf(alpha/2)) * np.sqrt(n-1)/np.sqrt(n) # статистика для распределения Стьюдента
    loc = 2*x.mean()/(5**2) - mu # мат. ожидание коэффициента ускорения
    scale = np.sqrt(var) / np.sqrt(n)
    return loc - t_stat*scale, loc + t_stat*scale
    
