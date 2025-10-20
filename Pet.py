class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        return f'{self.name} makes a noise.'

    def play(self):
        return f'You play with {self.name}'
        
    def treat(self):
        return f'You give {self.name} a treat'

    def __str__(self):
        return f'{self.name} the {self.age} year old {self.species}!'