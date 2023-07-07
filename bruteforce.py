import csv 
import time

CSV_PATH = "./assets/dataset1_Python_P7.csv"
STOCK_NAME_INDEX = 0
STOCK_PRICE_INDEX = 1
STOCK_INTERESTS_INDEX = 2

# TODO: faire les docstring

def bruteforce(path):
    rows = from_csv_to_rows(path)
    rows.pop(0)
    stocks = [from_row_to_stock(row) for row in rows]
    start_bruteforce = time.time()
    combination = recursive(stocks)
    end_bruteforce = time.time()
    combination = sorted(combination, key=lambda value: value["benefits"], reverse=True)
    winner = combination[0]
    time_spend = round(end_bruteforce - start_bruteforce,3)
    print(f"the winner is : {winner} and the algorithm tooks {str(time_spend)} seconds to be done")

def from_csv_to_rows(path: str):
    rows = []
    with open(path, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append(row)
    return rows

def from_row_to_stock(row: list):
    return {"name": row[STOCK_NAME_INDEX], "price": row[STOCK_PRICE_INDEX], "benefits": float(row[STOCK_INTERESTS_INDEX])}

def recursive(stocks, combo=None):
    if combo is None:
        combo = {"name": "", "price": 0, "benefits": 0}
    combination = []
    for i in range(len(stocks)):
        new_price = combo["price"] + float(stocks[i]["price"])
        if new_price > 500:
            continue
        new_name = combo["name"] + " " + stocks[i]["name"]
        new_benefits = combo["benefits"] + stocks[i]["benefits"]
        new_combo = {"name": new_name, "price": new_price, "benefits": new_benefits}
        combination.append(new_combo)
        combination += recursive(stocks[i+1:], new_combo)
    return combination

bruteforce(CSV_PATH)
