#from zvrkiwi import KIWIEstimator
import zvrkiwi
from xgboost import XGBClassifier

if __name__ == "__main__":
    clf = XGBClassifier()
    kclf = zvrkiwi.KIWIEstimator(clf)




