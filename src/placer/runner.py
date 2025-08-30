"""High level inference runner."""
from __future__ import annotations

from typing import Any

from .devices import get_device


class InferenceRunner:
    """Thin wrapper around :class:`placer.PLACER` for inference."""

    def __init__(self, weights_path: str | None = None, device: str | None = None) -> None:
        self.device = get_device(device)
        self.weights_path = weights_path
        self._model = None

    def load_model(self) -> Any:  # pragma: no cover - heavy model
        """Load the underlying PLACER model lazily."""
        if self._model is None:
            from .placer import PLACER

            self._model = PLACER(weights_path=self.weights_path, device=str(self.device))
        return self._model

    def run(self, pl_input: Any, nsamples: int = 10) -> Any:  # pragma: no cover - heavy model
        """Run predictions using the underlying model."""
        model = self.load_model()
        return model.run(pl_input, nsamples)
