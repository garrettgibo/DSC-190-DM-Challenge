"""Main entry point to rapidly test different models"""
from sklearn import metrics
from tqdm import tqdm

from models import SimpleLinear

import utils

if __name__ == "__main__":
    train_data_path = "data/train.csv"
    test_data_path = "data/test.csv"

    X_train, y_train = utils.load_data(train_data_path)
    X_test, _ = utils.load_data(test_data_path)

    # intialize model
    linear_1 = SimpleLinear("Simple Linear regressor")

    # train model on training data
    linear_1.train(X_train, y_train)

    # predict prices
    predictions = [linear_1(row) for row in tqdm(X_train, desc="Predicting")]

    # evaluate result
    rmse = metrics.mean_squared_error(y_train, predictions)
