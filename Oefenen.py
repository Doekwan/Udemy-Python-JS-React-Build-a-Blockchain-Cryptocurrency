# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:57:56 2021

@author: Wolf
"""

class Animal:
    def __init__(self, habitat, diet):
        self.habitat = habitat
        self.diet = diet

    def speak(self):
        print(f"I live in the {self.habitat} and eat {self.diet}")

animal_1 = Animal('jungle', 'meat')
animal_1.speak()

class Lion(Animal):
    def __init__(self, title, pride_size):
        super().__init__('savannah', 'meat')
        self.title = title
        self.pride_size = pride_size

    def roar(self):
        print(f"I am the {self.title} of my pride of {self.pride_size}")

lion_1 = Lion('chihuahua', 80)
lion_1.roar()
lion_1.speak()
