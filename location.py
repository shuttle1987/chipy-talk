import sys
current_location = sys.intern("Australia")

def set_to_australia():
    global current_location
    current_location = sys.intern("Australia")

def set_to(place):
    global current_location
    current_location = sys.intern(place)

def set_to_chicago():
    global current_location
    current_location = sys.intern("Chicago")

def get_current_location():
    global current_location
    return current_location

from enum import Enum
class TrickOrTreatState(Enum):
    REGULAR = 1
    MORE_TREATS = 2
    MORE_TRICKS = 3

trick_or_treat_state = TrickOrTreatState.REGULAR