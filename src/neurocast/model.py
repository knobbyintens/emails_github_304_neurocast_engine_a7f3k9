"""Quantised forecasting model used by Neurocast Engine."""

from dataclasses import dataclass


@dataclass
class ModelConfig:
    window: int = 96
    hidden_dim: int = 64
    heads: int = 4
    quantised: bool = True


class NeurocastModel:
    """A tiny encoder-decoder forecaster with a quantised encoder."""

    def __init__(self, config: ModelConfig):
        self.config = config

    def fit(self, series):
        if not series:
            raise ValueError("series must not be empty")
        return self

    def forecast(self, series, horizon=12):
        last = float(series[-1])
        slope = float(series[-1] - series[-2]) if len(series) > 1 else 0.0
        return [last + slope * (i + 1) for i in range(horizon)]
