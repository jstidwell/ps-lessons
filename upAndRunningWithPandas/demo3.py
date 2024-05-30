#!/usr/bin/env python
import pandas as pd

def read_json_df(path):
    df = pd.read_json(path)
    print("Printing Data Frame from JSON File:")
    print(df)
    return df

def df_to_json(df):
    json_string = df.to_json()
    print("Printing JSON String from Data Frame:")
    print(json_string)
    return json_string

def read_csv_df(path):
    df = pd.read_csv(path)
    print("Printing Data Frame from CSV File")
    print(df)
    return df

def read_csv_without_header_df(path):
    df = pd.read_csv(path, header=None)
    print("Printing Data Frame without Header from CSV File:")
    print(df)
    return df

def main():
    path = "demo3Data/example-1.json"
    df_json = read_json_df(path)

    print("\n")

    json_string = df_to_json(df_json)

    print("\n")

    path = "demo3Data/example-1.csv"
    df_csv = read_csv_df(path)

    print("\n")

    path = "demo3Data/example-2.csv"
    df_no_header_csv = read_csv_without_header_df(path)

if __name__ == "__main__":
    main()