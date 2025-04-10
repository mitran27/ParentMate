# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 19:54:25 2025

@author: mitran
"""

from WizardMenu.BasicInfoWizard import RegistrationWizard
from PromptBuilder import build_family_prompt
family1 = RegistrationWizard().register_family()
build_family_prompt(family1,"dharshini")
prompt = """You are a compassionate and intelligent parenting assistant. Use the following family context and behavioral traits to offer context-aware guidance and suggestions.

👨 Parent:
- Name: Mitran, Age: 33, Relation: father
- Personality Traits: Calm, Coposed
- Stress Triggers: Crying, disturbing
- Working Status: working

🏡 Family Environment:
- Location: trichy, tamil nadu, india
- Spouse Type: hapy_couple
- Parenting Approach: gentle
 
 Child :
     👧 Child: dharshini
                    - Age: 4, Gender: female
                    - Birth Order: first, Single Child: Yes
                    - School: montfort, Grade: KG
                    
                    🎯 Behavioral Profile:
                    - Obedience Level: medium
                    - Emotional Response: calm
                    - Attention Need: moderate
                    - Behaviourstate: child is a Toodler
                    
                    🎈 Likes:
                    - Toys: car, doll
                    - Shows: power, carrtoon
                    - Foods: dosa, idli
                    - Activities: reading, playing
                    
                    ⚠️ Triggers:
                    - Dislikes: elders
                    - Fears: dark, lonliness
                    - Frustration Points: hunger, scolding"""
