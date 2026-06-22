"""
Модуль, реализующий экосистему.
"""

from typing import List
from organism import Organism

class Ecosystem:
    """Управляет совокупностью организмов и симулирует их жизнедеятельность."""

    def __init__(self) -> None:
        """Инициализирует пустую экосистему."""
        self.organisms: List[Organism] = []

    def add_organism(self, organism: Organism) -> None:
        """Добавляет организм в экосистему."""
        self.organisms.append(organism)

    def simulate_day(self, energy_food: float = 10.0) -> None:
        """
        Симулирует один день: каждый живой организм получает энергию (еду).
        Мёртвые организмы выводятся в лог.

        :param energy_food: количество энергии, получаемой за день (можно позже сделать разным для разных видов)
        """
        for org in self.organisms:
            if org.is_alive():
                org.eat(energy_food)
            else:
                print(f"{org.name} мёртв.")

    def get_alive_count(self) -> int:
        """Возвращает количество живых организмов."""
        return sum(1 for org in self.organisms if org.is_alive())

    def __str__(self) -> str:
        return f"Экосистема: {len(self.organisms)} организмов, живых: {self.get_alive_count()}"