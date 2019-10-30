from typing import List

import upsidedown

def map():
    """Print a map of Australia"""
    raise NotImplementedError

names_defined_here = globals()

def generate() -> List[str]:
    """Generate the method names"""
    global names_defined_here
    secret_names = ["upsidedown", "names_defined_here"]
    return [upsidedown.transform(name) for name in names_defined_here if name not in secret_names]

results = []
def __dir__() -> List[str]:
    global results
    if not results:
        results = generate()
    return results