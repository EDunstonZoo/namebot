# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from datetime import datetime as dt


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

from typing import Text, Dict, Any, List
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionSaveTimeDescription(Action):
   def name(self) -> Text:
      return "action_get_description_time"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      time = tracker.get_slot('time')
      time_object = dt.strptime(time, "%Y-%m-%dT%H:%M:%S.%f%z")
      out_str = time_object.strftime('%b %d %Y %I:%M%p')


      return [SlotSet("description_time", out_str if out_str is not None else [])]



     