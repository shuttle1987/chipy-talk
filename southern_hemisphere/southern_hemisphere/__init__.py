import sys
from typing import List

import upsidedown

names_defined_here = globals()


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