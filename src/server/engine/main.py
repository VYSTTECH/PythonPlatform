#coding: utf-8

import numpy as np 

class new_class: 
    def __init__(self, value): 
        self.value = value 

    def new_function(self):
        return self.value * 2 

if __name__ = "__main__":
    value = 10 

    first_class = new_class(value)
    print(first_class.new_function)

