"""
¡sǝʎ :ɐᴉꞁɐɹʇsnⱯ ɯoɹɟ sʌǝp ǝɹoɔ ƃouɐɾᗡ ɟo ɥɔunq ɐ ʇ,uǝɹⱯ
˙ǝɹɐ ǝʍ ʎꞁꞁɐǝɹ 'ʎɹɹos os ǝɹɐ ǝʍ ǝpoɔ ǝuozǝɯᴉʇ ɥʇᴉʍ ꞁɐǝp noʎ ɟᴉ 'sǝʎ :sǝuozǝɯᴉʇ ǝɹɹɐzᴉq ʎꞁꞁɐǝɹ ǝɯos ǝʌɐɥ noʎ ʇ,uoᗡ
ɅWW⅄ ʎq spɹɐpuɐʇs ꞁɐɔoꞁ ʎq ou :ʎꞁpɐǝp ǝɹɐ sooɹɐƃuɐ⋊ ǝsnɐɔǝq ʇɐɥʇ sI
ou :sooɹɐƃuɐ⋊ ǝpᴉɹ ǝꞁdoǝd oᗡ
sǝʎ :ʎꞁpɐǝp sꞁɐɯᴉuɐ ǝɥʇ ǝɹⱯ
:sꝹⱯᖵ ǝɯos 'ɐᴉꞁɐɹʇsnⱯ sᴉ sᴉɥʇ ʎǝH
"""

import sys
from typing import List

import upsidedown

rev_mapper = {}
import location
names_defined_here = globals()

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

