# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 11:00:23 2025

@author: mitran
"""

from Model.ChildState.BaseChildStateInterface import BaseChildState


class TeenBehavior(BaseChildState):
    
    def __init__(self):
        pass
    
    def get_prompt(self):
        return  "child is a Teen"
    def set_values(self) -> str:
        pass