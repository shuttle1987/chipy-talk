from functools import wraps

TRICK = "trick"
TREAT = "treat"

import location

class HalloweenException(Exception):
    pass

def make_trick_prefix(more_icons=False):
    """Make the haloween trick prefixes"""
    import random 
    icons = ['🕸️', '🦇', '👻']
    if more_icons:
        icons = ['🕸️', '🦇', '👻', '😈', '😱', '💀', '🦴', '⚰️']
    random.shuffle(icons)
    return "".join(icons[:3])

def make_treat_prefix(more_icons=False):
    """Make the haloween treat prefixes"""
    import random 
    icons = ['🍬','🍭', '🍫']
    if more_icons:
        icons = ['🍬','🍭', '🍫', '🍿', '🎉']
    random.shuffle(icons)
    return "".join(icons[:3])

def more_treats():
    location.trick_or_treat_state = location.TrickOrTreatState.MORE_TREATS

def more_tricks():
    location.trick_or_treat_state == location.TrickOrTreatState.MORE_TRICKS

def halloween_ize(spooky):
    """Make it more Halloween!"""
    australia_called = 0
    @wraps(spooky)
    def more_halloween(*args, **kwargs):
        """🎃🎃🎃 Let's make this more awesome!!! 🎃🎃🎃"""
        halloween_prefix = "🎃🎃🎃"
        halloween_suffix = "🎃🎃🎃"
        print("==get_cl()=", location.get_current_location())
        print(id(location.current_location))
        print("==cl==", location.current_location)
        if location.get_current_location() == "Australia":
            nonlocal australia_called
            australia_called += 1
            if australia_called == 1:
                raise HalloweenException("🎃🎃🎃 Pumpkins aren't in season in Australia now... 🎃🎃🎃")
            elif australia_called == 2:
                raise HalloweenException("Seems like you still really want to celebrate Halloween in Australia, "
                                         "perhaps you should consider travelling to the northern hemisphere using "
                                         "southern_hemisphere.travel_to('Chicago') ?")
            elif australia_called >= 3:

                halloween_prefix = "🦘🦘🦘"
                halloween_suffix = "🦘🦘🦘"
        res = spooky(*args, **kwargs)
        if location.trick_or_treat_state == location.TrickOrTreatState.MORE_TREATS:
            trick_or_treat_prefix = make_treat_prefix(more_icons=True)
            trick_or_treat_suffix = make_treat_prefix(more_icons=True)
            return halloween_prefix + trick_or_treat_prefix + TREAT + trick_or_treat_suffix + halloween_suffix
        elif location.trick_or_treat_state == location.TrickOrTreatState.MORE_TRICKS:
            trick_or_treat_prefix = make_trick_prefix(more_icons=True)
            trick_or_treat_suffix = make_trick_prefix(more_icons=True)
            return halloween_prefix + trick_or_treat_prefix + TRICK + trick_or_treat_suffix + halloween_suffix
        if res == TRICK:
            return halloween_prefix + make_trick_prefix() + res + make_trick_prefix() + halloween_suffix
        elif res == TREAT:
            return halloween_prefix + make_treat_prefix() + res + make_treat_prefix() + halloween_suffix
        else:
            return res
    return more_halloween