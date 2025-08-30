"""Device utilities for PLACER."""
from __future__ import annotations

import torch


def get_device(device: str | None = None) -> torch.device:
    """Return a torch device from a user hint.

    Parameters
    ----------
    device: str | None
        Desired device name ("cpu", "cuda", "mps"). If ``None`` the best
        available backend is selected.
    """
    if device is not None:
        dev = device.lower()
        if dev.startswith("cuda") and torch.cuda.is_available():
            return torch.device("cuda")
        if dev.startswith("mps") and torch.backends.mps.is_available():
            return torch.device("mps")
        return torch.device("cpu")

    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")
