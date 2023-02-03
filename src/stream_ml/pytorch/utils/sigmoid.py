"""Core feature."""

from __future__ import annotations

from typing import TYPE_CHECKING

import torch as xp

__all__: list[str] = []


if TYPE_CHECKING:
    from stream_ml.pytorch.typing import Array


_0 = xp.asarray(0)
_1 = xp.asarray(1)


def scaled_sigmoid(x: Array, /, lower: Array = _0, upper: Array = _1) -> Array:
    """Sigmoid function mapping ``(-inf, inf)`` to ``(lower, upper)``.

    Output for (lower, upper) is defined as:
    - If (finite, finite), then this is a scaled sigmoid function.
    - If (-inf, inf) then this is the identity function.
    - Not implemented for (+/- inf, any), (any, +/- inf)

    Parameters
    ----------
    x : Array
        X.
    lower : Array
        Lower.
    upper : Array
        Upper.

    Returns
    -------
    Array
    """
    if xp.isneginf(lower) and xp.isposinf(upper):
        return x
    elif xp.isinf(lower) or xp.isinf(upper):
        raise NotImplementedError

    return xp.sigmoid(x) * (upper - lower) + lower
