from popmon.config import config
from popmon.utils import filter_metrics


def test_filter_metrics():
    metrics = [
        "distinct_pull",
        "filled_pull",
        "nan_pull",
        "mean_pull",
        "std_pull",
        "p05_pull",
        "p10_pull",
        "p50_pull",
        "p85_pull",
        "p95_pull",
        "max_pull",
        "min_pull",
        "fraction_true_trend10_zscore",
        "ref_unknown_labels",
        "prev1_ks_zscore",
        "worst",
        "ref_max_prob_diff",
    ]
    expected = [
        "distinct_pull",
        "filled_pull",
        "nan_pull",
        "mean_pull",
        "std_pull",
        "p05_pull",
        "p50_pull",
        "p95_pull",
        "max_pull",
        "min_pull",
        "fraction_true_trend10_zscore",
        "ref_unknown_labels",
        "prev1_ks_zscore",
        "worst",
        "ref_max_prob_diff",
    ]
    assert (
        filter_metrics(
            metrics, ignore_stat_endswith=[], show_stats=config["limited_stats"]
        )
        == expected
    )
