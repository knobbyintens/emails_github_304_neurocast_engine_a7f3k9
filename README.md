# Neurocast Engine

Streaming time-series forecasting for constrained edge deployments.

**Status: Released — v1.2.0 (2025-09-30).** The implementation in this repository is
the one described in the showcase write-up; it is maintained and published here.

## Contents

- `src/neurocast/model.py` — quantised encoder/decoder and forecast head
- `src/neurocast/streaming.py` — sliding-window ingestion and online calibration
- `src/neurocast/calibration.py` — uncertainty calibration utilities
- `tests/test_model.py` — deterministic unit tests for the forecasting core
- `examples/run_retail_demo.py` — small end-to-end example

## Install / run

```
pip install -e .
python examples/run_retail_demo.py
```

## Licence

Apache-2.0.
