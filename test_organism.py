import pytest
from organism import Organism

def test_organism_creation():
    org = Organism("Тест", 50.0)
    assert org.name == "Тест"
    assert org.energy == 50.0
    assert org.is_alive() is True

def test_eat():
    org = Organism("Тест", 10.0)
    org.eat(5.0)
    assert org.energy == 15.0

def test_eat_negative_raises():
    org = Organism("Тест", 10.0)
    with pytest.raises(ValueError):
        org.eat(-1.0)

def test_is_alive():
    org = Organism("Тест", 0.0)
    assert org.is_alive() is False
    org.eat(1.0)
    assert org.is_alive() is True