import os
import dotenv

found_dotenv = dotenv.find_dotenv('.env')
dotenv.load_dotenv(found_dotenv)

def apply_func(func):
    return lambda x:func(x)
 
#def from_env(key):
     #return os.getenv(key)

from_env = apply_func(os.getenv)

# Accessing variables.
status = from_env('STATUS')
secret_key = from_env('PASSWORD')

# Using variables.
print(status)
print(secret_key)