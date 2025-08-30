import torch

from placer.devices import get_device


def test_get_device_cpu():
    dev = get_device("cpu")
    assert dev.type == "cpu"


def test_get_device_auto():
    dev = get_device()
    assert isinstance(dev, torch.device)
