"""
Global Variables
Initial commit: Jared Sanders

Certain variables shouldn't be modified. These are denoted by
the standard Python static syntax (i.e _varname_).

Other values are free to change and have been named as just
a regular variable.
"""

import os

# Colors
_BLACK_ = (0, 0, 0)

#Screen Dimens
_SIZE_ = (512, 768)

_CLOCK_SPEED_ = 60

#animator
_MSPEED_ = 9
_KICKMOVE_ = 0

#relative file path
PATH = os.path.dirname(os.path.realpath(__file__))

