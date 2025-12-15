import pickle
from sklearn.linear_model import LogisticRegression

class FailureModel:
    def __init__(self):
        self.model = LogisticRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict_proba(self, X):
        return self.model.predict_proba(X)[0][1]

    def save(self, path="model.pkl"):
        with open(path, "wb") as f:
            pickle.dump(self.model, f)

    def load(self, path="model.pkl"):
        with open(path, "rb") as f:
            self.model = pickle.load(f)
