"""
Data classes are classes to store data (state) without much behaviors (methods)

it's better to use Data classes, than "namedTuples"
"""


from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
