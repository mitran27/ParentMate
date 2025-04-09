# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 22:14:06 2025

@author: mitran
"""
from Model.BasicInfo import Family
def build_family_prompt(family: Family,child_name : str) -> str:
    parent = family.parent
    child_sections = []
    
    child = family.children[child_name]
        
    favorites = child.favorites
    triggers = child.triggers
    behavior= child.state.get_prompt()
    behavior_flags = child.behavior_flags
    

    child_section = f"""
                    👧 Child: {child.name}
                    - Age: {child.age}, Gender: {child.gender}
                    - Birth Order: {child.birth_order or "Not specified"}, Single Child: {"Yes" if child.is_single_child else "No"}
                    - School: {child.schooling.school_name if child.schooling else "N/A"}, Grade: {child.schooling.grade if child.schooling else "N/A"}
                    
                    🎯 Behavioral Profile:
                    - Obedience Level: {behavior_flags.obedience_level if behavior_flags else "N/A"}
                    - Emotional Response: {behavior_flags.emotional_response if behavior_flags else "N/A"}
                    - Attention Need: {behavior_flags.attention_need if behavior_flags else "N/A"}
                    - Behaviourstate: {behavior}
                    
                    🎈 Likes:
                    - Toys: {", ".join(favorites.toys) if favorites else "None"}
                    - Shows: {", ".join(favorites.shows) if favorites else "None"}
                    - Foods: {", ".join(favorites.foods) if favorites else "None"}
                    - Activities: {", ".join(favorites.activities) if favorites else "None"}
                    
                    ⚠️ Triggers:
                    - Dislikes: {", ".join(triggers.dislikes) if triggers else "None"}
                    - Fears: {", ".join(triggers.fears) if triggers else "None"}
                    - Frustration Points: {", ".join(triggers.frustration_triggers) if triggers else "None"}
                    """.strip()

    return f"""
You are a compassionate and intelligent parenting assistant. Use the following family context and behavioral traits to offer context-aware guidance and suggestions.

👨 Parent:
- Name: {parent.name}, Age: {parent.age}, Relation: {parent.relation}
- Personality Traits: {", ".join(parent.personality_traits)}
- Stress Triggers: {", ".join(parent.stress_triggers)}
- Working Status: {parent.working_status}

🏡 Family Environment:
- Location: {family.address.city}, {family.address.state}, {family.address.country}
- Spouse Type: {family.family_context.spouse_type}
- Parenting Approach: {family.family_context.parenting_approach or "Not specified"}

 Child :
     {child_section}
""".strip()
