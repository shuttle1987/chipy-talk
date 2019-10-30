import sys
from typing import List

import upsidedown

names_defined_here = globals()


rev_mapper = {}
import location

def worldmap():
    if location.get_current_location() == sys.intern("Australia"):
        from IPython.display import Image
        return Image("ausMap.png")
    else:
        from IPython.display import display, Javascript
        import folium
        m = folium.Map(location=[0,0], zoom_start=2)
        display(m)
        return Javascript('this.element.attr("class", "mymapoutput")')

def travelto(place: str) -> None:
    """Travel somewhere else"""
    from IPython.display import display, HTML
    if "Aus" in place:
        location.set_to_australia()
        # flip map
        return HTML(f"Travelled to {place}"+
        """
        <style>
        #mymapoutput * {
            display: inline-block;
            transform: rotate(180deg) !important;
        }
        </style>
        """)
    elif place in ["Chicago", "chicago"]:
        location.set_to_chicago()
        return HTML(f"Travelled to {place}"+
        """
        <style>
        #mymapoutput * {
            display: inline-block
            rotate(0deg) !important;
        }
        </style>
        """)
    else:
        location.set_to(place)
        return HTML(f"Travelled to {place}"+
        """
        <style>
        #mymapoutput * {
            display: inline-block
            rotate(0deg) !important;
        }
        </style>
        """)


def generate() -> List[str]:
    """Generate the method names"""
    global names_defined_here
    global rev_mapper
    secret_names = ["upsidedown", "names_defined_here", "rev_mapper"]
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
    if location.get_current_location() == sys.intern("Australia"):
        return results
    this = sys.modules[__name__]
    return dir(this)

