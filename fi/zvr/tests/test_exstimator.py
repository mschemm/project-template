import pytest
import numpy as np

from sklearn.datasets import load_iris
from numpy.testing import assert_array_equal
from numpy.testing import assert_allclose
from xgboost import XGBClassifier
from estimator import KIWIEstimator


@pytest.fixture
def data():
    return load_iris(return_X_y=True)


def test_kiwi_estimator(data):
    X, y = data
    clf = KIWIEstimator()
    assert type(clf.xgb_classifier) == type(XGBClassifier)

    clf.fit(X, y)
    assert hasattr(clf, 'X_')
    assert hasattr(clf, 'y_')

    y_pred = clf.predict(X)
    assert y_pred.shape == (X.shape[0],)
