"""PLACER package"""
from __future__ import annotations

try:  # Heavy model import
    from .placer import PLACER  # type: ignore
except Exception:  # pragma: no cover
    PLACER = None  # type: ignore

from .runner import InferenceRunner

__all__ = ["PLACER", "InferenceRunner"]
