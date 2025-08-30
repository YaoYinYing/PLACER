from __future__ import annotations

"""Minimal API example for using PLACER."""

from pathlib import Path

from placer.runner import InferenceRunner
from placer.modules.placer_input import PLACERinput

EXAMPLE_DIR = Path(__file__).resolve().parent


def main() -> tuple[InferenceRunner, PLACERinput]:
    """Build a runner and input object for the bundled example."""
    runner = InferenceRunner(device="cpu")
    pl_input = PLACERinput()
    pl_input.pdb(str(EXAMPLE_DIR / "input.pdb"))
    return runner, pl_input


if __name__ == "__main__":  # pragma: no cover - manual usage
    main()
