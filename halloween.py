from functools import wraps

TRICK = "trick"
TREAT = "treat"

import location

class HalloweenException(Exception):
    pass

def halloween_ize(func):
    australia_called = 0
    @wraps(func)
    def more_halloween(*args, **kwargs):
        """🎃🎃🎃 Let's make this more awesome!!! 🎃🎃🎃"""
        print(func.__name__ + " was called")
        halloween_prefix = "🎃🎃🎃"
        halloween_suffix = "🎃🎃🎃"
        if location.current_location == "Australia":
            nonlocal australia_called
            australia_called += 1
            if australia_called == 1:
                raise HalloweenException("🎃🎃🎃 Pumpkins aren't in season in australia now... 🎃🎃🎃")
            elif australia_called == 2:
                raise HalloweenException("Seems like you still really want to celebrate halloween in Australia, "
                                         "perhaps you should consider travelling to the northern hemisphere using "
                                         "southern_hemisphere.travel_to('Chicago') ?")
            elif australia_called >= 3:
                halloween_prefix = "🦘🦘🦘"
                halloween_suffix = "🦘🦘🦘"
        res = func(*args, **kwargs)
        if res == TRICK:
            return halloween_prefix + "🕸️ 🦇 👻 " + res + "🕸️ 🦇 👻 " + halloween_suffix
        elif res == TREAT:
            return halloween_prefix + "🍬 🍭 🍫 " + res + "🍬 🍭 🍫 " + halloween_suffix
        else:
            return res
    return more_halloween