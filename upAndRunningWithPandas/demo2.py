#!/usr/bin/env python
import pandas as pd

def build_data_df():
    new_data = {
        "Date": ["January 1", "January 2"],
        "Amount": [500.00, 600.00]
    }
    df_new_data = pd.DataFrame(new_data)
    print("Printing New Data:")
    print(df_new_data)
    return df_new_data

def build_sales_df():
    sales_data = {
        "Date": ["January 3", "January 4"],
        "Amount": [100.00, 200.00]
    }
    df_sales = pd.DataFrame(sales_data)
    print("Printing Sales Data:")
    print(df_sales)
    return df_sales

def concat_df(df_1, df_2):
    combined_df = pd.concat([df_1, df_2])
    combined_df.reset_index(drop=True, inplace=True)
    print("Printing Combined Data Frame")
    print(combined_df)
    return combined_df

def concat_new_column_df(df_1, df_2):
    combined_df = pd.concat([df_1, df_2], axis = 1)
    print("Printing Combined Data Frame with New Column")
    print(combined_df)
    return combined_df

def build_third_column_df():
    new_column_data = {
        "Location": ["Store A", "Store B"]
    }
    new_column_df = pd.DataFrame(new_column_data)
    print("Printing New Column Data Frame:")
    print(new_column_df)
    return new_column_df

def main():
    df_data = build_data_df()
    print("\n")
    df_sales = build_sales_df()
    print("\n")
    df_combined = concat_df(df_data, df_sales)
    print("\n")
    df_new_column = build_third_column_df()
    print("\n")
    df_combined = concat_new_column_df(df_combined, df_new_column)

if __name__ == "__main__":
    main()