from Pet import Pet

class Cat(Pet):
    def speak(self):
        return 'Meow!'
    def play(self):
        return f'You make {self.name} chase around a laser pointer.'
    def treat(self):
        return f'You give {self.name} some catnip.'