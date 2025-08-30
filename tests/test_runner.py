import pytest

from placer.runner import InferenceRunner


@pytest.mark.parametrize("device", [None, "cpu"])
def test_runner_init(device):
    runner = InferenceRunner(device=device)
    assert runner._model is None
    assert isinstance(str(runner.device), str)
