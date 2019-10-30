current_location = "Australia"

def set_to_australia():
    global current_location
    current_location = "Australia"

from enum import Enum
class TrickOrTreatState(Enum):
    REGULAR = 1
    MORE_TREATS = 2
    MORE_TRICKS = 3

trick_or_treat_state = TrickOrTreatState.REGULAR