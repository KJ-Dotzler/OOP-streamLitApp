#streamlit imports
import streamlit as st
import streamlit_extras as stE
import streamlit_lottie as stL
import streamlit_option_menu as opMen
import streamlit_ace as stAce

#wide layout to make sure explanation and code can fit the page
st.set_page_config(layout="wide", page_title='OOP for Beginners')

#module/class imports
import requests
import json
from Pet import Pet
from Dog import Dog
from Cat import Cat
from Bird import Bird

#globals for API/sandboxing code execution
starterCode = """
#this is test code, feel free to change it!
class Car:
    def __init__(self, make, model, year):
        #write your own definition here

    def value(self):
        return f'Your {self.year} {self.make} {self.model} is priceless'
    #feel free to write more methods if you want

car = Car()
print(car.value())
                   
                """
API_URL = 'https://emkc.org/api/v2/piston/execute'

def main():
    #page title, will appear on page in Large font
    st.title('Object Oriented Programming Example')

    

    #initialize the columns to display explanation next to buttons/text areas
    col1, col2 = st.columns(2)
    with col1:

        #create columns for the user inputs
        incol1, incol2, incol3 = st.columns(3)

        #initialized variable as none, will be reassigned to each different class accordingly
        userPet = None

        with incol1:
            #the text input area for the pet, capitalized to look better in a sentence
            name = st.text_input('Enter the name for a pet', 'Start typing...')
            name = name.capitalize()
        with incol2:
            #selectbox to ensure the correct class is picked, helps with capitalization or other errors
            species = st.selectbox('Pick a Species', ['Other', 'Cat', 'Bird', 'Dog'])

        with incol3:
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
        chcol1,chcol2,chcol3 = st.columns(3)

        #first checkbox will show the raw code for each class
        with chcol1:
            showCode = st.checkbox('Show Code?')
        
        #second checkbox will show a brief description of the code and objects/classes
        with chcol2:
            showExpl = st.checkbox('Show Explanation?')
        with chcol3:
            testCode = st.checkbox('Try your own code')

        
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
We start with the Pet class to get the general attributes and methods.\n
As you get specific types of pets like birds, cats, and dogs you give them
their own class that inherits the attributes from the general Pet class.\n
Since dogs bark and cats meow, you give change/override the speak method according to what they are.\n
These are just very basic examples of inheritance and polymorphism.""")
            
        if testCode:
            code_area = stAce.st_ace(
                value=starterCode,
                language='python',
                theme='chrome',
                key='codeSandbox',
                height=250
            ) 
            if st.button('Run Code'):
                codeToRun = {
                    'language' : 'python',
                    'version' : '3.10.0',
                    'files' : [{'name' : 'main.py', 'content' : code_area}],
                    'stdin' : '',
                    'args' : [],
                    'compile_timeout' : 10000,
                    'run_timeout' : 3000,
                    'compile_memory_limit' : -1,
                    'run_memory_limit' : -1
                }
                try:
                    resp = requests.post(API_URL, json=codeToRun, timeout=5)
                    result = resp.json()
                    runData = result.get('run', {})
                    stdout = runData.get('stdout', '')
                    stderr = runData.get('stderr', '')
                    extCode = runData.get('code', None)

                    if stdout:
                        st.success(f'Your code output:\n{stdout}')
                    elif stderr:
                        st.code(stderr)
                    elif extCode != None:
                        st.info(extCode)
                    else:
                        st.warning('No output, something went wrong.')
                        st.write(result)
                except Exception as e:
                    st.error(e)

            
if __name__ == '__main__':
    main()
