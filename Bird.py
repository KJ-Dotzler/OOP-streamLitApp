from Pet import Pet

class Bird(Pet):
    def speak(self):
        return 'Squawk!'
    def play(self):
        return f'{self.name} does a little dance on their perch.'
    def treat(self):
        return f'You give {self.name} a sesame stick.'