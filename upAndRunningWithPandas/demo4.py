#!/usr/bin/env python
import pandas as pd

def read_csv_to_df(path):
    df = pd.read_csv(path)
    return df

def main():
    path="demo4Data/phoneprices.csv"
    df_csv = read_csv_to_df(path)

    # Get Length of Data Frame
    print(len(df_csv), "\n")

    # View first 10 rows of Data Frame
    print(df_csv.head(10), "\n")

    # View last 10 rows of Data Frame
    print(df_csv.tail(10), "\n")

    # Slice specific columns from Data Frame
    df_slice = df_csv[["battery_power", "blue", "clock_speed"]]
    print(df_slice, "\n")

    # View specific # of rows and columns from Data Frame
    df_view = df_csv.iloc[0:4, 0:3]
    print(df_view, "\n")

    # View rows based on matching criteria/operator logic
    df_select_view = df_csv[df_csv["price_range"] == 1]
    print(df_select_view, "\n")

if __name__ == "__main__":
    main()