# DSC 190 Data Mining Challenge

HDSI, UCSD, Spring 2020

Original Kaggle link found
[here](https://www.kaggle.com/c/ucsd-spring20-dsc190-intro-to-data-mining/overview)

## Challenge Objective

Given the partial dataset of the Airbnb listings at New York City, you are
asked to design data mining models to build a relationship between the price
(dollars per day) and the other observed variables. That is, you are asked to
predict the price of the listing, given all its information.

## Data and Baselines

[data/train.csv](data/train.csv): It contains all the training data that you
can use in this challenge. The first column “id” provides you the unique key to
identify the listings. Different columns show different features/attributes of
a listing, including free texts, numerical features, and categorical features.
There are also many missing values. So please conduct some exploratory data
analyses (EDAs) first before you work on feature engineering.

[test.csv](data/test.csv): It contains all the listings that you need to
predict their prices. The format is the same as the train.csv, except that the
price column has been removed.

## Getting Started

### Prerequisites

- python 3.7
- pipenv

It is recommended you use pipenv to setup your virutal environment for python

### Usage

``` Shell
pipenv install
pipenv run main
```
