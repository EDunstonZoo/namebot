# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import FormValidationAction, Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType
from rasa_sdk.types import DomainDict


class ValidateActivityForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_activity_form"
    
    def validate_activity(self, slot_value: Any, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, domain: DomainDict) -> Dict[Text,Any]: 
        ### Check if date is in the future.
        if slot_value :
            dispatcher.utter_message(text=f"OK! You are going to {slot_value}")
            return{"activity": slot_value}
    
    def validate_time(self, slot_value: Any, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, domain: DomainDict) -> Dict[Text,Any]: 
        ### Check if date is in the future.
        if slot_value :
            dispatcher.utter_message(text=f"OK! You have a slot booked in your calender at\
                 {slot_value}")
            return{"time": slot_value}



     