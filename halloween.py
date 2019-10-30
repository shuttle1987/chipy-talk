from functools import wraps

TRICK = "trick"
TREAT = "treat"

import location

class HalloweenException(Exception):
    pass

def halloween_ize(spooky):
    """Make it more Halloween!"""
    australia_called = 0
    @wraps(spooky)
    def more_halloween(*args, **kwargs):
        """🎃🎃🎃 Let's make this more awesome!!! 🎃🎃🎃"""
        halloween_prefix = "🎃🎃🎃"
        halloween_suffix = "🎃🎃🎃"
        if location.current_location == "Australia":
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
        if res == TRICK:
            return halloween_prefix + "🕸️ 🦇 👻 " + res + "🕸️ 🦇 👻 " + halloween_suffix
        elif res == TREAT:
            return halloween_prefix + "🍬 🍭 🍫 " + res + "🍬 🍭 🍫 " + halloween_suffix
        else:
            return res
    return more_halloween