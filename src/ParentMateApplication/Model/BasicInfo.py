# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 10:36:36 2025

@author: mitran
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict
from Model.ChildState.BaseChildStateInterface import BaseChildState
# ---------- Basic Models for Initial Registration ----------

@dataclass
class ContactInfo:
    email: str
    phone: str

@dataclass
class Parent:
    name: str
    age: int
    gender: str  # "male", "female", "other"
    relation: str  # "mother", "father"
    contact_info: ContactInfo
    personality_traits: List[str]
    stress_triggers: List[str]
    working_status: str  # e.g., "working", "homemaker"
    contact_info: ContactInfo

@dataclass
class FamilyContext:
    spouse_type: str  # "single_parent", "happy_couple", "divorced", etc.
    parenting_approach: Optional[str] = None  # "gentle", "authoritative", etc.

@dataclass
class SchoolingInfo:
    school_name: str
    grade: str

@dataclass
class Favorites:
    toys: List[str] = field(default_factory=list)
    shows: List[str] = field(default_factory=list)
    foods: List[str] = field(default_factory=list)
    activities: List[str] = field(default_factory=list)

@dataclass
class Triggers:
    dislikes: List[str] = field(default_factory=list)  # Loud sounds, spicy food, etc.
    fears: List[str] = field(default_factory=list)      # Dark, being alone, etc.
    frustration_triggers: List[str] = field(default_factory=list)  # Ignored, being corrected publicly

@dataclass
class BehaviorFlags:
    obedience_level: str  # "low", "medium", "high"
    emotional_response: str  # "calm", "reactive", "aggressive", "timid"
    attention_need: str  # "low", "moderate", "high"

@dataclass
class Child:
    name: str
    age: int
    gender: str
    birth_order: Optional[str] = None  # "first", "second", etc.
    is_single_child: bool = False
    schooling: Optional[SchoolingInfo] = None
    favorites: Favorites = None
    triggers: Optional[Favorites] = None
    behavior_flags: Optional[Favorites] = None
    state: BaseChildState = None

@dataclass
class Address:
    city: str
    state: str
    country: str

@dataclass
class Family:
    family_id: str
    address: Address
    parent: Parent
    children: Dict[str, Child]
    family_context: FamilyContext
    registration_timestamp: str