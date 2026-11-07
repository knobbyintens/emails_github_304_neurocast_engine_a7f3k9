from src.neurocast.model import NeurocastModel, ModelConfig


def test_forecast_length():
    model = NeurocastModel(ModelConfig()).fit([1.0, 2.0, 3.0])
    assert len(model.forecast([1.0, 2.0, 3.0], horizon=5)) == 5


def test_empty_series_rejected():
    model = NeurocastModel(ModelConfig())
    try:
        model.fit([])
    except ValueError:
        return
    raise AssertionError("empty series should be rejected")
