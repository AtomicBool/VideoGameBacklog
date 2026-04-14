import math

def compare_taste(a: list[int], b: list[int]) -> float:
    dot = 0
    squared_norm_a = 0
    squared_norm_b = 0

    for i in range(6):
        dot += a[i] * b[i]
        squared_norm_a += a[i]**2
        squared_norm_b += b[i]**2

    if squared_norm_a == 0 or squared_norm_b == 0:
        return 0.0

    return dot / math.sqrt(squared_norm_a * squared_norm_b)