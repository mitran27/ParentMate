# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 10:47:54 2025

@author: mitran
"""

from Model.BasicInfo import *
from Model.ChildState.ChildStateFactory import ChildBehaviorFactory
import uuid,datetime
class RegistrationWizard:
    
    def __init__(self):
        pass

    def _get_input(self, prompt, default=None, options=None):
        if options:
            prompt += f" {options}"
        if default:
            prompt += f" (default: {default})"
        prompt += ": "
        value = input(prompt)
        return value.strip() if value.strip() else default

    def _collect_contact_info(self):
        email = self._get_input("Enter parent's email")
        phone = self._get_input("Enter parent's phone")
        return ContactInfo(email=email, phone=phone)

    def _collect_parent(self):
        print("\n Parent Information")
        name = self._get_input("Enter parent's name")
        age = int(self._get_input("Enter parent's age"))
        gender = self._get_input("Enter parent's gender", options=["male", "female", "other"])
        relation = self._get_input("Enter relation to child", options=["mother", "father"])
        contact_info = self._collect_contact_info()
        traits = self._get_input("Enter personality traits (comma separated)").split(",")
        stress_triggers = self._get_input("Stress triggers (comma separated)").split(",")
        working_status = self._get_input("Working status", options=["working", "homemaker", "freelancer", "retired"])

        return Parent(
            name=name,
            age=age,
            gender=gender,
            relation=relation,
            contact_info=contact_info,
            personality_traits=traits,
            stress_triggers=stress_triggers,
            working_status=working_status
        )

    def _collect_schooling(self):
        school = self._get_input("Enter school name")
        grade = self._get_input("Enter grade", options=["KG", "1st", "2nd", "3rd", "4th", "5th", "6th", "Middle", "High"])
        return SchoolingInfo(school_name=school, grade=grade)

    def _collect_favorites(self):
        toys = self._get_input("Favorite toys (comma separated)").split(",")
        shows = self._get_input("Favorite shows (comma separated)").split(",")
        foods = self._get_input("Favorite foods (comma separated)").split(",")
        activities = self._get_input("Favorite activities (comma separated)").split(",")
        return Favorites(toys=toys, shows=shows, foods=foods, activities=activities)

    def _collect_triggers(self):
        dislikes = self._get_input("Dislikes (comma separated)").split(",")
        fears = self._get_input("Fears (comma separated)").split(",")
        frustrations = self._get_input("Frustration triggers (comma separated)").split(",")
        return Triggers(dislikes=dislikes, fears=fears, frustration_triggers=frustrations)

    def _collect_behavior_flags(self):
        obedience = self._get_input("Obedience level", options=["low", "medium", "high"])
        emotion = self._get_input("Emotional response", options=["calm", "reactive", "aggressive", "timid"])
        attention = self._get_input("Attention need", options=["low", "moderate", "high"])
        return BehaviorFlags(
            obedience_level=obedience,
            emotional_response=emotion,
            attention_need=attention
        )

    def _collect_child(self):
        name = self._get_input("Enter child's name")
        age = int(self._get_input("Enter child's age"))
        gender = self._get_input("Enter child's gender", options=["male", "female", "other"])
        is_single_child = self._get_input("Is this a single child?", default="no", options=["yes", "no"]) == "yes"
        birth_order = self._get_input("Birth order", options=["first", "second", "third", "only", "none"])
        
        schooling = self._collect_schooling()
        favorites = self._collect_favorites()
        triggers = self._collect_triggers()
        behavior = self._collect_behavior_flags()
        
        
        childstate = ChildBehaviorFactory.get_behavior(self._get_input("Enter child's Behavioural state", options=["toddler", "teen", "autistic"]))
        childstate.set_values()
        

        
        
        
        return Child(
            name=name,
            age=age,
            gender=gender,
            is_single_child=is_single_child,
            birth_order=birth_order,
            schooling=schooling,
            favorites=favorites,
            triggers=triggers,
            behavior_flags=behavior,
            state=childstate
        )

    def _collect_address(self):
        city = self._get_input("Enter your city")
        state = self._get_input("Enter your state")
        country = self._get_input("Enter your country", default="India")
        return Address(city=city, state=state, country=country)

    def _collect_family_context(self):
        spouse_type = self._get_input("Spouse type", options=["single_parent", "happy_couple", "divorced", "separated", "widowed"])
        parenting_approach = self._get_input("Parenting approach", options=["gentle", "authoritative", "permissive", "uninvolved", "strict"])
        return FamilyContext(spouse_type=spouse_type, parenting_approach=parenting_approach)

    def register_family(self):
        print("\n🧩 --- Family Registration Wizard ---\n")
        parent = self._collect_parent()

        children = {}
        num_children = int(self._get_input("How many children do you want to register?", default="1"))
        for i in range(num_children):
            print(f"\n👶 --- Entering details for Child {i + 1} ---")
            child = self._collect_child()
            children[child.name]=child

        address = self._collect_address()
        family_context = self._collect_family_context()

        family = Family(
            family_id=str(uuid.uuid4()),
            address=address,
            parent=parent,
            children=children,
            family_context=family_context,
            registration_timestamp=str(datetime.datetime.now())
        )
        print("\n✅ Family registered successfully!\n")
        return family
