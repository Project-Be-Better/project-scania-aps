import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    train_df = pd.read_csv("data/aps_failure_training_set.csv", skiprows=20, na_values=["na"])
    test_df = pd.read_csv("data/aps_failure_test_set.csv", skiprows=20, na_values=["na"])

    print("Train shape:", train_df.shape)
    print("Test shape:", test_df.shape)
    print(train_df.head())


if __name__ == "__main__":
    main()
