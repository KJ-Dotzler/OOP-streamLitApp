import streamlit as st
from Pet import Pet
from Dog import Dog
from Cat import Cat
from Bird import Bird
def main():
    st.title('Object Oriented Programming Example')
    st.set_page_config(layout="wide")
    col1, col2 = st.columns(2)
    with col1:
        userPet = None
        name = st.text_input('Enter the name for a pet', 'Start typing...')
        name = name.capitalize()
        species = st.selectbox('Pick a Species', ['Other', 'Cat', 'Bird', 'Dog'])
        age = st.number_input("Enter the pet's age", min_value=0)

        if species == 'Dog':
            userPet = Dog(name, species, age)
        elif species == 'Cat':
            userPet = Cat(name, species, age)
        elif species == 'Bird':
            userPet = Bird(name, species, age)
        else:
            userPet = Pet(name, species, age)
        bcol1,bcol2,bcol3,bcol4 = st.columns(4)
        result = ''
        with bcol1:
            if st.button("Create Pet!"):
                result = f'Welcome! {userPet}'
        with bcol2:
            if st.button('Say hello?'):
                result = userPet.speak()
        with bcol3:
            if st.button('Play?'):
                result= userPet.play()
        with bcol4:
            if st.button('Give Treat?'):
                result = userPet.treat()
        st.success(result)
        chcol1,chcol2 = st.columns(2)
        with chcol1:
            showCode = st.checkbox('Show Code?')
        with chcol2:
            showExpl = st.checkbox('Show Explanation?')
    with col2:
        if showCode:
            st.code("""
#Pet class
class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        print(f'{self.name} makes a noise.')

    def play(self):
        print(f'You play with {self.name}')
        
    def treat(self):
        print(f'You give {self.name} a treat')

    def __str__(self):
        return f'{self.name} the {self.age} year old {self.species}!'
#Dog class
from Pet import Pet

class Dog(Pet):
    def speak(self):
        print("Woof! Woof!")
    def play(self):
        print(f'You play fetch with {self.name}.')
    def treat(self):
        print(f'You give {self.name} a treat.')
#Cat class
from Pet import Pet

class Cat(Pet):
    def speak(self):
        print('Meow!')
    def play(self):
        print(f'You make {self.name} chase around a laser pointer.')
    def treat(self):
        print(f'You give {self.name} some catnip.')
#Bird class
from Pet import Pet

class Bird(Pet):
    def speak(self):
        print('Squawk!')
    def play(self):
        print(f'{self.name} does a little dance on their perch.')
    def treat(self):
        print(f'You give {self.name} a sesame stick.')""", language="python")
        if showExpl:
            st.write("""
We start with the Pet class to get the general attributes and methods.
As you get specific types of pets like birds, cats, and dogs you give them
their own class that inherits the attributes from the general Pet class but
since dogs bark and cats meow, you give them different methods according to what they are.
These are just very basic examples of inheritance and polymorphism.""")
if __name__ == '__main__':
    main()
