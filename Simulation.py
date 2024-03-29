import random, sys
from Person import Person
from Virus import Virus
from filewriter import FileWriter

class Simulation:

    def __init__(self, initial_vaccinated, initial_infected, initial_healthy, virus, resultsfilename):
        '''Set up the initial simulation values'''

        self.virus = virus 
        self.initial_infected = initial_infected 
        self.initial_healthy = initial_healthy
        self.initial_vaccinated = initial_vaccinated

        self.population = []

        self.population_size = initial_infected + initial_healthy + initial_vaccinated


        self.total_dead = 0
        self.total_vaccinated = initial_vaccinated

        self.file_writer = FileWriter(resultsfilename)


    def create_population(self):
        '''Creates the population (a list of Person objects) consisting of initial infected people, initial healthy non-vaccinated people, and 
        initial healthy vaccinated people. Adds them to the population list'''

        for i in range(self.initial_infected):
            person = Person(False, virus)
            self.population.append(person)

        for i in range(self.initial_healthy):
            person = Person(False, None)
            self.population.append(person)

        for i in range(self.initial_vaccinated):
            person = Person(True, None)
            self.population.append(person)
        	
    def print_population(self):
        '''Prints out every person in the population and their current attributes'''
        #TODO: finish this method
        for person in self.population:
            print(person.is_alive)
            print(person.is_vaccinated)
            
        print("Population Size: {}".format(self.population_size))
        print("Initial Infected: {}".format(self.initial_infected))
        print("Initial Healthy: {}".format(self.initial_healthy))
        print("Initial Vaccinated: {}".format(self.initial_vaccinated))
        print("Total Dead: {}".format(self.total_dead))
        print("Total Vaccinated: {}".format(self.total_vaccinated))
            

    def get_infected(self):
    
        '''Gets all the infected people from the population and returns them as a list'''
        #TODO: finish this method
        infected_list = []
        for person in self.population:
            if person.infection is not None:
                infected_list.append(person)
        return infected_list
            


    def simulation_should_continue(self):
        '''Determines whether the simulation should continue.
        If everyone in the population is dead then return False, the simulation should not continue
        If everyone in the population is vaccinated return False
        If there are no more infected people left and everyone is either vaccinated or dead return False
        In all other cases return True'''
        #TODO: finish this method
        for i in self.population:
            if self.total_dead >= self.population_size:
                return False
            elif self.total_vaccinated >= self.population_size:
                return False
            elif len(self.get_infected()) == 0:
                return False
            else:
                return True

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        
        self.create_population()
        random.shuffle(self.population)

        self.print_population()
        
        time_step_counter = 0
        should_continue = True

        self.file_writer.init_file(self.virus, self.population_size, self.initial_vaccinated, self.initial_healthy, self.initial_infected)

        #keep looping until the simulation ends
        while self.simulation_should_continue():
            
            #save the current infected
            old_infected = self.get_infected()
            self.time_step(old_infected)
            #time step will create newly infected people, just determine the survivial of the previous infected people
            self.determine_survival(old_infected)

            time_step_counter += 1
            
        print(f'The simulation has ended after {time_step_counter} turns.')
        
        self.file_writer.write_results(time_step_counter, self.total_dead, self.total_vaccinated)

    def determine_survival(self, infected):
        '''Check if the current infected people survive their infection
        Call the did_survive_infection() method
        if it returns false then the person is no longer alive, does not have an infection and one is added to total dead
        if it returns true then the person no longer has an infection and is vaccinated, one is added to total vaccinated'''
        #TODO: finish this method
        for self.person in infected:
            if self.person.did_survive_infection() == False:
                self.total_dead += 1
            elif self.person.did_survive_infection() == True:
                self.total_vaccinated += 1
            else:
                print("Error")
            

    def time_step(self, infected):
        ''' For every infected person interact with a random person from the population 10 times'''

        # self.newly_infected = []
        # self.newly_dead = 0
        
        # for person in self.population:
        for infected_person in infected:
            interaction_count = 0

            for i in range(10):
                #TODO: get a random index for the population list
                random_index = random.randint(0, len(self.population)-1)
                #TODO: using the random index get a random person from the population
                random_person = self.population[random_index]
                #TODO: call interaction() with the current infected person and the random person
                self.interaction(infected_person, random_person)


    def interaction(self, infected, random_person):
        '''If the infected person is the same object as the random_person return and do nothing
        if the random person is not alive return and do nothing
        if the random person is vaccinated return and do nothing
        if the random person is not vaccinated:
            generate a random float between 0 and 1
            if the random float is less then the infected person's virus reproduction number then the random person is infected
            othersie the random person is vaccinated and one is added to the total vaccinated'''
        #TODO: finish this method
        if infected == random_person:
            return
        elif random_person.is_vaccinated == True:
            return
        elif random_person.is_alive == False:
            return
        elif random_person.is_vaccinated == False and random_person.is_alive == True:
            random_result = random.uniform(0,1)
            if random_result < self.virus.reproduction_num:
                random_person.infection = self.virus
                return random_person
            else: 
                random_person.is_vaccinated = True
                return random_person
        
        


if __name__ == "__main__":

    #Set up the initial simulations values
    virus_name = "Malaise"
    reproduction_num = 0.20
    mortality_num = .99

    initial_healthy = 10
    initial_vaccinated = 5

    initial_infected = 1

    virus = Virus(virus_name, reproduction_num, mortality_num)

    simulation = Simulation(initial_vaccinated, initial_infected, initial_healthy, virus, "results.txt")

    # secondary virus
    virus_name = "Dengue Fever"
    reproduction_num = 0.50
    mortality_num = .49

    initial_healthy = 80
    initial_vaccinated = 15

    initial_infected = 5

    virus2 = Virus(virus_name, reproduction_num, mortality_num)

    simulation2 = Simulation(initial_vaccinated, initial_infected, initial_healthy, virus2, "results2.txt")

    #run the simulation
    simulation.run()
    simulation2.run()