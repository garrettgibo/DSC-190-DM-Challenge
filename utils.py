"""Simple helpful utility functions"""
import pandas as pd


def load_data(file_path: str):
    """ Load data from csv file and parse features and labels.

    Args:
        file_path: path to file to load

    Returns:
        dataframe of features with corresponding feature names as column names;
        array of labels

    """
    all_data_df = pd.read_csv(file_path)
    features = all_data_df.loc[:, all_data_df.columns != "price"]
    labels = all_data_df["price"] if "price" in all_data_df.columns else None

    return features, labels
