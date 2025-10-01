from pydantic import BaseModel, EmailStr, Field
from typing import Optional
# by the help of pydantic we can create data models with validation
# we can also set default values, make fields optional, and add constraints to fields
# pydantic will automatically validate the data types and constraints when creating an instance of the model
# if the data is invalid, pydantic will raise a ValidationError
# pydantic models can be easily converted to and from dictionaries and JSON
# pydantic is very useful for data validation and serialization in web applications and APIs
# pydantic is also used in FastAPI for request and response models
# It will do type coercion, for example if we pass age as a string it will convert it to integer
# pydantic is very powerful and flexible, we can create complex nested models and use them for data validation and serialization
class Student(BaseModel):
    name: str ='nitish'  # we can set default values
    age : Optional[int] = None  # we can make fields optional
    email: EmailStr  # we can use specific types like EmailStr for validation
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')  # we can add constraints and
new_student = {'age':'32', 'name':'vikrant', 'email':'abc@adc.com', 'cgpa': '2'} #type coercion description to fields

student = Student(**new_student)

print(student.model_dump_json())  # we can convert the model to JSON
print(student.model_dump())  # we can convert the model to dictionary
print(student)  # we can access the fields like normal attributes












# class Student(BaseModel):

#     name: str = 'nitish'
#     age: Optional[int] = None
#     email: EmailStr
#     cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


# new_student = {'age':'32', 'email':'abc@gmail.com'}

# student = Student(**new_student)

# student_dict = dict(student)

# print(student_dict['age'])

# student_json = student.model_dump_json() 