"""Small end-to-end demo for Neurocast Engine."""

from src.neurocast.model import NeurocastModel, ModelConfig


def main():
    series = [10, 12, 13, 15, 16, 18, 19]
    model = NeurocastModel(ModelConfig()).fit(series)
    print(model.forecast(series, horizon=6))


if __name__ == "__main__":
    main()
