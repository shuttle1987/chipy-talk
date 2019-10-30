from functools import wraps

TRICK = "trick"
TREAT = "treat"

def halloween_ize(func):
    @wraps(func)
    def more_halloween(*args, **kwargs):
        """🎃🎃🎃 Let's make this more awesome!!! 🎃🎃🎃"""
        print(func.__name__ + " was called")
        res = func(*args, **kwargs)
        if res == TRICK:
            return "🎃 🕸️ 🦇 👻 " + res
        elif res == TREAT:
            return "🎃 🍬 🍭 🍫 " + res
        else:
            return res
    return more_halloween