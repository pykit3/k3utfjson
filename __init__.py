"""
# Name

utfjson: force `json.dump` and `json.load` in `utf-8` encoding.

# Status

This library is considered production ready.

"""

# from .proc import CalledProcessError
# from .proc import ProcError

__version__ = "0.1.0"
__name__ = "k3utfjson"

from .utfjson import (
    dump,
    load,
)

__all__ = [
    'dump',
    'load',
]
