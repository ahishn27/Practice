import os
import dotenv

def apply_func(func):
    return lambda x:func(x)

def square(x):
    return x**2

square = apply_func(square)




