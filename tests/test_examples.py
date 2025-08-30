from example.api_example import main


def test_api_example():
    runner, pl_input = main()
    assert runner.device.type == "cpu"
    assert "ATOM" in pl_input.pdb()
