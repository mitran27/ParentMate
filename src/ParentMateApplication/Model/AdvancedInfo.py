# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 10:40:23 2025

@author: mitran
"""


from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
# ---------- Advanced Attributes (Post-Login / Follow-up) ----------

@dataclass
class BehavioralTraits:
    empathy_level: str  # "low", "moderate", "high"
    adaptability_to_change: str
    routine_need: str
    stress_level: str
    emotional_sensitivity: str

@dataclass
class CognitiveState:
    age_group: str  # "toddler", "preschool", "teen", etc.
    verbal_ability: str
    consequence_understanding: str
    attention_span: str
    problem_solving_skills: str
    self_regulation: str

@dataclass
class SpecialNeeds:
    neurodivergence: Optional[str]  # e.g., "autism", "ADHD"
    medical_conditions: List[str]

@dataclass
class EducationSocialFactors:
    academic_pressure: str
    teacher_feedback: Optional[str]
    social_confidence: str
    media_exposure_level: str

@dataclass
class EnvironmentFactors:
    recent_changes_at_home: Optional[str]
    recent_loss_or_trauma: Optional[str]

@dataclass
class OneTimeChildState:
    adamant: str
    social_nature: str
    attachment_style: str
    impulsivity_level: str
    sensory_sensitivities: str
    learning_style: str

@dataclass
class OneTimeParentState:
    parenting_experience: str
    work_life_balance: str

@dataclass
class DesiredOutcome:
    long_term_goal: str  # "independent thinker", "emotionally resilient", etc.

@dataclass
class AdvancedChildProfile:
    child_id: str  # can be matched with main child record
    one_time_child_state: OneTimeChildState
    cognitive_state: CognitiveState
    behavioral_traits: BehavioralTraits
    special_needs: SpecialNeeds
    education_social_factors: EducationSocialFactors
    environment_factors: EnvironmentFactors
    desired_outcome: DesiredOutcome

@dataclass
class AdvancedParentProfile:
    parent_id: str  # matched with the main parent
    one_time_parent_state: OneTimeParentState