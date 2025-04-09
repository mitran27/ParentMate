# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 19:49:15 2025

@author: mitran
"""

from Model.ChildState.Implementation.Autistic import AutisticBehavior
from Model.ChildState.Implementation.Toddler import ToddlerBehavior
from Model.ChildState.Implementation.Teen import TeenBehavior

from Model.ChildState.BaseChildStateInterface import BaseChildState

class ChildBehaviorFactory:
    
    @staticmethod
    def get_behavior(child_type: str) -> BaseChildState:
        if child_type == "teen":
            return ToddlerBehavior()
        elif child_type == "toddler":
            return ToddlerBehavior()
        elif child_type == "autistic":
            return AutisticBehavior()
        # Add more cases as needed
        else:
            raise ValueError("Unsupported child type")