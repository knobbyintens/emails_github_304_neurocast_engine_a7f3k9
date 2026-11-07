"""Uncertainty calibration utilities."""


def empirical_coverage(residuals, lower, upper):
    if len(residuals) != len(lower) or len(residuals) != len(upper):
        raise ValueError("mismatched lengths")
    covered = sum(1 for r, lo, hi in zip(residuals, lower, upper) if lo <= r <= hi)
    return covered / max(len(residuals), 1)
