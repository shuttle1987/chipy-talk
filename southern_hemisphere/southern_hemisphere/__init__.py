import sys
from typing import List

import upsidedown

names_defined_here = globals()

import location

def travel_to(place: str) -> None:
    """Travel somewhere else"""
    if "Aus" in place:
        location.set_to_australia()
    else:
        location.current_location = place


def generate() -> List[str]:
    """Generate the method names"""
    global names_defined_here
    secret_names = ["upsidedown"]
    return [upsidedown.transform(name) for name in names_defined_here if name not in secret_names]

results = []
def __dir__() -> List[str]:
    global results
    if not results:
        results = generate()
        results.remove("upsidedown")
    return results