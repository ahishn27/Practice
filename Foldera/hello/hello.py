import os
import dotenv

#onlychange

found_env = dotenv.find_dotenv('.env')
dotenv.load_dotenv(found_env)

def apply_func(func):
    return lambda x:func(x)

from_env = apply_func(os.getenv)

secret_key = from_env('SECRET_KEY')

print(secret_key)