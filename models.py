"""Models used for prediction"""
from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self, name):
        self._name = name

    def __call__(self, data):
        return self.predict(data)

    def __repr__(self):
        return f"{self._name}()"

    @abstractmethod
    def train(self, data, labels):
        pass

    @abstractmethod
    def predict(self, features):
        pass


class SimpleLinear(Model):
    def __init__(self, name):
        super().__init__(name)

    def train(self, data, labels):
        print(f"Model {self} training")

    def predict(self, features):
        print(f"Model {self} prediciting")
