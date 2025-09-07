from typing import TypedDict

# no validation on the datatype 
class Person(TypedDict): # create a class inher it from the typedict

    name :str # key 
    age : int


# creating a dictonary

new_person: Person = {'name':"Ibtisam" , 'age':'22'}

print(new_person)