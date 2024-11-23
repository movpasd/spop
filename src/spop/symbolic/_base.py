from __future__ import annotations

from typing import TypedDict
from abc import ABC, abstractmethod


class SymbolicTypeError(Exception):
    """Raised if attempting to construct a symbolic object using invalid types"""


class SymbolicObject[TAst: TypedDict](ABC):
    """
    Base class for all symbolic objects

    Subclassing
    -----------
    * All subclasses should be immutable value objects; that is, once constructed, their
      attributes and properties should never change. Modifying a value object should be
      done by constructing a new one, possibly by chaining fluently connectedmethods.
      This also means that holding a reference to a `SymbolicObject` is the same thing
      as holding an clone of it.
    * Subclasses will often have methods that take a type `T` <= `SymbolicObject` as
      parameters in their types signatures. Implementations for these methods should
      raise `TypeError` if a value is given that is not a `SymbolicObject`, but should
      explicitly check for the case where the value _is_ a `SymbolicObject`, just not of
      `T`; in that case, a `SymbolicTypeError` should be raised.
    """
    __slots__ = ()

    # Equality checking methods separate from __eq__ are required since we'll be
    # overriding those
    @abstractmethod
    def identical_to(self, other: SymbolicObject | ScalarLit) -> bool: ...

    @abstractmethod
    def __repr__(self) -> str:
        """
        Should follow pattern
        <exposed interface class name>(<full mathematical description>)
        """

    @abstractmethod
    def __str__(self) -> str:
        """Should look like repr but prettied with newlines, etc, and no class name"""


type ScalarLit = float | int
