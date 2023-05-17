from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings

warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

from sklearn.datasets import load_breast_cancer
from fi.zvr.estimator import KIWIEstimator
from xgboost import XGBClassifier


if __name__ == "__main__":
    clf = XGBClassifier(objective="binary:logistic", random_state=42)

    cancer = load_breast_cancer()
    X = cancer.data
    y = cancer.target

    kclf = KIWIEstimator(clf)
    kclf.fit(X, y)

    for res in kclf.predict(X[0:5]):
        print(res)




