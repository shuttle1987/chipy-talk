import sys
from typing import List

import upsidedown

names_defined_here = globals()


rev_mapper = {}
import location

def map():
    print("Map here")

def travel_to(place: str) -> None:
    """Travel somewhere else"""
    if "Aus" in place:
        location.set_to_australia()
    else:
        location.current_location = place


def generate() -> List[str]:
    """Generate the method names"""
    global names_defined_here
    global rev_mapper
    secret_names = ["upsidedown", "names_defined_here"]
    rev_mapper = {upsidedown.transform(name): name for name in names_defined_here}
    return [upsidedown.transform(name) for name in names_defined_here if name not in secret_names]


for rev, regular in rev_mapper.items():
    this = sys.modules[__name__]
    setattr(this,rev,this.regular)
    #this.rev.__doc__ = upsidedown.transform(regular.__doc__)

def __getattr__(name):
    if name in rev_mapper:
        this = sys.modules[__name__]
        return getattr(this,rev_mapper[name])

results = []
def __dir__() -> List[str]:
    global results
    if not results:
        results = generate()
    return results

