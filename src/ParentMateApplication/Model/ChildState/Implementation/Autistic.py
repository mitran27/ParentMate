# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 11:00:36 2025

@author: mitran
"""

from Model.ChildState.BaseChildStateInterface import BaseChildState


class AutisticBehavior(BaseChildState):
    
    def __init__(self):
        pass    
    def get_prompt(self):
        return  "child is a Autistic"
    def set_values(self) -> str:
        pass