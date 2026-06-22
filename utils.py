import random

def random_energy(min_val: float = 0.0, max_val: float = 100.0) -> float:
    """Возвращает случайное значение энергии."""
    return round(random.uniform(min_val, max_val), 1)