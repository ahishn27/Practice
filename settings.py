#Package imports
import os
import dotenv

#searching the .env file in the directory 
found_dotenv = dotenv.find_dotenv('.env')

#Loading the .env file to get access to the variables
dotenv.load_dotenv(found_dotenv)

#apply_functions
def apply_func(func):
    return lambda x:func(x)

#functions gets the value based on the key passed 
def from_env(key):
     return os.getenv(key)

#common function
from_env = apply_func(os.getenv)

# Accessing variables from .env file
status = from_env('STATUS')
secret_key = from_env('PASSWORD')

#display statements
print(status)
print(secret_key)