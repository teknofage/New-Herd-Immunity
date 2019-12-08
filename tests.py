from Simulation import Simulation
from Person import Person
from Virus import Virus
import unittest
import pytest


class simulation_Tests(unittest.TestCase):
    def test_instantiation(self):
        _virus = self.Virus(self, 0.5, 0.5)
        _sim = simulation.Simulation(100, 0.5, _virus, 10)
        assert _sim.virus == _virus
        assert _sim.pop_size == 100
        assert _sim.total_dead == 0

    def test_create_population(self):
        _virus = virus.Virus('Virus', 0.5, 0.5)
        _sim = simulation.Simulation(100, 0.5, _virus, 10)
        _sim.population = _sim._create_population(_sim.initial_infected)
        infected = []
        is_vaccinated = []
        normal_people = []
        total = []
        for _person in _sim.population:
            total.append(_person)
            if _person.infection != None:
                infected.append(_person)
            elif _person.is_vaccinated == True:
                vaccinated.append(_person)
            else:
                normies.append(person)
        assert len(_sim.population) == 100
        assert len(infected) == 10
        assert len(vaccinated) == 50
        assert len(normal_people) == 40
        assert len(total) == 100
        assert len(total) == len(infected)+len(vaccinated)+len(normal_people)
    