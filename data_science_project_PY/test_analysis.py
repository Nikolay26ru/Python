import pytest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

def test_model_train():
    data = pd.DataFrame({"text": ["good", "bad"], "label": [1, 0]})
    X_train, X_test, y_train, y_test = train_test_split(data["text"], data["label"], test_size=0.5)
    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    model = LogisticRegression()
    model.fit(X_train_vec, y_train)
    assert hasattr(model, "predict")
