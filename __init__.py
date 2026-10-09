"""
# Name

utfjson: force `json.dump` and `json.load` in `utf-8` encoding.

# Status

This library is considered production ready.

"""

# from .proc import CalledProcessError
# from .proc import ProcError

from .utfjson import (
    dump,
    load,
)

__all__ = [
    "dump",
    "load",
]


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3utfjson")
