import streamlit as st
import streamlit_extras as stE
import streamlit_lottie as stL
import streamlit_option_menu as opMen
import streamlit_ace as stAce
from Pet import Pet
from Dog import Dog
from Cat import Cat
from Bird import Bird

def main():
    #page title, will appear on page in Large font
    st.title('Object Oriented Programming Example')

    #wide layout to make sure explanation and code can fit the page
    st.set_page_config(layout="wide")

    #initialize the columns to display explanation next to buttons/text areas
    col1, col2 = st.columns(2)
    with col1:

        #initialized variable as none, will be reassigned to each different class accordingly
        userPet = None

        #the text input area for the pet, capitalized to look better in a sentence
        name = st.text_input('Enter the name for a pet', 'Start typing...')
        name = name.capitalize()

        #selectbox to ensure the correct class is picked, helps with capitalization or other errors
        species = st.selectbox('Pick a Species', ['Other', 'Cat', 'Bird', 'Dog'])

        #havent tested for string input, might possibly change to text_input instead
        age = st.number_input("Enter the pet's age", min_value=0)

        #if/elif/else that creates each class based on the selectbox input
        if species == 'Dog':
            userPet = Dog(name, species, age)
        elif species == 'Cat':
            userPet = Cat(name, species, age)
        elif species == 'Bird':
            userPet = Bird(name, species, age)
        else:
            userPet = Pet(name, species, age)

        #create the columns for the buttons
        bcol1,bcol2,bcol3,bcol4 = st.columns(4)

        #set an empty string variable to be reused for each button press
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

        #use the success message to display each string result
        st.success(result)

        #set up checkbox columns
        chcol1,chcol2 = st.columns(2)

        #first checkbox will show the raw code for each class
        with chcol1:
            showCode = st.checkbox('Show Code?')
        
        #second checkbox will show a brief description of the code and objects/classes
        with chcol2:
            showExpl = st.checkbox('Show Explanation?')
    with col2:
        #if the showCode checkbox is checked
        if showCode:
            st.code("""
#Pet class
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
#Dog class
from Pet import Pet

class Dog(Pet):
    def speak(self):
        return "Woof! Woof!"
    def play(self):
        return f'You play fetch with {self.name}.'
    def treat(self):
        return f'You give {self.name} a treat.'
#Cat class
from Pet import Pet

class Cat(Pet):
    def speak(self):
        return 'Meow!'
    def play(self):
        return f'You make {self.name} chase around a laser pointer.'
    def treat(self):
        return f'You give {self.name} some catnip.'
#Bird class
from Pet import Pet

class Bird(Pet):
    def speak(self):
        return 'Squawk!'
    def play(self):
        return f'{self.name} does a little dance on their perch.'
    def treat(self):
        return f'You give {self.name} a sesame stick.'""", language="python")
        #if the showExplanation checkbox is checked
        if showExpl:
            st.write("""
We start with the Pet class to get the general attributes and methods.
As you get specific types of pets like birds, cats, and dogs you give them
their own class that inherits the attributes from the general Pet class but
since dogs bark and cats meow, you give them different methods according to what they are.
These are just very basic examples of inheritance and polymorphism.""")
            
if __name__ == '__main__':
    main()
