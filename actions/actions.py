# This file contains your custom actions which can be used to run
# custom Python code.

from typing import Any, Text, Dict, List

from rasa_sdk import Action 
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionShowProductAvailable(Action):

    def name(self) -> Text:
        return "action_product_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'product':
                name = e['value']

                if name == "bikes":
                    message = "We have Touring Bikes, Road Bikes, Mountain Bikes. See anything you like? Just ask it."

                elif name == "accessories":
                    message = "We have Belts, Caps, Ties. See anything you like? Just ask it."

                elif name == "fashion":
                    message = "We have Vintage fashion style, Casual clothes, Formal clothes. See anything you prefer? Just ask it."

        dispatcher.utter_message(text=message)
        return []


class ActionBikes(Action):

    def name(self) -> Text:
        return "action_bikes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'bikes':
                name = e['value']

                if name == "touring":
                    message = "We have KTM 390 Duke, Royal Enfield Himalayan."

                elif name == "road":
                    message = "We have Race bikes, Aero bikes."

                elif name == "mountain":
                    message = "We have Trail bikes, Downhill bikes."

        dispatcher.utter_message(text=message)
        return []


class ActionTouring(Action):

    def name(self) -> Text:
        return "action_touring"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'touring':
                name = e['value']

                if name == "KTM":
                    message = "https://cutt.ly/HnpIx7O"

                elif name == "Royal Enfield":
                    message = "https://cutt.ly/snpIbRF"

        dispatcher.utter_message(text=message)
        return []


class ActionRoad(Action):

    def name(self) -> Text:
        return "action_road"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'road':
                name = e['value']

                if name == "race":
                    message = "https://cutt.ly/3npIFjD"

                elif name == "aero":
                    message = "https://cutt.ly/JnpIRrU"

        dispatcher.utter_message(text=message)
        return []


class ActionMountain(Action):

    def name(self) -> Text:
        return "action_mountain"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'mountain':
                name = e['value']

                if name == "trail":
                    message = "https://cutt.ly/SnpIX3D"

                elif name == "downhill":
                    message = "https://cutt.ly/lnpILl3"

        dispatcher.utter_message(text=message)
        return []


class ActionAccessories(Action):

    def name(self) -> Text:
        return "action_accessories"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'accessories':
                name = e['value']

                if name == "belts":
                    message = "We have Buckle belt, Metal belts."

                elif name == "caps":
                    message = "We have Baseball Caps, Fedora Caps."

                elif name == "ties":
                    message = "We have Novelty Ties, Solid Ties."

        dispatcher.utter_message(text=message)
        return []


class ActionBelts(Action):

    def name(self) -> Text:
        return "action_belts"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'belts':
                name = e['value']

                if name == "metal":
                    message = "https://cutt.ly/Bnorn2J"

                elif name == "buckle":
                    message = "https://cutt.ly/HnorQzT"

        dispatcher.utter_message(text=message)
        return []


class ActionTies(Action):

    def name(self) -> Text:
        return "action_ties"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'ties':
                name = e['value']

                if name == "novelty":
                    message = "https://cutt.ly/znorXZq"

                elif name == "solid":
                    message = "https://cutt.ly/Enor2y0"

        dispatcher.utter_message(text=message)
        return []


class ActionCaps(Action):

    def name(self) -> Text:
        return "action_caps"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'caps':
                name = e['value']

                if name == "baseball":
                    message = "https://cutt.ly/8norpFm"

                elif name == "fedora":
                    message = "https://cutt.ly/6norxFX"

        dispatcher.utter_message(text=message)
        return []


class ActionFashion(Action):

    def name(self) -> Text:
        return "action_fashion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'fashion':
                name = e['value']

                if name == "vintage":
                    message = "We have Flared Jeans, Granny Glasses."

                elif name == "casual":
                    message = "We have Minidress, Shorts."

                elif name == "formal":
                    message = "We have Formal Shirts, Formal Jeans."

        dispatcher.utter_message(text=message)
        return []


class ActionVintageStyle(Action):

    def name(self) -> Text:
        return "action_vintage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'vintage':
                name = e['value']

                if name == "flared jeans":
                    message = "https://cutt.ly/mnoa0vG"

                elif name == "granny glasses":
                    message = "https://cutt.ly/cnosety"

        dispatcher.utter_message(text=message)
        return []


class ActionCasualClothes(Action):

    def name(self) -> Text:
        return "action_casual"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'casual':
                name = e['value']

                if name == "minidress":
                    message = "https://cutt.ly/wnoszmv"

                elif name == "shorts":
                    message = "https://cutt.ly/gnosnfn"

        dispatcher.utter_message(text=message)
        return []


class ActionFormalClothes(Action):

    def name(self) -> Text:
        return "action_formal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'formal':
                name = e['value']

                if name == "shirts":
                    message = "https://cutt.ly/rnosOQr"

                elif name == "jeans":
                    message = "https://cutt.ly/knosS6m"

        dispatcher.utter_message(text=message)
        return []


class ActionDiscountOffer(Action):

    def name(self) -> Text:
        return "action_discount_offer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'discount_offer':
                name = e['value']

                if name == "discount":
                    message = "You will have 3 chances to enter discount percentage. If you are lucky you can get discount up to 50%."

                elif name == "offer":
                    message = "You will have 3 chances to enter discount percentage. If you are lucky you can get this product for 50% off."

                elif name == "last":
                    message = "You will have 3 chances to enter discount percentage. First, let's begin the negotiations."

        dispatcher.utter_message(text=message)
        return []


class ActionDiscount(Action):

    def name(self) -> Text:
        return "action_discount"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'discount':
                discount1 = e['value']
                discount1 = int(discount1)

                if discount1 <= 10:
                    bot_discount1 = discount1
                    message = f"Seems reasonable, we have a deal! You can purchase this product for a discount of {bot_discount1}%."

                elif 10 < discount1 <= 100:
                    bot_discount1 = int(discount1 * 0.6)
                    message = f"That's too much to ask! How about a discount of {bot_discount1}%?"

        dispatcher.utter_message(text=message)
        return []


class ActionOffer(Action):

    def name(self) -> Text:
        return "action_offer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'offer':
                discount2 = e['value']
                discount2 = int(discount2)

                if discount2 <= 10:
                    bot_discount2 = discount2
                    message = f"Seems reasonable, we have a deal! You can purchase this product for a discount of {bot_discount2}%."

                elif 10 < discount2 <= 100:
                    bot_discount2 = int(discount2 * 0.75)
                    message = f"It's still slightly high! How about {bot_discount2}% off?"

        dispatcher.utter_message(text=message)
        return []


class ActionLast(Action):

    def name(self) -> Text:
        return "action_last"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        message = "Sorry, I didn't understand that."

        for e in entities:
            if e['entity'] == 'last':
                discount3 = e['value']
                discount3 = int(discount3)

                if discount3 <= 10:
                    bot_discount3 = discount3
                    message = f"Seems reasonable, we have a deal! You can purchase this product for a discount of {bot_discount3}%."cd

                elif 10 < discount3 <= 100:
                    bot_discount3 = int(discount3 * 0.9)
                    message = f"Okay, let's make it our last deal! How about {bot_discount3}% off?"

        dispatcher.utter_message(text=message)
        return []
