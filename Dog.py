from Pet import Pet

class Dog(Pet):
    def speak(self):
        return "Woof! Woof!"
    def play(self):
        return f'You play fetch with {self.name}.'
    def treat(self):
        return f'You give {self.name} a bone.'
    