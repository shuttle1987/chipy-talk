import sys
from typing import List

import upsidedown

names_defined_here = globals()

def generate() -> List[str]:
    """Generate the method names"""
    global names_defined_here
    return [upsidedown.transform(name) for name in names_defined_here]

def __dir__():
    global results
    if not results:
        results = generate()
        results.remove("upsidedown")
    return results