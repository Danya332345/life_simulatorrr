from organism import Organism

class Plant(Organism):
    """Класс растения, которое может фотосинтезировать."""

    def photosynthesize(self, sun_energy: float = 5.0) -> None:
        """
        Увеличивает энергию за счёт солнечного света.

        :param sun_energy: количество получаемой солнечной энергии
        """
        self.energy += sun_energy
        print(f"{self.name} фотосинтезировал и получил {sun_energy} энергии.")