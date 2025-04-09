# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 10:59:25 2025

@author: mitran
"""

from abc import ABC, abstractmethod

class BaseChildState(ABC):
    
    @abstractmethod
    def get_prompt(self) -> str:
        pass
    @abstractmethod
    def set_values(self) -> str:
        pass
    """@abstractmethod
    def communication_style(self) -> str:
        pass
    
    @abstractmethod
    def question_set(self) -> list:
        pass
    
    @abstractmethod
    def sensitivity_flags(self) -> list:
        pass
    
    @abstractmethod
    def suggestion_strategy(self) -> str:
        pass"""
