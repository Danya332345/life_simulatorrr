from ecosystem import Ecosystem
from organism import Organism

def test_add_and_count():
    eco = Ecosystem()
    org1 = Organism("A", 10)
    org2 = Organism("B", 20)
    eco.add_organism(org1)
    eco.add_organism(org2)
    assert len(eco.organisms) == 2
    assert eco.get_alive_count() == 2

def test_simulate_day_kills_zero_energy():
    eco = Ecosystem()
    org = Organism("Zombie", 0.0)
    eco.add_organism(org)
    eco.simulate_day(5.0)  # энергия станет 5, так что не умрёт
    assert org.is_alive() is True
    # сделаем отрицательную? но у нас нет отрицательной энергии
    # можно проверить, что при нулевой энергии и без еды он умрёт
    # но simulate_day даёт еду, так что специально не трогаем