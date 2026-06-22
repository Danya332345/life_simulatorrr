"""
Главный модуль для запуска симуляции.
"""

from ecosystem import Ecosystem
from animal import Animal
from plant import Plant

def main() -> None:
    """Запускает демонстрацию симуляции."""
    eco = Ecosystem()

    rabbit = Animal("Заяц", 20.0)
    fox = Animal("Лиса", 30.0)
    grass = Plant("Трава", 10.0)

    eco.add_organism(rabbit)
    eco.add_organism(fox)
    eco.add_organism(grass)

    print("=== Начальное состояние ===")
    print(eco)

    print("\n=== День 1 ===")
    eco.simulate_day(energy_food=5.0)  # все получают по 5 энергии

    print("\n=== Охота ===")
    fox.hunt(rabbit)   # лиса съедает зайца

    print("\n=== Состояние после охоты ===")
    print(eco)

    print("\n=== День 2 ===")
    eco.simulate_day(energy_food=5.0)

if __name__ == "__main__":
    main()