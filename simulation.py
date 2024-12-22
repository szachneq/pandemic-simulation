import numpy as np


class Simulation:
    def __init__(
        self, population, initially_infected, recovery_chance, transmission_rate
    ):
        self.population = population
        self.infected = initially_infected
        self.unaffected = population - initially_infected
        self.recovery_chance = recovery_chance
        self.transmission_rate = transmission_rate
        self.recovered = 0
        self.history = []

    def run(self):
        days = 0

        while self.infected > 0:
            new_infections = np.random.binomial(
                self.unaffected,
                self.transmission_rate * self.infected / self.population,
            )
            new_recoveries = np.random.binomial(self.infected, self.recovery_chance)

            self.unaffected -= new_infections
            self.infected += new_infections - new_recoveries
            self.recovered += new_recoveries

            self.history.append((self.unaffected, self.infected, self.recovered))
            days += 1

        return days
