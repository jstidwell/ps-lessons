#!/usr/bin/env python
import json
import csv

def readJsonFile(path):
    json_file = open(path)
    json_data = json.load(json_file)
    print("Printing JSON File Contents:")
    print(json_data)

def readCsvFile(path):
    with open(path, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print("Printing CSV File Contents:")
        for row in csv_reader:
            print(row)

def main():
    path = "demo1Data/example-1.json"
    readJsonFile(path)

    print("\n")

    path = "demo1Data/example-1.csv"
    readCsvFile(path)

if __name__ == "__main__":
    main()