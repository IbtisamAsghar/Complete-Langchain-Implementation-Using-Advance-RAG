from pydantic import BaseModel,EmailStr,Field
from typing import Optional

# Ensure datatype validation
class Student(BaseModel):
    name : str = "ibtisam"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0 , lt=4 , description='A decimal value representing the cgpa of the student') # applying the constraints

new_student = {'age':'22' , 'email':"ibti@gmail.com","cgpa":3.66} # implicit type conversion happen by the pydantic

student = Student(**new_student)

#print(student)
# print(type(student))

# converting pydantic object to dict 
student_dict = dict(student)

print(student_dict['cgpa'])

# converting pydantic object to json
student_json = student.model_dump_json()