import pytest

from sklearn.utils.estimator_checks import check_estimator
from estimator import KIWIEstimator


@pytest.mark.parametrize(
    "estimator",
    [KIWIClassifier()]
)
def test_all_estimators(estimator):
    return check_estimator(estimator)
